from Attributes import *

def DebugClusters(clusters, attrib):
    rep = []
    for a in clusters:
        tmp = []
        for k in range(0,len(a)):
            tmp.append(a[k][attrib])
        rep.append(tmp)
    print rep

def CU(clusters, attrib):
    Verbose = False
    
    m = len(clusters)

    Number_Of_Items = 0.0
    for c in clusters:
        Number_Of_Items += len(c)
    
    if (Verbose):
        print "m clusters: ", m, ", Number_Of_Items: ", Number_Of_Items
    
    # step 1, compute P(Ck) for all k
    P_Ck = []
    for k in range(0,m):
        P_Ck_val = float(len(clusters[k])) / Number_Of_Items
        P_Ck.append(P_Ck_val)

    if (Verbose):
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
                    if item[a] == value:
                        occurances += 1
            
            sumsumP_Ai_Vij += pow(float(occurances) / Number_Of_Items, 2)

    if (Verbose):
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
                    if item[a] == value:
                        occurances += 1

                items_in_cluster = len(cluster)

                sumsumP_Ai_Vij_particular_k += pow(float(occurances) / items_in_cluster, 2)

        #print sumsumP_Ai_Vij_particular_k
        sumsumP_Ai_Vij_Ck.append(sumsumP_Ai_Vij_particular_k)

    if (Verbose):
        print "__sum sum P(Ai=Vij|Ck): ", sumsumP_Ai_Vij_Ck

    CU = 0
    for k in range(0,m):
        CU += P_Ck[k] * (sumsumP_Ai_Vij_Ck[k] - sumsumP_Ai_Vij)
    return 1.0/m * (CU)

#clusters = [[{'BodyCover': 'feathers', 'BodyTemp': 'regulated', 'HeartChamber': 'four', 'Fertilization': 'internal'}], [{'BodyCover': 'hair', 'BodyTemp': 'regulated', 'HeartChamber': 'four', 'Fertilization': 'internal'}, {'BodyCover': 'tmp', 'BodyTemp': 'unregulated', 'HeartChamber': 'imperfect-four', 'Fertilization': 'internal'}, {'BodyCover': 'cornified-skin', 'BodyTemp': 'unregulated', 'HeartChamber': 'imperfect-four', 'Fertilization': 'internal'}]]

#print "IN_clusters_: ", clusters
#print "IN_attrib_: ", attributes

#print CU(clusters, attributes)
