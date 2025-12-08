import tkinter as tk
from dataclasses import dataclass
import random


@dataclass
class Question:
    prompt: str
    choices: list  
    correct_index: int


def build_basic_cmd_i_questions(): # <- this is where the questions are stored depending on the section/chapter
    q = []

    # How to create your own Questions
    # q.append(Question(prompt, choices, correct_index))
    # q.append(Question("Input the question you would like between the quotes in the first index of the list",
    # ["input the answer seperated by ',' and each answer input as a string
    # input the correct answer index as an int for example 0 <-- is an index "]
    # End Product should look like this 
    # q.append(Question(
    #     "What is the subject of this program?",
    #     ["Index 0", "Index 1", "Index 2", "Index 3"],
    #     0, <- which means the correct answer is Index 0
    # ))
    q.append(Question(
        "In Linux, which command shows your current username?",
        ["whoami", "who", "id -u", "user"],
        0,
    ))
    q.append(Question(
        "In Linux, which command shows your current username?",
        ["whoami", "who", "id -u", "user"],
        0,
    ))
    q.append(Question(
        "What is at the very top of the Linux filesystem tree?",
        ["/root", "/home", "/", "C:\\"],
        2,
    ))
    q.append(Question(
        "Which command changes directory to /etc?",
        ["cd etc", "cd /etc", "chdir /etc", "goto /etc"],
        1,
    ))
    q.append(Question(
        "Which command lists the contents of the current directory?",
        ["ls", "dir /p", "show", "list"],
        0,
    ))
    q.append(Question(
        "Which option with ls shows a long listing with permissions and sizes?",
        ["ls -a", "ls -l", "ls -h", "ls -p"],
        1,
    ))
    q.append(Question(
        "Which option with ls shows hidden files?",
        ["ls -h", "ls -s", "ls -a", "ls -H"],
        2,
    ))
    q.append(Question(
        "Which command clears the screen in the terminal?",
        ["clear", "cls", "screen", "wipe"],
        0,
    ))
    q.append(Question(
        "Which command shows brief help for a tool using its own built-in help?",
        ["tool /?", "tool --help", "help tool", "doc tool"],
        1,
    ))
    q.append(Question(
        "Which command shows the manual page for a command?",
        ["man", "help", "info", "doc"],
        0,
    ))
    q.append(Question(
        "The locate command is used to:",
        [
            "Search the whole system for file paths",
            "Edit files",
            "List running processes",
            "Show network interfaces",
        ],
        0,
    ))
    q.append(Question(
        "The whereis command is mainly used to:",
        [
            "Show environment variables",
            "Find binary, man page, and source",
            "Find only configuration files",
            "Search for text in a file",
        ],
        1,
    ))
    q.append(Question(
        "Which command is similar to Python's print(), echoing text to the terminal?",
        ["print", "say", "echo", "out"],
        2,
    ))
    q.append(Question(
        "The cat command is often used to:",
        [
            "Create and display small files",
            "Compile programs",
            "Change file permissions",
            "Monitor processes",
        ],
        0,
    ))
    q.append(Question(
        "Which redirection symbol is used with cat to create a file?",
        ["<", ">", ">>", "|"],
        1,
    ))
    q.append(Question(
        "Which command is used to create an empty file (if it does not exist)?",
        ["touch", "newfile", "mkfile", "make"],
        0,
    ))
    q.append(Question(
        "Which command creates a new directory?",
        ["mkdir", "makedir", "newdir", "mk"],
        0,
    ))
    q.append(Question(
        "Which option with mkdir creates nested (parent) directories as needed?",
        ["mkdir -r", "mkdir -p", "mkdir -n", "mkdir -R"],
        1,
    ))

    return q


def build_basic_cmd_ii_questions():
    q = []

    # Existing questions
    q.append(Question(
        "Which command is used to add a new user on Linux?",
        ["useradd", "sudo adduser", "mkuser", "newuser"],
        1,
    ))
    q.append(Question(
        "Where are user account details stored (like usernames) on Linux?",
        ["/etc/shadow", "/etc/passwd", "/etc/userdb", "/home/passwd"],
        1,
    ))
    q.append(Question(
        "Which command deletes a user?",
        ["sudo rmuser", "sudo deluser", "sudo removeuser", "del /user"],
        1,
    ))
    q.append(Question(
        "The file /etc/sudoers controls:",
        [
            "Kernel parameters",
            "Which users can use sudo",
            "SSH configuration",
            "Network routes",
        ],
        1,
    ))
    q.append(Question(
        "Which command switches to another user (e.g., root)?",
        ["sw", "chuser", "su", "switch"],
        2,
    ))
    q.append(Question(
        "The history size is controlled by which environment variable?",
        ["HISTORY", "HISTSIZE", "SIZEHIST", "HISTSAVE"],
        1,
    ))
    q.append(Question(
        "Which command shows the command history?",
        ["hist", "history", "cmdhis", "showhist"],
        1,
    ))
    q.append(Question(
        "To re-run command number 100 from history, you type:",
        ["run 100", "!100", "history 100", "redo 100"],
        1,
    ))
    q.append(Question(
        "The $ sign in the shell is used to:",
        [
            "Declare variables",
            "Retrieve the value of variables",
            "Create files",
            "Show process IDs",
        ],
        1,
    ))
    q.append(Question(
        "Which symbol is used for piping output of one command to another?",
        ["&", "|", ">", "<"],
        1,
    ))
    q.append(Question(
        "Which command searches processes by name (e.g., ssh)?",
        ["ps", "pgrep", "grep ps", "pfind"],
        1,
    ))
    q.append(Question(
        "The sort -r file.txt command:",
        [
            "Sorts file numerically",
            "Sorts file alphabetically",
            "Sorts file in reverse order",
            "Removes duplicate lines",
        ],
        2,
    ))
    q.append(Question(
        "Which option with sort removes duplicate lines?",
        ["-u", "-d", "-r", "-n"],
        0,
    ))
    q.append(Question(
        "The rev command in Linux:",
        [
            "Reverses line order in a file",
            "Reverses characters in each line",
            "Renames files",
            "Reverts file to backup",
        ],
        1,
    ))
    q.append(Question(
        "The uniq command usually works best when combined with:",
        ["cat", "sort", "grep", "ls"],
        1,
    ))
    q.append(Question(
        "grep \"^Hello\" file.txt will match lines:",
        [
            "Ending with Hello",
            "Containing Hello anywhere",
            "Starting with Hello",
            "Only equal to Hello",
        ],
        2,
    ))
    q.append(Question(
        "grep \"world$\" file.txt will match lines:",
        [
            "Starting with world",
            "Containing world anywhere",
            "That do NOT contain world",
            "Ending with world",
        ],
        3,
    ))
    q.append(Question(
        "sed 's/Hello/Hi/' file.txt will:",
        [
            "Delete lines with Hello",
            "Replace first Hello with Hi per line (stdout only)",
            "Replace all Hello with Hi and overwrite file",
            "Create a backup copy only",
        ],
        1,
    ))

    q.append(Question(
        "Find lines containing 'root' in /etc/passwd:",
        ["grep root /etc/passwd", "find root /etc/passwd", "search root /etc/passwd", "cat -g root /etc/passwd"],
        0,
    ))
    q.append(Question(
        "Install package nmap (Debian/Kali):",
        ["sudo apt install nmap", "apt-get make nmap", "sudo install nmap", "pkg nmap"],
        0,
    ))
    q.append(Question(
        "Update package lists (Debian/Kali):",
        ["sudo apt update", "sudo apt upgrade", "sudo apt refresh", "sudo apt sync"],
        0,
    ))
    q.append(Question(
        "Upgrade installed packages (Debian/Kali):",
        ["sudo apt upgrade", "sudo apt update", "sudo apt fix", "sudo apt full"],
        0,
    ))
    q.append(Question(
        "Count lines in access.log:",
        ["wc -l access.log", "lines access.log", "count access.log", "grep -n access.log"],
        0,
    ))
    q.append(Question(
        "Search 'error' in syslog:",
        ["grep error /var/log/syslog", "find error /var/log/syslog", "search error /var/log/syslog", "cat -e /var/log/syslog"],
        0,
    ))
    q.append(Question(
        "Show IP addresses with ip tool:",
        ["ip a", "ip show", "ip list", "ip addr all"],
        0,
    ))
    q.append(Question(
        "Show routing table with ip:",
        ["ip r", "ip route", "route ip", "netstat -r ip"],
        0,  # both ip r and ip route are valid; we pick one as correct
    ))
    q.append(Question(
        "Show manual page for chmod:",
        ["man chmod", "help chmod", "chmod --help", "doc chmod"],
        0,
    ))
    q.append(Question(
        "Change file perms to rwxr-xr-x (octal):",
        ["chmod 755 file.txt", "chmod 644 file.txt", "chmod 777 file.txt", "chmod 600 file.txt"],
        0,
    ))
    q.append(Question(
        "Change owner of file.txt to root:",
        ["sudo chown root file.txt", "chmod root file.txt", "owner root file.txt", "sudo own root file.txt"],
        0,
    ))
    q.append(Question(
        "Show network interfaces and addresses on Kali (modern):",
        ["ip a", "ifconfig -all", "netstat -i", "route print"],
        0,
    ))

    return q


def build_python_questions():
    q = []

    q.append(Question(
        "Which command shows the installed Python 3 version in Linux?",
        ["python --ver", "python3 -v", "python3 --version", "py3 --v"],
        2,
    ))
    q.append(Question(
        "Which file extension is commonly used for Python scripts?",
        [".pt", ".py", ".sh", ".ps"],
        1,
    ))
    q.append(Question(
        "Which is a correct first Python script to print Hello?",
        ["print('Hello')", "echo 'Hello'", "printf('Hello')", "say('Hello')"],
        0,
    ))
    q.append(Question(
        "Python is case sensitive. Which of these will cause an error?",
        ["print('hello')", "PRINT('hello')", "print(\"hello\")", "print('HELLO')"],
        1,
    ))
    q.append(Question(
        "Which function reads input from the keyboard?",
        ["read()", "scan()", "input()", "get()"],
        2,
    ))
    q.append(Question(
        "Which line correctly casts input to an integer?",
        [
            "x = int(input('value: '))",
            "x = integer(input('value: '))",
            "x = float('value: ')",
            "x = castint(input('value: '))",
        ],
        0,
    ))
    q.append(Question(
        "Which operator in Python performs exponentiation?",
        ["^", "**", "exp()", "//"],
        1,
    ))
    q.append(Question(
        "Strings in Python are:",
        [
            "Mutable sequences of characters",
            "Immutable sequences of characters",
            "Only one character long",
            "Not sequences at all",
        ],
        1,
    ))
    q.append(Question(
        "Given a = 'Hello, World!', what does a[1] return?",
        ["H", "e", "o", ","],
        1,
    ))
    q.append(Question(
        "Which slicing expression returns 'llo' from 'Hello'?",
        ["s[1:3]", "s[2:4]", "s[2:5]", "s[1:4]"],
        2,
    ))
    q.append(Question(
        "Which is the correct if statement to check if grade is >= 50?",
        [
            "if grade => 50:",
            "if grade >= 50:",
            "if (grade => 50):",
            "if grade =>= 50:",
        ],
        1,
    ))
    q.append(Question(
        "Which Python keyword is used for an alternative condition (else if)?",
        ["elseif", "elif", "else if", "elif()"],
        1,
    ))
    q.append(Question(
        "Which loop runs a fixed number of times based on a sequence?",
        ["for", "while", "loop", "repeat"],
        0,
    ))
    q.append(Question(
        "range(1, 5) generates:",
        ["1, 2, 3, 4, 5", "0, 1, 2, 3", "1, 2, 3, 4", "2, 3, 4, 5"],
        2,
    ))
    q.append(Question(
        "range(1, 10, 2) generates:",
        ["1, 2, 3, 4, 5", "1, 3, 5, 7, 9", "2, 4, 6, 8", "0, 2, 4, 6"],
        1,
    ))
    q.append(Question(
        "A while loop keeps running:",
        [
            "Exactly 10 times",
            "Until the condition is false",
            "Only once",
            "Only with range()",
        ],
        1,
    ))
    q.append(Question(
        "What is a common pitfall with while loops?",
        [
            "They cannot use break",
            "They are always infinite",
            "Condition not changing, causing infinite loop",
            "They only work with strings",
        ],
        2,
    ))
    q.append(Question(
        "Which keyword exits a loop immediately?",
        ["stop", "exit", "break", "leave"],
        2,
    ))
    q.append(Question(
        "Which keyword skips to the next iteration of a loop?",
        ["skip", "continue", "next", "pass"],
        1,
    ))

    return q


def build_bash_scripting_questions():
    q = []
    #When pop up cannot write via keyboard <---> Make remove and let the code sit for next year 
    #Someone might fix it and update the questions/code and to credit I Muwaahahahaha
    #Check Code down for Short_Ans structure
    # q.append(Short_Ans(
    #     "Command to print the working directory:",
    #     ["pwd"],
    #     "Short answer expected: pwd",
    #     difficulty=1,
    # ))
    q.append(Question(
        "Which line is the shebang for a Bash script?",
        ["#!/bin/bash", "#!/usr/bin/python", "#!/bash", "#!bash"],
        0,
    ))
    q.append(Question(
        "A Bash shell script is typically saved as:",
        [
            "A binary file only",
            "A plain-text file, often with .sh extension",
            "A .exe file",
            "A .py file",
        ],
        1,
    ))
    q.append(Question(
        "Which command gives execute permission to a script?",
        ["chmod +x script.sh", "exec script.sh", "run script.sh", "permit script.sh"],
        0,
    ))
    q.append(Question(
        "How do you run a script in the current directory named myscript.sh?",
        ["myscript.sh", "./myscript.sh", "run myscript.sh", "bash /bin/myscript.sh"],
        1,
    ))
    q.append(Question(
        "In Bash, how do you create a variable x with value 10?",
        ["x = 10", "var x = 10", "x=10", "int x = 10"],
        2,
    ))
    q.append(Question(
        "Which is used to get the value of a variable named name?",
        ["$name", "@name", "&name", "?name"],
        0,
    ))
    q.append(Question(
        "The read command is used to:",
        [
            "Print a variable",
            "Read input from the terminal",
            "Compile the script",
            "Open a file",
        ],
        1,
    ))
    q.append(Question(
        "Which read option shows a prompt directly with the command?",
        ["-s", "-p", "-n", "-t"],
        1,
    ))
    q.append(Question(
        "Which read option makes input silent (e.g., for passwords)?",
        ["-q", "-s", "-h", "-p"],
        1,
    ))
    q.append(Question(
        "Which character starts a comment in Bash scripts?",
        ["//", "#", "/*", "--"],
        1,
    ))
    q.append(Question(
        "Command substitution using $(...) is used to:",
        [
            "Comment code",
            "Run a command and store its output in a variable",
            "Start a subshell",
            "Create a function",
        ],
        1,
    ))
    q.append(Question(
        "Which special variable holds the script name?",
        ["$@", "$#", "$0", "$1"],
        2,
    ))
    q.append(Question(
        "Which special variable holds the number of arguments passed to the script?",
        ["$@", "$#", "$0", "$*"],
        1,
    ))
    q.append(Question(
        "In an if statement, -lt means:",
        ["less than", "less or equal", "greater than", "equal"],
        0,
    ))
    q.append(Question(
        "Which is a correct if structure in Bash?",
        [
            "if (cond) { ... }",
            "if [ cond ] then ... fi",
            "if cond: ... end",
            "if cond do ... done",
        ],
        1,
    ))
    q.append(Question(
        "Which keyword adds another condition after if in Bash?",
        ["elseif", "elif", "else if", "elif()"],
        1,
    ))
    q.append(Question(
        "Which is a basic for loop over numbers 1..5 using brace expansion?",
        [
            "for i in 1..5; do echo $i; done",
            "for i {1..5} do echo $i",
            "for i in {1..5}; do echo $i; done",
            "loop i 1 5 echo $i",
        ],
        2,
    ))
    q.append(Question(
        "In the expression $((x*y)) inside Bash, $(( ... )) is used for:",
        [
            "String concatenation",
            "Command substitution",
            "Arithmetic expansion",
            "Array indexing",
        ],
        2,
    ))

    return q   
# Short answer questions 
class Short_Ans:
    def __init__(self, prompt: str, acceptable: list[str], explain: str = "", difficulty: int = 1):
        self.prompt = prompt
        self.acceptable = [a.strip().lower() for a in acceptable]
        self.explain = explain
        self.difficulty = difficulty
    #DO NOT TOUCH IT WILL BREAK THE PROGRAM <- just fix it :)
    def ask(self, qnum: int, total: int) -> bool:
        print(f"{FG_AMBER}{BOLD}Q{qnum}/{total}:{RESET} {FG_WHITE}{self.prompt}{RESET}")
        print(f"{FG_GREY}(Type your answer then press Enter){RESET}")
        ans = input(f"{FG_NEON}> {RESET}").strip().lower()
        correct = ans in self.acceptable
        if correct:
            print(CAT_OK)
        else:
            print(CAT_BAD)
            key = self.acceptable[0] if self.acceptable else ""
            if key:
                print(f"{FG_YELLOW}One correct answer: {key}{RESET}")
        if self.explain:
            print(f"{FG_GREY}{self.explain}{RESET}")
        print()
        return correct 

class UndertaleQuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("System Programming Project - PMU Credit : Happy🐈 - BoB")
        self.root.geometry("1280x720")
        self.root.configure(bg="black")

        # State variables
        self.state = "menu"
        self.subjects = [
            "Basic Command I",
            "Basic Command II",
            "Python I & II",
            "Bash Scripting",
        ]
        self.menu_index = 0
        self.current_subject = None
        self.questions = []
        self.q_index = 0
        self.score = 0
        self.selected_option_index = 0
        self.locked = False

        # Build question banks
        self.bank_basic_i = build_basic_cmd_i_questions()
        self.bank_basic_ii = build_basic_cmd_ii_questions()
        self.bank_python = build_python_questions()
        self.bank_bash = build_bash_scripting_questions()
        # self.bank.new = new()

        #Layout
        self.header_frame = tk.Frame(self.root, bg="black", pady=8)
        self.header_frame.pack(fill="x")

        header_text = (
            "Prince Mohammad Bin Fahd University\n"
            "Student: Abdullah -> Happy 🐈<-\n"
            "Instructor: Dr. Ibrahim El Didi #BoB\n"
            "Subject: (select from menu)\n"
            "Project: Kali + Basics + Python\n"
            "My kat: /\\_/\\ \n"
            "       (=^.^=)\n"
            "      c(  <\n  <3 )<c\n"
        )
        self.header_label = tk.Label(
            self.header_frame,
            text=header_text,
            font=("Consolas", 12),
            fg="white",
            bg="black",
            justify="left",
        )
        self.header_label.pack(side="left", padx=20)

        self.score_label = tk.Label(
            self.header_frame,
            text="Score: 0 / 0",
            font=("Consolas", 12, "bold"),
            fg="#FFD700",
            bg="black",
        )
        self.score_label.pack(side="right", padx=20)

        self.content_frame = tk.Frame(self.root, bg="black")
        self.content_frame.pack(fill="both", expand=True, pady=10)

        self.footer_label = tk.Label(
            self.root,
            text="Use ↑ / ↓ to move, Enter to confirm.",
            font=("Consolas", 10),
            fg="#CCCCCC",
            bg="black",
        )
        self.footer_label.pack(side="bottom", pady=5)

        # Placeholders to be created in draw functions
        self.menu_labels = []
        self.title_label = None
        self.question_label = None
        self.option_labels = []
        self.feedback_label = None

        # Movement
        self.root.bind("<Up>", self.on_key_up)
        self.root.bind("<Down>", self.on_key_down)
        self.root.bind("<Return>", self.on_key_enter)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.draw_menu()

    # Drawing

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.menu_labels = []
        self.option_labels = []
        self.question_label = None
        self.feedback_label = None

    def update_header_subject(self, subject_text):
        header_text = (
            "Prince Mohammad Bin Fahd University\n"
            "Course: Programming Languagues\n"
            "Student: Abdullah -> Happy 🐈 <-\n"
            "Instructor: Dr. Ibrahim El Didi #BoB\n"
            f"Subject: {subject_text}\n"
            "Project: Kali + Basics + Python\n"
        )
        self.header_label.config(text=header_text)

    def draw_menu(self):
        self.state = "menu"
        self.clear_content()
        self.score_label.config(text="Score: 0 / 0")
        self.update_header_subject("(select from menu)")

        self.title_label = tk.Label(
            self.content_frame,
            text="== SELECT SUBJECT ==",
            font=("Consolas", 18, "bold"),
            fg="white",
            bg="black",
        )
        self.title_label.pack(pady=20)

        for i, subject in enumerate(self.subjects):
            lbl = tk.Label(
                self.content_frame,
                text=subject,
                font=("Consolas", 14),
                fg="white",
                bg="black",
                anchor="w",
            )
            lbl.pack(pady=5)
            self.menu_labels.append(lbl)

        self.menu_index = 0
        self.upd_menu()

    def upd_menu(self):
        for i, lbl in enumerate(self.menu_labels):
            if i == self.menu_index:
                lbl.config(text="▶ " + self.subjects[i], fg="#FFD700")
            else:
                lbl.config(text="  " + self.subjects[i], fg="white")

#Quiz Subjects Menu

    def Quiz_Boot(self, subject):
        self.current_subject = subject

        if subject == "Basic Command I":
            bank = self.bank_basic_i
        elif subject == "Basic Command II":
            bank = self.bank_basic_ii
        elif subject == "Python I & II":
            bank = self.bank_python
        else:
            bank = self.bank_bash

        # pick up to 50 questions (or all if fewer)
        # the more questions the more demand on the program
        # Creates bugs as it will show some questions twice?
        # check loop for upd_menu
        
        max_q = 50
        if len(bank) > max_q:
            self.questions = random.sample(bank, max_q)
        else:
            self.questions = list(bank)

        self.score = 0
        self.q_index = 0
        self.selected_option_index = 0

        self.update_header_subject(subject)
        self.score_label.config(text=f"Score: 0 / {len(self.questions)}")

        self.Questions_Gen()

    def Questions_Gen(self):
        self.state = "quiz"
        self.locked = False
        self.clear_content()

        if self.q_index >= len(self.questions):
            self.Credits()
            return

        q = self.questions[self.q_index]

        # Question text
        self.question_label = tk.Label(
            self.content_frame,
            text=f"Q{self.q_index+1}/{len(self.questions)}: {q.prompt}",
            font=("Consolas", 14, "bold"),
            fg="white",
            bg="black",
            wraplength=800,
            justify="left",
        )
        self.question_label.pack(pady=20, anchor="w")

        # Options
        self.option_labels = []
        self.selected_option_index = 0
        #Pent Testing Choice but re-work
        for idx, choice in enumerate(q.choices):
            lbl = tk.Label(
                self.content_frame,
                text=choice,
                font=("Consolas", 13),
                fg="white",
                bg="black",
                anchor="w",
            )
            lbl.pack(pady=3, anchor="w", padx=40)
            self.option_labels.append(lbl)

        self.upd_opt()

        # Feedback label
        self.feedback_label = tk.Label(
            self.content_frame,
            text="",
            font=("Consolas", 14),
            fg="#AAAAAA",
            bg="black",
            justify="left",
        )
        self.feedback_label.pack(pady=20, anchor="w", padx=40)
#From Penetration testing by Milio
    def upd_opt(self):
        for i, lbl in enumerate(self.option_labels):
            prefix = "   "
            color = "white"
            if i == self.selected_option_index:
                prefix = "🐈"
                color = "#00ffe5"
            lbl.config(text=prefix + self.questions[self.q_index].choices[i], fg=color)
        #If question too long it will push the cat, move it some where else
    def check_answer(self):
        if self.locked:
            return
        self.locked = True

        q = self.questions[self.q_index]
        correct = (self.selected_option_index == q.correct_index)

        if correct:
            self.score += 1
            cat_text = " /\\_/\\\n( o.o )  Purrr-fect!\n > ^ <  Correct!\n"
            self.feedback_label.config(text=cat_text, fg="#00FF7F")
        else:
            correct_choice = q.choices[q.correct_index]
            cat_text = (
                " /\\_/\\\n( x.x )  gitgud!\n > ^ <  Try again.\n\n"
                f"Correct: {correct_choice}"
            )
            self.feedback_label.config(text=cat_text, fg="#FF5555")

        self.score_label.config(
            text=f"Score: {self.score} / {len(self.questions)}"
        )

        # delaying each question, to see the correct answer and also to make sure no one double clicks
        self.root.after(2000, self.next_question)

    def next_question(self):
        self.q_index += 1
        if self.q_index >= len(self.questions):
            self.Credits()
        else:
            self.Questions_Gen()

    #Grades
    def Credits(self):
        self.state = "finished"
        self.clear_content()

        total = len(self.questions)
        score_text = f"Your score: {self.score} / {total}"

        if self.score == total:
            msg = "Flawless victory!"
        elif self.score >= total * 0.75:
            msg = "Great job!"
        elif self.score >= total * 0.5:
            msg = "Not bad — keep practicing!"
        else:
            msg = "Give it another go!"

        result_label = tk.Label(
            self.content_frame,
            text=score_text + "\n\n" + msg,
            font=("Consolas", 16, "bold"),
            fg="white",
            bg="black",
            justify="center",
        )
        result_label.pack(pady=40)

        hint_label = tk.Label(
            self.content_frame,
            text="Press Enter to go back to subject menu.\nPress Esc to quit.",
            font=("Consolas", 12),
            fg="#BBBBBB",
            bg="black",
        )
        hint_label.pack(pady=10)

    #Key
    def on_key_up(self, event):
        if self.state == "menu":
            self.menu_index = (self.menu_index - 1) % len(self.subjects)
            self.upd_menu()
        elif self.state == "quiz" and not self.locked:
            self.selected_option_index = (self.selected_option_index - 1) % len(self.option_labels)
            self.upd_opt()

    def on_key_down(self, event):
        if self.state == "menu":
            self.menu_index = (self.menu_index + 1) % len(self.subjects)
            self.upd_menu()
        elif self.state == "quiz" and not self.locked:
            self.selected_option_index = (self.selected_option_index + 1) % len(self.option_labels)
            self.upd_opt()

    def on_key_enter(self, event):
        if self.state == "menu":
            subject = self.subjects[self.menu_index]
            self.Quiz_Boot(subject)
        elif self.state == "quiz":
            self.check_answer()
        elif self.state == "finished":
            self.draw_menu()


#Write New Code Between These unless you want to fix something





# This is the code that should run with the program if you wanted short answers
def run_quiz():
    enable_ansi_on_windows()
    clear_screen()
    banner()
    lines = [
        "Answer questions to earn points.",
        "MCQ: type A/B/C/D. Some are short answers: type the command or code.",
        "Get it right to see the cat!",
    ]
    retro_frame(lines)
    print()
    time.sleep(0.9)

    all_q = build_questions()
    QUESTIONS_PER_RUN = 50
    total_to_ask = min(len(all_q), QUESTIONS_PER_RUN) if QUESTIONS_PER_RUN else len(all_q)
    # Take the first N
    # Sort the questions by difficulty
    questions = all_q[:total_to_ask]

    score = 0
    for i, q in enumerate(questions, start=1):
        correct = q.ask(i, total_to_ask)
        if correct:
            score += 1
        time.sleep(0.3)

    print(f"{FG_AMBER}{BOLD}Quiz Complete!{RESET}")
    print(f"{FG_CYAN}Score: {score}/{total_to_ask}{RESET}")
    if score == total_to_ask:
        print(f"{FG_NEON}{BOLD}Flawless victory!{RESET}")
    elif score >= total_to_ask * 0.75:
        print(f"{FG_GREEN}Great job!{RESET}")
    elif score >= total_to_ask * 0.5:
        print(f"{FG_YELLOW}Not bad—keep practicing!{RESET}")
    else:
        print(f"{FG_RED}Give it another go!{RESET}")

    print()
    print(f"{FG_GREY}R) Replay    Q) Quit{RESET}")
    while True:
        choice = input(f"{FG_NEON}> {RESET}").strip().upper()
        if choice in {"R", "Q"}:
            break
        print(f"{FG_GREY}Type R to replay or Q to quit.{RESET}")
    if choice == "R":
        run_quiz()
    else:
        clear_screen()
        print(f"{FG_NEON}Goodbye!{RESET}")

#No NOT DOWN IN THE MIDDLE

#Boot up!
if __name__ == "__main__":
    root = tk.Tk()
    app = UndertaleQuizGUI(root)
    root.mainloop()

