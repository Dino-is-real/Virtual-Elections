def cast_vote():
    import mysql.connector as mc
    name = input("Enter your name: ")
    d = int(input("Enter your birth date: "))
    m = int(input("Enter your birth month: "))
    y = int(input("Enter your birth year: "))

    from datetime import date

    def calculate_age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    age = calculate_age(date(y, m, d))
    print("Your age:", age)
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote!")
        quit()
    aad = input("Enter your aadhaar card no.:")
    db = mc.connect(host='localhost', user='root', password='Pirana@2022', database='elections')
    cur = db.cursor()
    sql = "Select * from votes where Aadhaar_ID = (%s)"
    val1 = (aad,)
    cur.execute(sql, val1)
    res = cur.fetchall()
    if len(res) == 1:
        print("You have already voted")
        quit()
    else:
        pass

    cur.close()
    db.close()

    db2 = mc.connect(host='localhost', user='root', password='Pirana@2022', database='elections')
    my_cursor = db2.cursor()
    sql1 = 'select * from voter_list where Aadhaar_ID = (%s)'
    val = (aad,)
    my_cursor.execute(sql1, val)
    result = my_cursor.fetchall()
    if len(result) == 1:
        pass
    else:
        quit()

    mail = str(result[0][4])

    import random
    import smtplib
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("otp2vote@gmail.com", "gbvk yega jzzk zccg")
    otp1 = random.randint(100000, 1000000)
    otp = "You OTP is " + str(otp1) + "\n DO NOT SHARE IT WITH ANYONE"
    s.sendmail("otp2vote@gmail.com", mail, otp)
    print("OTP sent successfully..")
    print(otp1)
    otp_input = int(input("Please enter the OTP: "))
    if otp_input == otp1:
        print("Access Granted")

    else:
        print("Access Denied...")
        quit()
    import tkinter
    def click1():
        print("You voted for Party A!")
        db = mc.connect(host='localhost', user='root', password='Pirana@2022', db='elections')
        mycursor = db.cursor()
        sql = "INSERT into votes(Name, Aadhaar_ID, vote) values(%s, %s, %s)"
        val = (name, aad, "A")
        mycursor.execute(sql, val)
        db.commit()
        quit()


    def click2():
        print("You voted for Party B!")
        db = mc.connect(host='localhost', user='root', password='Pirana@2022', db='elections')
        mycursor = db.cursor()
        sql = "INSERT into votes(Name, Aadhaar_ID, vote) values(%s, %s, %s)"
        val = (name, aad, "B")

        mycursor.execute(sql, val)
        db.commit()
        quit()


    window = tkinter.Tk()
    buttonA = tkinter.Button(window, text = "A")
    buttonA.config(command=click1)
    image1 = tkinter.PhotoImage(file='C:/Pranav/CS_PROJECT/Aparty.png')
    buttonA.config(image=image1)
    buttonA.pack()
    buttonB = tkinter.Button(window, text = "B")
    buttonB.config(command=click2)
    image2 = tkinter.PhotoImage(file='C:/Pranav/CS_PROJECT/Bparty.png')
    buttonB.config(image=image2)
    buttonB.pack()
    window.mainloop()

def cand_info():
    print("Welcome to candidate information!\nPlease choose the category of election from the following:-")
    print("1. Regional/District elections:\n2. State elections(LA):\n3. Union/centre elections(PA):")
    ch = int(input("Enter your choice[1/2/3]: "))
    import mysql.connector as mc
    db = mc.connect(host='localhost', user='root', password='Pirana@2022', database='elections')
    mycursor = db.cursor()
    if ch == 1:
        reg = input("Enter region/district: ")
        el = "District"
        sql = 'SELECT * from cand_list WHERE election = (%s) and location = (%s)'
        val = (el, reg)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        for x in result:
            print(x)
    elif ch == 2:
        st = input("Enter your state: ")
        el = "State"
        sql = 'SELECT * from cand_list WHERE election = (%s) and location = (%s)'
        val = (el, st)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        for x in result:
            print(x)
    elif ch == 3:
        cn = 'India'
        el = "Union"
        sql = 'SELECT * from cand_list WHERE election = (%s) and location = (%s)'
        val = (el, cn)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        for x in result:
            print(x)
    else:
        print("Invalid input!")
        quit()


def faq():
    print("Welcome to the FAQ session!")
    print("Here are some of the FAQs:-")
    print("1. Is this app safe?")
    print("2. What is the use of the app ? ")
    print("3. What type of elections can be conducted ?")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("The app will have a three layer security,\n1. Basic detail verification\n2. OTP verification\n3. Photo ID verifictaion")
        print("With proper infrastructure it can be made into a fool-proof software")
        print("For any other queries. You can personally contact us at ridgecraig@gmail.com")
    elif ch == 2:
        print("The app is/can be used to conduct elections of any kind.")
        print("Especially after the pandemic, we have to have an online alternative for such elections. ")
        print("For any other queries. You can personally contact us at ridgecraig@gmail.com")
    elif ch == 3:
        print("At the current stage of security, the software can conduct basic level election.")
        print("However, with upcoming updates, We can implement it at national level ")
        print("For any other queries. You can personally contact us at ridgecraig@gmail.com")
    else:
        print("For any other queries. You can personally contact us at ridgecraig@gmail.com")


#Finding Result
def result():
    #fetching data from votes table from mySQL
    cnt_a = 0
    cnt_b = 0
    import mysql.connector as mc
    db = mc.connect(host='localhost', user='root', password='Pirana@2022', database='elections')
    mycursor = db.cursor()
    sql = 'SELECT Vote, Count(Vote) from votes group by Vote '
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        if i[0] == "A":
            cnt_a = int(i[1])
        elif i[0] == "B":
            cnt_b = int(i[1])
    if cnt_b > cnt_a:
        print(f"Party BUll won by {cnt_b-cnt_a} votes")
    elif cnt_a > cnt_b:
        print(f"Party ANT wont by {cnt_a-cnt_b} votes")
    else:
        print("The results have tied. The winner will be announced later.")



    #plotting result on bargraph
    from matplotlib import pyplot as plt
    result_lst = [cnt_a, cnt_b]
    x_values = ["A","B"]
    plt.bar(x_values, result_lst, color=['Black', 'Red'])
    plt.show()

def voter_reg():
    print("Welcome for voter registration!")
    first_name = str(input("Enter your first name: "))
    sur_name = str(input("Enter your surname: "))
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote!")
    elif age < 18:
        print("You are not eligible to vote! ")
    else:
        print("Invalid input!")
    age = str(age)
    Aad_no = input("Enter your 12-digit Aadhaar number: ")
    phono = input("Enter your Phone number: ")
    email_id = input("Enter your gmail: ")

    import mysql.connector as mc
    db = mc.connect(host='localhost', user='root', password='Pirana@2022', db='elections')
    mycursor = db.cursor()
    sql = "insert into voter_list values('"+first_name+"','"+sur_name+"','"+phono+"','"+age+"','"+email_id+"','"+Aad_no+"')"
    mycursor.execute(sql)
    db.commit()
    print("Your Credentials have been successfully added! ")







