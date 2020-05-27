file = open("accuracy.html", "r")
acc_lines = file. readlines()

def Convert(string): 
    li = list(string.split(" ")) 
    return li

#function for string into list
newer=acc_lines[1]
str1 = newer
newer=Convert(str1)[2]
newer=float(newer)

older=acc_lines[0]
str1 = older
older=Convert(str1)[2]
older=float(older)

if newer<0.80:
    pyfile = open("flower_recog.py", "r")
    py_lines = file. readlines()

    def Convert(string): 
        li = list(string.split(" ")) 
        return li

    if acc_lines[2]=="dense":
        #function for string into list
        newer=acc_lines[1]
        str1 = newer
        newer=Convert(str1)[2]
        newer=float(newer)

        older=acc_lines[0]
        str1 = older
        older=Convert(str1)[2]
        older=float(older)

        #for dense layer
        if newer>=older:
            x=py_lines[112]
            str1 = x
            y=Convert(str1)[2]

            #To convert str datatype into int datatype
            y=int(y)
            y=y+1
            py_lines[112] = "d = {} \n".format(y)
            pyfile = open("flower_recog.py", "w")
            pyfile. writelines(py_lines)
            pyfile. close()

        else:
            acc_lines[2]="convo"
            file = open("accuracy.html", "w")
            file. writelines(acc_lines)
            
            x=py_lines[112]
            str1 = x
            y=Convert(str1)[2]

            #To convert str datatype into int datatype
            y=int(y)
            y=y-1
            py_lines[112] = "d = {} \n".format(y)
            pyfile = open("flower_recog.py", "w")
            pyfile. writelines(py_lines)
            pyfile. close()
            
file.close()
