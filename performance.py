# Student class
class Student:
    def __init__(self, name, scores):
        #Constructor
        #Initialize a student with a name and their scores.
     
        self.name = name
        self.scores = scores

    def calculate_average(self):
       
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
      
        return all(score >= passing_score for score in self.scores)


# PerformanceTracker class
class PerformanceTracker:
    def __init__(self):
        """
        Initialize the tracker with an empty dictionary to store students.
        """
        self.students = {}

    def add_student(self, name, scores):
      
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
       
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        """
        Display each student's performance and class average.
        """
        if not self.students:
            print("No student data available.")
            return

        print("\nStudent Performance:")
        for student in self.students.values():
            avg_score = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"Name: {student.name}, Average Score: {avg_score:.2f}, Status: {status}")

        class_average = self.calculate_class_average()
        print(f"\nClass Average Score: {class_average:.2f}")


# Main Program
def main():
    tracker = PerformanceTracker()

    while True:
        try:
            # Input student details
            name = input("\nEnter student name (or type 'done' to finish): ").strip()
            if name.lower() == 'done':
                break

            scores = []
            for subject in ['Math', 'Science', 'English']:
                score = int(input(f"Enter {name}'s score for {subject}: "))
                scores.append(score)

            tracker.add_student(name, scores)
        except ValueError:
            print("Invalid input. Please enter numeric scores.")

    # Display student performance
    tracker.display_student_performance()


if __name__ == "__main__":
    main()
