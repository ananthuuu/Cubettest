


my_dict = {"A":1,"B":2,"C":3,"D":4,"E":1,"F":3}
#   {1:["A","E"],3:["C","F"]}


valuelist=[]
keylist=[]

list1=[1,2,3,3,4,5,6,7]

listvalue=my_dict.values()
listkey=my_dict.values()


nonrepeatedval=set(value for value in listvalue if listvalue.count(value)>1)
nonrepeatedval=list(nonrepeatedval)

i=0
newdict={}

for keys,value in my_dict.items():
    
   
    if(value in nonrepeatedval) :
        
        try :

            newdict[value].append(keys)
        except :
            newdict[value]=[keys]



print(newdict)
        



    
