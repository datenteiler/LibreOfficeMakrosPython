from InputBox import InputBox

def myInputBox():
	result = InputBox("Meine Nachricht","Mein Titel","Standard Text")
	doc = XSCRIPTCONTEXT.getDocument()
	text = doc.getText()
	text.setString(result)
