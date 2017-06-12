def writing():
    with open("data.txt","w") as f:
        line1=input("Give me first line :- ")
        line2 = input("Give me second line :- ")
        line3 = input("Give me second line :- ")
        f.write(" %s \n %s \n %s \n" % (line1, line2, line3))
        f.close()


def reading():
    with open("data.txt","r") as f:
        print(f.read())
        f.close()

writing()
reading()