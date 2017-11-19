import os,sys,string

repl = False

if len(sys.argv) > 1:
	inp=sys.argv[1]
else:
	repl = True

lcmd = ""

# command substitutions
subs = {"E":"echo","T":"tr","L":"ls","C":"cut","O":"sort","K":"cat","G":"grep --color=never","Q":"exit","B":"tail","H":"head","R":"seq","F":"factor","S":"sed","W":"wc","M":"bc -l","?":"if",":":"else","U":"uniq"}
nopipe = [":",";"]
nosep = [":",";"]

def parse(cont):
	global lcmd
	quoted = False
	quote=""
	len_ = 0
	code=""
	for char in cont:
		if not quoted:
			if char in subs:
				if not lcmd in nosep:
					if len_ > 0 and char not in nopipe:
						code += " | "
					if len_ == -1 or char in nopipe:
						code += "; "
				else:
					code += " "
				lcmd = char
				code += subs[char]
			elif char in string.ascii_lowercase:
				code += " -"+char
			elif char == ";":
				if lcmd == "?":
					code += "; then"
				else:
					code += "; fi"
				lcmd=";"
			elif char == "\n":
				len_ = -2
			elif char in ["'",'"',"["]:
				if char == "[":
					code += " [[ "
				else:
					code += " "+char
				quote = char
				quoted = True
			else:
				code += char
		else:
			if char == "]":
				code += " ]] "
			else:
				code+=char
			if char in ["'",'"',"]"]:
				quoted=False
		len_ += 1

	if quoted:
		code+=quote

	code = code.replace("=="," -eq ")
	code = code.replace("!="," -neq ")
	code = code.replace(">="," -gte ")
	code = code.replace("<="," -lte ")
	code = code.replace(">"," -gt ")
	code = code.replace("<"," -lt ")

	print "Code: "+code+" ("+str(len(inp) - len(code))+")"

	for i,j in enumerate(sys.argv[2:]):
		code = code.replace("$"+str(i),j)
		print "$"+str(i)+": "+j

	print code
	os.system("bash -c '"+code+"'")

if not repl:
	f = open(inp)
	cont = f.read()
	parse(cont)
else:
	print "Golf Shell Version 1.0\n"
	while 1:
		inp = raw_input("> ")
		parse(inp)