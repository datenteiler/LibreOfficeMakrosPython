import sys
from MsgBox import MsgBox

def getPyVers():
    return "Die Python-Version ist {}.{}.{}".format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)

# Möchte man das Python-Makro aus der LO Symbolleiste aufrufen, erscheint die Fehlermeldung:
# "PythonVersion() takes 0 positional arguments but 1 was given".
# Die Methode ist so eingerichtet, dass sie keine Argumente akzeptiert. Das Argument 'self' wird 
# beim Aufruf der Methode aber implizit weitergereicht, so dass sie tatsächlich dann doch ein Argument erhält.
# Das Hinzufügen von 'self' zur Methodendefinition löst das Problem:
def PythonVersion(self):
    doc = XSCRIPTCONTEXT.getDocument()
    out = MsgBox(doc,getPyVers(),"Python-Version",1,0)

# Bei mehreren Methoden, werden alle exportiert,
# oder definiert, welche exportiert werden soll:
g_exportedScripts = PythonVersion,

