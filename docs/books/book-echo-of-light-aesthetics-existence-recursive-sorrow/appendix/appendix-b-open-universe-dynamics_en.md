# Appendix B: Open Universe Dynamics — Mathematical Models of Capacity Growth and Red Queen Games

This appendix provides dynamical proofs for Chapter 9 "Rejecting Heat Death" and Chapter 12 "No Omega Point." We will construct coupled equations describing the evolution of cosmic capacity, entropy, and agent complexity over time.

## B.1 Dynamic Bekenstein Bound

Consider an expanding universe dominated by dark energy $\Lambda$.

Although the event horizon is fixed, for computational cosmology, what matters more is the **number of computational nodes (QCA lattice points) within comoving volume** $N(t)$.

In QCA expansion model (node addition model):

$$N(t) \propto a(t)^3 \propto e^{3Ht}$$

where $H = \sqrt{\Lambda/3}$ is the Hubble constant.

The universe's potential **information capacity upper limit** $I_{max}(t)$ grows with $N(t)$:

$$I_{max}(t) \sim N(t) \sim e^{3Ht}$$

## B.2 Limits on Entropy Production

The universe's **used information (entropy)** $S(t)$ mainly comes from matter particle decoherence and black hole radiation.

Since total matter is conserved (or grows slower than volume), and computation processes are limited by light speed (Bremermann Limit):

$$\frac{dS}{dt} \le \frac{E_{total}}{\hbar} \cdot N_{particles}$$

In a sparse universe, $S(t)$ growth is at most linear or polynomial, far below $I_{max}(t)$'s exponential growth.

**Corollary B.1 (Infinite Blank Theorem)**:

$$\lim_{t \to \infty} \frac{S(t)}{I_{max}(t)} = 0$$

The universe's **Filling Ratio** tends to zero. This means the universe is forever "new," and heat death ($S \to I_{max}$) is mathematically impossible.

## B.3 Red Queen Game Equations

We use a variant of **Lotka-Volterra equations** to describe the game between agents ($A$) and environmental entropy ($E$).

* **Agent complexity ($C$)**: Represents $M_I$.

* **Environmental entropy pressure ($P$)**: Represents survival difficulty.

$$

\begin{cases}

\frac{dC}{dt} = \alpha C \cdot P - \beta C^2 & (\text{pressure drives evolution, but limited by metabolic cost}) \\

\frac{dP}{dt} = \gamma C - \delta P & (\text{intelligent activity produces waste heat increasing pressure, expansion dilutes pressure})

\end{cases}

$$

* **$\alpha C P$**: Red Queen term. The harsher the environment ($P$ large), the faster agents evolve to survive.

* **$\gamma C$**: Landauer waste heat term. Higher intelligence emits more entropy, pushing $P$ higher.

* **$-\delta P$**: Cosmic expansion term. Rapid space expansion dilutes waste heat.

**Phase Plane Analysis**:

When $\delta$ (expansion rate) is sufficiently large, this system has no stable fixed point (death), but forms **Limit Cycles** or **eternally diverging spirals**.

**Conclusion**:

As long as cosmic expansion ($\delta > 0$) can timely remove waste heat, agents can achieve **infinite exponential growth** in complexity through continuous arms races ($\alpha, \gamma$ cycles).

**Civilization's immortality is built on the foundation of cosmic expansion.**

