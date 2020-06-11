import uno
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxResults import OK, YES, NO, CANCEL

def MsgBox(doc, msgText, msgTitle, msgType, msgButtons):
    """
    Parameter: 
    msgText  :  Der Text in der MessageBox
    msgTitel :  Text der Titelleiste
    msgType  :  MESSAGEBOX = 0
                INFOBOX    = 1
                WARNINGBOX = 2
                ERRORBOX   = 3
                QUERYBOX   = 4

    msgButtons: BUTTONS_OK                 = 0
                BUTTONS_OK_CANCEL          = 1
                BUTTONS_YES_NO             = 2
                BUTTONS_YES_NO_CANCEL      = 3
                BUTTONS_RETRY_CANCEL       = 4
                BUTTONS_ABORT_IGNORE_RETRY = 5

    Rückgabewerte:  CANCEL = 0
                    OK     = 1
                    YES    = 2
                    NO     = 3
                    RETRY  = 4
                    IGNORE = 5
    """ 

    ctx = uno.getComponentContext()
    smgr = ctx.ServiceManager
    toolkit = smgr.createInstanceWithContext('com.sun.star.awt.Toolkit', ctx)
    parentWin = doc.CurrentController.Frame.ContainerWindow
    mBox = toolkit.createMessageBox(parentWin, msgType, msgButtons, msgTitle, msgText)
    return mBox.execute()




