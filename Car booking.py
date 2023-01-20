import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "rps@123", database = "kpmg")

mycursor = mydb.cursor()

class CarBooking:
   
    print("-----Car Booking System----- \n 1. Add Booking \n 2. Update Customer Information \n 3. Delete Customer ById \n 4. Search Customer Information  \n 5. Get All Customer Information ")
    option = int(input("Enter your option number : ")) 
    if option == 1:

        bookingId = int(input("Booking ID : ")) 
        ownerName = input("Owner Name : ")
        age = int(input("Age : "))
        gender = input("Gender : ")
        location = input("Location : ")
        entryTime = input ("Entry Time : ")
        contact = int(input("Contact : "))
        mycursor.execute(f"INSERT INTO  car_booking_info VALUES({bookingId},'{ownerName}',{age},'{gender}','{location}','{entryTime}',{contact})")
        mydb.commit()
        print("Booking Confirmed!")
    elif option == 2:
        
        bid = int(input("Enter Booking Id for updating data : "))
        bLocation = int(input("Enter updated location : "))
        mycursor.execute(f"UPDATE car_booking_info set location = {bLocation}  where bookingId = {bid}" )
        mydb.commit()

    elif option ==3:
       
        bid = int(input("Enter Booking Id for deleting data : "))
        mycursor.execute(f"DELETE FROM car_booking_info where bookingId = {bid}" )
        mydb.commit()
        print("Data deleted successfully!")

    elif option == 4:
       
        bid = int(input("Enter booking Id to search : "))
        mycursor.execute(f"SELECT * FROM  car_booking_info where bookingId = {bid}" )
        myresult = mycursor.fetchall()
        myData = pd.DataFrame(myresult)
        print(myData)
       
    elif option == 5:
          
        mycursor.execute("select count(*) from car_booking_info") 
        dataFetched = mycursor.fetchall()  
        for count in dataFetched:
            print("Total bookings till now : ",count)
        mycursor.execute("select * from car_booking_info")
        carBookings = mycursor.fetchall()
        dataFrame = pd.DataFrame(carBookings)
        print(dataFrame)
    else:
        print("Incorrect option entered!")
