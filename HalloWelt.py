def MeinErstesMakro():
    # Das Dokument aus dem Skriptkontext: 
    doc = XSCRIPTCONTEXT.getDocument()
    # Das text-Objekt mit getText()
    text = doc.getText()
    # Eine Zeichenkette wird ins Dokument geschrieben
    text.setString('Hallo Welt in Writer mit Python')
    return


