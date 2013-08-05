# -*- coding: utf-8 -*-

import pygtk
import gtk

from translate import TRANSLATE
from data import TITLE, DEFAULT_SIZE, PROGRAM_ICON, INPUT_WINDOW_SIZE
from project import Project


from error_manager import BsWException

class MainWindow(object):

    def __init__(self):

        #project courant

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_icon_from_file(PROGRAM_ICON)

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

        self.menu['new_project'] = gtk.MenuItem(label=TRANSLATE['NEW_PROJECT']['fr'])
        menu_file.append(self.menu['new_project'])

        self.menu['new_project'].connect_object("activate", self.new_project,())


        self.menu['save'] = gtk.MenuItem(label=TRANSLATE['SAVE']['fr'])
        menu_file.append(self.menu['save'])

        self.menu['save'].connect_object("activate", self.save_current_project,())


        self.widget = {}

        #ajout de la zone d'écriture
        self.widget['writing_zone'] = gtk.TextView()

        self.work_box.pack_start(self.widget['writing_zone'],expand=True,fill=True,padding=2)

        # affichage 

        for widget in self.widget.values():
            widget.show()

        for menu in self.menu.values():
            menu.show()

        self.window.show()
        self.new_project()


    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.

        return False


    def new_project(self, args=None):
        try:
            self.current_project =  Project()
            self.widget['writing_zone'].set_buffer(self.current_project.current_chapter['text'])
        except Exception as e:
            raise BsWException(e.message,e)
            
        self.window.set_title(TITLE + ' ('+ self.current_project.name + ')')

    def save_current_project(self, args):
        try:
            pass
        except Exception as e:
            raise BsWException(e.message,e)


    def destroy(self, widget, data=None):
        gtk.main_quit()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()
