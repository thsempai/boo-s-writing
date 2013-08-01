# -*- coding: utf-8 -*-

import pygtk
import gtk

from data import TITLE, DEFAULT_SIZE

class MainWindow(object):

    def __init__(self):

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title(TITLE)
        self.window.set_default_size(*DEFAULT_SIZE)

        self.window.connect("destroy", self.destroy)
        self.window.connect("delete_event", self.delete_event)

        self.window.set_border_width(10)

        # fenêtre en 3 parties

        self.table = gtk.Table(columns=3, rows=3, homogeneous=True)
        self.window.add(self.table)


        self.widget = {}

        self.widget['tag list'] = gtk.TreeView()
        self.widget['note list'] =  gtk.TreeView()
        self.widget['story list'] = gtk.TreeView()

        self.table.attach(self.widget['tag list'],0,1,0,1)
        self.table.attach(self.widget['note list'],0,1,1,2)
        self.table.attach(self.widget['story list'],0,1,2,3)

        self.widget['writing zone'] = gtk.TextView()

        self.table.attach(self.widget['writing zone'],1,2,0,3)

        for widget in self.widget.values():
            widget.show()

        self.table.show()
        self.window.show()



    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.

        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()