#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import io
import os
import collections
import wx
import sys
from wx.lib.mixins.listctrl import ColumnSorterMixin

#Sletter gamle filer før innlastning av nye:

try:
    os.remove("availability.txt")
except OSError:
    pass

try:
    os.remove("stations.txt")
except OSError:
    pass

try:
    os.remove("availability_match.txt")
except OSError:
    pass
	
#Kobler til data fra oslobysykkel med HTTP-bibloteket "requests": http://docs.python-requests.org/en/master/

url_stations = 'https://oslobysykkel.no/api/v1/stations'
headers_stations = {'Client-Identifier': 'Your ID Goes Here'}
r_stations = requests.get(url_stations, headers=headers_stations)

url_availability = 'https://oslobysykkel.no/api/v1/stations/availability'
headers_availability = {'Client-Identifier': 'Your ID Goes Here'}
r_availability = requests.get(url_availability, headers=headers_availability)

#Dekoder JSON med json-bibloteket og printer dataene (kommentert ut): https://docs.python.org/2/library/json.html#

data_stations = json.loads(r_stations.text)
data_availability = json.loads(r_availability.text)

j_stations = r_stations.json()
j_availability = r_availability.json()

#Henter ut verdier som skal brukes senere:

json_object_stations = json.loads(r_stations.text)
json_object_availability = json.loads(r_availability.text)


#Siden det finnes stasjoner i json-dataene for availability med "-1" locks og bikes,
#måtte jeg filtre de ut for å få en pen liste. Det er totalt 32 stasjoner som ikke finnes i json-dataene for stations, men som har "Locks: -1, Bikes: -1".

for each in j_stations['stations']:
	stations_file = open("stations.txt","a")
	stations_file.write("ID: ")
	stations_file.write(str(each['id']) + ", ")
	stations_file.write("Lokasjon: ")
	stations_file.write(str(each['title'].encode('utf-8')) + ", ")
	stations_file.write(str(each['subtitle'].encode('utf-8')) + ", ")
	stations_file.write("\n")
	stations_file.close()

for each in j_availability['stations']:
	stations_file = open("availability.txt","a")
	stations_file.write("ID: ")
	stations_file.write(str(each['id']) + ", ")
	stations_file.write("Locks: ")
	stations_file.write(str(each['availability']['locks']) + ", ")
	stations_file.write("Bikes: ")
	stations_file.write(str(each['availability']['bikes']) + "')")
	stations_file.write("\n")
	stations_file.close()

x=0

#Lager ny liste over alle stasjoner som ikke har "Locks: -1, Bikes: -1":

with open("availability_match.txt", 'a') as file:
	file.write("{\n")

for each in j_stations['stations']:
	x += 1
	stringToMatch = str(each['id'])
	matchedLine = ''

	with open("availability.txt", 'r') as file:
		for line in file:
			if stringToMatch in line:
				matchedLine = line
				break

#Formaterer som dictionary for visning senere
	with open("availability_match.txt", 'a') as file:

		Testline = matchedLine.strip('\n')
		Testline = Testline.replace(",", "', '")
		file.write(str(x) + " : ('" + str(each['title'].encode('utf-8').replace("'", "")) + " " + str(each['subtitle'].encode('utf-8').replace("'", "")) + "', '" + Testline + ",\n")

with open("availability_match.txt", 'rb+') as filehandle:
	filehandle.seek(-3, os.SEEK_END)
	filehandle.truncate()
with open("availability_match.txt", 'a') as file:
	file.write("\n}")

#Bruker Pythonwx, lånt metode fra http://zetcode.com/wxpython/advanced/

f = open('availability_match.txt','r')

bikestations = eval(f.read())



class SortedListCtrl(wx.ListCtrl, ColumnSorterMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        ColumnSorterMixin.__init__(self, len(bikestations))
        self.itemDataMap = bikestations

    def GetListCtrl(self):
        return self

class Bikestations(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(710, 500))

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, -1)

        self.list = SortedListCtrl(panel)
        self.list.InsertColumn(0, 'Lokasjon', width=400)
        self.list.InsertColumn(1, 'Identifikasjon', width=90)
        self.list.InsertColumn(2, 'Sykkellåser', wx.LIST_FORMAT_RIGHT, 90)
        self.list.InsertColumn(3, 'Sykkler', width=90)

        items = bikestations.items()

        for key, data in items:
            index = self.list.InsertItem(sys.maxint, data[0])
            self.list.SetItem(index, 1, data[1])
            self.list.SetItem(index, 2, data[2])
            self.list.SetItem(index, 3, data[3])
            self.list.SetItemData(index, key)

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)

app = wx.App()
Bikestations(None, -1, 'Oslo Bysykkel')
app.MainLoop()