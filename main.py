import os
import json



def openandwiteFile(Filetoread, pathtodumpjsondata):
    f = open(Filetoread, 'r')
    thisfile = json.load(f)
    reset_data = json.dumps(thisfile, indent=4)

    with open(pathtodumpjsondata, "w") as outfile:
        outfile.write(reset_data)



if __name__ == '__main__':
   openandwiteFile('./data/data_1.json', './schema/schema_12.json')