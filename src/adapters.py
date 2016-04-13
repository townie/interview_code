# The idea of this reader is that you can create an adapaters that know about how the data is stored
# and is able to read in the data into a standard interface to build a tree.

import node
import csv

class MajorPartnerCSVDataAdapter:
    # I dislike this name, but it is designed to illustrate the nature of this data source, 
    # desiging this API to consume a REST API might get versioned to: /data/major_partner/v1/nodes

    def __init__(self, file_path):
        self.file_path = file_path


    def read_data(self):
        nodes = []
        with open(self.file_path, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            # skip the headers, might want to extend this to look at headers 
            next(reader, None)
            
            for row in reader:
                nodes.append(node.Node(id=row[0], type=row[1], parent_id=row[2]))

        return nodes
