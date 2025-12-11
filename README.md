# The Shape of Agreement: Reference Implementation

**Operationalizing Sheaf Theory for Cooperative Logistics.**

This repository contains the reference implementation (Volume II) for the protocol defined in the monograph *The Shape of Agreement*. It provides the "Stitching Layer" necessary to transform heterogeneous supply chain data into a coherent Simplicial Complex using Large Language Models as topological restriction maps.

### 📂 Repository Structure

* **`orchestrator.py`**: The backend daemon that performs the "Observe-Orient-Decide-Act" loop. It manages the `H0` (Consensus) and `H1` (Waste) streams.
* **`app.py`**: The "One-Drop" Dashboard. A Streamlit-based interface for visualizing the Sheaf Cohomology of incoming data packets.
* **`requirements.txt`**: Dependency manifest.

### 🚀 Getting Started

To run the "Shadow Lab" locally:

1.  Clone the repository:
    ```bash
    git clone [https://github.com/sneverline/cooperative-sheaf-lab.git](https://github.com/sneverline/cooperative-sheaf-lab.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Dashboard:
    ```bash
    streamlit run app.py
    ```

### 🧠 Theoretical Basis

This code implements the **Cooperative Sheaf Protocol**:
1.  **Input:** Unstructured text/CSV from a supply chain node.
2.  **Restriction Map ($\rho$):** An LLM converts input to a strict JSON Schema.
3.  **Cohomology Check:**
    * If data fits the schema $\rightarrow$ Signal ($H^0$).
    * If data fails $\rightarrow$ Waste ($H^1$).
4.  **Auditor:** Automated repair logic applied to the Waste Stream.

### 🔗 Citations

* **Paper:** [arXiv:Pending] (The Shape of Agreement: Topological Foundations for Cooperative Logistics)
* **Author:** Sean Neverline, PhD (Independent Researcher)
* **Affiliation:** Black River Systems

---
*Status: Experimental / Proof of Concept.*
