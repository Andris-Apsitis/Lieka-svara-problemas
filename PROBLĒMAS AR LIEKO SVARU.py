print('%59s' % "Lieka svara problema")
print(" ")
print('%50s' % "***")
print("******************************************************************************************************")
print("Si programma palidzes saprast, vai Tev ir liekais svars un kas ir jamaina, lai cinitos ar lieko svaru.")
print("Si programma ir pedavata personam no 7 lidz 25 gadu vecumam.")
print("******************************************************************************************************")

# 1. Jautajums
print(" ")
print("1. Aizpildi savus datus")
dzimums=int(input(" 1)Dzimums (1-sieviete/2-viretis): "))
while dzimums!=1 and dzimums!=2:
 print("***Nepareiza atbilde!***")
 dzimums=int(input(" 1)Dzimums (1-sieviete/2-viretis): "))
vecums=int(input(" 2)Vecums: "))
svars=int(input(" 3)Svars (kg): "))
augstums=int(input(" 4)Augums (cm): "))
print(" ")

# 2. Jautajums
print("2. Vai Tu nodarbojies ar sportu?")
print(" 1)Ne")
print(" 2)Ja, 1 reizi nedela")
print(" 3)Ja, 2-3 reizes nedela") 
print(" 4)Ja, 4-5 reizes nedela")
print(" 5)Ja, 6-7 reizes nedela")
a=int(input("Atbildes Nr.: "))
print(" ")
while a!=1 and a!=2 and a!=3 and a!=4 and a!=5:
 print("")
 print("***Nepareiza atbilde!***")
 print("")
 print("2. Vai Tu nodarbojies ar sportu?")
 print(" 1)Ne")
 print(" 2)Ja, 1 reizi nedela")
 print(" 3)Ja, 2-3 reizes nedela") 
 print(" 4)Ja, 4-5 reizes nedela")
 print(" 5)Ja, 6-7 reizes nedela")
 a=int(input("Atbildes Nr.: "))  
 print(" ")
 
# 3. Jautajums
print("3. Cik aktivs ir Tavs dzives veids?")
print(" 1)Mazaktivs dzivesveids")
print(" 2)Aktivs dzivesveids")
b=int(input("Atbildes Nr.: "))
print(" ")
while b!=1 and b!=2:
 print("")
 print("***Nepareiza atbilde!***")
 print("")
 print("3. Cik aktivs ir Tavs dzives veids?")
 print(" 1)Mazaktivs dzivesveids")
 print(" 2)Aktivs dzivesveids")
 b=int(input("Atbildes Nr.: "))
 print(" ")  
 
# 4. Jautajums
print("4. Noverte savu edienkarti.")
print(" 1)Parmerigi lielas porcijas, vai augsts kaloriju saturs edienos, velas vakarinas")
print(" 2)Parmerigi lielas porcijas, vai augsts kaloriju saturs edienos")
print(" 3)Velas vakarinas")
print(" 4)Nav paresanas")
c=int(input("Atbildes Nr.: "))
print(" ")
while c!=1 and c!=2 and c!=3 and c!=4:
 print("")
 print("***Nepareiza atbilde!***")
 print("") 
 print("4. Novertejiet savu edienkarti.")
 print(" 1)Parmerigi lielas porcijas, vai augsts kaloriju saturs edienos, velas vakarinas")
 print(" 2)Parmerigi lielas porcijas, vai augsts kaloriju saturs edienos")
 print(" 3)Velas vakarinas")
 print(" 4)Nav paresanas")
 c=int(input("Atbildes Nr.: "))
 print(" ")  

# 5. Jautajums
print("5. Noverte savu uzturvertibas lidzsvaru.")
print(" 1)Tikai veseliga partika")
print(" 2)Reti edu kaitigu partiku")
print(" 3)Biezi edu kaitigu partiku")
d=int(input("Atbildes Nr.: "))
print(" ")
while d!=1 and d!=2 and d!=3:
 print("")
 print("***Nepareiza atbilde!***")
 print("")
 print("5. Noverte savu uzturvertibas lidzsvaru.")
 print(" 1)Tikai veseliga partika")
 print(" 2)Reti edu kaitigu partiku")
 print(" 3)Biezi edu kaitigu partiku")
 d=int(input("Atbildes Nr.: "))
 print(" ")  
 
# 6. Jautajums 
print("6. Vai Tev ir nervu vai endokrinu sistemas saslimsanas?")
print(" 1)Ja")
print(" 2)Ne")
e=int(input("Atbildes Nr.: "))
print(" ") 
while e!=1 and e!=2:
 print("")
 print("***Nepareiza atbilde!***")
 print("") 
 print("6. Vai Tev ir nervu vai endokrinu sistemas saslimsanas?")
 print(" 1)Ja")
 print(" 2)Ne")
 e=int(input("Atbildes Nr.: "))
 print(" ") 
  
# 7. Jautajums
print("7. Vai Tu lieto kadus medikamentus ilgtermina?")
print(" 1)Ja")
print(" 2)Ne")
f=int(input("Atbildes Nr.: "))
print(" ") 
while f!=1 and f!=2:
 print("")
 print("***Nepareiza atbilde!***")
 print("") 
 print("7. Vai Tu lieto kadus medikamentus ilgtermina?")
 print(" 1)Ja")
 print(" 2)Ne")
 f=int(input("Atbildes Nr.: "))
 print(" ")
  
print("******************************************************************************************************")
print(" ")

if vecums==9 or vecums==10 or vecums==11 or vecums==12 or vecums==13 or vecums==14:
 if dzimums==1:
  normsvars=augstums-106
  print("Tavs normals svars:", normsvars,"kg (±5 kg)")
 if dzimums==2:
  normsvars=augstums-105
  print("Tavs normals svars:", normsvars,"kg (±5 kg)" )  
if vecums==7 or vecums==8:
 if dzimums==1:
  normsvars=augstums-101
  print("Tavs normals svars:", normsvars,"kg (±5 kg)")
 if dzimums==2:
  normsvars=augstums-100
  print("Tavs normals svars:", normsvars,"kg (±5 kg)" )  
else:
 if dzimums==1:
  normsvars=augstums-113 
  print("Tavs normals svars:", normsvars,"kg (±5 kg)") 
 if dzimums==2:
  normsvars=augstums-110
  print("Tavs normals svars:", normsvars,"kg (±5 kg)" )
 
normsvars=normsvars+5
if normsvars>=svars:
 print("Tev nav leka svara")
 x=1
if normsvars<svars:
 liekkg=svars-normsvars
 print("Tev ir lekais svars:",liekkg,"kg")
 x=2
 
if vecums==9 or vecums==10 or vecums==11 or vecums==12 or vecums==13 or vecums==14:
 print("Tagat tev ir pubertatu periods un tava fiziska forma var strauji mainities.") 

print(" ")

if x==1:
 if a==1:
  print("Tev ir janodarbojas ar sportu lai atbalstitu savu fizisko formu.")
 if a==2:
  print("Tev petiek Tavas sportosanas, bet butu labi ja Tu nodarbotos ar sportu vairak.")
 if a==3 or a==4 or a==5:
  print("Tu daudz nodarbojies ar sportu, malacis!")
 if b==1:
  print("Butu labi, ja Tu vairak kusttos, jo tas labi ietekme uz tavu veselibu.")
 if b==2:
  print("Malacis, ka daudz kusties!")   
 if c==1:
  print("Tas nekas, ka Tev ir parmerigi lielas porcijas, vai augsts kaloriju saturs edienos, Tev") 
  print("ir labs metabolisms.")  
  print("Tev ir jaievero rezimu un neest pa velu.")    
 if c==2:
  print("Tas nekas, ka Tev ir parmerigi lielas porcijas, vai augsts kaloriju saturs edienos, Tev") 
  print("ir labs metabolisms.")
 if c==3:
  print("Tev ir jaievero rezimu un neest pa velu.") 
 if c==4:
  print("Malacis, ka ievero rezimu!") 
 if d==1:
  print("Malacis, ka edi veseligu partiku!")   
 if d==2:
  print("Reti est neveseligu partiku ir normali.") 
 if d==3:
  print("Butu labi, ja Tu mazak estu neveseligus produktus, jo tas slikti ietekme uz tavu veselibu.") 

 
if x==2:
 if a==1:
  print("Tev ir janodarbojas ar spoirtu lai atbalstitu savu fizisko formu, un Tavs svars samazinajas.")
 if a==2:
  print("Tev nepetiek Tavas sportosanas un butu labi ja Tu nodarbotos ar sportu vairak, lai")
  print("atbalstitu savu fizisko formu, un Tavs svars samazinajas.")
 if a==3 or a==4 or a==5:
  print("Tu daudz nodarbojies ar sportu, malacis!")
 if b==1:
  print("Tev nav aktivs dzivesvesveids, ir vajadzigs vairak pastaigaties, ilgi nesedet uz vietas,")
  print("jo ta varesi zaudet svaru.") 
 if b==2:
  print("Ar dzives veida aktivitati Tev viss normali.")
 if c==1:
  print("Tev ir jasamazina porcijas un kaloriju saturu edienos.")     
  print("Tev ir jaievero rezimu un neest pa velu.")   
 if c==2:
  print("Tev ir jasamazina porcijas un kaloriju saturu edienos.") 
 if c==3:
  print("Tev ir jaievero rezimu un neest pa velu.") 
 if c==4:
  print("Malacis, ka ievero rezimu!") 
 if d==1:
  print("Malacis, ka edi veseligu partiku!")   
 if d==2:
  print("Reti est neveseligu partiku ir normali, bet ja velies zaudetu svaru, tos ir jaizsledz.") 
 if d==3:
  print("Tev vajag iznemt no uztura neveseligus produktus, jo tas slikti ietekme uz tavu veselibu") 
  print("un veicina uz lieka svara rasanu.")
 if e==1 or f==1:
  print("Tev ir jaapmekle arsu vai dietologu un parunajiet par so situaciju.")  
      