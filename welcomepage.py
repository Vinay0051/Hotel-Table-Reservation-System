import tkinter as tk
from tkinter.font import Font
from tkinter import ttk

def open_booking_page():
    # Hide the main menu frame
    main_menu_frame.pack_forget()
    # Show the booking page frame
    booking_page_frame.pack(expand=True)

def book_reservation():
    # Code to handle booking reservation
    pass

def show_reservation():
    # Code to handle showing reservations
    pass

def staff_login():
    # Code to handle staff login
    pass

root = tk.Tk()
root.title("Hotel Reservation")

# Set the window size
window_width = root.winfo_screenwidth() // 2
window_height = root.winfo_screenheight() // 2
root.geometry(f"{window_width}x{window_height}")

# Create a custom font for the title
title_font = Font(family="Arial", size=window_height // 10, weight="bold")

# Create a frame to hold the main menu
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(side="top", fill="both", expand=True)

# Create the title label and place it in the main menu frame
title_label = tk.Label(main_menu_frame, text="HOTEL RESERVATION", font=title_font)
title_label.pack(pady=(window_height // 20, 0))

# Create a button to open the booking page
btn_book_reservation = tk.Button(main_menu_frame, text="Book Reservation", font=("Arial", 16), command=open_booking_page)
btn_book_reservation.pack(pady=(window_height // 20, 0))

# Create a frame to hold the booking page
booking_page_frame = tk.Frame(root)

# Create the icons representing dining tables
table_icons_frame = tk.Frame(booking_page_frame)
table_icons_frame.pack(side="left", fill="both", expand=True)

table_icons = []

for table_number in range(1, 11):
    table_icon = tk.Label(table_icons_frame, text=f"Table {table_number}", font=("Arial", 14), padx=10, pady=10)
    table_icon.pack()

    table_icons.append(table_icon)

# Create a frame to hold the dropdown menus
dropdown_frame = tk.Frame(booking_page_frame)
dropdown_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Create the dropdown menus
table_var = tk.StringVar()
date_var = tk.StringVar()
time_var = tk.StringVar()

table_label = tk.Label(dropdown_frame, text="Select Table", font=("Arial", 14))
table_label.pack(pady=(0, 10))

table_dropdown = ttk.Combobox(dropdown_frame, textvariable=table_var, font=("Arial", 12), state="readonly")
table_dropdown['values'] = ["Table 1", "Table 2", "Table 3", "Table 4", "Table 5",
                             "Table 6", "Table 7", "Table 8", "Table 9", "Table 10"]
table_dropdown.current(0)
table_dropdown.pack(pady=(0, 20))

date_label = tk.Label(dropdown_frame, text="Select Date", font=("Arial", 14))
date_label.pack(pady=(0, 10))

date_dropdown = ttk.Combobox(dropdown_frame, textvariable=date_var, font=("Arial", 12), state="readonly")
date_dropdown['values'] = ["2023-06-13", "2023-06-14", "2023-06-15", "2023-06-16"]
date_dropdown.current(0)
date_dropdown.pack(pady=(0, 20))

time_label = tk.Label(dropdown_frame, text="Select Time", font=("Arial", 14))
time_label.pack(pady=(0, 10))

time_dropdown = ttk.Combobox(dropdown_frame, textvariable=time_var, font=("Arial", 12), state="readonly")
time_dropdown['values'] = ["12:00 PM", "1:00 PM", "2:00 PM", "7:00 PM", "8:00 PM"]
time_dropdown.current(0)
time_dropdown.pack(pady=(0, 20))

# Create a button to book the reservation
btn_confirm_booking = tk.Button(dropdown_frame, text="Confirm Booking", font=("Arial", 16), command=book_reservation)
btn_confirm_booking.pack()

root.mainloop()
