import json

class InputOutput:
  def __init__(self, input, output):
    self.input = input
    self.output = output

class Question:
  def __init__(self, question):
    self.Question = question

def createQuestion(question):
  question = Question(question)
  return question

def createInputOutput(input, output):
  inputOutput = InputOutput(input, output)
  inputOutputD = json.dumps(inputOutput.__dict__)
  return inputOutputD

def generate():
  question = input("Question: ")
  options = []

  continueAdding = True
  while continueAdding:
    option = createInputOutput(input("Input: "), input("Output: "))
    options.append(option)
    continueAdding = input("Continue adding? (y/n): ").lower() == "y"

  question = createQuestion(question, options)
  questionD = json.dumps(question.__dict__)
  return question.__dict__
