import pygtk
import gtk

class BsWException(Exception):

    def __init__(self,message,exception=None,parent=None):
        
        super(BsWException,self).__init__()
        
        message = str(type(exception)) + ' : ' + message

        dialog_error = gtk.MessageDialog(parent=parent, flags=gtk.DIALOG_MODAL|gtk.DIALOG_DESTROY_WITH_PARENT, type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_OK,message_format = message)

        dialog_error.run()
        dialog_error.destroy()

        if exception:
            raise exception