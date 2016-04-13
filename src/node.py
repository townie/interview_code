# Node of data, which is an interchange between adapters and Tree 
# Also generic enough to be used to compose the Tree structure.... 
# I might be more weary of using this for data sets that are large than memory.
#
#
# On that note, I would probably not use this approach for data sets expected to be 
# larger a certain threshold. That threshold is determined on operations required on data,
# the size of the machine, and size of the data.
#
#
# For interest of debate, if we were interested in some distributed graph processing,
# I might consiering off loading this to a graph database(Neo4J/orientDB) or to Postrges(tree format) 
# or if we really need some scale(petabytes) then HDFS with Spark with graphX
# But for this ambgious dataset in-memory nodes will be.
# 
# Other point of design is around using children as a standard array vs a numpy array, was for brevity.

class Node:

    def __init__(self, id=0, type="", parent_id="", content=None):
        self.id = id
        self.type = type
        self.parent_id = parent_id
        self.content = content
        self.children = []

    def add_child(self, new_node):
    	self.children = self.children + [new_node]