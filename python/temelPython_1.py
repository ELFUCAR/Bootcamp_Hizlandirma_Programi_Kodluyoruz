#-----------  1.örnek --------------
inp=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
out=[]

def flatten(x):
    for i in x:
        if(isinstance(i,list)):
            flatten(i)
        else:
            out.append(i)

flatten(inp)
print(out)

#------------ 2.Örnek ------------------
inp= [[1, 2], [3, 4], [5, 6, 7]]
a=[]
inp.reverse()

def rev(x):
    for i in x:
        i.reverse()
        a.append(i)

rev(inp)
print(a)
