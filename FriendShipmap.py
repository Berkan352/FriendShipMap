import random
from pyvis.network import Network

isimler=["Berkan","Ömer","Abdullah","Ahmet","Mehmet","Elif","Aslı","Yaren","Mustafa","Sinan","Sinem","Merve",
         "Ali","Veli","Ayşe","Hatice","Uğur","Meltem","Tuğçe","Görkem","Hilal","Yavuz","Recep","Emine",
         "Bilal","Selçuk","Berat"]

idler = list(range(1,28))

renkler=['#3da831', '#9a31a8', '#3155a8', '#eb4034','#2a45b8','#2a45b8','#2a45b8','#3da831', '#9a31a8', '#3155a8', '#eb4034','#2a45b8','#2a45b8','#2a45b8',
         '#3da731', '#8a31a8', '#2135a8', '#eb4034','#2a25b8','#2a35b8','#2a46b8','#3da831', '#9a31a8', '#3155a8', '#eb4034','#2a45b8','#2a45b8']


net = Network(width="1000",height="600")



net.add_nodes(idler,
              label=isimler,
              color=renkler)

komsular=[]
for _ in range(40):
    x=random.choice(idler)
    y=random.choice(idler)
    if x==y:
        y=random.choice(idler)
    komsular.append((x,y))

net.add_edges(komsular)



net.neighbors(1)

net.get_adj_list()

nodes=net.nodes
edges=net.edges

def FindFriendshipDegree(isim1,isim2):
    isim1=isim1.lower()
    isim2=isim2.lower()
    name1=isim1.capitalize()
    name2=isim2.capitalize()
    id1= None
    id2=None
    for i,val in enumerate(nodes, start=1):
        if name1 in val.values():
            id1=i
        if name2 in val.values():
            id2 = i
    if id1 is None or id2 is None:
        print(f'{name1} ya da {name2} diye biri network içerisinde bulunmuyor')
        exit()

    toVisit=[id2]
    bl = True
    count = 1
    while bl:
        toVisit = [x for i in range(len(toVisit)) for x in net.neighbors(toVisit[i])]
        if id1 in toVisit:
            print("----------------------------------------------------------")
            print(f'{name1} ve {name2} arasındaki arkadaşlık derecesi {count}')
            print("----------------------------------------------------------")
            bl = False
        else:
            count += 1
            if not toVisit or count>6:
                print('Arkadaşlık ilişkileri bulunmamakta')
                break


isim1=input("Lütfen ilk ismi girin: ")
isim2=input("Lütfen ikinci ismi girin: ")

FindFriendshipDegree(isim1,isim2)

net.show('DataProject.html')




