# category utility measurement
# lets define attributes and values

from collections import defaultdict

attrib = defaultdict(list)

attrib['color'].append('r')
attrib['color'].append('g')
attrib['color'].append('b')
attrib['color'].append('y')

attrib['size'].append('s')
attrib['size'].append('m')
attrib['size'].append('l')

attrib['tax'].append('1')
attrib['tax'].append('0')

print "attrib: ", attrib.items()

items = []
items.append(['r','s','1'])
items.append(['r','l','0'])
items.append(['b','m','1'])
items.append(['g','m','1'])
items.append(['g','m','0'])

print items

clusters = []
clusters.append([items[0],items[1]])
clusters.append([items[2],items[3],items[4]])

print clusters

def CU(clusters, attrib):
    m = len(clusters)

    Number_Of_Items = 0.0
    for c in clusters:
        Number_Of_Items += len(c)
    
    print "m clusters: ", m, ", Number_Of_Items: ", Number_Of_Items
    
    # step 1, compute P(Ck) for all k
    P_Ck = []
    for k in range(0,m):
        P_Ck_val = float(len(clusters[k])) / Number_Of_Items
        P_Ck.append(P_Ck_val)

    print "__P(Ck) for all k: ", P_Ck

    # step 2, compute (sum sum P(Ai=Vij)^2)
    ## for each attrib, for each value, compute occurances / number of items
    sumsumP_Ai_Vij = 0
    
    for a in attrib:
        for value in attrib[a]:
            #print a, value

            occurances = 0
            for cluster in clusters:
                for item in cluster:
                    #print item
                    if (value in item):
                        occurances += 1
            
            sumsumP_Ai_Vij += pow(float(occurances) / Number_Of_Items, 2)

    print "__sum sum P(Ai=Vij)^2: ", sumsumP_Ai_Vij

    # step 3, compute (sum sum P(Ai=Vij|Ck))
    sumsumP_Ai_Vij_Ck = []
    for k in range(0,m):
        cluster = clusters[k]
        #print "cluster: ", cluster

        sumsumP_Ai_Vij_particular_k = 0
        
        for a in attrib:
            for value in attrib[a]:
                #print a, value

                occurances = 0
                for item in cluster:
                    if (value in item):
                        occurances += 1

                items_in_cluster = len(cluster)

                sumsumP_Ai_Vij_particular_k += pow(float(occurances) / items_in_cluster, 2)

        #print sumsumP_Ai_Vij_particular_k
        sumsumP_Ai_Vij_Ck.append(sumsumP_Ai_Vij_particular_k)

    print "__sum sum P(Ai=Vij|Ck): ", sumsumP_Ai_Vij_Ck

    CU = 0
    for k in range(0,m):
        CU += P_Ck[k] * (sumsumP_Ai_Vij_Ck[k] - sumsumP_Ai_Vij)
    return 1.0/m * (CU)


print CU(clusters, attrib)
