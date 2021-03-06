#!/usr/bin/env python
#
# This program scans SCAP xccdf content and compares 
# it to the ansible content to determine differences
# This presumes that the ansible tasks are following
# the proper naming convention as implemented in the
# ansible lockdown project.
#
# Author: Jonathan Davila <jdavila@redhat.com>
# 


import untangle

import sys
import os
import os.path
import argparse
import xml
from xml.sax._exceptions import SAXParseException 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compares Ansible content against a DISA STIG xccdf file")
    parser.add_argument('-x','--xccdf-file', required=True, dest='xccdf', help='Path to xccdf file generated by DISA zip file')
    parser.add_argument('-a','--ansible-content', required=True, dest='ans_cont', help='Path to your ansible content')
    args = parser.parse_args()

try:
    raw_data = untangle.parse(args.xccdf)
except xml.sax._exceptions.SAXParseException:
    sys.exit("The xccdf file: %s could not be found" % args.xccdf)

ansible_content = args.ans_cont

ids_in_xml = [vuln['id'] for vuln in raw_data.Benchmark.Group]
ids_in_tasks = set()

for dirpath, dirnames, filenames in os.walk(ansible_content):
        if 'tasks' in dirpath:
            for filename in [f for f in filenames if f.endswith(".yml")]:
                task_file = os.path.join(dirpath, filename)
                with open(task_file, 'r') as tf:
                    for line in tf:
                        if all(string in line for string in ['V-','name']) or \
                           all(string in line for string in ['V-','#']): 
                            try:
                                ids_in_tasks.add(line.split('|')[1].strip())
                            except IndexError:
                                continue

for rule in [xml_rule for xml_rule in ids_in_xml if xml_rule not in ids_in_tasks]:
    print rule

