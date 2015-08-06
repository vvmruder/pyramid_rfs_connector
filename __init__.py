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
__create_date__ = '06.08.15'

from pyramid.config import Configurator


def includeme(config):
    """
    By including this in your pyramid web app you get access to connectors for remote file systems, like
    WebDav or SFTP.

    :param config: The pyramid apps config object
    :type config: Configurator
    """
    settings = config.get_settings()
    config.include('pyramid_mako')
    config.add_static_view('pyramid_rfs_connector', 'pyramid_rfs_connector:static',
        cache_max_age=int(settings["default_max_age"])
    )
