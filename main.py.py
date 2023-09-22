#----- importing modules -----
import matplotlib.pyplot as plt

#----- First Come First Serve -----
def FCFS(seq,start):
    new_list = seq.copy()
    new_list.insert(0,start)
    str2 = str(new_list)
    #Only to move X-axis from bottom to top
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    #--------------------------------------
    x=new_list.copy()
    y=[]
    new_list.reverse()
    new_list_size= len(new_list)
    headmovement=0
    for i in range(0,new_list_size):
        y.append(-i)
        if i!=new_list_size-1:
            headmovement=headmovement+abs(new_list[i]-new_list[i+1])
    str1 = "headmovement = "+ str(headmovement)+ " cylinders"       
    plt.xlim(0,max_range)
    plt.plot(x,y,color='seagreen',markerfacecolor='aquamarine' ,marker='o',linewidth = 2.5, linestyle='--')
    plt.yticks([])
    plt.title("First Come First Serve Disk Scheduling algorithm")
    plt.text(0, -len(x),str1,fontsize=13)
    plt.text(132.8, -len(x),str2,fontsize=13)
    plt.show()

#------ LOOK Algorithm -----
def LOOK(seq,start):
    #for right
    new_list = seq.copy()
    new_list.insert(0,start)
    str2 = str(new_list)
    lst1=[]; lst2=[]
    x=[];y=[]
    #Only to move X-axis from bottom to top
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    #--------------------------------------
    for i in range(1,len(new_list)):
        if new_list[i]>=start:
            lst1.append(new_list[i])
        else:
            lst2.append(new_list[i])
    if max_range -max(new_list)< min(new_list):
        lst1.sort()
        lst2.sort(reverse=True)
        x.append(start)
        x.extend(lst1)
        x.extend(lst2)
    else:
        lst1.sort()
        lst2.sort(reverse=True)
        x.append(start)
        x.extend(lst2)
        x.extend(lst1)
    for i in range(0,len(new_list)):
        y.append(-i)
    headmovement=0
    for i in range(0,len(x)-1):
        headmovement=headmovement+abs(x[i]-x[i+1])
    str1 = "headmovement = "+ str(headmovement)+ " cylinders"
    plt.xlim(0,max_range)
    plt.plot(x,y,color='seagreen',markerfacecolor='aquamarine' ,marker='o',linewidth = 2.5, linestyle='--')
    plt.title("LOOK Disk Scheduling algorithm")
    plt.yticks([])
    plt.text(0, -9,str1,fontsize=13)
    plt.text(132.8, -9,str2,fontsize=13)
    plt.show()

#----- SCAN Algorithm -----
def SCAN(seq,start):
    new_list = seq.copy()
    new_list.insert(0,start)
    str2 = str(new_list)
    x=[];y=[]
    #Only to move X-axis from bottom to top
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    #--------------------------------------
    lst1=[]; lst2=[]
    for i in range(1,len(new_list)):
        if new_list[i]>=start:
            lst1.append(new_list[i])
        else:
            lst2.append(new_list[i])
    if max_range -max(new_list)< min(new_list):
        lst1.sort()
        lst2.sort(reverse=True)
        x.append(start)
        x.extend(lst1)
        x.append(max_range)
        x.extend(lst2)
    else:
        lst2.sort(reverse=True)
        lst1.sort()
        x.append(start)
        x.extend(lst2)
        x.append(0)
        x.extend(lst1)
    # print(max(new_list)-max_range)
    for i in range(0,len(new_list)+1):
        y.append(-i)
    headmovement=0
    for i in range(0,len(x)-1):
        headmovement=headmovement+abs(x[i]-x[i+1])
    str1 = "headmovement = "+ str(headmovement)+ " cylinders"
    plt.xlim(0,max_range)
    plt.plot(x,y,color='seagreen',markerfacecolor='aquamarine' ,marker='o',linewidth = 2.5, linestyle='--')
    plt.title("SCAN Disk Scheduling algorithm")
    plt.yticks([])
    plt.text(0, -10,str1,fontsize=13)
    plt.text(132.8, -10,str2,fontsize=13)
    plt.show()

#----- C-SCAN Algorithm -----
def C_SCAN(seq,start):
    #for right
    new_list = seq.copy()
    new_list.insert(0,start)
    str2 = str(new_list)
    lst1=[]; lst2=[]
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    #--------------------------------------
    for i in range(1,len(new_list)):
        if new_list[i]>=start:
            lst1.append(new_list[i])
        else:
            lst2.append(new_list[i])
    lst1.sort()
    lst2.sort()
    x=[];y=[]
    x.append(start)
    x.extend(lst1)
    x.append(max_range)
    x.append(0)
    x.extend(lst2)
    for i in range(0,len(new_list)+2):
        y.append(-i)
    headmovement=0
    for i in range(0,len(x)-1):
        if x[i]==max_range and x[i+1]==0:
            headmovement = headmovement+0
        else:
            headmovement=headmovement+abs(x[i]-x[i+1])
    str1 = "headmovement = "+ str(headmovement)+ " cylinders"
    plt.xlim(0,max_range)
    plt.plot(x,y,color='seagreen',markerfacecolor='aquamarine' ,marker='o',linewidth = 2.5, linestyle='--')
    plt.title("C-SCAN Disk Scheduling algorithm")
    plt.yticks([])
    plt.text(0, -11,str1,fontsize=13)
    plt.text(132.8, -11,str2,fontsize=13)
    plt.show()

#------ Shortest Seek Time First -----
def SSTF(seq,start):
    #for right
    new_list = seq.copy()
    new_list_2=new_list.copy()
    new_list_2.insert(0,start)
    str2 = str(new_list_2)
    # new_list.insert(0,start)
    x=[];y=[]
    #Only to move X-axis from bottom to top
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    #--------------------------------------
    x.append(start)
    temp = start
    mindiff=max_range+10
    minIdx=0
    new_list.sort()
    while len(new_list)>0:
        mindiff=max_range+10
        for i in range(0,len(new_list)):
            if abs(temp-new_list[i])<=mindiff:
                mindiff=temp-new_list[i]
                minIdx=i
        temp=new_list[minIdx]    
        x.append(new_list[minIdx])
        new_list.pop(minIdx)    
    for i in range(0,len(seq)+1):
        y.append(-i)
    headmovement=0
    for i in range(0,len(x)-1):
        headmovement=headmovement+abs(x[i]-x[i+1])
    str1 = "headmovement = "+ str(headmovement)+ " cylinders"
    plt.xlim(0,max_range)
    plt.plot(x,y,color='seagreen',markerfacecolor='aquamarine' ,marker='o',linewidth = 2.5, linestyle='--')
    plt.title("SSTF Disk Scheduling algorithm")
    plt.yticks([])
    plt.text(0, -9,str1,fontsize=13)
    plt.text(132.8, -9,str2,fontsize=13)
    plt.show()
    # print(x)  
      

#----- C-LOOK Algorithm -----
def C_LOOK(seq,start):
    #for right
    new_list = seq.copy()
    new_list.insert(0,start)
    str2 = str(new_list)
    lst1=[]; lst2=[]
    #Only to move X-axis from bottom to top
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    #--------------------------------------
    for i in range(1,len(new_list)):
        if new_list[i]>=start:
            lst1.append(new_list[i])
        else:
            lst2.append(new_list[i])
    lst1.sort()
    lst2.sort()
    x=[];y=[]
    x.append(start)
    x.extend(lst1)
    x.extend(lst2)
    for i in range(0,len(new_list)):
        y.append(-i)
    headmovement=0
    for i in range(0,len(x)-1):
        headmovement=headmovement+abs(x[i]-x[i+1])
    str1 = "headmovement = "+ str(headmovement)+ " cylinders"
    plt.xlim(0,max_range)
    plt.plot(x,y,color='seagreen',markerfacecolor='aquamarine' ,marker='o',linewidth = 2.5, linestyle='--')
    plt.title("C-LOOK Disk Scheduling algorithm")
    plt.yticks([])
    plt.text(0, -9,str1,fontsize=13)
    plt.text(132.8, -9,str2,fontsize=13)
    plt.show()

#----- Taking Input -----
max_range=int(input("Enter Number Of Tracks : "))
max_range=max_range-1
list_sequence = [int(x) for x in input("Enter the Requests sequence : ").split()]
if max(list_sequence) > max_range or min(list_sequence) < 0 :
    flag=0
    while flag==0:
        print("Values cant be greater "+str(max_range)+" and less than 0 ...")
        list_sequence = [int(x) for x in input("Enter the Requests sequence : ").split()]
        if max(list_sequence) > max_range or min(list_sequence) < 0 :
            flag=0
        else:
            flag=1
initial = int(input("Enter initial head position : "))
if initial>max_range or initial<0:
    flag = 0
    while flag==0:
        print("Enter initial head position in the specified range : ")
        initial = int(input("Enter initial head position : "))
        if initial>max_range or initial<0:
            flag=0
        else:
            flag=1
#-----------------------------------------------------




# print(list_sequence)
FCFS(list_sequence,initial)
# SSTF(list_sequence,initial)
# SCAN(list_sequence,initial)
# LOOK(list_sequence,initial)
# C_SCAN(list_sequence,initial)
# C_LOOK(list_sequence,initial)




