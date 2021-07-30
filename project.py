import sqlite3

connection=sqlite3.connect("my.db")


      
crsr=connection.cursor()

print("***********************WELCOME**************************")
# 

def Admin_page():
    global f
    f=0    
    while (f==0):
        print("PRESS 1  FOR LOGIN" )
        print("PRESS 2 FOR REGISTER" )


        choice1=int(input())
        if choice1==1:
            print("plz enter user id and password")
            userID=input()
            password=input()
            with open ("b.txt","r")as f:
                x1=f.readline().strip("\n")
                y1=f.readline().strip("\n")
                # print(x1,y1)
            if userID ==x1  and  password==y1:
                print("succesfully login")
                main()
                

                
            else:
                print("invalid")
                print()
                print("*****C FOR CONTINUE Q FOR EXIT*******")
                ch = input()
                if ch == "Q":
                    exit()
                else:
                    Admin_page()

               

        if choice1==2:
            print(" plz add userid")
            x=input()
            print("*******plz set password*****")
            y=input()
            with open ("b.txt","w")as f:
                f.write(x+"\n")
                f.write(y)
            print("***************succesfully REGISTER*****************")
            print()
            print("*****C FOR CONTINUE Q FOR EXIT*******")
            ch = input()
            if ch == "Q":
                exit()
            else:
                Admin_page()



def main():

        
    class patient():
            # count = 0

        def __init__(self, name, age, gender, id):
            self.name = name
            self.age = age
            self.gender = gender
            self.id = id

        # def show_details(self):
        #     print("patient details are ")
        #     print("patient name -", self.name)

        #     print("patient id-", self.id)
        #     print("patient age -", self.age)
        #     print("patient gender -", self.gender)

         
        def availability():
            print("/////////////////dr timing/////////////////////")
            print("    ")
            print("10;00am __ dr mathur")
            print("5;37 _ dr sethi")

        def add_patient() :
            print("plz fill this details ")
            print("enter name,age ,gender  ")
            name1 = input()

         
            age1 = int(input())
            gender1 = input()
                        
            q_insert=""" insert into patient (name,age ,gender)
                           values (? ,?, ?);"""

            if crsr.execute(q_insert,(name1,age1,gender1)):

                print("added succesfully")
                connection.commit()
            
            print("****************PATIENT  is added ********************")
            print() 
            print("----------------")
            print(" Q for exit""*************""  C for continue")



        def tota_availablebed():
            count = """  
              select count (age)
              from patient 
              where age > 0;"""

            if crsr.execute(count):

                x=crsr.fetchall()
                l=int(x[0][0])
                # print(l)
                print("Total no of available bed are {}".format(1000 -l ))
                print()
                print(" Q for exit""*************""  C for continue")
                
        def show_listbyid():
            print("plz give id " )
            id1=int(input())
            id_query="""  select * from patient where id = ? ;"""
            if crsr.execute(id_query,(id1,)):#   ###########variable id1 pass in form of tuple  for ? value in query (binding)
                for i in crsr.fetchall():
                    print(i)          


        # mohit = patient("mohit rana", 17, "male", 1)
        # shanu = patient("shanu singh", 19, "male", 2)
        # a = []
        # a.append(patient("mohit rana", 17, "male", 1))
        # a.append(patient("shanu singh", 19, "male", 2))
    p=1
    # print(type(mohit))
    while (1):
        if p==1:
            print("*************************WELCOME  to ABC HOSPITAL********************************")
            p=0
        print("____________________________________________________________")
        print("**************************PLZ SELECT OPTION *************************************")
        print()

        print("PRESS 1-for  all patient list ")
        print("PRESS 2-for doctor avalibilty")
        print("PRESS 3- patient complete details ")
        print("PRESS 4- for adding new patient  ")
        print("PRESS 5- Total No of BED AVAILABLE in hospital")

        choice = int(input())

        if (choice == 1):
            print("******LIST OF PATIENT**********")
            quer1 = """ 
                           select *  from patient  """
            if crsr.execute(quer1):
                # print(len(crsr.fetchall()))
                for i in crsr.fetchall():
                    print(i)
            #
            # connection.commit()
            # connection.close()
            print(" Q for exit""*************""  C for continue")
            choice2 = input()
            if (choice2 == "Q"):
                exit()
            else:
                continue

           
        if (choice == 2):
            patient.availability()
            print("Q for exit", "c for continue")
            choice2 = input()
            if (choice2 == "Q"):
                exit()
            else:
                continue

        if (choice == 3):
            patient.show_listbyid()
            print("Q for exit", "c for continue")      
            choice2 = input()
            if (choice2 == "Q"):
                exit()
            else:
                continue

        if (choice == 4):
            patient.add_patient()
            choice2 = input()
            if (choice2 == "Q"):
                exit()
            else:
                continue

        if (choice == 5):
            patient.tota_availablebed()
            choice2 = input()
            if (choice2 == "Q"):
                exit()
            else:
                continue

        else:
            print("********* plz select valid option*********")
            print()
            print(" Q for exit""*************""  C for continue")
            choice2 = input()
            if (choice2 == "Q"):
                exit()
            else:
                continue

    connection.commit()
# connection.close()


if __name__ == '__main__':
    Admin_page()
        
