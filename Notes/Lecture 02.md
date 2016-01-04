The cable equation
==================

*A. Roth*

How do neurons transform synaptic inputs into AP output? What are the functional compartments in neurons (spines, spine clusters, branchlets and dendritic regions)?

Ingredients
-----------

- Membrane potential V(x,t)
- Axial current i_a(x,t)
- Membrane current i_m(x,t)

Parameters:

- Specific resistivity of intracellular medium R_i = 70-150 Ωcm (these units are due to R = R_i * L * A where A = πd²/4)

- Specific capacity of the cell membrane C_m = ~1μF cm⁻²

- Specific membrane resistance R_m = 10 to 100 kΩ cm²

The equation
------------

λ² d²V/dx² = (V - Vrest) + τ_m dV/dt - r_m i_pip(x,t)
