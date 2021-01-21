# -*- coding: utf-8 -*-


data = open('normdata.txt').read().split("\n")

allowed_keys=['BNF','SWD','PND','VIAF','GKD','GND','LCCN','NDL','NS']

for l in data:
	
	tok = l.split()
	if len(tok)==2:
		e = tok[0]
		#print (e)
		
		norm = tok[1].split('|')
		for no in norm:
			n = no.split("=")
			if len(n)==2:
				k = n[0]
				v = n[1]
				if k in allowed_keys and len(v)>0:
					#print (e, k, v)

	
					print( '<https://de.wikipedia.org/wiki/' + e + '>  <http://wlo.yovisto.com/ontology/1.0/normdata>  """' + k + '=' + v + '""" . \n' )
		
		