# Made for picoCTF challenge, caesar cipher1
import sys

cipher = sys.argv[1]
answer = ""

# if no offset is given, let's try them all!
if len(sys.argv) == 3:
	offsetArg = int(sys.argv[2])
else:
	offsetArg = 0

def realIndex(letter, offset):
	global answer
	realindex = listAlphabet.index(letter.upper()) + offset
	
	if realindex > 25:
			realindex -= 26
	answer += listAlphabet[realindex]

listAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
if offsetArg == 0:
	start = 0
	i = 26
else:
	start = offsetArg - 1
	i = offsetArg
	

for offset in range(start, i):
	for letter in cipher:
		realIndex(letter, offset)
	print offset, answer.lower()
	answer = ""

# python picoCTF-caesar_cipher1.py yjhipvddsdasrpthpgrxewtgdqnjytto

# 0 yjhipvddsdasrpthpgrxewtg dqnjytto
# 1 zkijqweetebtsquiqhsyfxuh erokzuup
# 2 aljkrxffufcutrvjritzgyvi fsplavvq
# 3 bmklsyggvgdvuswksjuahzwj gtqmbwwr
# 4 cnlmtzhhwhewvtxltkvbiaxk hurncxxs
# 5 domnuaiixifxwuymulwcjbyl ivsodyyt
# 6 epnovbjjyjgyxvznvmxdkczm jwtpezzu
# 7 fqopwckkzkhzywaownyeldan kxuqfaav
# 8 grpqxdllaliazxbpxozfmebo lyvrgbbw
# 9 hsqryemmbmjbaycqypagnfcp mzwshccx
# 10 itrszfnncnkcbzdrzqbhogdq naxtiddy
# 11 justagoodoldcaesarcipher obyujeez <-- Correct one
# 12 kvtubhppepmedbftbsdjqifs pczvkffa
# 13 lwuvciqqfqnfecguctekrjgt qdawlggb
# 14 mxvwdjrrgrogfdhvduflskhu rebxmhhc
# 15 nywxeksshsphgeiwevgmtliv sfcyniid
# 16 ozxyflttitqihfjxfwhnumjw tgdzojje
# 17 payzgmuujurjigkygxiovnkx uheapkkf
# 18 qbzahnvvkvskjhlzhyjpwoly vifbqllg
# 19 rcabiowwlwtlkimaizkqxpmz wjgcrmmh
# 20 sdbcjpxxmxumljnbjalryqna xkhdsnni
# 21 tecdkqyynyvnmkockbmszrob ylietooj
# 22 ufdelrzzozwonlpdlcntaspc zmjfuppk
# 23 vgefmsaapaxpomqemdoubtqd ankgvqql
# 24 whfgntbbqbyqpnrfnepvcure bolhwrrm
