print("WELCOME TO OPERATING SYSTEM")
print("V 0.1")
print("")
def commandLoop(additionaltext):
    print(additionaltext)
    global cmd == input("Enter Command: ")

commandLoop()
if cmd == "Save test":
    with open ("Save.txt", "a") as file:
        file.write("Save Test\n")
        file.close()
        pass
    commandLoop("Modified Save file")
else:
    commandLoop("No command found")
