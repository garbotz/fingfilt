### readme 
### hdf
hand dictionary filter

##### What does it do?
Given a string as a query, returns a list of words that match typing metrics.

##### String queries
`*` = any key  
`l` = any left hand key  
`r` = any right hand key  
`1,2,3,4,5,6,7,8,9,0` = any key from column #  
Planned: `[1,2,3][4,5]` any key from column group  
Planned: `l[4,5] r[8,7] ` as repeatable sequence  

##### Examples
```
> python hdf.py
-h for help, check readme for usage

> python hdf.py lrlr
257 MATCHES (0.0023%)

> python hdf.py lr
23 MATCHES (0.0002%)

> python hdf.py lr -p
['ah', 'ai', 'am', 'an', 'ay', 'bi', 'bo', 'by', 'do', 'eh', 'el', 'em', 'en', 'go', 'pi', 'sh', 'si', 'so', 'ti', 'to', 'wo', 'xi', 'xu']

> python hdf.py 288 -pl
ski

> python hdf.py 288* -pl
sike
skid
skim
skin
skip
skis
skit

> python hdf.py 28lr -pl
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

> python hdf.py -h
usage: hdf.py [-h] [-f] [-g] [-p] [-pl] [-s] [-vr] [-vm] [[...]]

Hand Dictionary Filter v0.2

positional arguments:


optional arguments:
  -h, --help  show this help message and exit
  -f          create list as output-query.txt in directory
  -g          UNAVAILABLE generate random values instead of filtering
  -p          get list as an array
  -pl         get list as one entry per line
  -s          silence all output
  -vr         verbose: show failures
  -vm         verbose: show passes
```