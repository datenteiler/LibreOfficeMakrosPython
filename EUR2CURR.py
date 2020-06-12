# coding: utf-8
from __future__ import unicode_literals
import urllib.request, uno, json

def EUR2CURR(currency):
    url = "https://api.exchangeratesapi.io/latest"
    request = urllib.request.urlopen(url)
    #response=requests.get(url)
    data = json.load(request)
    rate = data["rates"][currency]
    return rate
    
def data2sheet():
    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.getCurrentComponent()
    active_sheet = model.CurrentController.ActiveSheet
    
    cellC4 = active_sheet.getCellRangeByName("C4")
    cellC4.Value = format(EUR2CURR("USD"),'.2f')
    cellC5 = active_sheet.getCellRangeByName("C5")
    cellC5.Value = format(EUR2CURR("GBP"),'.2f')
    cellC6 = active_sheet.getCellRangeByName("C6")
    cellC6.Value = format(EUR2CURR("JPY"),'.2f')
    cellC7 = active_sheet.getCellRangeByName("C7")
    cellC7.Value = format(EUR2CURR("CNY"),'.2f')
    return

g_exportedScripts = data2sheet,
