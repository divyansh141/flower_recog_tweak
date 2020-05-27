file = open("accuracy.txt", "r")
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

    if acc_lines[2]=="convo":
        #for convolution layer
        if newer>=older:
            x=py_lines[111]
            str1 = x
            y=Convert(str1)[2]

            #To convert str datatype into int datatype
            y=int(y)
            y=y+1
            py_lines[111] = "c = {} \n".format(y)
            pyfile = open("flower_recog.py", "w")
            pyfile. writelines(py_lines)
            pyfile. close()

        else:
            acc_lines[2]="dense"
            file = open("accuracy.txt", "w")
            file. writelines(acc_lines)
            
            x=py_lines[111]
            str1 = x
            y=Convert(str1)[2]

            #To convert str datatype into int datatype
            y=int(y)
            y=y-1
            py_lines[111] = "c = {} \n".format(y)
            pyfile = open("flower_recog.py", "w")
            pyfile. writelines(py_lines)

            #for dense
            z=py_lines[112]
            str1 = z
            z1=Convert(str1)[2]

            #To convert str datatype into int datatype
            z1=int(z1)
            z1=z1+1
            py_lines[112] = "d = {} \n".format(z1)
            pyfile = open("flower_recog.py", "w")
            pyfile. writelines(py_lines)
            pyfile. close()

file.close()
