root = ["", "home", "root"]
dirs = []
path = []
curr_path = [] or ["", "home", "root"]


# To create directory
def mkdir():
    global dirs
    if dir in dirs:
        print("Directory already exist.")
    else:
        dirs.append(dir)
        path.append(dir)


# shows directory
def ls():
    global path
    if path == root:
        path = dirs
        path = path[0]
    print(*path, sep="\n")


# change directory
def cd():
    global curr_path, dir, path
    if dir == "":
        curr_path = root
        path = root
    elif dir in dirs:
        curr_path.append(dir)
        path.clear()
    elif dir == "..":
        curr_path.pop()
        print(*curr_path, sep="/")
        i = len(dirs) - 1
        if dirs[i] in path:
            i = i - 1
            path.pop()
            path.append(dirs[i])
        else:
            path.append(dirs[i])
    else:
        print("Directory doesn't exist.")


# show current directory
def pwd():
    global curr_path
    print(*curr_path, sep="/")


# remove directory
def rm():
    global dirs
    if dir in dirs:
        dirs.remove(dir)
        if dir in path:
            path.remove(dir)
    else:
        print("Directory does not exist.")


# clean session data like it is executed just now
def session_clear():
    global dirs
    dirs.clear()
    global curr_path
    curr_path.clear()
    curr_path = root
    global path
    path.clear()


def commands(argument):
    comm = {
        "mkdir": mkdir,
        "ls": ls,
        "cd": cd,
        "pwd": pwd,
        "rm": rm,
        "session_clear": session_clear,
        "exit": exit,
    }
    if n in comm:
        # Get the function from comm dictionary
        func = comm.get(argument)
        # Execute the function
        func()
    else:
        print("command does not exist!")


print("There are total 7 commands: mkdir, ls, cd, pwd, rm, session_clear, exit.")

while True:
    n = input("$: ")
    a = []
    a.append(n.split(" "))
    n = a[0][0]
    if n in ["mkdir", "rm"] and len(a[0]) == 1:
        print("{}:missing operand".format(n))
    elif len(a[0]) == 1:
        dir = ""
    elif len(a[0]) == 2:
        dir = a[0][1]
    else:
        print("Invalid Syntax")
    commands(n)
