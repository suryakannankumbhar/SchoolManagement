import mysql.connector

def selection():
    db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
    cursor = db.cursor()
    
    while True:
        head = "SCHOOL DATA MANAGEMENT SYSTEM"
        print(head.center(60))
        print()
        menu = "MAIN MENU"
        print(menu.center(60))
        print()
        print("1. STUDENT MANAGEMENT")
        print("2. EMPLOYEE MANAGEMENT")
        print("3. FEE MANAGEMENT")
        print("4. EXAM MANAGEMENT")
        print("5. EXIT")
        ch = int(input("\nEnter Your Choice (1-5): "))
        
        if ch == 1:
            print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
            print('a. NEW ADMISSION')
            print('b. UPDATE STUDENT DETAILS')
            print('c. ISSUE TC')
            print('d. VIEW STUDENT DETAILS')
            c = input("Enter Your Choice (a-d): ")
            print('\nInitially the details are:\n')
            display1()
            if c == 'a':
                insert1()
                print('\nModified details are:\n')
                display1()
            elif c == 'b':
                update1()
                print('\nModified details are:\n')
                display1()
            elif c == 'c':
                delete1()
                print('\nModified details are:\n')
                display1()
            elif c == 'd':
                print('\nStudent Details:\n')
                display1()
            else:
                print('Enter correct choice...!!')
        
        elif ch == 2:
            print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
            print('a. NEW EMPLOYEE')
            print('b. UPDATE STAFF DETAILS')
            print('c. DELETE EMPLOYEE')
            print('d. VIEW EMPLOYEE DETAILS')
            c = input("Enter Your Choice (a-d): ")
            if c == 'a':
                insert2()
                print('\nModified details are:\n')
                display2()
            elif c == 'b':
                update2()
                print('\nModified details are:\n')
                display2()
            elif c == 'c':
                delete2()
                print('\nModified details are:\n')
                display2()
            elif c == 'd':
                print('\nEmployee Details:\n')
                display2()
            else:
                print('Enter correct choice...!!')
        
        elif ch == 3:
            print('WELCOME TO FEE MANAGEMENT SYSTEM')
            print('a. NEW FEE')
            print('b. UPDATE FEE')
            print('c. EXEMPT FEE')
            print('d. VIEW FEE DETAILS')
            c = input("Enter Your Choice (a-d): ")
            if c == 'a':
                insert3()
            elif c == 'b':
                update3()
            elif c == 'c':
                delete3()
            elif c == 'd':
                print('\nFee Details:\n')
                display3()
            else:
                print('Enter correct choice...!!')
        
        elif ch == 4:
            print('WELCOME TO EXAM MANAGEMENT SYSTEM')
            print('a. EXAM DETAILS')
            print('b. UPDATE DETAILS')
            print('c. DELETE DETAILS')
            print('d. VIEW EXAM DETAILS')
            c = input("Enter Your Choice (a-d): ")
            if c == 'a':
                insert4()
            elif c == 'b':
                update4()
            elif c == 'c':
                delete4()
            elif c == 'd':
                print('\nExam Details:\n')
                display4()
            else:
                print('Enter correct choice...!!')
        
        elif ch == 5:
            print('Exiting the program. Goodbye!')
            break
        
        else:
            print('Enter correct choice..!!')

def insert1():
    admno = int(input("Enter Admission No : "))
    sname = input("Enter Student Name : ")
    dob = input("Enter Date of Birth (yyyy-mm-dd): ")
    cls = input("Enter class for admission: ")
    cty = input("Enter City: ")
    
    db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
    cursor = db.cursor()

    sql = "INSERT INTO student(Adm_No, St_Name, DOB, Class, City) VALUES (%s, %s, %s, %s, %s)"
    values = (admno, sname, dob, cls, cty)
    
    try:
        cursor.execute(sql, values)
        db.commit()
        print("Student record inserted successfully.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def display1():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()

        if not results:
            print("No student records found.")
        else:
            for c in results:
                admno = c[0]
                sname = c[1]
                dob = c[2]
                cls = c[3]
                cty = c[4]
                print(f"(Adm_No={admno}, St_Name={sname}, DOB={dob}, Class={cls}, City={cty})")
    except Exception as e:
        print("Error: unable to fetch data")
        print(e)

    db.close()

def update1():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno = c[0]
            sname = c[1]
            dob = c[2]
            cls = c[3]
            cty = c[4]
    except:
        print("Error: unable to fetch data")
    print()
    tempst = int(input("Enter Admission No: "))
    temp = input("Enter new class: ")
    try:
        sql = "UPDATE student SET Class=%s WHERE Adm_No=%s"
        cursor.execute(sql, (temp, tempst))
        db.commit()
        print("Student class updated successfully.")
    except Exception as e:
        print("Error:", e)
    db.close()

def delete1():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno = c[0]
            sname = c[1]
            dob = c[2]
            cls = c[3]
            cty = c[4]
    except:
        print("Error: unable to fetch data")
    temp = int(input("\nEnter adm no to be deleted: "))
    try:
        sql = "DELETE FROM student WHERE Adm_No=%s"
        cursor.execute(sql, (temp,))
        ans = input("Are you sure you want to delete the record (y/n): ")
        if ans.lower() == 'y':
            db.commit()
            print("Student record deleted successfully.")
        else:
            db.rollback()
            print("Deletion canceled.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def insert2():
    empno = int(input("Enter Employee No: "))
    ename = input("Enter Employee Name: ")
    job = input("Enter Designation: ")
    hiredate = input("Enter date of joining: ")
    
    db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
    cursor = db.cursor()
    
    sql = "INSERT INTO Employee(Emp_ID, Emp_Name, job, hiredate) VALUES (%s, %s, %s, %s)"
    values = (empno, ename, job, hiredate)
    
    try:
        cursor.execute(sql, values)
        db.commit()
        print("Employee record inserted successfully.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def display2():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM Employee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            empno = c[0]
            ename = c[1]
            job = c[2]
            hiredate = c[3]
            print(f"(Emp_ID={empno}, Emp_Name={ename}, Job={job}, Joining_date={hiredate})")
    except:
        print("Error: unable to fetch data")
        db.close()

def update2():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM Employee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            empno = c[0]
            ename = c[1]
            job = c[2]
            hiredate = c[3]
    except:
        print("Error: unable to fetch data")
        print()

    tempst = int(input("Enter Employee No: "))
    temp = input("Enter new designation: ")

    try:
        sql = "UPDATE Employee SET Job=%s WHERE Emp_ID=%s"
        cursor.execute(sql, (temp, tempst))
        db.commit()
        print("Employee designation updated successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()

def delete2():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM Employee"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            empno = c[0]
            ename = c[1]
            job = c[2]
            hiredate = c[3]
    except:
        print("Error: unable to fetch data")
    temp = int(input("\nEnter Employee ID to be deleted: "))
    try:
        sql = "DELETE FROM Employee WHERE Emp_ID=%s"
        cursor.execute(sql, (temp,))
        ans = input("Are you sure you want to delete the record (y/n): ")
        if ans.lower() == 'y':
            db.commit()
            print("Employee record deleted successfully.")
        else:
            db.rollback()
            print("Deletion canceled.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def insert3():
    admno = int(input("Enter Admission No: "))
    fee = float(input("Enter Fee Amount: "))
    month = input("Enter Month: ")

    db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
    cursor = db.cursor()

    sql = "INSERT INTO Fee(Adm_No, Fee, Month) VALUES (%s, %s, %s)"
    values = (admno, fee, month)

    try:
        cursor.execute(sql, values)
        db.commit()
        print("Fee details inserted successfully.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def display3():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM Fee"
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            print("No fee details found.")
        else:
            print("Fee Details:")
            for c in results:
                admno = c[0]
                fee = c[1]
                month = c[2]
                print(f"(Adm_No={admno}, Fee={fee}, Month={month})")
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()

def update3():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()

        sql = "SELECT * FROM Fee"
        cursor.execute(sql)
        results = cursor.fetchall()

        for c in results:
            admno = c[0]
            fee = c[1]
            month = c[2]

        tempst = int(input("Enter Admission No: "))
        temp = input("Enter new fee amount: ")

        sql_update = "UPDATE Fee SET Fee=%s WHERE Adm_No=%s"
        cursor.execute(sql_update, (temp, tempst))
        db.commit()
        print("Fee amount updated successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()

def delete3():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()

        sql = "SELECT * FROM Fee"
        cursor.execute(sql)
        results = cursor.fetchall()

        for c in results:
            admno = c[0]
            fee = c[1]
            month = c[2]

    except Exception as e:
        print("Error: unable to fetch data")

    temp = int(input("\nEnter admission no to be deleted: "))

    try:
        sql = "DELETE FROM Fee WHERE Adm_No=%s"
        cursor.execute(sql, (temp,))
        ans = input("Are you sure you want to delete the record (y/n): ")
        if ans.lower() == 'y':
            db.commit()
            print("Record deleted successfully.")
        else:
            db.rollback()
            print("Deletion canceled.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def insert4():
    sname = input("Enter Student Name: ")
    admno = int(input("Enter Admission No: "))
    per = float(input("Enter percentage: "))
    res = input("Enter result: ")
    
    db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
    cursor = db.cursor()
    sql = "INSERT INTO Exam(Adm_No, St_Name, Percentage, Result) VALUES (%s, %s, %s, %s)"
    values = (admno, sname, per, res)
    
    try:
        cursor.execute(sql, values)
        db.commit()
        print("Record inserted successfully.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

def display4():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM Exam"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno = c[0]
            sname = c[1]
            per = c[2]
            res = c[3]
            print(f"(St_Name={sname}, Adm_No={admno}, Percentage={per}, Result={res})")
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()

def update4():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM Exam"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno = c[0]
            sname = c[1]
            per = c[2]
            res = c[3]
    except:
        print("Error: unable to fetch data")
        print()

    tempst = int(input("Enter Admission No: "))
    temp = input("Enter new result: ")

    try:
        sql = "UPDATE Exam SET Result=%s WHERE Adm_No=%s"
        cursor.execute(sql, (temp, tempst))
        db.commit()
        print("Result updated successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()

def delete4():
    try:
        db = mysql.connector.connect(user='root', password='surya', host='localhost', database='csproject')
        cursor = db.cursor()
        sql = "SELECT * FROM Exam"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            admno = c[0]
            sname = c[1]
            per = c[2]
            res = c[3]
    except:
        print("Error: unable to fetch data")

    temp = int(input("\nEnter Admission No to be deleted: "))
    try:
        sql = "DELETE FROM Exam WHERE Adm_No=%s"
        cursor.execute(sql, (temp,))
        ans = input("Are you sure you want to delete the record (y/n): ")
        if ans.lower() == 'y':
            db.commit()
            print("Record deleted successfully.")
        else:
            db.rollback()
            print("Deletion canceled.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

selection()
