def odd_index_sum(sia):
    jami = 0
    for index in range(len(sia)):
        if index % 2 != 0:
            jami += sia[index]
    return jami
sia = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = odd_index_sum(sia)
print(result)