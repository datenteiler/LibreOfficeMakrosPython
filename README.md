# LibreOffice Makros in Python

Die Python-Skripte mit den Makros werde im Verzeichnis `~/.config/libreoffice/4/user/Scripts/python/` abgespeichert, damit sie im Pythonpfad sind und von LibreOffice gefunden werden. Unter Windows ist das der Pfad `%appdata%\LibreOffice\4\user\Scripts\python`. Das Verzeichnis muss eventuell noch angelegt werden. Wichtig ist bei beiden Systemen, auf die Schreibweise der Verzeichnisnamen zu achten: Es muss `Scripts\python` heißen, mit großem "S" in "Scripts" und kleinem "p" in "python".

## Pythonpath
Dateien mit Funktionen/Modulen, die von verschiedenen Dateien aus importiert werden sollen, müssen im Unterverzeichnis `Scripts/python/pythonpath/` liegen, denn auch dieses Verzeichnis liegt im Pythonpfad.

## Makros ausführen
Um das Makro auszuführen, klickt man unter "Extras -> Makros -> Makros ausführen…", dann "Meine Makros" und wählt den Namen des Makros aus, unter dem die Python-Datei abgespeichert wurde. Es wird immer die Funktion selbst aufgerufen, so dass der komplette Code innerhalb von Funktionen sein sollte und nicht außerhalb davon.

## Das Argument 'self'
Möchte man das Python-Makro aus der Symbolleiste von LibreOffice aufrufen, erscheint die Fehlermeldung: "PythonVersion() takes 0 positional arguments but 1 was given". Die Methode ist so eingerichtet, dass sie keine Argumente akzeptiert. Das Argument 'self' wird aber beim Aufruf der Methode implizit weitergereicht, so dass sie tatsächlich dann doch ein Argument erhält. Das Hinzufügen von 'self', oder einem anderen, zur Not leeren Argument, zur Methodendefinition löst das Problem, z.B. in der Datei `PythonVersion.py`:
 
```python
def PythonVersion(self):
```
## Mehrere Methoden
Bei mehreren Methoden, werden alle exportiert. Um das zu verhindern können einzelne Methode definiert werden, welche exportiert werden sollen:

```python
g_exportedScripts = PythonVersion,
```

## Beispiel
Das Beispiel ist ein LibreOffice Calc Sheet, das Währungen in Euro umrechnet, nachdem man auf den Button "Umrechnen" geklickt hat. Das Python-Makro ist in das Dokument eingebettet. Damit das Sheet mit dem Makro in LibreOffice funktioniert, muss das "Sicherheitslevel" unter "Extras -> Optionen... -> Sicherheit -> Makrosicherheit..." auf **Mittel** gesetzt werden.
