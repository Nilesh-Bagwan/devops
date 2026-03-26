def main():
    try:
        # 1. Take score as input and convert to an integer
        score_input = input("Enter your score (0-100): ")
        score = int(score_input)

        # 2. Grade logic using if-elif-else
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        # 3. Print the result
        print(f"Score: {score} | Grade: {grade}")

    except ValueError:
        print("Invalid input! Please enter a whole number.")
    
if __name__ == "__main__":
    main()