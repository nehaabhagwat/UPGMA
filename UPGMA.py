__author__ = "Neha Bhagwat"

# UPGMA.py
# Author: Neha Bhagwat
# Last Updated: December 30, 2017
# Program to implement the UPGMA Algorithm


class Cluster:
    def __init__(self, cluster_list):
        self.cluster_list = cluster_list
        self.num_of_sequences = len(cluster_list)

def find_min(distance_matrix):
    minimum_distance = float("inf")
    cluster1_index = 0
    cluster2_index = 0

    for i in range(0, len(distance_matrix)):
        for j in range(0, len(distance_matrix[i])):
            if distance_matrix[i][j] < minimum_distance:
                minimum_distance = distance_matrix[i][j]
                cluster1_index = i
                cluster2_index = j

    return (cluster1_index, cluster2_index)

def combine_cluster_names(list_of_sequences, cluster1_index, cluster2_index):
    if cluster1_index > cluster2_index:
        temp = cluster1_index
        cluster1_index = cluster2_index
        cluster2_index = temp

    list_of_sequences[cluster1_index].cluster_list = list_of_sequences[cluster1_index].cluster_list + list_of_sequences[cluster2_index].cluster_list
    list_of_sequences[cluster1_index].num_of_sequences = len(list_of_sequences[cluster1_index].cluster_list)
    del list_of_sequences[cluster2_index]
    return list_of_sequences    

def combine_clusters(distance_matrix, cluster_names, cluster1_index, cluster2_index):
    if cluster1_index > cluster2_index:
        temp = cluster1_index
        cluster1_index = cluster2_index
        cluster2_index = temp
    print "Merging clusters " + str(cluster_names[cluster1_index].cluster_list) + " and " + str(cluster_names[cluster2_index].cluster_list) + " at height " + str(distance_matrix[cluster2_index][cluster1_index]) + "."
    new_cluster_distances = []
    for index in range(0, cluster1_index):
        new_cluster_distances.append(((distance_matrix[cluster1_index][index]*len(cluster_names[cluster1_index].cluster_list))+ (distance_matrix[cluster2_index][index]*len(cluster_names[cluster2_index].cluster_list)))/(len(cluster_names[index].cluster_list) * (len(cluster_names[cluster2_index].cluster_list)+len(cluster_names[cluster1_index].cluster_list))))
    print "Printing clusters: "
    for ele in list_of_sequences:
        print ele.cluster_list
    print "\n\n"
    distance_matrix[cluster1_index] = new_cluster_distances

    for index in range(cluster1_index + 1, cluster2_index):
        distance_matrix[index][cluster1_index] = ((distance_matrix[index][cluster1_index]*len(cluster_names[cluster1_index].cluster_list)) + (distance_matrix[cluster2_index][index]*len(cluster_names[cluster2_index].cluster_list)))/(len(cluster_names[index].cluster_list) * (len(cluster_names[cluster2_index].cluster_list)+len(cluster_names[cluster1_index].cluster_list)))

    for index in range(cluster2_index + 1, len(distance_matrix)):
        distance_matrix[index][cluster1_index] = ((distance_matrix[index][cluster1_index]*len(cluster_names[cluster1_index].cluster_list)) + (distance_matrix[index][cluster2_index]*len(cluster_names[cluster2_index].cluster_list)))/(len(cluster_names[index].cluster_list) * (len(cluster_names[cluster2_index].cluster_list)+len(cluster_names[cluster1_index].cluster_list)))                                
        del distance_matrix[index][cluster2_index]

    del distance_matrix[cluster2_index]
    return distance_matrix
    
def implement_UPGMA(distance_matrix, list_of_sequences):
    while len(list_of_sequences) > 1:
        cluster1_index, cluster2_index = find_min(distance_matrix)
        
        distance_matrix = combine_clusters(distance_matrix, list_of_sequences, cluster1_index, cluster2_index)
        list_of_sequences = combine_cluster_names(list_of_sequences, cluster1_index, cluster2_index)
    return list_of_sequences        

if __name__ == "__main__":
    input_file = open("input_matrix.txt")
    distance_matrix_text = input_file.readlines()
    distance_matrix = []
    for line in distance_matrix_text:
        line = line.split(",")
        distance_matrix.append(line)
    new_distance_matrix = []
    list_of_sequences = []
    count = 1
    for row in distance_matrix:
        new_cluster = Cluster([count])
        list_of_sequences.append(new_cluster)
        count += 1
        # row = row[1:]
        new_row = []
        for ele in row:
            ele = float(ele.rstrip('\n'))
            new_row.append(ele)
        new_distance_matrix.append(new_row)
    distance_matrix = new_distance_matrix
    for ele in list_of_sequences:
        print ele.cluster_list
    num_of_nodes = len(distance_matrix)
    # print num_of_nodes
    print "\n\n"
    for i in range(0, len(distance_matrix)):
        distance_matrix[i] = distance_matrix[i][:i]

for ele in implement_UPGMA(distance_matrix, list_of_sequences):
    print ele.cluster_list
    # print distance_matrix
