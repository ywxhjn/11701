#输入有多少个人
number = int(input("人数？"))
survivor = 0
#建立一个有number个人的列表
survivors = [i for i in range(1,number+1)]
#输出列表survivos
print(survivors)
#当列表中只有一个人的时候，则停止循环
#不知道循环终止的条件的时候可用while循环 
while len(survivors) > 1:
#前面十二个人报完数之后就把他们放到最后面去，既不影响整体的长度，也不影响整体的顺序，还可以保持无限循环
#妙不可言a！    
    for person in range(12):
        survivor = survivors.pop(0)
        survivors.append(survivor)
    del survivors[0]
print(survivors)     
   
