# -*- coding: utf-8 -*-
from rdflib import Graph, RDF
from rdflib.namespace import SKOS

g = Graph()
g.parse("https://raw.githubusercontent.com/openeduhub/oeh-metadata-eaf-sachgebietssystematiken/master/eaf-sachgebietssystematik-all.ttl", format="ttl")

data = open('labels.txt').read().split('\n')
labels = {}

for l in data:	
	t = l.split('-->')	
	if len(t)==2:
		k = t[0].strip()
		v = t[1].strip()
		if not k in labels.keys():
			labels[k]=[]
		labels[k].append(v)
		
#print (labels)
for s, p, o in g.triples((None,  RDF.type, SKOS.Concept)):
	for s2, p2, o2 in g.triples((s,  SKOS.note , None)):					
				
		#print( "# " + o2)				
		if o2.strip() in labels.keys():			
			
			for l in labels[o2.strip()]:
				print( "<" + str(s2) + "> <" + str(SKOS.related) + "> <https://de.wikipedia.org/wiki/" + l + "> . " )
		
		