print("WELCOME TO OPERATING SYSTEM")
print("V 0.1")
cmd = None
def cmdl(at):
    print(at)
    cmd = input("Enter Command: ")

if cmd == "Save test":
    with open("Save.txt", "a") as file:
        file.write("Save Test\n")
        file.close()
    cmdl("Saved")
elif cmd == None:
    print("")
    cmdl("")
else:
    cmdl("Failed")
