import json
import os

def createDirectory(directory):
  try: 
    os.mkdir(directory) 
  except OSError as error: 
    pass

def createInputFile(name, value, directory):
  f = open(directory+"/"+str(name)+".in", "w")
  f.write(value)
  f.close()

def createOutputFile(name, value, directory):
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
  
def main():
  file = open("preguntas.json")
  data = json.load(file)

  for elementA in data:
    for directory in elementA:
      createDirectory(directory)
      for e in elementA[directory]:
        createInputFile(e["id"], e["input"], directory)
        createOutputFile(e["id"], e["output"], directory)
        addGitIgnore(directory)
        createZipFile(directory, directory)
      dropDirectory(directory)

if __name__ == "__main__":
  main()