# wlo-metadata-mappings

## WLO Sachgebietssystematiken 

Directory ```subjectAreas``` contains two helper scripts to map WLO [Sachgebietsystematiken](https://github.com/openeduhub/oeh-metadata-eaf-sachgebietssystematiken) to Wikipedia articles.

The first script `mapSachgebietLabels.py` extracts labels from the provided TTL file and maps these labels to Wikipedia. Therefore it uses our [entity linking tool](https://github.com/yovisto/kea-el-rest) as service. 

The output of the first script (e.g. `labels.txt`) is a list of labels and the corresponding Wikipedia article, if one was found.
Naturally, these results are not perfect at all, therfore it is nescessary to manually revise them and take into account possible ambiguities. 

After revision and correction of the output file, the second script `createSachgebieteTTL.py` can be used, to generate a TTL file containing the mappings (cf. `sachgebieteMapping.ttl`).


## WLO Schlagwortverzeichnis


Directory ```keywords``` contains two helper scripts to map WLO [Schlagwortverzeichnis](https://github.com/openeduhub/oeh-metadata-eaf-schlagwortverzeichnis) to Wikipedia articles.

The first script `mapKeywordLabels.py` extracts labels from the provided TTL file and maps these labels to Wikipedia. Therefore it uses our [entity linking tool](https://github.com/yovisto/kea-el-rest) as service. 

The output of the first script (e.g. `kwlabels.txt`) is a list of labels and the corresponding Wikipedia article, if one was found.
Naturally, these results are not perfect at all, therfore it is nescessary to manually revise them and take into account possible ambiguities. 

After revision and correction of the output file, the second script `createKeywordsTTL.py` can be used, to generate a TTL file containing the mappings (cf. `keywordMapping.ttl`).


## Wikipedia Normdata

The directory ```normdata``` contains a script to convert the extracted normdata from the [kea-wiki-extraction](https://github.com/yovisto/kea-wiki-extraction) tool in an RDF form.

Therefor you need to copy the ```normdata.txt``` file from [kea-wiki-extraction](https://github.com/yovisto/kea-wiki-extraction) to this directory an the execute the Python script ```createNormdataTTL.py```. 

An example result has been provided in the file ```normdata.ttl.zip``` (extracted as of 07. Dec. 2020)

