# Language Practice Bot

Welcome to the **Language Practice Bot**! This is a Python application that helps you practice translating English words into other languages through a friendly graphical user interface (GUI). It's a fun and interactive way to enhance your vocabulary in Spanish, French, German, and Italian.

## Repository

GitHub Repository: [https://github.com/Mohamadaliibrahim/language_practice_bot.git](https://github.com/Mohamadaliibrahim/language_practice_bot.git)

---

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
- [Vocabulary Expansion](#vocabulary-expansion)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **Multi-language Support**: Practice translations in Spanish, French, German, and Italian.
- **Graphical User Interface**: User-friendly GUI built with Tkinter.
- **Randomized Questions**: Words are randomly selected to challenge your memory.
- **Multiple Choice Questions**: Each question offers multiple options to choose from.
- **Immediate Feedback**: Get instant feedback on your answers.
- **Progress Tracking**: See your score at the end of the quiz.
- **Option to Stop Quiz**: You can stop the quiz at any time and view your results.

---

## Demo

![Language Practice Bot Screenshot](screenshot.png)

*Screenshot of the Language Practice Bot in action.*

---

## Installation

### Prerequisites

- **Python 3.x**: Make sure you have Python 3 installed on your system.

### Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/Mohamadaliibrahim/language_practice_bot.git
```

Navigate to the project directory:

```bash
cd language_practice_bot
```

### Install Dependencies

#### Tkinter Installation

**Tkinter** is the standard GUI library for Python. It usually comes pre-installed with Python, but if it's not available on your system, follow the instructions below:

- **Windows and macOS**:

  Tkinter is included with the standard Python installation. No additional steps are needed.

- **Linux (Ubuntu/Debian-based distributions)**:

  Install Tkinter using the following command:

  ```bash
  sudo apt-get install python3-tk
  ```

- **Linux (Fedora/Red Hat-based distributions)**:

  Install Tkinter using the following command:

  ```bash
  sudo dnf install python3-tkinter
  ```

- **Verify Tkinter Installation**:

  You can verify if Tkinter is installed by running:

  ```bash
  python3 -m tkinter
  ```

  A small window titled "Tk" should appear if Tkinter is installed correctly.

#### Other Dependencies

No additional Python packages are required for this project.

---

## Usage

1. **Prepare the Vocabulary File**:

   Ensure that the `vocabulary.json` file is in the project directory. This file contains the words and their translations.

2. **Run the Application**:

   In your terminal, navigate to the project directory and run:

   ```bash
   python3 language_practice_gui.py
   ```

3. **Interact with the GUI**:

   - **Welcome Screen**: Click the **Start** button to begin.
   - **Select Language**: Choose the language you want to practice.
   - **Answer Questions**: Select the correct translation for each English word presented.
   - **Get Feedback**: After each question, you'll receive immediate feedback.
   - **Stop Quiz**: You can click the **Stop Quiz** button at any time to end the quiz and see your results.
   - **View Results**: At the end, your score will be displayed, and you can choose to play again or exit.

---

## Vocabulary Expansion

The vocabulary is stored in the `vocabulary.json` file. You can expand or modify this file to include more words or additional languages.

**Example Entry in `vocabulary.json`**:

```json
{
    "hello": {
        "Spanish": "hola",
        "French": "bonjour",
        "German": "hallo",
        "Italian": "ciao"
    }
}
```

**Adding More Words**:

1. Open `vocabulary.json` in a text editor.
2. Add new words following the existing structure.
3. Ensure that the JSON syntax is correct (proper commas, brackets, and quotes).
4. Save the file.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the Repository**: Click the **Fork** button on the GitHub repository page.

2. **Clone Your Fork**:

   ```bash
   git clone https://github.com/your-username/language_practice_bot.git
   ```

3. **Create a New Branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**: Enhance features, fix bugs, or improve documentation.

5. **Commit Your Changes**:

   ```bash
   git commit -am 'Add your commit message here'
   ```

6. **Push to Your Fork**:

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Submit a Pull Request**: Go to the original repository and submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **Tkinter**: For providing the GUI framework.
- **Contributors**: Thanks to everyone who has contributed to this project.
- **Language Learners**: Inspired by those who are passionate about learning new languages.

---

Feel free to contact me if you have any questions or suggestions!

---

*This README was generated to provide clear instructions and information about the Language Practice Bot project.*
