def wtlw(i):
  if len(i) > 10:
      return i[0] + str(len(i)-2) + i[-1]
  else:
      return i

def main():
  x = input().split(" ")
  n = int(x[0])
  x = x[1:]

  for i in range(n):
    x[i] = wtlw(x[i])
    
  print(" ".join(x))
if __name__ == "__main__":
    main()

