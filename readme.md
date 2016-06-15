### Finger Filter
fingfilt.py readme.md

##### What does it do?
Returns an alphabetical list of all words that match finger patterns, based on columns.

##### String queries
`*` = any key  
`l` = any left hand key
`r` = any right hand key
`1,2,3,4,5,6,7,8,9,0` = any key from column #  
Planned: `[123][45]` any key from column groups  

##### Usage Examples

```
> fingfilt
-h for help, check readme for usage
```

Number words matching length: 2, 1st char: left hand, 2nd char: right hand.
```
> fingfilt lr
23 MATCHES (0.0002%)
```

Print results as array.
```
> fingfilt lr -p
['ah', 'ai', 'am', 'an', 'ay', 'bi', 'bo', 'by', 'do', 'eh', 'el', 'em', 'en', 'go', 'pi', 'sh', 'si', 'so', 'ti', 'to', 'wo', 'xi', 'xu']
```

Words typed in sequence: column 2, column 8, column 8. Print one line per word.
```
> fingfilt 288 -pl
ski
```

Same, with a fourth key of any type.
```
> fingfilt 288* -pl
sike
skid
skim
skin
skip
skis
skit
```

Column 2, column 8, any left hand, any right hand. Print one line per word.
```
> fingfilt 28lr -pl
sial
sick
sigh
sign
sith
siti
sizy
wich
wick
wiry
wish
with
```

Output to a txt file.
```
> fingfilt lrr -f
OUTPUT output-lrr.txt
```

Uses argparse and has basic help functionality.
```
> fingfilt.py -h
usage: fingfilt.py [-h] [-f] [-g] [-p] [-pl] [-s] [-vr] [-vm] [[...]]

Hand Dictionary Filter v0.2

positional arguments:


optional arguments:
  -h, --help  show this help message and exit
  -f          create list as output-query.txt in directory
  -p          get list as an array
  -pl         get list as one entry per line
  -s          silence all output
  -vr         verbose: show failures
  -vm         verbose: show passes
```