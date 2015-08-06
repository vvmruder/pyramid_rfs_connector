# -*- coding: iso-8859-1 -*-

# Copyright (c) 2012 - 2015, GIS-Fachstelle des Amtes für Geoinformation des Kantons Basel-Landschaft
# All rights reserved.
#
# This program is free software and completes the GeoMapFish License for the geoview.bl.ch specific
# parts of the code. You can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

__author__ = 'Clemens Rudert'

from python_webdav.connection import Connection, Client
import os
import base64
import binascii





"""
WebDavConnection stellt einen vereinfachten Zugriff auf Webdavressourcen zur Verfuegung.
Die Klasse wird erzeugt indem
ihr die URL (komlette URL z.B.: https://www.geo.bl.ch/webdav/baugesuchsscan_temp/) uebergeben wird.
Es ist moeglich Nutzername und Passwort zu uebergeben. Falls dies nicht geschieht, wird eine Anfrage ohne Nutzerdaten
gestartet.

Standardmaessig nutzt dieser Helper den Pfad CERT_PATH = "/etc/ssl/certs/ca-certificates.crt" um alle verfuegbaren
Certifikate nutzen zu koennen. Das kann angepasst werden.
ACHTUNG: Anpassung an httplib2 wegen Problems mit SSL3 Verbindungen. => Siehe Workaround for SSL3.

Standardmaessig nutzt dieser Helper den Pfad LOCAL_PATH = "/var/sig/public/" um heruntergeladene Dateien abzuspeichern.
Das kann geaendert werden.
ACHTUNG: Schreibrechte pruefen!
"""


class WebDavConnection():
    CERT_PATH = "/etc/ssl/certs/ca-certificates.crt"
    LOCAL_PATH = "/var/sig/public/"

    def __init__(self, url, username='', password=''):
        self.connection = Connection(
            {'host': url, 'port': 443, 'username': username, 'password': password, 'realm': '', 'path': ''})
        self.connection.httpcon.ca_certs = self.CERT_PATH
        self.webdavclient = Client()
        self.url = url

    def download_file(self, remote_file_name):
        try:
            self.webdavclient.get_file(self.connection, remote_file_name, self.LOCAL_PATH + remote_file_name)
            f = open(self.LOCAL_PATH + remote_file_name)
            file_data = f.read()
            if '404 Not Found' in file_data:
                os.remove(self.LOCAL_PATH + remote_file_name)
                return None
            else:
                return self.LOCAL_PATH + remote_file_name
        except Exception as e:
            print e
            pass

    def upload_file(self, remote_file_name, local_file_name):
        try:
            self.webdavclient.send_file(self.connection, remote_file_name, self.LOCAL_PATH + local_file_name)
            #return self.url + remote_file_name
        except Exception as e:
            print e
            pass
        
    def send_put(self, remote_file_name, local_file_name):
        try:
            f = open(self.LOCAL_PATH + local_file_name, 'rb')
            data = f.read()
            self.connection.send_put(self.url + remote_file_name.encode('utf-8'), data)
            #return self.url + remote_file_name
        except Exception as e:
            print e
            pass