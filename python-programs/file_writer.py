def main():
    filename = "my_notes.txt"
    content = "Hello! This is a text file created using Python.\n"
    content += "We used the 'w' mode to write this contffffffent."

    try:
        with open(filename, "w") as file:
            file.write(content)
            
        print(f"Success: Content written to '{filename}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
