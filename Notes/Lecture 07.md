Modeling Synapses
=================

When neurotransmitters are released in the intra-synaptic space, it usually binds to ion channels, opening them. This causes a change in the voltage around the synapse region on the dendrite.

When a vesicle is released by the axon of a pre-synaptic cell, the change of the contact area causes a change of  its conductance.

The diffusion of the neurotransmitter in a private one-to-one synapse is much slower than the diffusion in a synaptic region between many cells.

We can probe the response of the Glutamate receptor, by  a fast application of Glutamate. The speed of binding of Glu (measured by the current due to the passage of ions through the Glu-activated channel) depends on the concentration of glutamate on the intra-synaptic region.

Monte-Carlo models simulate all the possible states of receptors, counting the number of bound Glu molecules and the activation of the channel.

The number of opened channels can be model by simple equations: they open quickly and close exponentially.

g = g_max (t - t0)/τ exp(t - t0/τ)
