# -*- coding: utf-8 -*-

import pygtk
import gtk

from translate import TRANSLATE
from data import TITLE, DEFAULT_SIZE, PROGRAM_ICON, INPUT_WINDOW_SIZE
from project import Project
from tools import Dialog, FileChooserDialog

from error_manager import BsWException

class MainWindow(object):

    def __init__(self):

        #project courant

        self.current_project = Project()

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_icon_from_file(PROGRAM_ICON)

        self.window.set_title(TITLE + ' ('+ self.current_project.name + ')')
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
        self.widget['writing_zone'] = gtk.TextView(self.current_project.current_chapter['text'])

        self.work_box.pack_start(self.widget['writing_zone'],expand=True,fill=True,padding=2)

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


    def new_project(self, args):
        try:

            dialog = Dialog(title=TRANSLATE['NEW_PROJECT']['fr'],message=TRANSLATE['NEW_PROJECT_TXT']['fr'],parent=self.window,entry=True)
            new_project_name = dialog.run()

            if new_project_name:
                self.window.set_title(TITLE + ' ('+ new_project_name + ')')
            
                self.current_project = Project(name=new_project_name)
                self.widget['writing_zone'].set_buffer(self.current_project.current_chapter['text'])
            dialog.destroy()
        except Exception as e:
            raise BsWException(e.message,e)
            


    def save_current_project(self, args):
        try:
            if self.current_project.path:
                self.current_project.save()
            else:

                file_dialog = FileChooserDialog(TRANSLATE['SAVE_PROJECT']['fr'])
                directory_path = file_dialog.run()
                file_dialog.destroy()

                file_name = self.current_project.name
                file_name = file_name.replace('-','_')
                file_name = file_name.replace(' ','_')

                self.current_project.save(directory_path+'/'+file_name)
        except Exception as e:
            raise BsWException(e.message,e)


    def destroy(self, widget, data=None):
        gtk.main_quit()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()
