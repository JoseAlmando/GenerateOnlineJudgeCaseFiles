import json
import os
from typing import final
import createQuestion


def createJSONFile(name, question):
  # Create a JSON file
  try:
    f = open(name  + ".json", "r+")
  except:
    f = open(name  + ".json", "w+")
    f.write('[]')
  finally:
    f.close()

  with open(name + ".json", "r") as json_file:
    data = json.load(json_file)

  data.append(question)

  with open(name + ".json", "w") as json_file:
    json.dump(data, json_file)

def main():

  filename = input("Enter the name of the file: ")
  question = createQuestion.generate()
  #question.replace('\\', "===")
  print(question)


  #createJSONFile(filename, question)
  #createFiles(filename)

if __name__ == "__main__":
  main()