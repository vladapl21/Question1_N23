def IterativeVowels(Value):
  Total = 0
  Value = str(Value)
  for x in Value:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
      Total += 1
  return Total

print(IterativeVowels("house"))

Total = 0
def RecursiveVowels(Value):
  global Total
  if Value == "":
    return print(Total)
  elif Value[0] == "a" or Value[0] == "e" or Value[0] == "i" or Value[0] == "o" or Value[0] == "u":
    Total += 1 
    RecursiveVowels(Value[1:])
  else:
    RecursiveVowels(Value[1:])


RecursiveVowels("imagine")
    