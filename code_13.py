def merge_sorted(eastside,westside):
    #input logic to merge but not in one line 1
    e = w = 0
    result = []
    while e < len(eastside) and w < len(westside):
        if eastside[e] < westside[w]: 
            result.append(eastside[e])
            e += 1  
        else:
            result.append(westside[w])
            w += 1
    
    while e < len(eastside[e]):
        result.append(eastside[e])
        e += 1

    while w < len(westside[w]):
        result.append(westside[w])
        w  += 1
    return result

def get_merge_sorted_list (unsorted_list):
    #division part done in class 
    if len (unsorted_list)==1:
        return unsorted_list
    # ^we need to divide the list until there are individual sections of each element of the list 
    midland = int((len(unsorted_list)//2))
    #^ find the mid point
    eastside = unsorted_list [:midland]
    westside = unsorted_list [midland:]
    #^name each half for when we merge 
    halfeast= get_merge_sorted_list (eastside)
    halfwest= get_merge_sorted_list (westside)
    #^ using recursion 
    return sorted(eastside + westside)


if __name__ == "__main__":
    unsorted_list=[4,8,6,1,0,6,8,6,3,9,]
    result = get_merge_sorted_list(unsorted_list)
    print(result)
