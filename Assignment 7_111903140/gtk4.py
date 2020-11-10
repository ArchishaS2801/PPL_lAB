#!/usr/bin/env python


import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Hello World")
window.show()

#observe: All class names are in "Title case".

#Line below: b becomes an object of type Button with the text

# Hello PPL on in.

b = Gtk.Button("Hello PPL")

# this adds the button to the window. Try commenting the line below.

#Now we'll set some "event handlers"

def hello(widget, data=None):
 
    print ("hello there!",widget,data)

#in the above, observe what is printed for p. Note that it is the object (self) getting passed.

b.connect_object("clicked", hello, None) # "clicked" has been pre-defined by gtk to mean left-mouse click.

def delete_event(widget, data=None):

    print ("Delete event has occured")

    return False

def destroy(widget, data=None):

    print ("Destroy event has occured")

    Gtk.main_quit()
 
window.connect_object("delete_event",delete_event, None)

window.connect_object("destroy",destroy, None)

window.add(b)

window.show()

b.show()

Gtk.main()
