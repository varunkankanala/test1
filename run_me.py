while True:
    read = input("Enter something: ")
    f = open("/app/dump", "a")
    f.write(read)
    f.close()
    print(read)