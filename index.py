import json
import os

file = open("preguntas.json")
data = json.load(file)

def createInput(name, value, directory):
  try: 
    os.mkdir(directory) 
  except OSError as error: 
    pass
  f = open(directory+"/"+str(name)+".in", "w")
  f.write(value)
  f.close()

def createOutput(name, value, directory):
  try: 
    os.mkdir(directory) 
  except OSError as error: 
    pass
  f = open(directory+"/"+str(name)+".out", "w")
  f.write(value)
  f.close()

def addGitIgnore(dir):
  f = open(".gitignore", "r+")
  information = f.read()
  information = information.split("\n")
  if (dir + "/") not in information:
    f.write(dir+"/\n")
    f.write(dir+".zip\n")
  f.close()

def createZipFile(name, directory):
  import zipfile
  try:
      import zlib
      compression = zipfile.ZIP_DEFLATED
  except:
      compression = zipfile.ZIP_STORED
  zip = zipfile.ZipFile(name+".zip", "w")
  for root, dirs, files in os.walk(directory):
    for file in files:
      zip.write(os.path.join(root, file), file, compression)
  zip.close()

def dropDirectory(directory):
  import shutil
  shutil.rmtree(directory)

for elementA in data:
  for element in elementA:
    for e in elementA[element]:
      createInput(e["id"], e["input"], element)
      createOutput(e["id"], e["output"], element)
      addGitIgnore(element)
      createZipFile(element, element)
    dropDirectory(element)
