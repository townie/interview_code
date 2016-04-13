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
    		print("staring insert for id: " + new_node.id)
    		new_tree.insert_node_under_parent(child_node=new_node)

    	return new_tree


class Tree:
	# This tree is implemented for dfs inserts and traversal from root.
	# I was planning on also a building an index into each not for O(1) lookup time... but python 
	# object references got me a little tripped up so I moved on beyond that for a naive DFS.
	#
	# To support a DFS search pattern for the need to find the adjency list with 
	# a cahce of recently visited top_level_collector nodes.

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
				print("under_current.id: "+under_current.id+" - child_node.id: " +child_node.id + "desired parent_id:" + child_node.parent_id )
				if under_current.id == child_node.parent_id:
					print("FOUND node: " + under_current.id)
					return under_current
				else:
					self.dfs_find(under_current, child_node)


	def insert_node_under_parent(self, child_node=None, starting_node=None):
		# Wrapper for DFS finding pattern
		if starting_node == None:
			starting_node = self.root

		print("inserting_id: " + child_node.id + "parent_id => " + child_node.parent_id)
		parent_node = self.dfs_find(starting_node, child_node)
		if parent_node == None:
			# I might consider adding better error handing here for things that are not in graph since this is 
			# not my favorite way of handling this.
			return None 
		parent_node.add_child(child_node)

	def build_adjency_list_for_red_node_ancestor(self, top_level_collector='r'):
		# Hate this method name, but in the sake of clarity of this example
		# @param [String] top_level_collector - could be extended to any order of filters/collectors
		self.dfs_collector_cache(top_level_collector, self.root)

	def dfs_collector_cache(self, tlck, start_node, current_current_map={}, id_of_recent_collector=None):
		# @param [String] tlck - top_level_collector_key 
		print(start_node.id)
		if start_node.type == tlck:
			id_of_recent_collector = start_node.id
			# pdb.set_trace()
			current_current_map[start_node.id] = {}

		if start_node.children:
			for child in start_node.children:
				if current_current_map.has_key(start_node.id):
					depth = current_current_map[start_node.id] 
				else:
					depth = current_current_map[start_node.id] = {}

				if depth.has_key(child.type):
					current_current_map[start_node.id][child.type].append(child.id)
				else:
					current_current_map[start_node.id][child.type] = [child.id]
				self.dfs_collector_cache(tlck, child, current_current_map, id_of_recent_collector)
		else:
			return current_current_map
