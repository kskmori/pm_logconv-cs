# -*- coding: utf-8 -*-

# sosreport plugin for pm_logconv-cs : Pacemaker and Corosync log converter
#
# Copyright (C) 2016 NIPPON TELEGRAPH AND TELEPHONE CORPORATION

### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin

# the class name determines the plugin name
# if you want to override it simply provide a @classmethod name()
# that returns the name you want
class pm_logconv_cs(Plugin, RedHatPlugin):
    """Pacemaker and Corosync log message converter
    """

#    packages = [
#        "pm_logconv-cs",
#        ]

    def setup(self):
        self.add_copy_spec([
                "/etc/pm_logconv.conf",
                "/var/log/pm_logconv.out",
                ])
