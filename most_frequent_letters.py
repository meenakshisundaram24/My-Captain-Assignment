def most_frequent(word ):
    unique=set(word)
    most={}
    most_values=[]
    sorted_most={}
    
    for i in unique:            #creating a dictionary with letters and their frequency 
        count=0
        for j in word:
            if(i==j):
                count+=1
        most[i]=count
        most_values.append(count)     
        
    most_values=sorted(most_values,reverse=True)

    
    for i in most_values:        # sorting the dictionary in decreasing order of frequencies 
        for k in most:
            if(i==most[k]):
                sorted_most[k]=i
    return sorted_most

string=input("Enter a string : ")
string=string.lower()
most_dict=most_frequent(string)
for i in most_dict:
    print(i," = ",most_dict[i])
