#args and kwargs complex code
def student_report(name, *marks, **details):

    print(f"Student: {name}")

    total = sum(marks)
    average = total / len(marks)

    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

    print("\nAdditional details:")

    for key, value in details.items():
        print(f"{key}: {value}")


student_report(
    "Dwitiya",
    85, 92, 78, 88, 95,
    age=20,
    branch="CSE",
    college="BVP",
    year=2
)