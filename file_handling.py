emp_list = ["Aman", "Shivam", "Shubham"]

for emp in emp_list:
    with open(f"{emp}.txt", "w") as file:
        pass

print("Files created successfully!")