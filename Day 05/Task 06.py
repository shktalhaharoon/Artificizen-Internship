def check_file(file_name):
    print("Reading File:", file_name)
    try:
        file = open(file_name, "r")
        data = file.read()
        file.close()
        number = int(data)
        answer = 50 / number
        print("Result:", answer)

    

    except ValueError:
        print("Error: File should contain a valid number.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except Exception as error:
        print("Unexpected Error:", error)


    except FileNotFoundError:
        print("Error: File not found.")


check_file("data.txt")