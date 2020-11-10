#!/usr/bin/python

#the 3 lines below import the pygtk and gtk library. the second line

# verifies that we are using 2.0 or above versions of pygtk.

#import pygtk

#pygtk.require('2.0')

#import gtk
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# the line below cretes an object of type Window. gtk.WINDOW_TOPLEVEL means

# it is a normal window that we see.

window = Gtk.Window(title="Hello World")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()

