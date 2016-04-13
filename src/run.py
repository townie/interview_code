import adapters
import tree
ad = adapters.MajorPartnerCSVDataAdapter("/Users/keith/repos/personal/rby_nodes/data/rby.csv")
nodes = ad.read_data()

ti = tree.TreeInterface(nodes)
t = ti.build_from_nodes()

keymap = t.build_adjency_list_for_red_node_ancestor()