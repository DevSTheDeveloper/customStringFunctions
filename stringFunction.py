def to_lowercase(string):
  result = ''
  for char in string:
    if ('A' <= char <= 'Z'):
      result += chr(ord(char) + 32) 
    else:
      result += char
  return result

def to_uppercase(string):
  result = ''
  for char in string:
    if ('a' <= char <= 'z'):
      result += chr(ord(char) - 32) 
    else:
      result += char
  return result

def number_of_word(string):
  count = 0
  if string[0] != ' ':
    count = 1
  spaceFound = 0
  for char in string:
    if (char == ' '):
      spaceFound = 1
    elif spaceFound == 1:
      count += 1
      spaceFound = 0 
  return count
      
def upperCount(string):
  total = 0
  for char in string:
    if ('A' <= char <= 'Z'):
      total += 1
  return total
 
def lowerCount(string):
  total = 0
  for char in string:
    if ('a' <= char <= 'z'):
      total += 1
  return total
  
def totalRepeat(string, word):
  total = 0 
  tempWord = ''
  string = to_lowercase(string)
  word = to_lowercase(word)
  for char in string:
    if char != ' ':
      tempWord += char
    else:
      if tempWord != '':
        if tempWord == word:
          total += 1
        tempWord = ''
  return total
  
def stringLength(string):
  total = 0 
  for char in string:
    total += 1
  return total 
  
def convert_ASCII(string):
  for char in string:
    print(ord(char))
  return
  
def reverse_string(string):
  total = stringLength(string)
  tempString = '' 
  for i in range (total - 1, -1, -1):
    tempString += string[i]
  return tempString
    
def merge_strings(string1, string2):
  merged = string1 + string2
  return merged
  
inputString = str(input("Please enter 1st string: "))
inputString2 = str(input("Please enter 2nd string: "))

#print(inputString)
#totalCapital = upperCount(inputString)
#totalLower = lowerCount(inputString)
#print("The total number of upper count is: " + str(totalCapital))
#print("The total number of lower count is: " + str(totalLower))
#wordRepeat = totalRepeat(inputString, "are")
#print(wordRepeat)
#print(stringLength(inputString))
#convert_ASCII(inputString)

#print(reverse_string(inputString))
print(merge_strings(inputString, inputString2))
