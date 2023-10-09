#programms to display the fibonacci sequence up to n-th term

nterms=int(input("how meny terms "))

#first two terms

n1=0
n2=1
count=0

#check if the number of terms is valid
if nterms <= 0 :
    print("please enter a positive number")

#if there is only one term, return n1

elif nterms ==1:
    print("fibanacci sequence upto",nterms,":")
    print(n1)
#generate fibonacci sequence

else:
    print("fibonacci sequence :")
    while count < nterms :
        print(n1)
        nth=n1+n2
        #update values
        n1=n2
        n2=nth
        count+=1

