#!/bin/python

import os
import re
import yaml


p = re.compile(r'(?P<nbr>[0-9]+)')

for f in os.listdir('.') :
 if os.path.isdir(f) :
  taskf = f + '/task.yaml'
  if os.path.exists(taskf) :
   with open(taskf,'r') as stream:
    datal = yaml.safe_load(stream)
    m = p.search(datal['name'])
   if m is not None : 
    print('updating ' + taskf)
    datal['categories'] = ['session' + m.group('nbr')]
    if not m.group('nbr') == '1' : 
     datal['accessible'] = False
     print('set accessible False')
    os.rename(taskf,taskf + '.old')
    with open(taskf,'w') as outfile:
     yaml.dump(datal, outfile, default_flow_style=False, allow_unicode=True)
   else : 
    print("no Session nbr in " + taskf)