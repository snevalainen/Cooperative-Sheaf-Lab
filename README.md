# The Shape of Agreement: Reference Implementation

**Operationalizing Sheaf Theory for Cooperative Logistics.**

This repository contains the reference implementation (Volume II) for the protocol defined in the monograph *The Shape of Agreement*. It provides the "Stitching Layer" necessary to transform heterogeneous supply chain data into a coherent Simplicial Complex using Large Language Models as topological restriction maps.

## 📂 Repository Structure

* **`orchestrator.py`**: The backend daemon that performs the "Observe-Orient-Decide-Act" loop. It manages the `H0` (Consensus) and `H1` (Waste) streams.
* **`app.py`**: The "One-Drop" Dashboard. A Streamlit-based interface for visualizing the Sheaf Cohomology of incoming data packets.
* **`requirements.txt`**: Dependency manifest.

## 📚 Technical Documentation and Provenance

This research formalizes the shift from adversarial, DAG-based logistics to a cooperative, Sheaf-theoretic framework. It introduces the "Thermodynamic Mandate" for global economic alignment.

* **Primary Strategic Framework (Econ Version):** * [`The_Shape_of_Agreement_ECON.pdf`](./The_Shape_of_Agreement_ECON.pdf) — *Submitted to SSRN, Dec 2025.*
    * Focus: Nash Equilibrium, Dirichlet Energy, and Systemic Waste ($H^1$).
    * [Source Files](./The_Shape_of_Agreement_ECON_Source.zip)

* **Technical Foundation (Math Version):** * [`The_Shape_of_Agreement_MATH.pdf`](./The_Shape_of_Agreement_MATH.pdf)
    * Focus: Mathematical Foundations, Cellular Sheaves, and Simplicial Homology.
    * [Source Files](./Cohomology-Engine-Paper-Source.zip)

## 🚀 Getting Started

To run the "Shadow Lab" locally:

1.  Clone the repository:
    ```bash
    git clone [https://github.com/snevalainen/cooperative-sheaf-lab.git](https://github.com/snevalainen/cooperative-sheaf-lab.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Dashboard:
    ```bash
    streamlit run app.py
    ```

┌──────────────────────────────────────────────────────────────────┐
│  ⚠️  NOTICE: PROPRIETARY IMPLEMENTATION & CORE AUTOMATION        │
└──────────────────────────────────────────────────────────────────┘

While this project (The Shape of Agreement/Project White Piece/Black River Systems) provides an open-source framework for 
the Quaternionic Sheaf Laplacian (Section 6 of the GitBook), the 
following components are proprietary and excluded from this repository:

1. THE STITCHING LAYER SEEDS: The deterministic basis-generation 
   algorithms and salt-distribution protocols used for production-
   grade data obfuscation.

2. GLOBAL SECTION RESOLVERS: The private, high-performance Slerp 
   optimizers used to align multi-party logistic networks at scale.

3. LEGACY ADAPTER INTERFACES: The secure handshake protocols 
   designed for specific Tier-1 ERP and TMS integrations.

The mathematical definitions provided herein are for academic 
validation and interoperability testing. Production-grade deployment 
requires access to the White Piece Core Engine. For institutional 
partnership or pilot inquiries, please contact the Architect.

## 🧠 Theoretical Basis

This code implements the **Cooperative Sheaf Protocol**:
1.  **Input:** Unstructured text/CSV from a supply chain node.
2.  **Restriction Map ($\rho$):** An LLM converts input to a strict JSON Schema.
3.  **Cohomology Check:**
    * If data fits the schema $\rightarrow$ Signal ($H^0$).
    * If data fails $\rightarrow$ Waste ($H^1$).
4.  **Auditor:** Automated repair logic applied to the Waste Stream.

## 📝 Citation

If you use this protocol in your research, please cite as:

> **Nevalainen, S. (2025).** *The Shape of Agreement: Topological Foundations for Cooperative Logistics.* Black River Systems Technical Report.

**BibTeX:**

```bibtex
@techreport{nevalainen2025shape,
  title={The Shape of Agreement: Topological Foundations for Cooperative Logistics},
  author={Nevalainen, Shawn},
  year={2025},
  institution={Black River Systems},
  month={December}
}

---
*Status: Experimental / Proof of Concept.*
