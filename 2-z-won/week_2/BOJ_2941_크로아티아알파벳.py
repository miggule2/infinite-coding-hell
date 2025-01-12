cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
sentence = input()

for i in cro_list:
    sentence = sentence.replace(i, "1")
print(len(sentence))

            