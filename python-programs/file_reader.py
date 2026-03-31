def main():
    filename = "my_notes.txt"

    try:
        with open(filename, "r") as file:
            content = file.read()

            print("--- File Content ---")
            print(content)
            print("--------------------")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
