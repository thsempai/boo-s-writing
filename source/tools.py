
import pygtk
import gtk

class Dialog(gtk.Dialog):

    def __init__(self,title,message=None,parent=None,entry=False,modal=True,buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_OK, gtk.RESPONSE_OK)):


        self.entry = None

        flags = gtk.DIALOG_DESTROY_WITH_PARENT

        if modal:
            flags |= gtk.DIALOG_MODAL

        super(Dialog,self).__init__(title = title, parent = parent,flags = flags ,buttons=buttons)

        label = gtk.Label(message)

        self.vbox.pack_start(label)
        
        if entry:
            self.entry = gtk.Entry()
            self.vbox.pack_end(self.entry)

        self.show_all()

    def run(self):
        
        result = super(Dialog, self).run()

        if result == gtk.RESPONSE_OK:
            if self.entry:
                ret = self.entry.get_text()
            else:
                ret = True
        else:
            ret = None
        return ret


class FileChooserDialog(gtk.FileChooserDialog):
    
    def __init__(self,title,parent=None,action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_OK, gtk.RESPONSE_OK)):

        super(FileChooserDialog,self).__init__(title=title, parent=parent, action=action, buttons=buttons, backend=None)

    def run(self):
        result = super(FileChooserDialog, self).run()

        if result == gtk.RESPONSE_OK:
            file_name = self.get_filename()
        else:
            file_name = None
        return file_name