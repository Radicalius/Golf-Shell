import os,sys,string

repl = False

if len(sys.argv) > 1:
	inp=sys.argv[1]
else:
	repl = True

# command substitutions
subs = {"E":"echo","T":"tr","L":"ls","C":"cut","O":"sort","K":"cat","G":"grep","Q":"exit","B":"tail","H":"Head","R":"seq","F":"factor","S":"sed -n","W":"wc"}

def parse(cont):
	quoted = False
	quote=""
	len_ = 0
	code=""
	for char in cont:
		if not quoted:
			if char in subs:
				if len_ > 0:
					code += " | "
				if len_ == -1:
					code += "; "
				code += subs[char]
			elif char in string.ascii_lowercase:
				code += " -"+char
			elif char == "\n":
				len_ = -2
			elif char in ["'",'"']:
				quoted = True
				quote = char
				code += " "+char
			else:
				code += char
		else:
			code+=char
			if char in ["'",'"']:
				quoted=False
		len_ += 1

	if quoted:
		code+=quote

	for i,j in enumerate(sys.argv[2:]):
		code = code.replace("$"+str(i),j)
		print j

	print code, len(inp) - len(code)
	os.system(code)

if not repl:
	f = open(inp)
	cont = f.read()
	parse(cont)
else:
	print "Golf Shell Version 1.0\n"
	while 1:
		inp = raw_input("> ")
		parse(inp)