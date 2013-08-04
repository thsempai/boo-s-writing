# -*- coding: utf-8 -*

import pygtk
import gtk

class Project(object):
    
    def __init__(self,**kwargs):

        if not kwargs.has_key('name'):
            kwargs['name'] = 'project'

        self.name = kwargs['name']
        self.path = None
        self.chapter = [{'name':'chap1','text':gtk.TextBuffer()}]
        self.current_chapter = self.chapter[0]