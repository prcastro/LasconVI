#!/usr/bin/env python

# run using command line: 'python -i cable.py'

from neuron import gui, h  # h stands for hoc

# create the cable
cable = h.Section()  # the name here is used for graphics but doesn't produce a hoc pointer
cable.L, cable.diam, cable.nseg = 10000, 1, 1001 # microns, microns, num
cable.insert('hh')  # this is a SECTION level call that puts 'pas' into all of the 1001 SEGMENTs
# cable.g_pas, cable.e_pas = 1/20000.0, -65  # 1/(Ohm cm^2) = Siemens/cm^2, mV;  this access will set all of the segments

cabref = h.SectionRef(sec=cable)  # a workaround to end up with a hoc object that points to the python object
h('objref cable')  # creates the object reference in hoc
h.cable=cabref     # aligns the pointers; if had a hoc file that defined the cell would go other direction

h.xopen("cable.ses")

# here's a more pythonic way to set pas params that accesses segments via dot notation
# def setpas (sec, gpas=1/20000, epas=-65):  # provide defaults
#     for seg in sec:                        # iterate over all of the segments in a section
#         seg.pas.g, seg.pas.e = gpas, epas  # this is the more pythonic segmentwise way to do this
#
# setpas(cable)
