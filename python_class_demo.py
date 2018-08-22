#!/usr/bin/env python

from class_example.class_example import ClassExample
from class_example.other_class_example import OtherClassExample
from class_example.example_interface import ExampleInterface

print( "--- Class Example ---")

class_a = ClassExample()
class_b = OtherClassExample()

print( "ClassExample->process_val(2): %d" % class_a.process_val(2) )
print( "ClassExample->process_other_val(2): %d" % class_a.process_other_val(2) )
print( "OtherClassExample->process_val(2): %d" % class_b.process_val(2) )

print( "--- Class as Interface ---")

a = 5
b = 1

interface = ExampleInterface(a, b)

print("InterfaceExample->a: (%s) %s" % (type(interface.a).__name__, str(interface.a)) )
print("InterfaceExample->b: (%s) %s" % (type(interface.b).__name__, str(interface.b)) )
