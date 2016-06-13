# hand dictionary filter.
# delivers a sorted list with words that match a requested query.
# Philip Crosby, June 3 2016

import sys
import argparse
dictionary=open("dict.txt").read().splitlines()

def run(manual_args=None):
	args=parse_args(manual_args)
	output=[]
	matches=0
	rejects=0
	if args.text:
		query=args.text[0]
		inputlen=len(query)
		for word in dictionary:
			match = True			
			if (len(word) < inputlen) or (len(word) > inputlen):
				match = False
			else:
				pos = 0
				while pos < inputlen:
					wordkey = word[pos]
					querykey = query[pos]
					if querykey in {'0','1','2','3','4','5','6','7','8','9'}:
						if get_column(wordkey) != get_column(querykey):
							match = False
					elif querykey == 'l':
						if get_hand(wordkey) != 'l':
							match = False
					elif querykey == 'r':
						if get_hand(wordkey) != 'r':
							match = False
					if match == False:
						if args.v or args.vr: print "'%s' FAIL ON %s"%(word,word[pos])
						break
					else:
						if args.v or args.vm: print "'%s' PASS ON %s"%(word,word[pos])
						pos += 1
			if match:
				output.append(word)
				if args.v:
					print "'%s' ADDED"%word
				matches+=1
			else:
				rejects+=1
			
		send_output(output,matches,rejects,args)

def get_column(key):
	col={0:"0p;/",1:"1qaz",2:"2wsx",3:"3edc",4:"4rfv",5:"5tgb",6:"6yhn",7:"7ujm",8:"8ik,",9:"9ol."}
	for pos in col:
		if key in col[pos]:
			return pos

def get_hand(key):
	col = get_column(key)
	if col <= 5:
		return 'l'
	elif col >= 6:
		return 'r'

def send_output(output,matches,rejects,args):
	if matches == 0:
		print "NO MATCHES"
	else:
		if args.p:
			print output
		elif args.pl: 
			for word in output:
				print word
		elif args.f:
			for word in output:
				with open("output/output-{}.txt".format(query),'a') as tmp:
					tmp.write("{}\n".format(word))
			print "OUTPUT -> output/output-%s.txt"%(query)
		else:
			total=float(matches+rejects)
			percent=float(matches/total)
			print "%s MATCHES (%.4f%%)"%(matches,percent)

def parse_args(args=None):
	parser=argparse.ArgumentParser()
	parser.add_argument('text', metavar='', nargs="*")
	parser.add_argument('-s', action="store_true", 
		help="silence output, but still print to file")
	parser.add_argument('-p', action="store_true", 
		help="instead of creating a text file, output as array")
	parser.add_argument('-pl', action="store_true", 
		help="instead of creating a text file, output as 1 per line")	
	parser.add_argument('-g', action="store_true", 
		help="generate random values instead of filtering")	
	parser.add_argument('-f', action="store_true", 
		help="render results to file with filter as filename (if matches found)")	
	parser.add_argument('-v', action="store_true", 
		help="verbose mode, show pass and fails")
	parser.add_argument('-vr', action="store_true", 
		help="verbose mode, show only rejects")
	parser.add_argument('-vm', action="store_true", 
		help="verbose mode, show only matches")	
	return parser.parse_args(args)

run()