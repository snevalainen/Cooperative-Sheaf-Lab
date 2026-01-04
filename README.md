# THE SHAPE OF AGREEMENT: RESEARCH FRAMEWORK

**Topological Models for Cooperative Logistics (Simulation & Prototype)**

This repository contains the experimental reference implementation (Volume II) for the theoretical framework defined in the monograph *The Shape of Agreement*. 

It serves as a **Research Instrument** designed to test a single hypothesis: that Sheaf Theory and Simplicial Homology can be effective tools for measuring data consistency (or "waste") in heterogeneous supply chains. It utilizes Large Language Models as probabilistic restriction maps to simulate the alignment of unstructured data.

## 📂 REPOSITORY STRUCTURE

* **`orchestrator.py`**: The simulation backend. It runs the Observe-Orient-Decide-Act loop to process incoming data streams, separating them into $H^0$ (Consensus) and $H^1$ (Torsion/Waste) flows.
* **`app.py`**: The "Shadow Node" Dashboard. A Streamlit-based visualization tool for observing Sheaf Cohomology metrics in real-time.
* **`requirements.txt`**: Dependency manifest.

## 📚 THEORETICAL FOUNDATIONS

This research investigates the shift from adversarial, DAG-based logistics to a cooperative, topological framework. It explores the **Thermodynamic Hypothesis**—that economic alignment minimizes systemic friction.

* **[The_Shape_of_Agreement_ECON.pdf](./The_Shape_of_Agreement_ECON.pdf)**
    * *Focus:* Game Theory, Nash Equilibrium, and the "Dirichlet Energy" model of cost.
    * *Status:* Preprint submitted to SSRN (Dec 2025).

* **[The_Shape_of_Agreement_MATH.pdf](./The_Shape_of_Agreement_MATH.pdf)**
    * *Focus:* Simplicial Complexes, Cellular Sheaves, and the Hodge Decomposition.
    * *Status:* Mathematical definition of the idealized model.

## 🚀 GETTING STARTED

**To run the Simulation Environment locally:**

1.  Clone the repository.
    ```bash
    git clone [https://github.com/snevalainen/cooperative-sheaf-lab.git](https://github.com/snevalainen/cooperative-sheaf-lab.git)
    ```
2.  Install dependencies.
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Dashboard.
    ```bash
    streamlit run app.py
    ```

## ⚠️ RESEARCH CONTEXT & SCOPE

This repository is an **experimental prototype**. It differs from a production protocol in the following ways:

1.  **Probabilistic Ingestion:** The "Restriction Maps" in this codebase use Large Language Models (LLMs). While effective for simulation, they are probabilistic. A production implementation would require deterministic parsers to guarantee the *Sheaf Gluing Axiom*.
2.  **Vectorization:** The mapping of categorical data (SKUs, IDs) to the Vector Spaces required for the Sheaf Laplacian is an active area of research. This implementation uses experimental embedding techniques.
3.  **Security:** This repo focuses on the mathematical logic of alignment. Production-grade encryption, salt distribution, and enterprise ERP adapters are outside the scope of this public research release.

For institutional inquiries regarding the theoretical framework or pilot partnerships, please contact the Principal Investigator.

## 🧠 THEORETICAL LOGIC

This code implements the **Cooperative Sheaf Protocol** in a simulated environment:

1.  **Input:** Unstructured text (PDF/Email) or CSV from a supply chain node.
2.  **Restriction Map ($\rho$):** An LLM acts as a functor, attempting to map input to a strict JSON Schema.
3.  **Cohomology Check:**
    * If data fits the constraints, it contributes to **$H^0$ (Global Section)**.
    * If data fails (torsion), it is isolated in the **$H^1$ (Waste Stream)**.
4.  **Auditor:** Heuristic logic is applied to analyze the source of the Torsion.

## 📝 CITATION

If you use this framework in your research, please cite as follows:

Nevalainen, S. (2025). *The Shape of Agreement: Topological Foundations for Cooperative Logistics*. Black River Systems Technical Report.

```bibtex
@techreport{nevalainen2025shape,
  title={The Shape of Agreement: Topological Foundations for Cooperative Logistics},
  author={Nevalainen, Shawn},
  year={2025},
  institution={Black River Systems},
  month={December}
}
