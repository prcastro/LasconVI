Matching Passive
================

Passive models are useful to model subthreshold mechanisms.

Problems
--------

- Spines
- Errors in parameters/recordings
- How to deal with voltage-gated channels

Reconstruction of cell morphology
---------------------------------

Inspecting microscopy and estimating spines zooming into the effective surface (reconstructing the volume from slices).

Fitting voltage responses to current pulses
-------------------------------------------

Done using numerical optimization, so that the fit constrains R_m and C_m.

C = C_m * A = Q/V (V is measured right after the peak, see slides)

Since t_m = R_m * C_m, and we know t_m and C_m, we also know R_m. To estimate the statistical errors, a bootstrap procedure is used.

Post-Sinaptic currents
----------------------

Post sinaptic currents are simulated with smooth currents injected at the artifical cell.
