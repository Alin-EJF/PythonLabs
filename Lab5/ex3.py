def vowels_1( string ):
    return [ch for ch in string if ch.lower() in "aeiou"]

def vowels1( word ):
    list= []
    for letter in word:
        if letter in "aeiou":
            list.append( letter )

    return list

vowels2 = lambda word: [letter for letter in word if letter in "aeiou"]
vowels3 = lambda string: list(filter(lambda x: x.lower() in "aeiou", string))

print( vowels_1( "Programming in Python is fun" ) )
print( vowels1( "Programming in Python is fun" ) )
print( vowels2( "Programming in Python is fun" ) )
print( vowels3( "Programming in Python is fun" ) )




            

