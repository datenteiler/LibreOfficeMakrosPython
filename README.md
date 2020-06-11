# LibreOffice Makros in Python

Die Python-Skripte mit den Makros speichert man Verzeichnis "~/.config/libreoffice/4/user/Scripts/python/" untergebracht, damit sie im Pythonpfad sind und von LibreOffice erkannt werden. Unter Windows ist der Pfad "%appdata%\LibreOffice\4\user\Scripts\python". Das Verzeichnis muss vermutlich noch angelegt werden. Wichtig ist bei beiden Systemen, auf die Schreibweise der Verzeichnisnamen zu achten: Es muss "Scripts\python" heißen, mit großem „S“ in „Scripts“ und kleinem „p“ in „python“.

Dateien mit Funktionen/Modulen, die von verschiedenen Dateien aus importiert werden sollen, müssen im Unterverzeichnis "~/.config/libreoffice/4/user/Scripts/python/pythonpath/" liegen, denn auch dieses Verzeichnis liegt im Pythonpfad.
