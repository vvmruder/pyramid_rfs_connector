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


class WebDavConnection():
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

    CERT_PATH = "/etc/ssl/certs/ca-certificates.crt"

    def __init__(self, url, username='', password=''):
        self.__url__ = url
        self.__username__ = username
        self.__password__ = password
        self.webdavclient = Client()

    def __create_connection__(self):
        connection = Connection({
            'host': self.__url__,
            'port': 443,
            'username': self.__username__,
            'password': self.__password__,
            'realm': '',
            'path': ''
        })
        connection.httpcon.ca_certs = self.CERT_PATH
        return connection

    def download_file(self, src, dst):
        try:
            client = Client()
            client.get_file(self.__create_connection__(), src, dst)
            f = open(dst)
            file_data = f.read()
            if '404 Not Found' in file_data:
                os.remove(dst)
                return None
            else:
                return dst
        except Exception as e:
            print e
            pass

    def upload_file(self, src, dst):
        try:
            client = Client()
            client.send_file(self.__create_connection__(), dst, src)
        except Exception as e:
            print e
            pass
        
    def send_put(self, src, dst):
        try:
            f = open(src, 'rb')
            data = f.read()
            self.__create_connection__().send_put(os.path.join(self.__url__, dst.encode('utf-8')), data)
        except Exception as e:
            print e
            pass