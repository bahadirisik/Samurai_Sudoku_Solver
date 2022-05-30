import time
import threading
from numpy import *
import concurrent.futures
import matplotlib.pyplot as plt 
import copy

matris=[]
gecici_matris=[]
gecici_matris2=[]
gecici_matris3=[]
gecici_matris4=[]
sol_ust=[]
sag_ust=[]
orta_matris=[]
orta_matriis=[]
sol_alt=[]
sag_alt=[]
sol_ust_dizi=[]
sag_ust_dizi=[]
sol_alt_dizi=[]
sag_alt_dizi=[]
orta_matris_dizi=[]
tut=0
q1=0

q2=0
tut2=0
asil_dizi1=[]
asil_dizi2=[]
asil_dizi3=[]
asil_dizi4=[]
asil_dizi5=[]
asil_dizi6=[]
asil_dizi7=[]
asil_dizi8=[]
sol_ust_doru=[]
sol_alt_doru=[]
sag_ust_doru=[]
sag_alt_doru=[]
dizi=[]
a=[]
b=[]
c=[]
d=[]
e=[]
time_dizi=[]
time_dizi1=[]
time_dizi2=[]
time_dizi3=[]
time_dizi4=[]
time_dizi5=[]
time_dizi6=[]
time_dizi7=[]
time_dizi8=[]
time_dizi9=[]
time_dizi10=[]
zaman=[]
zaman4=[]
cift_thread=False
sol_ust_cozum=[]
sag_ust_cozum=[]
sol_alt_cozum=[]
sag_alt_cozum=[]
orta_cozum=[]
a1=0
a2=0
a3=0
a4=0
a5=0



time1=time.perf_counter()
time6=time.perf_counter()
print("time1:",time1)
f = open("orta.txt", "w")
f1 = open("sol_ust.txt", "w")
f2 = open("sag_ust.txt", "w")
f3 = open("sol_alt.txt", "w")
f4 = open("sag_alt.txt", "w")
file = open("read.txt", "r")
con=0
for line in file:
    matris.append(line)
        
for i in matris:
    gecici_matris.append(",".join(i))

for i in gecici_matris:
    gecici_matris2.append(gecici_matris[con].split(","))
    con=con+1

con = 0 
for i in gecici_matris2:
    if(con != 20):
        i.pop()
    con =con +1
con=0

for i in gecici_matris2:
    con1=0
    for j in i:
        if(j=='*'):
            gecici_matris2[con][con1]=0
        else:
            gecici_matris2[con][con1]=int(gecici_matris2[con][con1])
        con1=con1+1
    con=con+1


for i in gecici_matris2:
    if(len(i)==18):
        gecici_matris3.append(i[0:9])
        gecici_matris3.append(i[9:18])
    elif(len(i)==9):
        gecici_matris3.append(i)
    elif(len(i)==21):
        gecici_matris3.append(i[0:9])
        gecici_matris3.append(i[6:15])
        gecici_matris3.append(i[12:21])


con =0
for i in gecici_matris3:
    if(con==0 or con==2 or con==4 or con==6 or con==8 or con==10 or con==12 or con==15 or con==18):
        sol_ust.append(i)
    elif(con==1 or con==3 or con==5 or con==7 or con==9 or con==11 or con==14 or con==17 or con==20):
        sag_ust.append(i)
    elif(con==13 or con==16 or con==19 or con==21 or con==22 or con==23 or con==25 or con==28 or con==31 ):
        orta_matris.append(i)
    elif(con==24 or con==27 or con==30 or con==33 or con==35 or con==37 or con==39 or con==41 or con==43 ):
        sol_alt.append(i)
    else:
        sag_alt.append(i)
    con = con +1





def solve1(grid,dizi1,dizi,time0,kopya,kopya1,kopya2,kopya3,kopya4,cozum1,tut1):
    
    dizi=[]
    
    global q1
    global zaman

    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(grid,row, column, number,kopya,kopya1,kopya2,kopya3,kopya4):
                        time3=time.perf_counter()
                        toplam=time3-time1
                        zaman4.append(toplam)
                        q1=q1+1
                        grid[row][column] = number
                        if(tut1==0):
                            
                            cozum1.append([row,column,number])
                            
                        solve1(grid,dizi1,dizi,time0,kopya,kopya1,kopya2,kopya3,kopya4,cozum1,tut1)
                        grid[row][column] = 0
            
                return 
    tut1+=tut1
    for i in grid:
        for j in i:
            dizi.append(j)
            
    dizi1.append(dizi)

def solve2(grid,dizi1,dizi,time0,kopya,kopya1,kopya2,kopya3,kopya4):
    global cift_thread
    global tut2
    global q2
    global zaman
    cift_thread=True
    for row in range(8,-1,-1):
        for column in range(8,-1,-1):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(grid,row, column, number,kopya,kopya1,kopya2,kopya3,kopya4):
                        time4=time.perf_counter()
                        toplam1=time4-time6
                        zaman.append(toplam1)

                        q2=q2+1
                        grid[row][column] = number   
                        solve2(grid,dizi1,dizi,time0,kopya,kopya1,kopya2,kopya3,kopya4)
                        grid[row][column] = 0
            
                return 


    
#check if the number is valid
def possible(grid,row, column, number,kopya,kopya1,kopya2,kopya3,kopya4):
    
    #Is the number appearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Is the number appearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    #Is the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    #burası sol ust bölüm
    if grid[len(grid)-1]["ad"]=='sol_ust' or  grid[len(grid)-1]["ad"]=='orta_matris':
        a=3-9+row
        b=3-9+column
        if(a==0 and b==0 or a==0 and b==1 or a==0 and b==2 or a==1 and b==0 or a==1 and b==1 or a==1 and b==2 or a==2 and b==0 or a==2 and b==1 or a==2 and b==2):
            if(grid[len(grid)-1]["ad"]=='orta_matris'):
                for i in range(len(kopya4[0])):
                    if kopya4[a][i] == number :
                        return False
                
                for i in range(len(kopya4)):
                    if kopya4[i][b] == number :
                        return False
            if(grid[len(grid)-1]["ad"]=='sol_ust'):
                for i in range(len(kopya[0])):
                    if kopya[a][i] == number :
                        return False
                
                for i in range(len(kopya)):
                    if kopya[i][b] == number :
                        return False
    

    #sağ üst bölüm
    if grid[len(grid)-1]["ad"]=='sag_ust' or  grid[len(grid)-1]["ad"]=='orta_matris':
        a=row-6
        b=6+column
        if(a==0 and b==6 or a==0 and b==7 or a==0 and b==8 or a==1 and b==6 or a==1 and b==7 or a==1 and b==8 or a==2 and b==6 or a==2 and b==7 or a==2 and b==8):
            if(grid[len(grid)-1]["ad"]=='orta_matris'):
                for i in range(len(kopya3[0])):
                    if kopya3[a][i] == number :
                        return False
                
                for i in range(len(kopya3)):
                    if kopya3[i][b] == number :
                        return False
            if(grid[len(grid)-1]["ad"]=='sag_ust'):
                for i in range(len(kopya[0])):
                    if kopya[a][i] == number :
                        return False
                
                for i in range(len(kopya)):
                    if kopya[i][b] == number :
                        return False
    #sol alt bölüm 
    if grid[len(grid)-1]["ad"]=='sol_alt' or  grid[len(grid)-1]["ad"]=='orta_matris':
        a=6+row
        b=column-6
        if(a==6 and b==0 or a==6 and b==1 or a==6 and b==2 or a==7 and b==0 or a==7 and b==1 or a==7 and b==2 or a==8 and b==0 or a==8 and b==1 or a==8 and b==2):
            if(grid[len(grid)-1]["ad"]=='orta_matris'):
                for i in range(len(kopya2[0])):
                    if kopya2[a][i] == number :
                        return False
            
                for i in range(len(kopya2)):
                    if kopya2[i][b] == number :
                        return False
            
            if(grid[len(grid)-1]["ad"]=='sol_alt'):
                for i in range(len(kopya[0])):
                    if kopya[a][i] == number :
                        return False
            
                for i in range(len(kopya)):
                    if kopya[i][b] == number :
                        return False
   
    
    #Burası sağ alt bolüm yada orta sol ust
    if grid[len(grid)-1]["ad"]=='sag_alt' or  grid[len(grid)-1]["ad"]=='orta_matris':
        a=6+row
        b=6+column
        if(a==6 and b==6 or a==6 and b==7 or a==6 and b==8 or a==7 and b==6 or a==7 and b==7 or a==7 and b==8 or a==8 and b==6 or a==8 and b==7 or a==8 and b==8):
            if(grid[len(grid)-1]["ad"]=='orta_matris'):
                
                for i in range(0,9):
                    if kopya1[a][i] == number:
                        return False
            
                for i in range(0,9):
                    if kopya1[i][b] == number:
                        return False
            if(grid[len(grid)-1]["ad"]=='sag_alt'):
                for i in range(0,9):
                    if kopya[a][i] == number:
                        return False
            
                for i in range(0,9):
                    if kopya[i][b] == number:
                        return False

    return True





orta_matris_kopya = copy.deepcopy(orta_matris)
sol_alt_kopya = copy.deepcopy(sol_alt)
sol_ust_kopya = copy.deepcopy(sol_ust)
sag_ust_kopya = copy.deepcopy(sag_ust)
sag_alt_kopya = copy.deepcopy(sag_alt)


orta_matris.append({"ad":"orta_matris"})
sol_alt.append({"ad":"sol_alt"})
sol_ust.append({"ad":"sol_ust"})
sag_alt.append({"ad":"sag_alt"})
sag_ust.append({"ad":"sag_ust"})

orta_matris_kopya1 = copy.deepcopy(orta_matris)
sol_alt_kopya1 = copy.deepcopy(sol_alt)
sol_ust_kopya1 = copy.deepcopy(sol_ust)
sag_ust_kopya1 = copy.deepcopy(sag_ust)
sag_alt_kopya1 = copy.deepcopy(sag_alt)


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.submit(solve1,grid=sol_ust,dizi1=sol_ust_dizi,dizi=a,time0=time_dizi,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya,cozum1=sol_ust_cozum,tut1=a1)
    executor.submit(solve1,grid=sol_alt,dizi1=sol_alt_dizi,dizi=b,time0=time_dizi1,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya,cozum1=sol_alt_cozum,tut1=a2)
    executor.submit(solve1,grid=sag_ust,dizi1=sag_ust_dizi,dizi=c,time0=time_dizi2,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya,cozum1=sag_ust_cozum,tut1=a3)
    executor.submit(solve1,grid=sag_alt,dizi1=sag_alt_dizi,dizi=d,time0=time_dizi3,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya,cozum1=sag_alt_cozum,tut1=a4)
    executor.submit(solve1,grid=orta_matris,dizi1=orta_matris_dizi,dizi=e,time0=time_dizi4,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya,cozum1=orta_cozum,tut1=a5)
    executor.submit(solve2,grid=sol_ust,dizi1=sol_ust_dizi,dizi=a,time0=time_dizi6,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya)
    executor.submit(solve2,grid=sol_alt,dizi1=sol_alt_dizi,dizi=b,time0=time_dizi7,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya)
    executor.submit(solve2,grid=sag_ust,dizi1=sag_ust_dizi,dizi=c,time0=time_dizi8,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya)
    executor.submit(solve2,grid=sag_alt,dizi1=sag_alt_dizi,dizi=d,time0=time_dizi9,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya)
    executor.submit(solve2,grid=orta_matris,dizi1=orta_matris_dizi,dizi=e,time0=time_dizi10,kopya=orta_matris_kopya,kopya1=sol_ust_kopya,kopya2=sag_ust_kopya,kopya3=sol_alt_kopya,kopya4=sag_alt_kopya)

print(len(sag_ust_dizi))
print("asdasdasdasdasdasdas",len(sol_ust_dizi))
print(len(sag_alt_dizi))
print(len(orta_matris_dizi))
print(len(sol_alt_dizi))



for i in orta_cozum:
    f.write(f"{str(i[0])}  {str(i[1])} ---->  {str(i[2])} \n")
for i in sol_ust_cozum:
    f1.write(f"{str(i[0])}  {str(i[1])} ---->  {str(i[2])} \n")
for i in sag_ust_cozum:
    f2.write(f"{str(i[0])}  {str(i[1])} ---->  {str(i[2])} \n")
for i in sol_alt_cozum:
    f3.write(f"{str(i[0])}  {str(i[1])} ---->  {str(i[2])} \n")
for i in sag_alt_cozum:
    f4.write(f"{str(i[0])}  {str(i[1])} ---->  {str(i[2])} \n")


uzunluk=[]
  
print(orta_matris_dizi)

uzunluk.append(len(time_dizi))
uzunluk.append(len(time_dizi1))
uzunluk.append(len(time_dizi2))
uzunluk.append(len(time_dizi3))
uzunluk.append(len(time_dizi4))

for i in range(1,max(uzunluk)+1):
    time_dizi5.append(round(0.1*i,1))



print("uznumsdasdasdasdasdasdasdasdasdas",uzunluk.index(max(uzunluk)))

print(uzunluk[uzunluk.index(max(uzunluk))])

print(time_dizi10)
print(time_dizi9)
print(time_dizi8)
print(time_dizi7)
print(time_dizi6)



   
     

print(len(sol_ust_dizi))
print(len(sol_alt_dizi))
print(len(sag_alt_dizi))
print(len(sag_ust_dizi))
print(len(orta_matris_dizi))


def sol_yukari_func(dizi,dizi1):
    asil_dizi=[] 
    for i in dizi:
        
        asil_dizi.append(i[0])
        asil_dizi.append(i[1])
        asil_dizi.append(i[2])
        asil_dizi.append(i[9])
        asil_dizi.append(i[10])
        asil_dizi.append(i[11])
        asil_dizi.append(i[18])
        asil_dizi.append(i[19])
        asil_dizi.append(i[20])
    
    for i in range(0,len(dizi)):
        
        dizi1.append(asil_dizi[i*9:(i+1)*9])
def sag_assagi_func(dizi,dizi1):
    asil_dizi=[] 
    for i in dizi:
        
        asil_dizi.append(i[60])
        asil_dizi.append(i[61])
        asil_dizi.append(i[62])
        asil_dizi.append(i[69])
        asil_dizi.append(i[70])
        asil_dizi.append(i[71])
        asil_dizi.append(i[78])
        asil_dizi.append(i[79])
        asil_dizi.append(i[80])
    
    for i in range(0,len(dizi)):
        
        dizi1.append(asil_dizi[i*9:(i+1)*9])     

def sag_yukari_func(dizi,dizi1):
    asil_dizi=[] 
    for i in dizi:
        
        asil_dizi.append(i[6])
        asil_dizi.append(i[7])
        asil_dizi.append(i[8])
        asil_dizi.append(i[15])
        asil_dizi.append(i[16])
        asil_dizi.append(i[17])
        asil_dizi.append(i[24])
        asil_dizi.append(i[25])
        asil_dizi.append(i[26])
    
    for i in range(0,len(dizi)):
        
        dizi1.append(asil_dizi[i*9:(i+1)*9])

def sol_assagi_func(dizi,dizi1):
    asil_dizi=[] 
    for i in dizi:
        
        asil_dizi.append(i[54])
        asil_dizi.append(i[55])
        asil_dizi.append(i[56])
        asil_dizi.append(i[63])
        asil_dizi.append(i[64])
        asil_dizi.append(i[65])
        asil_dizi.append(i[72])
        asil_dizi.append(i[73])
        asil_dizi.append(i[74])
    
    for i in range(0,len(dizi)):
        
        dizi1.append(asil_dizi[i*9:(i+1)*9])

def sorgula(dizi,dizi1,dizi2):
    for i in dizi:
        x=0
        for j in dizi1:
            if(i==j):
                dizi2.append(x)
            x=x+1

def son_durum(dizi,dizi1,dizi2,dizi3):
    for i in dizi:
        for j in dizi1:
            if i == j :
                for x in dizi2:
                    if i ==x:
                        for u in dizi3:
                            if i==u:
                                return i

def a(dizi,dizi1,sayi):
    x=0
    for i in dizi:
        if i==dizi1[sayi]:
            return x
        x=x+1



sol_yukari_func(orta_matris_dizi,asil_dizi1)
sag_yukari_func(orta_matris_dizi,asil_dizi2)
sol_assagi_func(orta_matris_dizi,asil_dizi3)
sag_assagi_func(orta_matris_dizi,asil_dizi4)
sag_assagi_func(sol_ust_dizi,asil_dizi5)
sol_assagi_func(sag_ust_dizi,asil_dizi6)
sag_yukari_func(sol_alt_dizi,asil_dizi7)
sol_yukari_func(sag_alt_dizi,asil_dizi8)

print("asdasdasdasd",asil_dizi1)

sorgula(asil_dizi5,asil_dizi1,sol_ust_doru)
sorgula(asil_dizi8,asil_dizi4,sag_alt_doru)
sorgula(asil_dizi6,asil_dizi2,sag_ust_doru)
sorgula(asil_dizi7,asil_dizi3,sol_alt_doru)

print("\n\n")
print(sol_ust_doru)
print(sag_alt_doru)
print(sag_ust_doru)
print(sol_alt_doru)


print("Son çözüm budur baba",son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru))
print(a(asil_dizi8,asil_dizi4,son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru)))
print(a(asil_dizi5,asil_dizi1,son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru)))
print(a(asil_dizi6,asil_dizi2,son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru)))
print(a(asil_dizi7,asil_dizi3,son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru)))





print(orta_matris[:len(orta_matris)-1])
print(len(orta_matris))
tut3=0
for i in range(0,9):
    for j in range(0,9):
        orta_matris[i][j]=orta_matris_dizi[son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru)][tut3]
        tut3=tut3+1
tut3=0
for i in range(0,9):
    for j in range(0,9):
        sol_alt[i][j]=sol_alt_dizi[a(asil_dizi7,asil_dizi3,son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru))][tut3]
        tut3=tut3+1
tut3=0
for i in range(0,9):
    for j in range(0,9):
        sol_ust[i][j]=sol_ust_dizi[a(asil_dizi5,asil_dizi1,son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru))][tut3]
        tut3=tut3+1
tut3=0
for i in range(0,9):
    for j in range(0,9):
        sag_alt[i][j]=sag_alt_dizi[a(asil_dizi8,asil_dizi4,son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru))][tut3]
        tut3=tut3+1
tut3=0
for i in range(0,9):
    for j in range(0,9):
        sag_ust[i][j]=sag_ust_dizi[a(asil_dizi6,asil_dizi2,son_durum(sol_ust_doru,sag_alt_doru,sag_ust_doru,sol_alt_doru))][tut3]
        tut3=tut3+1
print("sol ust")
print(matrix(sol_ust[:9]))
print("\n")
print("sag ust")
print(matrix(sag_ust[:9]))
print("\n")
print("orta ")
print(matrix(orta_matris[:9]))
print("\n")
print("sol alt")
print(matrix(sol_alt[:9]))
print("\n")
print("sag alt")
print(matrix(sag_alt[:9]))

print("zaman4 size ",zaman4[0])
print("zaman4 size ",zaman4[len(zaman4)-1])

sayıcı=0
sayac=0
kac_tane=[]
doru=True



while(doru):
    for i in zaman4:
        if i>=round(zaman4[0]+sayıcı,2) and i<=round(zaman4[0]+sayıcı+0.1,2):
            sayac+=1
    kac_tane.append(sayac)
    sayac=0
    sayıcı+=0.1
    if(round(zaman4[0]+sayıcı+0.1,2)>=zaman4[len(zaman4)-1]):
        doru=False

print(kac_tane)
kac_tane1=[]
if(cift_thread):
    sayıcı1=0
    sayac1=0
    
    doru1=True
    while(doru1):
        for i in zaman:
            if i>=round(zaman[0]+sayıcı1,2) and i<=round(zaman[0]+sayıcı1+0.1,2):
                sayac1+=1
        kac_tane1.append(sayac1)
        sayac1=0
        sayıcı1+=0.1
        if(round(zaman[0]+sayıcı1+0.1,2)>=zaman[len(zaman)-1]):
            doru1=False
kac_tane2=[]
if(cift_thread):

    print(kac_tane1)
    
    if(len(kac_tane)>len(kac_tane1)):
        for i in range(0,len(kac_tane1)):
            kac_tane2.append(kac_tane[i]+kac_tane1[i])
        
        for i in range(len(kac_tane1),len(kac_tane)):
            kac_tane2.append(kac_tane[i])
        
        
    else:
        for i in range(0,len(kac_tane)):
            kac_tane2.append(kac_tane[i]+kac_tane1[i])
        for i in range(len(kac_tane),len(kac_tane1)):
            kac_tane2.append(kac_tane1[i])
    

print(kac_tane2)

z1=[]
z2=[]
y=0
for i in kac_tane:
    z1.append(round(0+y,2))
    y+=0.1

if(cift_thread):
    y=0
    for i in kac_tane2:
        z2.append(round(0+y,2))
        y+=0.1

print(z1)
print(z2)

plt.plot(z1,kac_tane)
plt.plot(z2,kac_tane2)
plt.show()

time2=time.perf_counter()
print(f'asdasdas in {round(time2-time1,2)} second(s)')
file.close()
f.close()

