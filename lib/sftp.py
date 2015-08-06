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

__author__ = 'Karsten Deininger'

import paramiko

class SFTPConnection():
    """Klasse: SFTPConnection
    SFTPConnection bietet Methoden fuer den Zugriff auf SFTP-Server.
    Grundlage bildet die Bibliothek 'paramiko'.
    
    LOCAL_PATH gibt das lokale Wurzelverzeichnis fuer den Datentransfer
    mit dem SFTP-Server an. Dieses ist per Default auf '/var/sig/public'
    gesetzt.

    :param host: Adresse des SFTP-Servers
    :param port: [optional] Port des SFTP-Servers (Default: 22)
    :param username: [optional] Benutzername fuer die Anmeldung
    :param password: [optional] Passwort fuer die Anmeldung
    """
    def __init__(self, host, port=22, username='', password=''):
        self.transport = paramiko.Transport((host, port))
        self.transport.connect(username=username, password=password, hostkey=None)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        
    def get(self, src_file, dst_file):
        """Uebertraegt eine Datei vom SFTP in das lokale Verzeichnis.
        :param src_file: Datei auf dem SFTP
        :param dst_file: lokale Zieldatei
        """
        self.sftp.get(src_file, dst_file)

    def put(self, src_file, dst_file):
        """Uebertraegt eine Datei vom lokalen Verzeichnis auf den SFTP.
        :param src_file: lokale Datei
        :param dst_file: Zieldatei auf dem SFTP
        :return: SFTPAttributes
        """
        return self.sftp.put(src_file, dst_file)
    
    def remove(self, path):
        """Entfernt die Datei/das Verzeichnis auf dem SFTP.
        :param path: Datei-/Verzeichnisname auf dem SFTP
        """
        self.sftp.remove(path)
        
    def rename(self, oldpath, newpath):
        """Aendert den Namen einer Datei/eines Verzeichnisses auf dem SFTP.
        :param oldpath: alter Datei-/Verzeichnisname
        :param newpath: neuer Datei-/Verzeichnisname
        """
        self.sftp.rename(oldpath, newpath)

    def listdir(self, path='.'):
        """Listet alle Elemente im angegebenen Verzeichnis auf.
        :param path: Verzeichnis, das aufgelistet werden soll
        :return: Liste an enthaltenen Elementen
        """
        return self.sftp.listdir(path)

    def listdir_attr(self, path='.'):
        """Listet die Attribute aller Elemente im angegebenen Verzeichnis auf.
        :param path: Verzeichnis, dessen Elemente untersucht werden sollen
        :return: Liste mit SFTPAttributes für jedes enthaltene Element
        """
        return self.sftp.listdir_attr(path)

    def close(self):
        """Schliesst die Verbindung zum SFTP."""
        self.transport.close()