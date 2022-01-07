def elfname(name):
      name = name.lower()
      elfName = ""
      firstLetter = True
      arrayElfName = []
      for letter in name:
        arrayElfName.append(letter)
      arrayElfName.sort()
      for letter in arrayElfName:
        if letter in "abcdefghijklmnopqrstuvwxyz":
          if firstLetter:
            letter = letter.upper()
            firstLetter = False
          elfName = elfName + letter
      print(elfName)
