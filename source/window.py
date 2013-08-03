# -*- coding: utf-8 -*-

import pygtk
import gtk

from translate import TRANSLATE
from data import TITLE, DEFAULT_SIZE

class MainWindow(object):

    def __init__(self):

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title(TITLE)
        self.window.set_default_size(*DEFAULT_SIZE)

        self.window.connect("destroy", self.destroy)
        self.window.connect("delete_event", self.delete_event)

        self.window.set_border_width(10)

        # disvison de la fenêtre

        self.main_box = gtk.VBox(homogeneous=False)
        self.main_box.show()

        self.work_box = gtk.HBox(homogeneous=False)
        self.work_box.show()
        self.main_box.pack_end(self.work_box,expand=True,fill=True,padding=2)

        self.left_box = gtk.VBox(homogeneous=False)
        self.work_box.pack_start(self.left_box,expand=True,fill=False,padding=2)

        self.window.add(self.main_box)

        # ajout du menu

        menu_bar = gtk.MenuBar()
        self.main_box.pack_start(menu_bar,expand=False,fill=False,padding=2)
        menu_bar.show()

        self.menu = {}
        
        menu_file = gtk.Menu()
        self.menu['file'] = gtk.MenuItem(label=TRANSLATE['FILE']['fr'])
        self.menu['file'].set_submenu(menu_file)
        menu_bar.append(self.menu['file'])

        # into menu file

        self.menu['save'] = gtk.MenuItem(label=TRANSLATE['SAVE']['fr'])
        menu_file.append(self.menu['save'])


        self.widget = {}

        #ajout de la zone d'écriture
        self.widget['writing zone'] = gtk.TextView()

        self.work_box.pack_start(self.widget['writing zone'],expand=True,fill=True,padding=2)

        # affichage 

        for widget in self.widget.values():
            widget.show()

        for menu in self.menu.values():
            menu.show()

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