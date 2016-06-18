### Fing(er) Filt(er) v0.3
fingfilt.py readme.md

##### What does it do?
Returns an alphabetical list of all words that match finger patterns, based on columns.

##### String queries
`*` = any key  
`l` = any left hand key  
`r` = any right hand key  
`1234567890` = any key from column #  

##### Usage Examples

Find all 3-letter words that can be typed in sequence column 2, column 8, column 8. Print as list.
```
> fingfilt 2 8 8 -pl
ski
```

Find all 4-letter words that can be typed column 2, column 8, column 8, any.  
```
> fingfilt 2 8 8 * -pl
sike
skid
skim
skin
skip
skis
skit
```

Add multiple columns to increase filter range per position.  
```
> fingfilt 29 38 38 -pl
led
lee
lei
lek
lid
lie
odd
ode
oke
sec
...
```

'l' and 'r' are shorthand for columns 12345 and 67890.
```
> fingfilt 2 8 l r -pl
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
...
```

A list not working for you? Return an array.
```
> fingfilt l r -p
['ah', 'ai', 'am', 'an', 'ay', 'bi', 'bo', 'by', 'do', 'eh', 'el', 'em', 'en', 'go', 'pi', 'sh', 'si', 'so', 'ti', 'to', 'wo', 'xi', 'xu']
```

Or output as a text file.
```
> fingfilt l r -f
OUT: output-lr.txt
```