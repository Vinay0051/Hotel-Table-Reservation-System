import csv

def write_to_csv(data):
    with open('customer_bookings.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def read_csv():
    with open('customer_bookings.csv', 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def verify_booking(date, time,table_no):
    bookings = read_csv()
    for row in bookings:
        if row[2] == table_no :
            if row[3] == date and row[4] == time:
                return False
    return True

def main():
    print("Welcome to the Customer Booking System")
    print("-------------------------------------")
    table_no = input("Enter table number: ")
    date = input("Enter the booking date: ")
    time = input("Enter the booking time: ")

    verify = verify_booking(date,time,table_no)

    if verify:
        name = input("Enter your name: ")
        number = input("Enter your phone number: ")
        data = [name, number, table_no, date, time]
        write_to_csv(data)
        print("Booking successfully saved.")
    else:
        print("Slot not available")

if __name__ == '__main__':
    main()
