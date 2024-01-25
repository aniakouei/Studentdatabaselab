# create three lists:name, hometown, favorite food
#ask user to input choice to learn more about certain student or display names of all students
#prompt user for the number of the student
#validate number of user
#prompt user for category
#validate category
#allow user to type response in upper or lowercase
#Prompt user if they want to repeat
#use length of the list in the code to measure


def display_student_info():
    names = ["John", "Alice", "Bob", "Mary"]
    hometowns = ["Charlotte", "Seattle", "Chicago", "New York"]
    favorite_foods = ["Pizza", "Sushi", "Burger", "Pasta"]


    list_length = len(names)

    while True:
        try:

            print("\nOptions:")
            print("1. Display information about a specific student")
            print("2. Display a list of all students")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                student_number = int(input(f"Welcome! Which student would you like to learn more about? Enter a student number (1 to {list_length}): "))

                if student_number < 1 or student_number > list_length:
                    print("Invalid student number. Please try again.")

                index = student_number - 1

                print(f"\nStudent's Name: {names[index]}")

                category = input("Which category to display? (hometown/favorite food): ").lower()

                if category not in ["hometown", "favorite food"]:
                    print("Invalid category. Please enter 'hometown' or 'favorite Food'.")

                if category == "hometown":
                    print(f"{names[index]}'s hometown is {hometowns[index]}")
                else:
                    print(f"{names[index]}'s favorite food is {favorite_foods[index]}")

                another_student = input("Do you want to learn about another student? (yes/no): ").lower()
                if another_student != "yes":
                    print("Thank you! ")
                    break


            elif choice == "2":
                print("\nList of all students:")
                for i in range(list_length):
                    print(f"{i + 1}. {names[i]}")

            elif choice == "3":
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    display_student_info()