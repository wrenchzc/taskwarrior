#! /usr/bin/python
################################################################################
## taskwarrior - a command line task list manager.
##
## Copyright 2006 - 2011, Paul Beckingham, Federico Hernandez.
## All rights reserved.
##
## This program is free software; you can redistribute it and/or modify it under
## the terms of the GNU General Public License as published by the Free Software
## Foundation; either version 2 of the License, or (at your option) any later
## version.
##
## This program is distributed in the hope that it will be useful, but WITHOUT
## ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
## FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
## details.
##
## You should have received a copy of the GNU General Public License along with
## this program; if not, write to the
##
##     Free Software Foundation, Inc.,
##     51 Franklin Street, Fifth Floor,
##     Boston, MA
##     02110-1301
##     USA
##
################################################################################

import sys
import commands
import json

# Use the taskwarrior 1.9.4+ _query command to issue a query and return JSON
command = "/usr/local/bin/task _query " + " ".join (sys.argv[1:])

# Generate output.
print "<tasks>"
for task in commands.getoutput (command).split (",\n"):
  data = json.loads (task)
  print "  <task>"
  for attribute in data.items ():
    if attribute[0] == "annotations":
      print "    <annotations>"
      for anno in attribute[1]:
        print "      <annotation>"
        for item in anno.items ():
          print "        <{0}>{1}</{0}>".format (item[0], item[1])
        print "      </annotation>"
      print "    </annotations>"
    elif attribute[0] == "tags":
      print "    <tags>"
      for tag in attribute[1]:
        print "      <tag>{0}</tag>".format (tag)
      print "    </tags>"
    else:
      print "    <{0}>{1}</{0}>".format (attribute[0], attribute[1])
  print "  </task>"
print "</tasks>"
sys.exit (0)

################################################################################

