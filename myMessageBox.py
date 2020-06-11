from MsgBox import MsgBox

def myMessageBox():
    doc = XSCRIPTCONTEXT.getDocument()
    out = MsgBox(doc,"Schreibe 'Hallo Welt!' in das Dokument!","Ein Eintrag?",4,5)
    text = doc.getText()
    # Eine Zeichenkette wird ins Dokument geschrieben
    if out == 1:
        text.setString("Hallo Welt!")
