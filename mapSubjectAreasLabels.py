# -*- coding: utf-8 -*-
import json, os, requests
from rdflib import Graph, RDF
from rdflib.namespace import SKOS

g = Graph()
g.parse("https://raw.githubusercontent.com/openeduhub/oeh-metadata-eaf-sachgebietssystematiken/master/eaf-sachgebietssystematik-all.ttl", format="ttl")

labels=set()

for s, p, o in g.triples((None,  RDF.type, SKOS.Concept)):
	for s2, p2, o2 in g.triples((s,  SKOS.note , None)):			
		labels.add(str(o2))

for l in labels:	
		url = "https://wlo.yovisto.com/services/extract/" + l   		
		content = requests.get(url)
		js = json.loads(content.content)

		for e in js['entities']:
			print( l,"  -->  " , e['entity'] )
		
# now, verify the labels manually
