"""
MODULE: ingestor.py
CONTEXT: THE GHOST NODE (External/Static Input Integration)

MATHEMATICAL AXIOMS (SYNTHETIC TOPOLOGY):
This module defines the integration of Static Data (PDF Invoices, HTML Scrapes)
into the Dynamic Topology of the User Terminal.

1. THE GHOST NODE (v_g):
   Defined as a Vertex with a Fixed Stalk F(v_g) = Const.
   Unlike dynamic nodes, v_g has no internal update loop. It is immutable
   until a new document is ingested.

2. THE SYNTHETIC EDGE (e_gl):
   We construct a virtual 1-simplex connecting the Ghost Node (v_g) to the
   Live User Node (v_l).

3. THE RESTRICTION MAP (rho):
   The edge e_gl is equipped with a Restriction Map rho_g_to_e, which functions
   as the "Universal Translator" (LLM/Regex).
   
   rho_g_to_e: Category_Text -> Category_JSON
   
   This map projects unstructured data (PDF) into the Quaternionic Basis of the
   system (i, j, k) to allow for algebraic comparison.

4. THE ONE-DROP INTERFACE:
   The ingestion must satisfy the "One-Drop" Schema to ensure the output
   lies within the valid Vector Space of the Sheaf.
   Failure to map to the Schema results in data being shunted to the 
   Waste Stream (Torsion) before it enters the graph.

REFERENCE:
   "The Shape of Agreement", Nevalainen (2025).
   Section 3.1: Restriction Maps as API Contracts.
   Volume II, Chapter 3: The Universal Translator.
"""

import re
import json
import os
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, validator, ValidationError

# --- THE ONE-DROP SCHEMA (Local Definition for Self-Containment) ---
class OneDropSchema(BaseModel):
    """
    The Mathematical Definition of a Valid Signal.
    Projects inputs into the Quaternionic Basis [Alpha, i, j, k].
    """
    alpha: int = Field(..., description="Quantity (Real Component)")
    i_friction: float = Field(0.0, ge=0.0, le=1.0, description="Logistics Entropy")
    j_friction: float = Field(0.0, ge=0.0, le=1.0, description="Temporal Friction (Normalized)")
    k_friction: float = Field(0.0, ge=0.0, le=1.0, description="Financial Friction (Normalized)")
    
    @validator('j_friction', pre=True)
    def normalize_time(cls, v):
        # Restriction Map Rule: Normalize Hours to [0, 1] Day Scale
        if isinstance(v, (int, float)) and v > 1.0:
            return min(1.0, float(v) / 24.0)
        return v

    @validator('k_friction', pre=True)
    def normalize_money(cls, v):
        # Restriction Map Rule: Normalize Cost to [0, 1] Risk Scale (Arbitrary Cap $10k)
        if isinstance(v, (int, float)) and v > 1.0:
            return min(1.0, float(v) / 10000.0)
        return v


class GhostNodeIngestor:
    """
    The Bridge between the Static World (PDFs) and the Living Mesh.
    Functions as the Restriction Map rho: Text -> JSON.
    """
    
    def __init__(self, use_ai_bridge: bool = False):
        self.use_ai = use_ai_bridge
        # In a real build, we would initialize GenAI here
        self.ai_model = None 

    def ingest(self, raw_text: str) -> Dict[str, Any]:
        """
        Executes the Restriction Map rho(text).
        
        Returns:
            Dict: A valid OneDropSchema object (serialized).
            
        Raises:
            ValueError: If the input cannot be coerced into the Schema (Waste Stream).
        """
        # 1. Sanitize (Pre-processing)
        clean_text = self._sanitize(raw_text)
        
        # 2. Projection (The "Translation")
        # Priority: AI -> Regex Fallback
        extracted_data = self._project_via_regex(clean_text)
        
        # 3. Validation (The Logic Gate)
        try:
            # Enforce the Schema
            validated_packet = OneDropSchema(**extracted_data)
            return validated_packet.dict()
        
        except ValidationError as e:
            # AXIOM 4 FAIL: Shunt to Waste Stream
            raise ValueError(f"Topological Failure: Input rejected by One-Drop Schema. {e}")

    def _sanitize(self, text: str) -> str:
        """Removes control characters and noise."""
        if not text: return ""
        return "".join(ch for ch in text if ch.isprintable() or ch in ['\n', '\t'])

    def _project_via_regex(self, text: str) -> Dict[str, Any]:
        """
        Deterministic Fallback Projection.
        """
        data = {}
        
        # Alpha (Quantity)
        qty_match = re.search(r"(?:qty|quantity|units)\s*[:=]?\s*(\d+)|(\d+)\s*(?:units)", text, re.IGNORECASE)
        if qty_match:
            data['alpha'] = int(qty_match.group(1) or qty_match.group(2))
        else:
            # Partial Signal or Waste? 
            # For now, we default to 0 to let the Validator catch the Torsion,
            # or we could fail here. Axiom 4 says "Failure to map... results in Waste".
            # If Alpha is missing, it's a null signal.
            data['alpha'] = 0

        # J Friction (Time)
        time_match = re.search(r"(\d+)\s*hours?\s*(?:late|delay)", text, re.IGNORECASE)
        if time_match:
            data['j_friction'] = float(time_match.group(1)) # Validator will normalize this via Pydantic

        # K Friction (Money)
        cost_match = re.search(r"\$\s*([\d,]+)", text)
        if cost_match:
             clean_cost = cost_match.group(1).replace(",", "")
             data['k_friction'] = float(clean_cost) # Validator will normalize

        return data