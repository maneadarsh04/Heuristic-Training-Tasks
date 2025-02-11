#(\n) is used to start from a new line and (\t) is used to give space in the sentence. 
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t Up above the world so high,\n\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are!")
#Below examples are on different types of slicing methods in string. [Note: Python reads space between words as a character when slicing. Check example 2.]
#string1
str1= 'Hello, my name is Adarsh.'
#string2
str2 = 'This is a python script.'

#example 1 (Slicing)
#in below example the command will only print after the start index till the end index that is till "l", and it does not count from the start side(H).
#"1" is start index and "3" is end index.
print("example 1")
print(str1[1:3])

#example 2 (Slicing from the start)
#below example is for slicing from the start, we will not give the start index by leaving the left side of the colon empty and give end index.
#in below example the "6" denotes the end index, so by not mentioning the start index the slicing starts from the very first character.
print("example 2")
print(str2[:6])

#example 3 (Slicing to the end)
#Below example will slice till the end, if we don't give end index and only start index."3" is the start index.
# Will skip the 3rd character and start printing from 3rd character onwards.
print("example 3")
print(str1[3:])

#example 4 (Negative Indexing)
#Negative indexing starts slicing from the end of the string. So the sequencing of the index starts from the right side with (-) numbering.
#in below example (-13) is the character 'P' but it will be skipped and (-12) character will be start and (-2) is the end index and it won't print the letter 't' as the printing stops at (-2).
print("example 4")
print(str2[-13:-2])