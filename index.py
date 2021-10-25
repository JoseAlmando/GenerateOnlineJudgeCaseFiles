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

for elementA in data:
  for element in elementA:
    for e in elementA[element]:
      createInput(e["id"], e["input"], element)
      createOutput(e["id"], e["output"], element)