# tab = [i for i in range(100)]
# for i in range(2):
#     tab[0:1] = []
#     print(tab[0:1])
#     print(tab)

tab = [i for i in range(100)]
for i in range(3):
    print(tab[len(tab)-1:len(tab)])
    tab[len(tab)-1:len(tab)] = []


