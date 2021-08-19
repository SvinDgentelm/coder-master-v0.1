print ("Выбирете режим:")
print ("1 - Кодироваие (буквы в dec askii)")
print ("2 - Декодирование (dec askii в буквы) :")
rezhim = int(input())



if rezhim == 1 :

  word = input('Введите фразу:')
  for i in word :
    if i == "A" :
      print (65,end = " ")

    elif i == "B" :
      print (66,end = " ")

    elif i == "C" :
      print (67,end = " ")

    elif i == "D" :
      print (68,end = " ")

    elif i == "E" :
      print (69,end = " ")

    elif i == "F" :
      print (70,end = " ")

    elif i == "G" :
      print (71,end = " ")

    elif i == "H" :
      print (72,end = " ")

    elif i == "I" :
      print (73,end = " ")

    elif i == "J" :
      print (74,end = " ")

    elif i == "K" :
      print (75,end = " ")

    elif i == "L" :
      print (76,end = " ")

    elif i == "M" :
      print (77,end = " ")

    elif i == "N" :
      print (78,end = " ")

    elif i == "O" :
      print (79,end = " ")

    elif i == "P" :
      print (80,end = " ")

    elif i == "Q" :
      print (81,end = " ")

    elif i == "R" :
      print (82,end = " ")

    elif i == "S" :
      print (83,end = " ")

    elif i == "T" :
      print (84,end = " ")

    elif i == "U" :
      print (85,end = " ")

    elif i == "V" :
      print (86,end = " ")

    elif i == "W" :
      print (87,end = " ")

    elif i == "X" :
      print (88,end = " ")

    elif i == "Y" :
      print (89,end = " ")

    elif i == "Z" :
      print (90, end = " ")

    if i == "a" :
      print (97,end = " ")

    elif i == "b" :
      print (98,end = " ")

    elif i == "c" :
      print (99,end = " ")

    elif i == "d"  :
     print (100,end = " ")

    elif i == "e" :
      print (101,end = " ")

    elif i == "f" :
      print (102,end = " ")

    elif i == "g" :
      print (103,end = " ")

    elif i == "h" :
      print (104,end = " ")

    elif i == "i" :
      print (105,end = " ")

    elif i == "j" :
      print (106,end = " ")

    elif i == "k" :
      print (107,end = " ")

    elif i == "l" :
      print (108,end = " ")

    elif i == "m" :
      print (109,end = " ")
           
    elif i == "n" :
      print (110,end = " ")

    elif i == "o" :
      print (111,end = " ")

    elif i == "p" :
      print (112,end = " ")

    elif i == "q" :
      print (113,end = " ")

    elif i == "r" :
      print (114,end = " ")

    elif i == "s" :
      print (115,end = " ")

    elif i == "t" :
      print (116,end = " ")

    elif i == "u" :
      print (117,end = " ")

    elif i == "v" :
      print (118,end = " ")   

    elif i == "w" :
      print (119,end = " ")

    elif i == "x" :
      print (120,end = " ")

    elif i == "y" :
      print (121,end = " ")

    elif i == "z" :
      print (122, end = " ")

    elif i == "!" :
      print (33, end=' ')

    elif i == "(" :
      print (40, end=' ')

    elif i == ")" :
      print (41, end=' ')

    elif i == "," :
      print (44, end=' ')

    elif i == "." :
      print (46, end=' ')

    elif i == " " : 
      print (32, end = ' ')

    elif i == "0" : 
      print (48, end = ' ')

    elif i == "1" : 
      print (49, end = ' ')

    elif i == "2" : 
      print (50, end = ' ')

    elif i == "3" : 
      print (51, end = ' ')

    elif i == "4" : 
      print (52, end = ' ')

    elif i == "5" : 
      print (53, end = ' ')

    elif i == "6" : 
      print (54, end = ' ')

    elif i == "7" : 
      print (55, end = ' ')

    elif i == "8" : 
      print (56, end = ' ')

    elif i == "9" : 
      print (57, end = ' ')                       





elif rezhim == 2 : 
  shet1 = 0
  word = input('Введите фразу:')
  shet2 = ''
  shet3 = ''
  shet4 = ''
  word += " "

  for i in word : 
    if shet1 + 2 <= len(word) or shet1 + 3 <= len(word) :
      

      if word[0 + shet1] != " " and word[0 + shet1 + 1] != " " and word[0 + shet1 + 2] == " " :
        
        

        shet2 = word[0 + shet1]
        shet3 = word[0 + shet1 + 1]
        shet5 = shet2 + shet3
        

        if shet5 == "65" :
          print ("A",end = "")

        elif shet5 == "66" :
              print ("B",end = "")

        elif shet5 == "67" :
              print ("C",end = "")

        elif shet5 == "68"  :
             print ("D",end = "")

        elif shet5 == "69" :
              print ("E",end = "")

        elif shet5 == "70" :
              print ("F",end = "")

        elif shet5 == "71" :
              print ("G",end = "")

        elif shet5 == "72" :
              print ("H",end = "")

        elif shet5 == "73" :
              print ("I",end = "")

        elif shet5 == "74" :
              print ("G",end = "")

        elif shet5 == "75" :
              print ("K",end = "")

        elif shet5 == "76" :
              print ("L",end = "")

        elif shet5 == "77" :
              print ("M",end = "")
           
        elif shet5 == "78" :
              print ("N",end = "")

        elif shet5 == "79" :
              print ("O",end = "")

        elif shet5 == "80" :
              print ("P",end = "")

        elif shet5 == "81" :
              print ("Q",end = "")

        elif shet5 == "82" :
              print ("R",end = "")

        elif shet5 == "83" :
              print ("S",end = "")

        elif shet5 == "84" :
              print ("T",end = "")

        elif shet5 == "85" :
              print ("U",end = "")

        elif shet5 == "86" :
              print ("V",end = "")   

        elif shet5 == "87" :
              print ("W",end = "")

        elif shet5 == "88" :
              print ("X",end = "")

        elif shet5 == "89" :
              print ("Y",end = "")

        elif shet5 == "90" :
              print ("Z", end = "")

        elif shet5 == "32" :
              print (" ", end = "")

        elif shet5 == "97" :
              print ("a", end='')

        elif shet5 == "98" :
              print ("b", end='')

        elif shet5 == "99" :
              print ("c", end='')

        elif shet5 == "33" :
              print ("!", end='')

        elif shet5 == "40" :
              print ("(", end='')

        elif shet5 == "41" :
              print (")", end='')

        elif shet5 == "44" :
              print (",", end='')

        elif shet5 == "46" :
              print (".", end='')

        elif shet5 == "48" : 
              print ('0', end = '')

        elif shet5 == "49" : 
              print ('1', end = '')

        elif shet5 == "50" : 
              print ('2', end = '')

        elif shet5 == "51" : 
              print ('3', end = '')

        elif shet5 == "52" : 
              print ('4', end = '')

        elif shet5 == "53" : 
              print ('5', end = '')

        elif shet5 == "54" : 
              print ('6', end = '')

        elif shet5 == "55" : 
              print ('7', end = '')

        elif shet5 == "56" : 
              print ('8', end = '')

        elif shet5 == "57" : 
            print ('9', end = '')                        

        shet1 += 3   


      elif word[0 + shet1] != " " and word[0 + shet1 + 1] != " " and word[0 + shet1 + 2] != " " and word[0 + shet1 + 3] == " " :
        shet2 = word[0 + shet1]
        shet3 = word[0 + shet1 + 1]
        shet4 = word[0 + shet1 + 2]

        shet5 = shet2 + shet3 + shet4

        if shet5 == "100" :
          print ("d",end = "")

        elif shet5 == "101" :
              print ("e",end = "")

        elif shet5 == "102" :
              print ("f",end = "")                                                                                        
        elif shet5 == "103"  :
             print ("g",end = "")

        elif shet5 == "104" :
              print ("h",end = "")

        elif shet5 == "105" :
              print ("i",end = "")

        elif shet5 == "106" :
              print ("j",end = "")

        elif shet5 == "107" :
              print ("k",end = "")

        elif shet5 == "108" :
              print ("l",end = "")

        elif shet5 == "109" :
              print ("m",end = "")

        elif shet5 == "110" :
              print ("n",end = "")

        elif shet5 == "111" :
              print ("o",end = "")

        elif shet5 == "112" :
              print ("p",end = "")
           
        elif shet5 == "113" :
              print ("q",end = "")

        elif shet5 == "114" :
              print ("r",end = "")

        elif shet5 == "115" :
              print ("s",end = "")

        elif shet5 == "116" :
              print ("t",end = "")

        elif shet5 == "117" :
              print ("u",end = "")

        elif shet5 == "118" :
              print ("v",end = "")

        elif shet5 == "119" :
              print ("w",end = "")

        elif shet5 == "120" :
              print ("x",end = "")

        elif shet5 == "121" :
              print ("y",end = "")   

        elif shet5 == "122" :
              print ("z",end = "")

        
        shet1 += 4