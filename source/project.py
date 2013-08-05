# -*- coding: utf-8 -*

import pygtk
import gtk

import os

from tools import Dialog
from error_manager import BsWException
from translate import TRANSLATE
from tools import Dialog, FileChooserDialog

class Project(object):
    
    def __init__(self,**kwargs):

        self.path = None
        self.create_project()
        self.save()

        self.chapter = [{'name':'chap1','text':gtk.TextBuffer()}]
        self.current_chapter = self.chapter[0]

    def create_project(self):
        dialog = Dialog(title=TRANSLATE['NEW_PROJECT']['fr'],message=TRANSLATE['NEW_PROJECT_TXT']['fr'],entry=True)
        project_name = dialog.run()

        if project_name:
            self.name = project_name
        dialog.destroy()

    def save(self,path=None):

        if self.path is None:

            file_dialog = FileChooserDialog(TRANSLATE['SAVE_PROJECT']['fr'])
            directory_path = file_dialog.run()
            file_dialog.destroy()

            file_name = self.name
            file_name = file_name.replace('-','_')
            file_name = file_name.replace(' ','_')

            path = directory_path + '/' + file_name

            if os.path.exists(path):
                dialog = Dialog(title=TRANSLATE['DIRECTORY_ALREADY_EXISTS']['fr'],message = TRANSLATE['DIRECTORY_ALREADY_EXISTS_TXT']['fr'])
                ok = dialog.run()
                dialog.destroy()

                if not ok:
                    return
            else:
                os.makedirs(path)

            




            