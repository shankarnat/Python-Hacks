data = [1,2,3,3,4,5, 1]
chunk_set = list(set(data))
chunk_s1 = [5,2,4,3,1]
print(chunk_set)

hunk_mapping =[chunk_s1.index(d) for d in data]

print(hunk_mapping)
