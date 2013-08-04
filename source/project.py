# -*- coding: utf-8 -*

import pygtk
import gtk

class Project(object):
    
    def __init__(self):

        self.name = 'project'
        self.path = None
        self.chapter = [{'name':'chap1','text':gtk.TextBuffer()}]
        self.current_chapter = self.chapter[0]