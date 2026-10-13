class student:
    def __init__(self, name, grade,id):
        self.name = name
        self.grade = grade
        self.id = id

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}, ID: {self.id}")

if __name__ == "__main__":
    student1 = student("Alice", "A", 1)
    student2 = student("Bob", "B", 2)

    student1.display()
    student2.display()