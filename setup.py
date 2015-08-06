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

from setuptools import setup, find_packages

setup(
    name='pyramid_rfs_connector',
    version='1.0',
    description='Provides connectors for different remote file systems for the pyramid web framework',
    author='gis-fachstelle-bl',
    author_email='support.gis@bl.ch',
    url='http://www.geo.bl.ch',
    install_requires=[
        'pyramid',
        'python_webdav',
        'paramiko'
    ],
    packages=find_packages(),
    zip_safe=False
)