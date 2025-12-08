import tkinter as tk
from dataclasses import dataclass
import random
from PIL import Image, ImageTk 


@dataclass
class Question:
    # Sans asks (the quiz prompt)
    prompt: str
    # All the paths you can choose (the multiple choice options)
    choices: list
    # Which path is the pacifist route (the correct answer index)
    correct_index: int


def build_basic_cmd_i_questions(): # <- this is where the questions are stored depending on the section/chapter
    q = []
    # How to create your own Questions
    # q.append(Question(prompt, 4-choices seperateed by commasinside a list, correct_index))
    #q.append(Question("Who is the author", ["BoB", "Bob", "BOB!", "Bob"], 0))
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
        ["ip r", "ip routes", "route ip", "netstat -r ip"],
        0,
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
# This class is designed for terminal input/output, for future adaptation.
class Short_Ans:
    def __init__(self, prompt: str, acceptable: list[str], explain: str = "", difficulty: int = 1):
        self.prompt = prompt
        self.acceptable = [a.strip().lower() for a in acceptable]
        self.explain = explain
        self.difficulty = difficulty
    #DO NOT TOUCH IT WILL BREAK THE PROGRAM <- just fix it :)
    def ask(self, qnum: int, total: int) -> bool:
        return False 

class UndertaleQuizGUI:
    def __init__(self, root):
        # The main game window
        self.root = root
        self.root.title("System Programming Project - PMU Credit : Happy🐈 - BoB")
        self.root.geometry("1280x720")
        
        # 1. Image Path (Use your actual filename)
        image_path = "ImprovisedProject\\bg.jpg"  # <-- Use your actual filename here add \\ to the path
        
        try:
            pil_image = Image.open(image_path)
            
            self.bg_image = ImageTk.PhotoImage(pil_image)
            
        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found. Using fallback dark color.")
            # Fallback color (if image fails) because it always does
            #WARNING <---CRASHES IF YOU COMMENT IT--->
            self.root.configure(bg="#050505")
            self.bg_image = tk.PhotoImage(width=1, height=1) 
        
        # 4. Create the background label (which holds the image)
        self.background_label = tk.Label(self.root, image=self.bg_image)
        # 5. Place the label to cover the entire window
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #Background Color <-Do no touch->
        self.WIDGET_BG_COLOR = "#050505" 

        # State variables
        # What part of the game we are in (menu, quiz, finished)
        self.game_state = "menu"
        # The different levels/boss fights you can choose from
        self.boss_fights = [
            "Basic Command I",
            "Basic Command II",
            "Python I & II",
            "Bash Scripting",
        ]
        # Which option the arrow is pointing at in the menu right now
        self.menu_pointer = 0
        # The name of the boss fight we picked (current quiz subject)
        self.current_fight_name = None
        # The list of questions for the current boss fight
        self.fight_questions = []
        # The index of the current question we are on
        self.question_count = 0
        # How many times we hit the enemy (the score)
        self.mercy_score = 0
        # Which option the cat arrow is pointing at for the answer
        self.choice_cursor = 0
        # Did the user already answer this question? Don't let them click again!
        self.fight_locked = False

        # Build question banks
        # The basic Linux commands, part 1 questions
        self.bank_basic_i = build_basic_cmd_i_questions()
        # The basic Linux commands, part 2 questions
        self.bank_basic_ii = build_basic_cmd_ii_questions()
        # Python questions
        self.bank_python = build_python_questions()
        # Bash scripting questions
        self.bank_bash = build_bash_scripting_questions()
        # self.bank.new = new()

        #Layout
        # Header
        self.header_frame = tk.Frame(self.root, bg=self.WIDGET_BG_COLOR, pady=8) #FIXED DO NOT CHANGE
        self.header_frame.pack(fill="x")

        header_text = (
            "Prince Mohammad Bin Fahd University\n"
            "Student: Abdullah -> Happy 🐈<-\n"
            "Instructor: Dr. Ibrahim El Didi #BoB\n"
            "Subject: (select from menu)\n"
            "Project: Kali + Basics + Python\n"
            "My kat: /\\_/\\ \n"
            "       (=^.^=)\n"
            "      c(  <\n  <3 )<c\n"
        )
        # Header Text
        self.header_label = tk.Label(
            self.header_frame,
            text=header_text,
            font=("Consolas", 12),
            fg="white",
            bg=self.WIDGET_BG_COLOR, # <--- FIXED
            justify="left",
        )
        self.header_label.pack(side="left", padx=20)

        # Score Board
        self.score_label = tk.Label(
            self.header_frame,
            text="Score: 0 / 0",
            font=("Consolas", 12, "bold"),
            fg="#FFD700",
            bg=self.WIDGET_BG_COLOR, # <--- FIXED
        )
        self.score_label.pack(side="right", padx=20)

        # The main area where the questions/menu go
        self.content_frame = tk.Frame(self.root, bg=self.WIDGET_BG_COLOR) # <--- FIXED
        self.content_frame.pack(fill="both", expand=True, pady=10)

        # The hint text at the bottom
        self.footer_label = tk.Label(
            self.root,
            text="Use ↑ / ↓ to move, Enter to confirm.",
            font=("Consolas", 10),
            fg="#CCCCCC",
            bg=self.WIDGET_BG_COLOR, # <--- FIXED (Placed on root, but still needs color set)
        )
        self.footer_label.pack(side="bottom", pady=5)

        # Placeholders to be created in draw functions
        # The list of subject names on the menu
        self.menu_labels = []
        # The "SELECT SUBJECT" title
        self.title_label = None
         # The question text itself
        self.question_label = None
        # The list of option labels for the question
        self.option_labels = []
     # The box where the cat tells you if you are right or wrong
        self.feedback_label = None

        # Movement
        # Binding arrow keys to movement
        self.root.bind("<Up>", self.on_key_up)
        self.root.bind("<Down>", self.on_key_down)
        self.root.bind("<Return>", self.on_key_enter)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.draw_menu()

    # Drawing

    # Clears data on the screen, to go on to the next page
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.menu_labels = []
        self.option_labels = []
        self.question_label = None
        self.feedback_label = None

    # This changes the Subject
    def update_header_subject(self, subject_text):
        header_text = (
            "Prince Mohammad Bin Fahd University\n"
            "Course: Programming Languagues\n"
            "Student: Abdullah -> Happy 🐈 <-\n"
            "Instructor: Dr. Ibrahim El Didi #BoB\n"
            f"Subject: {subject_text}\n"
            "Project: Kali + Basics + Python\n"
        )
        #background is already set in __init__

        self.header_label.config(text=header_text)

    # Draws the main menu screen
    def draw_menu(self):
        # Set the state to menu, so self. can work
        self.game_state = "menu"
        self.clear_content()
        self.score_label.config(text="Score: 0 / 0")
        self.update_header_subject("(select from menu)")

        self.title_label = tk.Label(
            self.content_frame,
            text="== SELECT BOSS FIGHT (Chapter) ==",
            font=("Consolas", 18, "bold"),
            fg="white",
            bg=self.WIDGET_BG_COLOR, # <--- FIXED
        )
        self.title_label.pack(pady=20)

        # subject options
        for i, subject in enumerate(self.boss_fights):
            lbl = tk.Label(
                self.content_frame,
                text=subject,
                font=("Consolas", 14),
                fg="white",
                bg=self.WIDGET_BG_COLOR, # <--- FIXED
                anchor="w",
            )
            lbl.pack(pady=5)
            self.menu_labels.append(lbl)

        # Reset pointer and update the GUI
        self.menu_pointer = 0
        self.upd_menu()

    # Start the actual quiz when a subject is picked
    # Fight
    def Quiz_Boot(self, subject):
        self.current_fight_name = subject

        # Load the right list of questions
        if subject == "Basic Command I":
            bank = self.bank_basic_i
        elif subject == "Basic Command II":
            bank = self.bank_basic_ii
        elif subject == "Python I & II":
            bank = self.bank_python
        else:
            bank = self.bank_bash

        # pick up to 50 questions (or all if fewer)
        # the more questions the bigger the array/list need to adjust manually
        
        # Max number of questions to pick
        max_q_limit = 50
        if len(bank) > max_q_limit:
            # Pick a random sample of the questions
            # If questions > 50 it will pick 50 random questions and sort them in order
            self.fight_questions = random.sample(bank, max_q_limit)
        else:
            # Or just use all the questions if there aren't many
            self.fight_questions = list(bank)

        # Reset points
        self.mercy_score = 0
        self.question_count = 0
        self.choice_cursor = 0

        self.update_header_subject(subject)
        self.score_label.config(text=f"Score: 0 / {len(self.fight_questions)}")

        # Start the first question
        self.Questions_Gen()

    # Change the color and arrow for the menu options
    def upd_menu(self):
        for i, lbl in enumerate(self.menu_labels):
            if i == self.menu_pointer:
                # Highlight the selected option
                lbl.config(text="▶ " + self.boss_fights[i], fg="#FFD700", bg=self.WIDGET_BG_COLOR)
            else:
                # Un-highlight the others
                lbl.config(text="  " + self.boss_fights[i], fg="white", bg=self.WIDGET_BG_COLOR)

    # Draws the current question screen
    def Questions_Gen(self):
        self.game_state = "quiz"
        # Unlock the answer submission
        self.fight_locked = False
        self.clear_content()

        if self.question_count >= len(self.fight_questions):
            self.Credits()
            return

        # Get the current question
        current_question = self.fight_questions[self.question_count]

        # Question text
        self.question_label = tk.Label(
            self.content_frame,
            text=f"Q{self.question_count+1}/{len(self.fight_questions)}: {current_question.prompt}",
            font=("Consolas", 14, "bold"),
            fg="white",
            bg=self.WIDGET_BG_COLOR, # <--- FIXED
            wraplength=800,
            justify="left",
        )
        self.question_label.pack(pady=20, anchor="w")

        # Options
        self.option_labels = []
        # Reset the pointer at index 0
        self.choice_cursor = 0
        #Pent Testing Choice but re-work
        for idx, choice in enumerate(current_question.choices):
            lbl = tk.Label(
                self.content_frame,
                text=choice,
                font=("Consolas", 13),
                fg="white",
                bg=self.WIDGET_BG_COLOR, # <--- FIXED
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
            bg=self.WIDGET_BG_COLOR, # <--- FIXED
            justify="left",
        )
        self.feedback_label.pack(pady=20, anchor="w", padx=40)
#From Penetration testing by Milio

    # Change the cursor (cat) position on the options list
    def upd_opt(self):
        for i, lbl in enumerate(self.option_labels):
            prefix = "   "
            color = "white"
            if i == self.choice_cursor:
                # Highlight the selected option with the cat emoji
                prefix = "🐈"
                color = "#00ffe5"
            # Ensure the background color is consistently set here too
            lbl.config(text=prefix + self.fight_questions[self.question_count].choices[i], fg=color, bg=self.WIDGET_BG_COLOR) # <--- FIXED

    def check_answer(self):
        if self.fight_locked:
            return
        self.fight_locked = True

        # Get the current question
        q = self.fight_questions[self.question_count]
        # Check if the chosen index is the correct index
        correct = (self.choice_cursor == q.correct_index)

        if correct:
            # Increase the score/hit counter
            self.mercy_score += 1
            cat_text = " /\\_/\\\n( o.o )  Purrr-fect!\n > ^ <  Correct!\n"
            self.feedback_label.config(text=cat_text, fg="#00FF7F")
        else:
            correct_choice = q.choices[q.correct_index]
            cat_text = (
                " /\\_/\\\n( x.x )  gitgud!\n > ^ <  Try again.\n\n"
                f"Correct: {correct_choice}"
            )
            self.feedback_label.config(text=cat_text, fg="#FF5555")

        # Update the score display at the top
        self.score_label.config(
            text=f"Score: {self.mercy_score} / {len(self.fight_questions)}"
        )

        # delaying each question, to see the correct answer and also to make sure no one double clicks
        # Wait a bit then move to the next question
        self.root.after(2000, self.next_question)

    # Move to the next question or the final screen
    def next_question(self):
        self.question_count += 1
        # Check if we are done
        if self.question_count >= len(self.fight_questions):
            self.Credits()
        else:
            self.Questions_Gen()

    #Grades
    # The final screen showing the results and letting you quit/restart
    def Credits(self):
        self.game_state = "finished"
        self.clear_content()

        total = len(self.fight_questions)
        score_text = f"Your score: {self.mercy_score} / {total}"

        # Determine the final message based on percentage
        if self.mercy_score == total:
            msg = "Your Killing it"
        elif self.mercy_score >= total * 0.75:
            msg = "Great job!"
        elif self.mercy_score >= total * 0.5:
            msg = "Not bad keep practicing!"
        else:
            msg = "Damm.........\n, try another time, but this time study please"

        result_label = tk.Label(
            self.content_frame,
            text=score_text + "\n\n" + msg,
            font=("Consolas", 16, "bold"),
            fg="white",
            bg=self.WIDGET_BG_COLOR, # <--- FIXED
            justify="center",
        )
        result_label.pack(pady=40)

        hint_label = tk.Label(
            self.content_frame,
            text="Press Enter to go back to subject menu.\nPress Esc to quit.",
            font=("Consolas", 12),
            fg="#BBBBBB",
            bg=self.WIDGET_BG_COLOR, # <--- FIXED
        )
        hint_label.pack(pady=10)

    #Key
    # Handle the 'Up' key press
    def on_key_up(self, event):
        if self.game_state == "menu":
            # Move the menu pointer up (circularly)
            self.menu_pointer = (self.menu_pointer - 1) % len(self.boss_fights)
            self.upd_menu()
        # Only allow movement if it's a quiz and not locked (answered)
        elif self.game_state == "quiz" and not self.fight_locked:
            # Move the option selector up (circularly)
            self.choice_cursor = (self.choice_cursor - 1) % len(self.option_labels)
            self.upd_opt()

    # Handle the 'Down' key press
    def on_key_down(self, event):
        if self.game_state == "menu":
            # Move the menu pointer down (circularly)
            self.menu_pointer = (self.menu_pointer + 1) % len(self.boss_fights)
            self.upd_menu()
        elif self.game_state == "quiz" and not self.fight_locked:
            self.choice_cursor = (self.choice_cursor + 1) % len(self.option_labels)
            self.upd_opt()

    # enter key
    def on_key_enter(self, event):
        if self.game_state == "menu":
            # Start the selected quiz
            subject = self.boss_fights[self.menu_pointer]
            self.Quiz_Boot(subject)
        elif self.game_state == "quiz":
            # Submit the current answer
            self.check_answer()
        elif self.game_state == "finished":
            # Go back to the menu
            self.draw_menu()


#Boot up!
if __name__ == "__main__":
    root = tk.Tk()
    app = UndertaleQuizGUI(root)

    root.mainloop()
