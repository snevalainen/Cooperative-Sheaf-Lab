# The Shape of Agreement: Reference Implementation

**Operationalizing Sheaf Theory for Cooperative Logistics.**

This repository contains the reference implementation (Volume II) for the protocol defined in the monograph *The Shape of Agreement*. It provides the "Stitching Layer" necessary to transform heterogeneous supply chain data into a coherent Simplicial Complex using Large Language Models as topological restriction maps.

## 📂 Repository Structure

* **`orchestrator.py`**: The backend daemon that performs the "Observe-Orient-Decide-Act" loop. It manages the `H0` (Consensus) and `H1` (Waste) streams.
* **`app.py`**: The "One-Drop" Dashboard. A Streamlit-based interface for visualizing the Sheaf Cohomology of incoming data packets.
* **`requirements.txt`**: Dependency manifest.

## 📚 Technical Documentation & Provenance

This repository houses not only the core implementation of the Cohomology Engine but also the foundational academic paper that details the application of algebraic topology to systemic risk modeling.

### **Foundational Paper Draft**

This is the complete, timestamped draft of the paper submitted for academic review.

* **PDF File:** [`Cohomology-Engine-Paper-Draft.pdf`](./Cohomology-Engine-Paper-Draft.pdf)
* **Source Files:** [`Cohomology-Engine-Paper-Source.zip`](./Cohomology-Engine-Paper-Source.zip)

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
