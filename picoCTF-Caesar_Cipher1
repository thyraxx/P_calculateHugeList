# Made for picoCTF challenge, caesar cipher1
# Could've used just an online tool, but where's the fun in that
import sys

cipher = sys.argv[1]
answer = ""
offsetArg = 0

# if no offset is given, let's try them all!
if len(sys.argv) == 3:
	offsetArg = int(sys.argv[2])

def realIndex(letter, offset):
	global answer
	realindex = listAlphabet.index(letter.upper()) + offset
	
	if realindex > 25:
			realindex -= 26
	answer += listAlphabet[realindex]

listAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
if offsetArg == 0:
	i = 25
else:
	i = offsetArg

for offset in range(0, i):
	for letter in cipher:
		realIndex(letter, offset)
	print offset, answer.lower()
	answer = ""

# python pythonfile shiftedtext OPTIONAL n iterations
# python picoCTF-caesar_cipher1.py yjhipvddsdasrpthpgrxewtgdqnjytto

# 0 yjhipvddsdasrpthpgrxewtgdqnjytto
# 1 zkijqweetebtsquiqhsyfxuherokzuup
# 2 aljkrxffufcutrvjritzgyvifsplavvq
# 3 bmklsyggvgdvuswksjuahzwjgtqmbwwr
# 4 cnlmtzhhwhewvtxltkvbiaxkhurncxxs
# 5 domnuaiixifxwuymulwcjbylivsodyyt
# 6 epnovbjjyjgyxvznvmxdkczmjwtpezzu
# 7 fqopwckkzkhzywaownyeldankxuqfaav
# 8 grpqxdllaliazxbpxozfmebolyvrgbbw
# 9 hsqryemmbmjbaycqypagnfcpmzwshccx
# 10 itrszfnncnkcbzdrzqbhogdqnaxtiddy
# 11 justagoodoldcaesarcipherobyujeez <-- Correct one
# 12 kvtubhppepmedbftbsdjqifspczvkffa
# 13 lwuvciqqfqnfecguctekrjgtqdawlggb
# 14 mxvwdjrrgrogfdhvduflskhurebxmhhc
# 15 nywxeksshsphgeiwevgmtlivsfcyniid
# 16 ozxyflttitqihfjxfwhnumjwtgdzojje
# 17 payzgmuujurjigkygxiovnkxuheapkkf
# 18 qbzahnvvkvskjhlzhyjpwolyvifbqllg
# 19 rcabiowwlwtlkimaizkqxpmzwjgcrmmh
# 20 sdbcjpxxmxumljnbjalryqnaxkhdsnni
# 21 tecdkqyynyvnmkockbmszrobylietooj
# 22 ufdelrzzozwonlpdlcntaspczmjfuppk
# 23 vgefmsaapaxpomqemdoubtqdankgvqql
# 24 whfgntbbqbyqpnrfnepvcurebolhwrrm
