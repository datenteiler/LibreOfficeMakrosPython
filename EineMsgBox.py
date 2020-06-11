import uno
from msgbox import MsgBox

def MyMsgBox(msgText,msgType,msgTitle):
    # Auf den Kontext achten:
    msgbox = MsgBox(XSCRIPTCONTEXT.getComponentContext())
    msgbox.addButton("OK")
    msgbox.addButton("Cancel")
    msgbox.renderFromButtonSize()
    msgbox.numberOflines = 2
    return msgbox.show(msgText,msgType,msgTitle) 


def EineMsgBox():
    result = MyMsgBox("Eine kurze Nachricht.\nDie noch mehr sagen will.",1,"Der Titel")
    if result == "OK":
        # Auf den Kontext achten:
        doc = XSCRIPTCONTEXT.getDocument()
        # Auf die Texteigenschaft des Dokuments zugreifen
        text = doc.getText()
        # Eine Zeichenkette wird ins Dokument geschrieben
        text.setString('Hallo Welt in Writer mit Python')
    return
    
g_exportedScripts = EineMsgBox,
