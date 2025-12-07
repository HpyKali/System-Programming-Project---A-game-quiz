This program is a **Graphical User Interface (GUI) quiz game** designed to test and reinforce knowledge of core Linux commands, Python fundamentals, and Bash scripting. It was developed as a personal study tool to prepare for exams and explore new topics.

**I hope you find it useful\!**

| Detail | Value |
| :--- | :--- |
| **Author** | Abdullah (`#Happy`) |
| **Instructor** | Ibrahim El Didi (`@BoB`) |
| **Subject** | Kali, Linux Basics, Python, Bash Scripting |
| **Technology**| Python, Tkinter (GUI), Pillow (Image Handling) |
| **Prince Mohammed Bin Fahd University** |

How to Install and Run

### 1\. Requirements

This program requires the **Pillow** library for image handling, in addition to the standard Python libraries (`tkinter`, `dataclasses`, `random`).

### 2\. Installation (Setup)

Open your terminal or command prompt and install the necessary package:

  * **Windows CMD:**
    ```bash
    pip install Pillow
    ```
  * **Linux/macOS (Bash):**
    ```bash
    pip3 install Pillow
    ```

### 3\. Run the Program

1.  Copy the entire Python code.
2.  Paste it into a file named, for example, `QuizGame.py`.
3.  Place your background image file (e.g., `bg.jpg`) in the same directory.
4.  Execute the script from your terminal:
    ```bash
    python QuizGame.py
    # OR
    python3 QuizGame.py
    ```
5.  Enjoy\!

-----

## Program Configuration and Key Libraries

The core functionality and structure of the quiz rely on standard Python libraries.

### Main Libraries Used

| Library | Purpose & Note | Documentation |
| :--- | :--- | :--- |
| **`tkinter`** | **Primary GUI library.** Tkinter provides pre-built code and widgets (like Frames and Labels) to easily construct the graphical interface, making up over 90% of the program's user-facing structure. | [GeeksforGeeks Tkinter Documentation](https://www.geeksforgeeks.org/python/python-gui-tkinter/) |
| **`dataclasses`** | **Data Structure.** Used to cleanly define the `Question` objects, which store the prompt, choices, and correct answer index. This is where the program stores all quiz data, marks, and settings. | [Python docs: dataclasses](https://docs.python.org/3/library/dataclasses.html) |
| **`random`** | **Logic.** Used to randomly sample questions from the question banks for each quiz run. | |
| **`PIL/ImageTk`** | **Image Handling.** Used to load and display the background image (`bg.jpg`) within the Tkinter window. | |

### Configuration Note

When modifying the code, please be advised that removing or adding any structural elements (like indentation, parentheses, or commas) can easily break the program. Feel free to experiment with the code only if you understand the Python syntax fully.
