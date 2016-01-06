Qualitative Analysis of Dynamical Systems for Neuroscience
=============================================

Are there electrophysiological classes of neurons? Even cells from different morphologic classes can present the same behavior.

Understanding this can be done using bottom-up modeling, building simple models focusing on dynamical properties is these cells. The model will actually be the simplest one that accounts for phenomenology.

Base concepts
-------------

Dynamical system is an evolution rule in state space. These rules will define a trajectory in the state space.

Phenomenology
-------------
What do neurons do?


Modeling:
- Important variables
 - V
 - Conductance (ion)
- Qualitative behavior
 - AP (threshold)
 - Resting
 - PSP
 - All-or-None behavior
- Transformations/computations
 - Integrate
 - Comparisons

One-dimensional model
---------------------

When modeling, we start only with V as state variable. We can represent the state space on the real line, and represent the resting state as a point on the line (V*). Arrows would represent the movement on the line (the derivative). Instead of arrows, we could plot the magnitude of the arrows as a function of V. This function can be linear (see slides) or, more interestingly, a quadratic function

When the function is quadratic, we have two equilibrium points, a stable one (resting state) and an unstable one. After crossing the unstable equilibrium, the variable V will increase forever.

Another representation of a dynamical system is a landscape. If the landscape is defined by a function with a parameter (that changes the landscape),, onde of the values of this parameter leads to a qualitative change in behavior. This is a bifurcation (see slides).

Rheobase and threshold are not very mathematically very well defined concepts. Also, the only way to account for all the phenomenology is to use more dimensions.
