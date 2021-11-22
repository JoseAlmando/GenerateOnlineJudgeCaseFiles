#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
 
def  isGirlOrBoy(username):
    letters = []
    for i in username:
        if i in letters:
            continue
        letters.append(i)
        
    if (len(letters) % 2 == 0):
        return True
    return False

def wtlw(i):
  if len(i) > 10:
      return i[0] + str(len(i)-2) + i[-1]
  else:
      return i
 
abecedary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def testcase_bg():
  uinput = ""
  for i in range(20):
    for j in range(random.randint(1,99)):
      uinput += random.choice(abecedary)
    print('{"input":' + f'"{uinput}",')
    if isGirlOrBoy(uinput):
      print('"output": "CHAT WITH HER!"')
    else:
      print('"output": "IGNORE HIM!"')
    print("},")
    uinput = ""

def testcase_wtlw():
  for i in range(20):
    usalida = ""
    uinput = ""
    x = random.randint(1,100)
    uinput = ""
    for y in range(x):
      palabra = ""
      for j in range(random.randint(1,20)):
        palabra += random.choice(abecedary) 
      uinput += palabra + " "
      usalida += wtlw(palabra) + " "


    print('{"input":' + f'"{x} {uinput.strip()}",')
    print('"output":' + f'"{usalida.strip()}"')
    print("},")

def main():
  testcase_wtlw()

if __name__ == "__main__":
    main()


