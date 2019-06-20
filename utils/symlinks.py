#!../venv/bin/python

import os, sys, re 

#INIT VARS 
app_dir = ['templates','static']

# listing existing modules 
existing_mods = []
dirs = os.listdir('../') 
for dir in dirs :
  if re.match('mod_',dir) :
    existing_mods.append(dir)

# removing unused directories 
for dir in app_dir :
  subdir = os.listdir('../' + dir)
  for item in subdir :
    curdir = '../' + dir + '/' + item
    if (item not in existing_mods) or (not os.path.exists(curdir)) :
      os.remove(curdir)

# add symlinks 
for mod in existing_mods :
  for dir in app_dir : 
    target = '../' + mod + '/' + dir 
    link = '../' + dir + '/' + mod 
    if os.path.isdir(target) and not (os.path.exists(link)): 
      os.symlink(target,link) 
