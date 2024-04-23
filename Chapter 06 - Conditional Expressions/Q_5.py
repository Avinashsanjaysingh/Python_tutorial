# Write a program which finds out whether a given name is present in a list or not.


l = ["Aarav Patel","Ananya Sharma","Arjun Singh","Aishwarya Reddy","Aditya Kumar","Bhavya Gupta","Deepak Verma","Divya Mishra","Gaurav Joshi","Geetika Kapoor","Harshita Singh","Ishaan Sharma","Jaya Khanna","Kabir Kapoor","Kriti Chauhan","Lakshya Verma","Megha Agarwal","Naman Gupta","Neha Sharma","Omkar Patel","Pooja Mishra","Pranav Verma","Qureshi Ali","Rahul Singh","Riya Kapoor","Rohan Sharma","Sanya Singh","Shubham Patel","Sneha Reddy","Tanvi Verma","Ujjwal Chauhan","Vidya Kumar","Varun Agarwal","Yash Joshi","Zoya Khan","Sandeep Maddheshiya","Avinash Singh","Arif Ali","Kunal Singh"]

l = [word.lower() for word in l]

a = input("\nEnter your name: ")
b = []
b.append(a)
b = [word.lower() for word in a]

if b in l:
    print("\nYour name is in the list.")
else:
    print("\nYour name is not in the list.")




