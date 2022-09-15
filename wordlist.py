import sys
import random
import argparse

def outfile(filename, text, mode="a"):
	"Save text in file"
	#Open and Write File
	try:
		log = open(filename, mode)
		log.write(text)
		log.close()
	except Exception as e:
		print("[!] {} => Doesn't exist or busy".format(filename))

def strip(vstr):
    " Strip if str "
    if type(vstr) == type(''): 
        vstr = vstr.strip()
    return vstr

DICTIONARY_WORST = ['123123','111111','iloveyou','12345','123456','1234567','12345678','123456789','qwerty','abc123','test','test1','password','password1','asdf','admin','555555','qwerty123','1q2w3e4r5t','123qwe']
# ToDo: Dictionary by country or language
DICTIONARY_CITY = ["Colombia","Antioquia","Medellin","Nacional","Bogota","Barranquilla","Cartagena","Panama"]
USERPATTERNS = ['N', 'AL', 'AAL', 'N.L']
PASSPATTERNS = ['D', 'L', 'M', 'H']
# ToDo: Modify limit
WORDLIST_RANDOM_LIMIT = 4000

def username(pattern, domain, outname=None):
	"Generate username patterns and save it in file"

	with_domain = domain!=''
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	names = ["juan","daniel","fernando","luciana","isabella","mariana","maria","jose","sara","paula","santiago","luz","irene","nicolas","matias","miguel","david","samuel","emiliano","alejandra","alejandro","pablo","andres","felipe","ana","lucia","sofia","valentina","luisa","fernanda","alex","alexandra","alexa","augusto","federico","william","sergio","jesus","francisco", "diego","jorge","nubis","luis","omar","rafael","blanca","carmen","cecilia","flor","gladys","isabel","margarita","mercedes","olga","patricia","paola","rosalba","sandra","teresa","yolanda","jairo","john","julio","horacio","byron","hector","leon","cristobal","justin"]
	last_names = ["rodriguez","gonzalez","martinez","garcia","lopez","hernandez","perez","gomez","diaz","sanchez","ortiz", "ramirez","torres","rojas","vargas","moreno","gutierrez","jimenez","munoz","castro","alvarez","ruiz","suarez","romero","herrera","valencia","quintero","restrepo","giraldo","morales","mejia","arias","parra","jaramillo","cardenas","osorio","castillo","salazar","cardona","florez","medina","rivera","montoya","cortes","correa","marin","rincon","zapata","escobar","velasquez"]
	wordlist = []
	print("[?] Valid Options Are {}".format(", ".join(USERPATTERNS)))
	#evaluate patterns
	if pattern == 'N':
		print ("[+] Generating under {} pattern".format(pattern))
		limit = WORDLIST_RANDOM_LIMIT
		index = 0
		#examples 2755106, 7 digits => 8 and strip 0
		#examples 27551060, 8 digits
		#examples 275510601, 9 digits
		#examples 1050321152, 10 digits
		while index < limit:
			dig8  = int("".join(map(str, random.sample(range(0, 10), 8))))
			dig9  = int("".join(map(str, random.sample(range(0, 10), 9))))
			wordlist.append (str(dig8))
			wordlist.append (str(dig9))
			wordlist.append ("10"+str(dig8))
			wordlist.append ("11"+str(dig8))
			index+=1
	elif pattern == 'AL':
		print ("[+] Generating under {} pattern".format(pattern))
		for n in alphabet:
			for l in last_names:
				wordlist.append (n+l)
	elif pattern == 'AAL':
		print ("[+] Generating under {} pattern".format(pattern))
		for n in alphabet:
			for m in alphabet:
				for l in last_names:
					wordlist.append (n+m+l)
	elif pattern == 'N.L':
		print ("[+] Generating under {} pattern".format(pattern))
		for n in names:
			for l in last_names:
				wordlist.append(n+"."+l)
	else:
		return None
	#Add domain if was given
	if with_domain:
		print("[+] Adding domain {}{}".format(pattern,"@"+domain))
		for idx in range(0,len(wordlist)):
			wordlist[idx] += "@"+domain
	wordlen = str(len(wordlist))
	top3 = wordlist[0:3]
	print("[+] Top3 is {} ".format(" ".join(top3)))

	if outname:
		print("[+] Saving {} users into {}".format(wordlen, outname))
		outfile(outname, "\n".join(wordlist), "w")

	return wordlist

def password(pattern, outname):
	"Generate password patterns and save it in file"

	print("[+] Generating Passwords")
	#defining arrays and mapping its form
	worst = ['123123','111111','iloveyou','12345','123456','1234567','12345678','123456789','qwerty','abc123','test','test1','password','password1','asdf','admin','555555','qwerty123','1q2w3e4r5t','123qwe']
	city = ["Colombia","Antioquia","Medellin","Nacional","Bogota","Barranquilla","Cartagena","Panama"]
	city_lower = list(map(str.lower, city))
	city_upper = list(map(str.upper, city))
	month = ["Enero", "Febrero", "Marzo", "Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
	month_lower = list(map(str.lower, month))
	month_upper = list(map(str.upper, month))
	other = ["Amor","Banco","Prosperar","Amistad","Familia","Felicidad","Esperanza","Amigos","Futuro","Trabajo","Deporte"]
	other_lower = list(map(str.lower, other))
	other_upper = list(map(str.upper, other))
	years = list(map(lambda x: "20"+str(x),range(20,15,-1)))
	symbols = ["*", ".", "+"]
	wordlist = []
	print("[?] Valid Options Are {}".format(", ".join(PASSPATTERNS)))
	#evaluate patterns
	if pattern == 'Default' or pattern == 'D':
		print ("[+] Generating under {} pattern".format(pattern))
		wordlist += worst
	elif pattern == 'Low' or pattern == 'L':
		print ("[+] Generating under {} pattern".format(pattern))
		wordlist += city
		wordlist += month
		wordlist += other
		wordlist += city_lower
		wordlist += month_lower
		wordlist += other_lower
		wordlist += city_upper
		wordlist += month_upper
		wordlist += other_upper
	elif pattern == 'Medium' or pattern == 'M':
		print ("[+] Generating under {} pattern".format(pattern))
		for n in years:	wordlist += list(map(lambda x: x+n,city))
		for n in years:	wordlist += list(map(lambda x: x+n,month))
		for n in years:	wordlist += list(map(lambda x: x+n,other))
	elif pattern == 'High' or pattern == 'H':
		print ("[+] Generating under {} pattern".format(pattern))
		for n in years:	
			for s in symbols:
				wordlist += list(map(lambda x: x+n+s,city))
		for n in years:	
			for s in symbols:
				wordlist += list(map(lambda x: x+n+s,month))
		for n in years:	
			for s in symbols:
				wordlist += list(map(lambda x: x+n+s,other))
		for n in years:	
			for s in symbols:
				wordlist += list(map(lambda x: x+s+n,city))
		for n in years:	
			for s in symbols:
				wordlist += list(map(lambda x: x+s+n,month))
		for n in years:	
			for s in symbols:
				wordlist += list(map(lambda x: x+s+n,other))
	else:
		return None
	wordlen = str(len(wordlist))
	top5 = wordlist[0:3]
	print("[+] Top3 is {} ".format(" ".join(top5)))
	print("[+] Saving {} passwords into {}".format(wordlen, outname))
	if outname:
		outfile(outname, "\n".join(wordlist), "w")

def wordlist(cmd):
	" Wordlist main function "
	print("[>] Wordlist Module")
	parser = argparse.ArgumentParser(
		prog="wordlist",
        description="Generate a wordlist by pattern"
    )
	parser.add_argument('-m', 
        action="store", dest='mode', default=None, 
        help="mode", required=False
    )
	parser.add_argument('-p',
        action="store", dest='pattern', default=None, 
        help="pattern", required=False
    )
	parser.add_argument('-d',
        action="store", dest='domain', default='', 
        help="domain", required=False
    )
	parser.add_argument('-o',
        action="store", dest='outname', default=None, 
        help="outname", required=False
    )
	parameters = parser.parse_args(cmd.split())	
	
	mode = strip(parameters.mode)
	domain = strip(parameters.domain)
	pattern = strip(parameters.pattern)
	outname = strip(parameters.outname)
	if mode == "user":
		if pattern not in USERPATTERNS:
			print("[?] Valid user options are {}".format(", ".join(USERPATTERNS)))
			print("[!] Try again using -p")
			print("[!] Unrecognized pattern")
			return False
	elif mode == "pass":
		print("[?] Valid pass options are {}".format(", ".join(PASSPATTERNS)))
		if pattern not in PASSPATTERNS:
			print("[!] Try again using -p")
			print("[!] Unrecognized pattern")
			return False
	else:
		print("[!] Try again using -m")
		print("[?] Valid options are: {}".format(",".join(["user", "pass"])))
		print("[!] Unrecognized mode")
		return False
	if not outname:
		print("[!] Try again using -o name")
		print("[!] Unrecognized outname")
		return False
	print("[?] Domain can be used with -d domain.com")
	if mode == "user":
		return username(pattern, domain, outname)
	elif mode == "pass":
		return password(pattern, outname)
	else:
		return None

if __name__ == '__main__':
	args = sys.argv[1:]
	cmdline = " ".join(args)
	wordlist(cmdline)