# Appendix A: Mathematical Formalism and Notation

**(附录 A：数学形式体系与符号定义)**

> **"To ensure the rigor and falsifiability of this book's theory, this appendix provides strict mathematical definitions of the core concepts of Interactive Computational Cosmology (ICC). These definitions constitute the formal foundation for all inferences in the main text, for professional readers in physics, computer science, and mathematics to consult and verify."**

In the main text, we combined physical intuition with engineering metaphors in our narrative. Here, we restore these concepts to pure **Mathematical Structures**. The ICC model is built at the intersection of quantum information theory, operator algebra, and computational complexity theory.

## A.1 Spacetime Lattice and Hilbert Space

ICC model assumes physical reality is discrete at the microscopic level. We define spacetime as a **Discrete Manifold** or **Graph**.

**Definition A.1.1 (Holographic Lattice $\Lambda$)**

Spacetime background is defined as a $D$-dimensional lattice graph $\Lambda = (V, E)$, where:

* $V$ is the set of vertices, representing the smallest spatial units (Planck volume $l_P^3$). $|V| < \infty$ (according to the finite information axiom).

* $E$ is the set of edges, representing local interactions or adjacency relations.

* **Distance Metric**: The distance $d(x, y)$ on the graph is defined as the number of edges on the shortest path connecting vertices $x, y \in V$.

**Definition A.1.2 (Global Hilbert Space $\mathcal{H}_{total}$)**

The system's global state space is the tensor product of local Hilbert spaces defined on $V$:

$$\mathcal{H}_{total} = \bigotimes_{x \in V} \mathcal{H}_x$$

where $\mathcal{H}_x \cong \mathbb{C}^d$ is the state space of qubits (or quantum logic gates) located at each node, with dimension $d$ usually taken as $2$ (Qubit).

Global dimension $\dim(\mathcal{H}_{total}) = d^{|V|}$.

## A.2 Algebraic Structure of the CITM

**(交互式图灵机 (CITM) 的代数结构)**

The physical model of local observers is formalized as an **interactive automaton**.

**Definition A.2.1 (CITM Six-Tuple)**

A classical interactive Turing machine is defined as a tuple $\mathcal{M} = (S, \Sigma, \Gamma, \delta, s_0, \mathcal{O})$, where:

* $S$: Finite set of internal states (classical physical states).

* $\Sigma$: Input alphabet (sensory data).

* $\Gamma$: Output alphabet (actions/measurements).

* $s_0 \in S$: Initial state.

* $\mathcal{O}$: **Oracle Interface**.

* $\delta$: **Transition Function**, defined as:

    $$\delta: S \times \Sigma \times \Omega \to S \times \Gamma$$

    where $\Omega$ is the output space of oracle $\mathcal{O}$.

**Definition A.2.2 (Oracle Function)**

Oracle $\mathcal{O}$ is a non-algorithmic mapping, representing the resolution of system uncertainty by the environment (or consciousness). Physically, it corresponds to the selection operator of **POVM (Positive Operator-Valued Measure)**:

$$\mathcal{O}(t): \rho_S(t) \to k \in \{1, \dots, N\}$$

where $k$ is the index of measurement results, satisfying Born's rule probability distribution $p_k = \text{Tr}(M_k \rho_S M_k^\dagger)$.

## A.3 The Holographic Isomorphism Map $\Phi$

**(全息同构映射 $\Phi$)**

This section provides the strict algebraic formulation of the **"Holographic Equivalence Principle"** in the main text.

Let $\mathfrak{A}$ be the observable algebra ($C^*$-algebra) of the global system, and $\mathfrak{B}$ be the observable algebra of the local system.

**Theorem A.3.1 (Physical Application of Stinespring Dilation Theorem)**

For any dissipative (non-unitary) dynamical map $\Lambda_t: \mathfrak{B} \to \mathfrak{B}$ experienced by a local observer (i.e., time evolution), if $\Lambda_t$ satisfies **Complete Positivity** and **Trace-Preserving**, then there necessarily exist:

1.  An environment Hilbert space $\mathcal{K}$.

2.  A global unitary operator $U_t \in \mathcal{L}(\mathcal{H}_S \otimes \mathcal{K})$.

3.  An isometric embedding $V: \mathcal{H}_S \to \mathcal{H}_S \otimes \mathcal{K}$.

Such that for any local state $\rho$, we have:

$$\Lambda_t(\rho) = \text{Tr}_{\mathcal{K}} (U_t (\rho \otimes |0\rangle\langle 0|) U_t^\dagger)$$

**Definition A.3.2 (Holographic Map $\Phi$)**

The map $\Phi$ defines the equivalence relation between **QTM View** and **CITM View**:

$$\Phi: \text{QTM}(\mathcal{H}_{total}, U) \xrightarrow{\cong} \text{CITM}(\mathcal{H}_S, \mathcal{O})$$

This map is bijective if and only if the observer cannot access environmental degrees of freedom $\mathcal{K}$. Physically, this corresponds to the existence of a **Horizon**.

## A.4 Complexity Classes and Physical Limits

**(计算复杂性类与物理极限)**

The boundaries of physical laws are defined by computational complexity theory.

**Definition A.4.1 (Physically Realizable Class BQP)**

All physically observable processes must belong to the **Bounded-Error Quantum Polynomial-Time (BQP)** complexity class.

$$\text{Physics} \subseteq \text{BQP}$$

This means that any physical process requiring exponential time (such as solving NP-complete problems) to complete (e.g., traversing all many-world branches) is **Physically Forbidden** within macroscopic finite time.

**Corollary A.4.1 (Inaccessibility of Many Worlds)**

Since verifying "other parallel universes exist" requires performing quantum state tomography or reversing decoherence, its complexity belongs to **QMA-Hard** or higher. Therefore, for BQP-restricted observers, many worlds are **computationally undecidable**. This constitutes solid mathematical grounds for the CITM model's single-history view.

## A.5 Topological Index of Consciousness $\nu$

**(意识的拓扑指标 $\nu$)**

In Chapter 8, we defined consciousness as a topological soliton in causal networks. Here we provide its algebraic topological definition.

**Definition A.5.1 (Strongly Connected Components of Causal Graph)**

Let the causal influence graph of the system within time window $\tau$ be $G_\tau$. Define $C_i$ as the **Strongly Connected Component (SCC)** in the graph, i.e., for any two points $a, b$ within the component, there exist paths $a \to b$ and $b \to a$.

**Definition A.5.2 (Integrated Information $\Phi_{IIT}$)**

According to Tononi's Integrated Information Theory (IIT), the system's level of consciousness is related to the Minimum Information Partition (MIP) of the causal network:

$$\Phi_{IIT} = D_{KL}(P_{whole} || P_{partitioned})$$

**Definition A.5.3 (Topological Consciousness Index $\nu$)**

We define consciousness as a $\mathbb{Z}_2$ topological invariant. For any subsystem $\Omega$:

$$\nu(\Omega) = \begin{cases} 1 & \text{if } \Omega \text{ is a MSCC and } \Phi_{IIT}(\Omega) > \text{Threshold} \\ 0 & \text{otherwise} \end{cases}$$

* **$\nu=1$**: This subsystem is an **Autonomous Agent**, possessing an oracle interface.

* **$\nu=0$**: This subsystem is an **Automaton**, only performing feedforward computation.

## A.6 Summary

**(总结)**

This appendix proves that *Principles of Interactive Computational Cosmology* is not built on empty philosophical speculation but on strict mathematical structures at the intersection of **Quantum Mechanics (unitarity), Thermodynamics (entropy bounds), and Computer Science (complexity)**.

All narratives in the main text are **holographic projections** of the above mathematical equations in natural language.
