# Tree and TreeInterface are designed to encapsulate the data and also encapsulate the data manipulation

import node
import pdb
import copy

class TreeInterface:
	
    def __init__(self, nodes):
        self.nodes = nodes

    def build_from_nodes(self):
    	# Returns a fully populated Tree 
    	root_node = next(nd for nd in self.nodes if nd.parent_id == "" )
    	self.nodes.remove(root_node)
    	new_tree = Tree(root_node)

    	for new_node in self.nodes:
    		# print("staring insert for id: " + new_node.id)
    		new_tree.insert_node_under_parent(child_node=new_node)

	 	return new_tree


class Tree:
	# This tree is implemented with an index into the tree for quick inserts and a full tree implementation
	# to support a DFS search pattern for the need to find the adjency list

	def __init__(self, root=None):
		self.root = root
		self.id_dictionary = {}
	
	def dfs_find(self, current_root_node, child_node):
		if current_root_node.id == child_node.id:
			print("current_root_node.id: "+current_root_node.id+" - child_node.id: " +child_node.id )
			return child_node

		if current_root_node.id == child_node.parent_id:
			print("current_root_node.id: "+current_root_node.id+" - child_node.id: " +child_node.id )
			return current_root_node
		else:
			for under_current in current_root_node.children:
				print("under_current.id: "+under_current.id+" - child_node.id: " +child_node.id )
				if under_current.id == child_node.parent_id:
					return under_current
				else:
					self.dfs_find(under_current, child_node)



	def insert_node_under_parent(self, child_node=None, starting_node=None):
		if starting_node == None:
			starting_node = self.root

		print("inserting_id: " + child_node.id + "parent_id => " + child_node.parent_id)
		parent_node = self.dfs_find(starting_node, child_node)

		parent_node.add_child(child_node)










# if self.id_dictionary.has_key(parent_id) is True:
# 	# insert into that nodes children
# 	print("existing parent: " + parent_id + " new_node.id: " + new_node.id)
# 	# print("existing node being added: " + new_node.id)
# 	print self.id_dictionary[parent_id]
# 	# self.id_dictionary[parent_id].children.append(new_node)
# 	# if new_node.id == "5":
# 	# 	pdb.set_trace()
# 	self.id_dictionary[parent_id].children.append(new_node)
# 	reference_node = next(x for x in self.id_dictionary[parent_id].children if x.id == new_node.id)
# 	self.id_dictionary[new_node.id] = reference_node
# else:
# 	print("NEW parent: " + parent_id + " new_node.id: " + new_node.id)
# 	self.id_dictionary[new_node.id] = new_node
# 	print self.id_dictionary[new_node.id].children


# 	# for c in self.id_dictionary[parent_id].children:
# 		# print c.parent_id
# else: 
# 	# print("new parent: " + parent_id)
# 	# print("new node being added: " + new_node.id)
# 	# insert into that node and
# 	self.id_dictionary[new_node.id] = new_node
# 	# for c in self.id_dictionary[parent_id].children:
# 	# 	print c.id
# 	# print self.id_dictionary


# traverse tree till parent_id == new_node.parent_id


# def 





