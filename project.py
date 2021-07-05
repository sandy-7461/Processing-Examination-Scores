import re
import math
name=input("Enter the file name from which you want to read the data:")
ip_file=open(name) #opening the input file
line=ip_file.readlines()
marks=[]
A,B,C,D,F=0,0,0,0,0
for i in line :
    mark=re.split(' |\n',i)
    for j in mark :
        if(j!='' and int(j)<101 and int(j)>-1 ) :
            temp=int(j)
            marks.append(temp)
            if(temp>=90):
                A+=1
            elif(temp>=80):
                B+=1
            elif(temp>=70):
                C+=1
            elif(temp>=60):
                D+=1
            else:
                F+=1
count=[len(str(A)),len(str(B)),len(str(C)),len(str(D)),len(str(F))]
min_space=3*max(count)+min(count)
n=len(marks)
avg=sum(marks)/n
print("\n     Exam Stats\n")
print("Number of scores: ",n)
print("Average score: %.2f"%avg)
psd=0

#calculating Population Standard deviation for the given marks

for i in marks :
    psd=psd+math.pow((i-avg),2)
psd=psd/n
psd=math.sqrt(psd)
print("Population standard deviation: %.2f"%psd)
print("\nA count: ",A,end="")
for i in range(min_space-len(str(A))) :
    print(" ",end="")
print("%.2f%%"%(A*100/n))
print("B count: ",B,end="")
for i in range(min_space-len(str(B))) :
    print(" ",end="")
print("%.2f%%"%(B*100/n))
print("C count: ",C,end="")
for i in range(min_space-len(str(C))) :
    print(" ",end="")
print("%.2f%%"%(C*100/n))
print("D count: ",D,end="")
for i in range(min_space-len(str(D))) :
    print(" ",end="")
print("%.2f%%"%(D*100/n))
print("F count: ",F,end="")
for i in range(min_space-len(str(F))) :
    print(" ",end="")
print("%.2f%%"%(F*100/n))
print("\nMinimum score: ",min(marks))
print("Maximum score: ",max(marks))
ip_file.close() #closing the input file

#program for storing the above data in a file

name=input("\nEnter the name of the file in which you want to store the following data:")
op_file=open(name,'w')
op_file.write("     Exam Stats\n\n")
op_file.write("Number of scores: %d\n"%n)
op_file.write("Average score: %.2f\n"%avg)
op_file.write("Population standard deviation: %.2f\n"%psd)
op_file.write("\nA count: %d"%A)
for i in range(min_space-len(str(A))) :
    op_file.write(" ")
op_file.write("%.2f%%\n"%(A*100/n))
op_file.write("B count: %d"%B)
for i in range(min_space-len(str(B))) :
    op_file.write(" ")
op_file.write("%.2f%%\n"%(B*100/n))
op_file.write("C count: %d"%C)
for i in range(min_space-len(str(C))) :
    op_file.write(" ")
op_file.write("%.2f%%\n"%(C*100/n))
op_file.write("D count: %d"%D)
for i in range(min_space-len(str(D))) :
    op_file.write(" ")
op_file.write("%.2f%%\n"%(D*100/n))
op_file.write("F count: %d"%F)
for i in range(min_space-len(str(F))) :
    op_file.write(" ")
op_file.write("%.2f%%"%(F*100/n))
op_file.write("\n\nMinimum score: %d\n"%min(marks))
op_file.write("Maximum score: %d"%max(marks))
op_file.close() #closing the output file
print("The above data is sucessfully stored in ",name," file")








