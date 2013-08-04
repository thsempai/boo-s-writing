# -*- coding: utf-8 -*

import pygtk
import gtk

import os

from tools import Dialog
from error_manager import BsWException
from translate import TRANSLATE
class Project(object):
    
    def __init__(self,**kwargs):

        if not kwargs.has_key('name'):
            kwargs['name'] = 'project'

        self.name = kwargs['name']
        self.path = None
        self.chapter = [{'name':'chap1','text':gtk.TextBuffer()}]
        self.current_chapter = self.chapter[0]

    def save(self,path=None):

        if not path:
            path = self.path

            if not path:
                raise BsWException('No path gived for saving!')

        if os.path.exists(path):
            dialog = Dialog(title=TRANSLATE['DIRECTORY_ALREADY_EXISTS']['fr'],message = TRANSLATE['DIRECTORY_ALREADY_EXISTS_TXT']['fr'])
            ok = dialog.run()
            dialog.destroy()

            if not ok:
                return
        else:
            os.makedirs(path)

            




            