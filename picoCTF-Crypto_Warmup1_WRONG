# Made for a picoCTF crypto challenge.
# Thought you only needed to crossreference the letters, but didn't work.
# So reworked code for multiple iterations, also didn't work
# I was looking at this completely wrong, found out it's a Tabula Recta with a personalized key

listAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
indexlist = []
keyindex = []
answer = ""
i = 0
while(1):
	word = raw_input("Enter word: ")
	keyword = raw_input("Enter keyword: ")
	for x in range(0, 2):
		for letter in word:
			indexlist.append(listAlphabet.index(letter.upper()))
		for keyletter in keyword:
			keyindex.append(listAlphabet.index(keyletter.upper()))
		word = ""
		while(i < len(indexlist)):
			realindex = indexlist[i] + keyindex[i]
			i += 1
			if realindex > 25:
				realindex -= 26
			word += listAlphabet[realindex]
		print word


#     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
#    +----------------------------------------------------
# A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
# D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
# E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
# F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
# G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
# H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
# I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
# J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
# K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
# L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
# M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
# N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
# O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
# P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
# Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
# R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
# S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
# T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
# U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
# V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
# W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
# X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
# Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
# Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

# message: llkjmlmpadkkc
# key: thisisalilkey
# answer: ???
