l = [16,20,16,18,38,33,20,18,90]

l_uniques = sorted(set(l))
compressed_l = [l_uniques.index(i)+1 for i in l]

print(compressed_l)
# output = [1, 3, 1, 2, 5, 4, 3, 2, 6]