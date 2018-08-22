#!/usr/bin/env python

from class_example.class_example import ClassExample
from class_example.other_class_example import OtherClassExample

interface = ClassExample()
other_interface = OtherClassExample()

print( "ClassExample->process_val(2): %d" % interface.process_val(2) )
print( "ClassExample->process_other_val(2): %d" % interface.process_other_val(2) )
print( "OtherClassExample->process_val(2): %d" % other_interface.process_val(2) )
