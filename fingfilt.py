'''
MIT License

Copyright (c) 2016 Philip Crosby

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
import argparse
args=[]
output=[]
query=""
matches=0
rejects=0
dictionary=open("dict_english.txt").read().splitlines()

def parse_args(args=None):
	parser=argparse.ArgumentParser(description="Fing(er)Filt(er) v0.3")
	parser.add_argument('text', metavar='', nargs="*")
	parser.add_argument('-f', action="store_true", help="create list as output-query.txt in directory")	
	parser.add_argument('-p', action="store_true", help="get list as an array")
	parser.add_argument('-pl', action="store_true", help="get list as one entry per line")	
	parser.add_argument('-s', action="store_true", help="silence all output")	
	return parser.parse_args(args)

def run(manual_args=None):
	global args
	args=parse_args(manual_args)
	if args.text:
		create_output(args.text)
		send_output()
	
def create_output(text):
	global dictionary, output, matches, rejects
	for word in dictionary:
		match=True
		if length_pass(len(word),len(text)):
			pos=0
			while pos < len(text):
				if text[pos] == 'l':
					if not column_pass(word[pos],'12345'):
						match=False
				elif text[pos] == 'r':
					if not column_pass(word[pos],'67890'):
						match=False
				elif not column_pass(word[pos],text[pos]):
					match=False
				if match==False:
					break
				else:
					pos+=1
		else:
			match=False
		if match:
			output.append(word)
			matches+=1
		else:
			rejects+=1

def length_pass(wordlen,querylen):
	match=True
	if wordlen != querylen:
		match=False
	return match

def column_pass(letter,query):
	incols=False
	targetcolumn=get_column(letter)
	sep = map(int, query)
	for column in sep:
		if targetcolumn == column:
			incols=True
			break
	return incols

def send_output():
	global args, matches, rejects, output
	if matches == 0:
		print None
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

def get_output(query):
	global output
	output = []
	create_output(query)
	return output

def get_column(key):
	col={0:"p",1:"qaz",2:"wsx",3:"edc",4:"rfv",5:"tgb",6:"yhn",7:"ujm",8:"ik,",9:"ol"}
	for pos in col:
		if key in col[pos]:
			return pos

run()