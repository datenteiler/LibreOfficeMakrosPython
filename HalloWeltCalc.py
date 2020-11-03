## Im Terminal:
## soffice --calc --accept="socket,host=localhost,port=2002;urp;"

import uno
localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext(
 "com.sun.star.bridge.UnoUrlResolver", localContext)
ctx = resolver.resolve(
 "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext(
 "com.sun.star.frame.Desktop",ctx)

def MeinErstesMakroInCalc():
    workbook = desktop.getCurrentComponent()
    active_sheet = workbook.CurrentController.ActiveSheet
    cell = active_sheet.getCellRangeByName("B2")
    cell.String = "Hallo Welt!"

MeinErstesMakroInCalc()
