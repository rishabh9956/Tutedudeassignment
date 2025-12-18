student_marks = {
    "Aarav Sharma": 85,
    "Ananya Verma": 92,
    "Rohan Gupta": 78,
    "Priya Singh": 88,
    "Aditya Mishra": 90,
    "Neha Patel": 81,
    "Rahul Khanna": 75,
    "Kavya Iyer": 89,
    "Aman Tiwari": 67,
    "Pooja Malhotra": 84,
    "Sarthak Jain": 91,
    "Riya Choudhary": 86,
    "Mohit Aggarwal": 73,
    "Sneha Kulkarni": 95,
    "Kunal Mehta": 79
}
user_input = input("Enter Student Name: ").strip()
if user_input in student_marks :
          print(f"Marks of {user_input}: {student_marks[user_input]}")
    
else:
        print(user_input +" Not Found in Directory")
    
