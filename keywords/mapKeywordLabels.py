# -*- coding: utf-8 -*-
import json, os, requests
from rdflib import Graph, RDF
from rdflib.namespace import SKOS

g = Graph()
g.parse("https://raw.githubusercontent.com/openeduhub/oeh-metadata-eaf-schlagwortverzeichnis/main/data/eaf-graph-by-subject-all.ttl", format="ttl")

labels=set()

for s, p, o in g.triples((None,  RDF.type, SKOS.Concept)):
	for s2, p2, o2 in g.triples((s,  SKOS.prefLabel , None)):			
		labels.add(str(o2))

#print (labels)

for l in sorted(labels):	
		print ("# " + l)
		url = "https://wlo.yovisto.com/services/extract/" + l.replace("/"," ")   		
		content = requests.get(url)
		js = json.loads(content.content)
		
		for e in js['entities']:
			print( l,"  -->  " , e['entity'] , flush=True)
	
# now, verify the labels manually
