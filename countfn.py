def r():
    i=input("Enter file name-> ")
    n=0
    o= open(i,"r")
    for i in o:
        words=i.split(" ")
        n=n+len(words)
    print("Number of word=",n)
r()
