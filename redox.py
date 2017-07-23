from random import randint

def add_new_node(node_name, nodes_list):
	node_id = "n" + str(len(nodes_list))
	new_node = {'id':node_id, 'label':node_name, 'size':3, 'x': randint(0,9), 'y': randint(0,9)}
	nodes_list.append(new_node)
	return new_node


def get_node_id(node_name, nodes_list):
	found_node = [node for node in nodes_list if node['label'] == node_name]
	
	if len(found_node) == 0:
		return add_new_node(node_name, nodes_list)['id']

	return found_node[0]['id']


def make_edge(source_node_id, target_node_id, edges_list):
	existing_edge = [edge for edge in edges_list if edge['source'] == source_node_id and edge['target'] == target_node_id]
	if len(existing_edge) > 0:
		return
	else:
		new_edge_id = "e" + str(len(edges_list))
		new_edge = {'id':new_edge_id, 'source':source_node_id, 'target':target_node_id}
		edges_list.append(new_edge)


def add_new_claim(doctor_name, facility_name, nodes_list, edges_list):
	doctor_node_id = get_node_id(doctor_name, nodes_list)
	facility_node_id = get_node_id(facility_name, nodes_list)
	make_edge(doctor_node_id, facility_node_id, edges_list)


def get_doc_name_from_claim(redox_claim):
	doctor = redox_claim['Providers'][0]
	doc_name = doctor['FirstName'] + ' ' + doctor['LastName']
	return doc_name


def get_facility_name_from_claim(redox_claim):
	return redox_claim['Visit']['Location']['Facility']


def save_to_json_file(data, file_path):
	file = open(file_path, 'w')
	j = json.dumps(data)
	file.write(j)
	file.close()


def get_from_json_file(file_path):
	file = open(file_path, 'r')
	data = json.loads(file.read())
	file.close()
	return data


def save_claim_from_redox_data(redox_data, path_to_graph_data):
	existing_graph = get_from_json_file(path_to_graph_data)
	nodes, edges = existing_graph['nodes'], existing_graph['edges']

	claim = redox_data['Claims'][0]
	doc_name = get_doc_name_from_claim(claim)
	facility_name = get_facility_name_from_claim(claim)
	add_new_claim(doc_name, facility_name, nodes, edges)

	new_graph = {'nodes':nodes, 'edges':edges}
	save_to_json_file(new_graph)

