file=input("Enter the file name : ")
ext=""
ans=""
for i in range(0,len(file)):
    if(file[i]=="."):
        ext=file[i+1:]

if(ext=="py"):
    ans="python"
elif(ext=="txt"):
    ans="text"
elif(ext=="doc" or ext=="docx"):
    ans="document"
elif(ext=="pdf"):
    ans="Portable document format"
else:
    print("Invalid File name ")
print("The extension of the file is :",ans)
    
        
