def group_by_rhyme(words):
     #dictionary
     rhyme_dict = {}

     for word in words:
         last_two_letters = word[-2:]
         if last_two_letters not in rhyme_dict:            #100% could've used lambda, no time to change
             rhyme_dict[last_two_letters] = [word] #letters - key, word - value
         else:
             rhyme_dict[last_two_letters].append(word)
     return rhyme_dict


print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte','alarme', 'tigani','ciolani','sarmani']))