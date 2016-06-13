# hand dictionary filter.
# delivers a sorted list with words that match a requested query.
# Philip Crosby, June 3 2016

import sys
import argparse
dictionary=open("hdfdict.txt").read().splitlines()

def run(manual_args=None):
	args=parse_args(manual_args)
	output=[]
	matches=0
	rejects=0
	if not args.text:
		if not args.s:
			print "-h for help, check readme for usage"
	else:
		query=args.text[0]
		inputlen=len(query)
		for word in dictionary:
			wordlen=len(word)
			match = True			
			if (wordlen < inputlen) or (wordlen > inputlen):
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
						if args.vr: print "'%s' FAIL ON %s"%(word,word[pos])
						break
					else:
						if args.vm: print "'%s' PASS ON %s"%(word,word[pos])
						pos += 1
			if match:
				output.append(word)
				if args.vm: print "'%s' ADDED"%word
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
				with open("output-{}.txt".format(args.text[0]),'a') as tmp:
					tmp.write("{}\n".format(word))
			print "OUTPUT -> output/output-%s.txt"%(args.text[0])
		else:
			total=float(matches+rejects)
			percent=float(matches/total)
			print "%s MATCHES (%.4f%%)"%(matches,percent)

def parse_args(args=None):
	parser=argparse.ArgumentParser(description="Hand Dictionary Filter v0.2")
	parser.add_argument('text', metavar='', nargs="*")
	parser.add_argument('-f', action="store_true", help="create list as output-query.txt in directory")	
	parser.add_argument('-g', action="store_true", help="UNAVAILABLE generate random values instead of filtering")	
	parser.add_argument('-p', action="store_true", help="get list as an array")
	parser.add_argument('-pl', action="store_true", help="get list as one entry per line")	
	parser.add_argument('-s', action="store_true", help="silence all output")
	parser.add_argument('-vr', action="store_true", help="verbose: show failures")
	parser.add_argument('-vm', action="store_true", help="verbose: show passes")
	return parser.parse_args(args)

run()