# MindMatters 🧠 - A Mental Health Quiz

MindMatters is a thoughtful web application designed to guide users through a self-assessment quiz for mental well-being. Built as one of my first full-stack projects using Flask, it features a comprehensive questionnaire that provides gentle, actionable recommendations based on the user's responses.

---

## 📚 Table of Contents

* [Features](#-features)
* [Quiz Structure](#-quiz-structure)
* [Tech Stack](#-tech-stack)
* [Setup and Installation](#-setup-and-installation)
* [Contact](#-contact)

---

## ✨ Features

* **Comprehensive Assessment**: A structured 30-question quiz that covers a range of topics related to mental well-being.
* **Three-Tier Questioning**: Questions are grouped into three distinct levels, progressing from general wellness to more specific topics.
* **Personalized Recommendations**: Provides simple, actionable advice based on the final quiz outcome, from wellness activities to suggesting professional consultation.
* **Informational Resources Page**: Includes a dedicated page offering helpful information and resources related to mental health awareness.
* **Lightweight & Fast**: Built with a simple Flask and HTML/CSS stack for a responsive user experience.

---

## 🔬 Quiz Structure

The core of this project is a comprehensive 30-question quiz structured to provide a holistic overview.

1.  **Level 1 (Foundational Questions)**: All users begin with 10 questions covering general feelings and stress levels.
2.  **Level 2 (Specific Scenarios)**: The quiz continues with the next 10 questions, delving into more specific life situations and emotional responses.
3.  **Level 3 (Detailed Assessment)**: The final 10 questions explore topics in greater detail to build a complete picture.
4.  **Final Recommendations**: After all 30 questions are answered, a total score is calculated. The application then provides a final recommendation based on this score, which may include wellness tips or suggest consulting a healthcare professional.

---

## 🛠️ Tech Stack

* **Backend**: `Flask` (Python)
* **Frontend**: `HTML5`, `CSS3` (with Jinja2 templating)

---

## ⚙️ Setup and Installation

This project is lightweight and easy to run locally.

### Prerequisites
* Python 3.8+
* Git

### Steps
1.  **Clone the Repository:**
    ```sh
    git clone [https://github.com/Srinidhi945/micro_project.git](https://github.com/Srinidhi945/micro_project.git)
    cd micro_project
    ```

2.  **Create and Activate a Virtual Environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    As this project primarily uses Flask, you can install it directly.
    ```sh
    pip install Flask Flask-WTF
    ```

4.  **Run the Application:**
    ```sh
    python app.py
    ```

5.  **View in Browser:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## 📞 Contact

* **LinkedIn Profile**: [https://www.linkedin.com/in/srinidhi-poreddy](https://www.linkedin.com/in/srinidhi-poreddy)
* **Project Link**: [https://github.com/Srinidhi945/micro_project](https://github.com/Srinidhi945/micro_project)
