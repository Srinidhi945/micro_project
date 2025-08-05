# MindMatters 🧠 - An Adaptive Mental Health Quiz

MindMatters is a thoughtful web application designed to guide users through a self-assessment quiz for mental well-being. Built as one of my first full-stack projects using Flask, it features an adaptive questionnaire that tailors its length and depth based on user responses, providing gentle recommendations at the end.

---

## 📚 Table of Contents

* [Features](#-features)
* [The Adaptive Quiz Logic](#-the-adaptive-quiz-logic)
* [Tech Stack](#-tech-stack)
* [Setup and Installation](#-setup-and-installation)
* [Project Structure](#-project-structure)
* [Contact](#-contact)

---

## ✨ Features

* **Adaptive Questioning**: The quiz dynamically adjusts, presenting more questions only if initial answers indicate a potential need for further assessment.
* **Three-Tier Structure**: A gentle progression through up to 30 questions across three distinct levels of detail.
* **Personalized Recommendations**: Provides simple, actionable advice based on the quiz outcome, from wellness activities to suggesting professional consultation.
* **Informational Resources Page**: Includes a dedicated page offering helpful information and resources related to mental health awareness.
* **Lightweight & Fast**: Built with a simple Flask and HTML/CSS stack for a responsive user experience.

---

## 🔬 The Adaptive Quiz Logic

The core of this project is the logic that determines the user's path through the quiz.

1.  **Level 1 (Initial Screening)**: All users start with 10 foundational questions.
2.  **Evaluation Point**: After Level 1, a score is calculated. If the score is below a certain threshold, the quiz concludes with positive wellness recommendations (e.g., "Do yoga, exercise").
3.  **Level 2 (Deeper Dive)**: If the threshold is met, the user is presented with the next set of 10 more specific questions.
4.  **Final Evaluation**: A similar threshold logic is applied. This determines whether the user moves to the final level or receives moderate recommendations.
5.  **Level 3 (Detailed Assessment)**: For users whose answers indicate a higher level of concern, the final 10 questions are presented.
6.  **Final Recommendations**: The application provides its final recommendation based on the total score, which may include strongly suggesting the user consult with a healthcare professional.

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
    ````sh
    git clone [https://github.com/Srinidhi945/micro_project.git](https://github.com/Srinidhi945/micro_project.git)
    cd micro_project
    ````

2.  **Create and Activate a Virtual Environment:**
    ````sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ````

3.  **Install Dependencies:**
    As this project primarily uses Flask, you can install it directly.
    ````sh
    pip install Flask
    ````

4.  **Run the Application:**
    ````sh
    python app.py
    ````

5.  **View in Browser:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

---


## 📞 Contact

* **LinkedIn Profile**: [https://www.linkedin.com/in/srinidhi-poreddy](https://www.linkedin.com/in/srinidhi-poreddy)
* **Project Link**: [https://github.com/Srinidhi945/micro_project](https://github.com/Srinidhi945/micro_project)
