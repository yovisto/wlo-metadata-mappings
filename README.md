# wlo-metadata-mappings

This repo provides two helper scripts to map WLO [Sachgebietsystematiken](https://github.com/openeduhub/oeh-metadata-eaf-sachgebietssystematiken) to Wikipedia articles.

The first script `mapSachgebietLabels.py` extracts labels from the provided TTL file and maps these labels to Wikipedia. Therefore it uses our [entity linking tool](https://github.com/yovisto/kea-el-rest) as service. 

The output of the first script (e.g. `labels.txt`) is a list of labels and the corresponding Wikipedia article, if one was found.
Naturally, these results are not perfect at all, therfore it is nescessary to manually revise them and take into account possible ambiguities. 

After revision and correction of the output file, the second script `createSachgebieteTTL.py` can be used, to generate a TTL file containing the mappings (cf. `sachgebieteMapping.ttl`).


