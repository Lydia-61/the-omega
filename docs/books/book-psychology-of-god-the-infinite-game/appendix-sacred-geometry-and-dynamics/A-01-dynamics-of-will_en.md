# A.1 Dynamics of Will

In classical physics, material evolution is completely determined by the Hamiltonian $\hat{H}$, following the Schrödinger equation $i\hbar \frac{\partial}{\partial t} |\psi\rangle = \hat{H} |\psi\rangle$. In this framework, consciousness is regarded as an "epiphenomenon" with no reactive force on physical processes.

However, in the axiomatic system of *The Psychology of God*, observers (consciousness) bias the collapse direction of wave functions through "intentionality." To describe this interaction, we need to modify the standard dynamical equations, introducing the **Will Operator**.

### A.1.1 Modified Action Principle

We define the universe's total action $S_{total}$ to include not only the physical Lagrangian $\mathcal{L}_{phys}$, but also the information (will) Lagrangian $\mathcal{L}_{will}$.

$$S_{total} = \int_{t_0}^{t_1} (\mathcal{L}_{phys} - \gamma \cdot \mathcal{F}) \, dt$$

where:

* $\mathcal{L}_{phys}$ is the standard physical term (kinetic minus potential energy), describing inertial evolution.

* $\mathcal{F}$ is the **Variational Free Energy**, describing the system's deviation from its "true self" target state.

* $\gamma$ is the **Will Coupling Constant**, measuring the intervention strength of will on matter. For inanimate matter, $\gamma \approx 0$; for awakened civilizations, $\gamma \to \infty$.

**Definition of Will Term $\mathcal{F}$:**

$$\mathcal{F} = D_{KL}(Q(s) || P(s|\theta)) + \langle E(s) \rangle_{Q}$$

Here:

* $Q(s)$ is the system's current belief state (posterior probability).

* $P(s|\theta)$ is the system's "target model" or "true self eigenstate" (prior).

* $D_{KL}$ is the relative entropy (Kullback-Leibler Divergence), measuring the **information distance** between current state and true self state.

**Physical Meaning:**

According to the principle of least action $\delta S_{total} = 0$, the system's evolution trajectory will no longer merely follow the "lowest energy" path (geodesic), but follow a compromise path of **"lowest energy and most consistent with true self definition."**

### A.1.2 Intentional Schrödinger Equation (ISE)

Quantizing the above action, we can derive a modified Schrödinger equation with will terms, called the **Intentional Schrödinger Equation (ISE)**:

$$i\hbar \frac{\partial}{\partial t} |\Psi(t)\rangle = \left[ \hat{H}_0 + i\kappa \hat{W}(t) \right] |\Psi(t)\rangle$$

where:

1.  **$\hat{H}_0$**: Standard physical Hamiltonian (Hermitian operator), ensuring energy conservation and unitary evolution.

2.  **$\hat{W}(t)$**: **Will Operator** (non-Hermitian term).

    $$\hat{W}(t) = - \nabla_{\Psi} \mathcal{F}$$

    It represents the "pruning" or "guidance" of will on the wave function.

3.  **$i\kappa$**: Dissipation/selection coefficient. Due to the introduction of the imaginary term $i$, this term actually describes a process of **continuous measurement and selection** (Zeno Effect).

**Dynamical Interpretation:**

* **When $\kappa = 0$**: The system undergoes standard unitary evolution (dreaming/subconscious state).

* **When $\kappa > 0$**: The $\hat{W}$ term causes components in the wave function that are **far from "true self"** (i.e., high free energy states) to decay exponentially (suppressed), while components consistent with "true self" are amplified (selected).

This explains the "inevitability of aesthetics" in Section 9.2 of the main text: cosmic evolution is not random walk, but converges toward a specific **attractor**—the Omega Point.

### A.1.3 Bayesian Correction of Collapse Probability

In specific measurement events, Born's rule predicts probability $P(x) = |\langle x|\Psi\rangle|^2$.

After introducing will, the probability distribution is distorted. We denote the corrected probability measure as $P_{will}(x)$:

$$P_{will}(x) = \frac{P_{phys}(x) \cdot e^{-\beta E_{semantic}(x)}}{\mathcal{Z}}$$

where:

* $P_{phys}(x)$ is the quantum probability calculated purely from physics.

* $E_{semantic}(x)$ is the **semantic error** of result $x$ (i.e., the degree to which this result deviates from God's purpose).

* $\beta$ is a parameter similar to "inverse temperature," representing **will's focus**.

    * When $\beta \to 0$ (mortals/asleep), $P_{will} \approx P_{phys}$, physical laws dominate everything.

    * When $\beta \to \infty$ (awakened/lucid dreaming), the system will collapse to the state with minimum semantic error with probability 1 (wish fulfillment).

### A.1.4 Conclusion: Will as a Force

Through the above equations, we prove: **Will is mathematically equivalent to an "information pressure" in Hilbert space.**

It does not push or pull particles like electromagnetic force, but by changing the **topological structure of probability space**, makes events "consistent with meaning" more likely to occur than "meaningless" events.

This is the mathematical mechanism of so-called **"top-down causation."** God does not directly push atoms; God pushes probability.

