import smtplib, ssl

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

if newer>=0.80:
    import smtplib, ssl

    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "divyanshjangir141@gmail.com"
    receiver_email = "divyanshjangir141@gmail.com"
    password = "your password"
    message = " Your desired accuracy is reached"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
file.close()
