from flask_wtf.csrf import generate_csrf
from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# Set the secret key
app.config['SECRET_KEY'] = 'RTFP_m!ndm@tters'

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Static first 10 questions
static_questions = [
    "How often do you feel stressed?",
    "How often do you feel anxious?",
    "How often do you have trouble sleeping?",
    "How often do you feel down or depressed?",
    "How often do you feel overwhelmed?",
    "How often do you feel irritable?",
    "How often do you experience changes in appetite?",
    "How often do you feel fatigued?",
    "How often do you have trouble concentrating?",
    "How often do you feel hopeless?"
]

# Additional questions to be shown based on the score of the first 10 questions
additional_questions = {
    'low': [
        "How often do you struggle to relax or unwind?",
        "How often do you feel unsupported by those around you?",
        "How often do you avoid physical exercise?",
        "How often do you feel unable to enjoy your hobbies or activities?",
        "How often do you neglect self-care activities?",
        "How often do you feel your work-life balance is unhealthy?",
        "How often do you feel isolated from social activities or loved ones?",
        "How often do you feel dissatisfied with your overall quality of life?",
        "How often do you struggle to practice mindfulness or stay present?",
        "How often do you avoid seeking professional help or counseling when needed?",
        "How often do you feel dissatisfied with your level of personal growth and development?",
        "How often do you struggle to handle setbacks or challenges in your life?",
        "How often do you feel a lack of purpose or direction in your life?",
        "How often do you struggle to maintain a positive outlook on life?",
        "How often do you feel unable to set boundaries and assert yourself?",
        "How often do you feel disconnected from your community or a sense of belonging?",
        "How often do you struggle to cope with negative emotions such as anger or sadness?",
        "How often do you feel unable to express your thoughts and feelings openly with others?",
        "How often do you fail to celebrate your accomplishments and successes?",
        "How often do you neglect activities that nourish your mind, body, and spirit?"
    ],
    'medium': [
        "How often do you notice negative changes in your mood or behavior?",
        "How often do you struggle to cope with major life changes or challenges?",
        "How often do you face unresolved conflicts in your personal or professional life?",
        "How often do you feel a lack of purpose or fulfillment in your daily activities?",
        "How often do you struggle to manage your workload and responsibilities?",
        "How often do past traumatic experiences affect you?",
        "How often do you engage in negative thoughts or self-criticism?",
        "How often do you experience physical symptoms related to stress or anxiety?",
        "How often do you fail to prioritize your mental health in your daily routine?",
        "How often do you rely on unhealthy habits or coping mechanisms?",
        "How often do you struggle to maintain boundaries in your relationships?",
        "How often do you feel stuck or stagnant in areas of your life?",
        "How often do you neglect your creativity and imagination?",
        "How often do you experience changes in your sleep patterns?",
        "How often do you struggle to cultivate balance and harmony in your life?",
        "How often do you feel you lack goals or aspirations to work towards?",
        "How often do you struggle to cope with uncertainty or ambiguity?",
        "How often do you feel disconnected from something greater than yourself?",
        "How often do you struggle to cultivate resilience in the face of adversity?",
        "How often do you feel there are aspects of your life that you want to improve or change?"
    ],
    'high': [
        "How often do you experience traumatic events or loss?",
        "How often do you struggle to cope with overwhelming emotions or situations?",
        "How often do you deal with persistent negative thought patterns?",
        "How often do you struggle to manage your time and energy effectively?",
        "How often do you notice changes in your appetite or eating habits?",
        "How often do you struggle to maintain optimism and hope for the future?",
        "How often do you experience recurring nightmares or sleep disturbances?",
        "How often do you handle conflicts or disagreements in your relationships poorly?",
        "How often do you experience symptoms of burnout or emotional exhaustion?",
        "How often do you struggle to practice self-compassion and forgiveness towards yourself?",
        "How often do you find it difficult to identify and challenge irrational beliefs or cognitive distortions?",
        "How often do you struggle to cultivate a sense of identity and self-worth during difficult times?",
        "How often do you lack a support network or community you can turn to for help?",
        "How often do you struggle with existential questions or concerns about the meaning of life?",
        "How often do you experience changes in your relationships or social connections?",
        "How often do you find it difficult to navigate transitions or changes in your life circumstances?",
        "How often do you deal with unresolved conflicts or tensions within yourself or with others?",
        "How often do you struggle to cultivate a sense of acceptance and peace with things you cannot change?",
        "How often do you neglect activities that nourish your mind, body, and spirit?",
        "How often do you struggle to find meaning and purpose in challenging experiences or adversity?"
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/brief')
def brief():
    return render_template('brief.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        first_10_answers = {}
        for question_id in range(1, 11):
            answer = request.form.get(f'q{question_id}')
            if answer:
                first_10_answers[question_id] = get_score(answer)

        # Ensure that first_10_answers is not empty
        if not first_10_answers:
            # Handle case where no answers were provided
            return redirect(url_for('quiz'))

        # Calculate the total score
        score = sum(first_10_answers.values())
        category = get_category(score)
        # Get the username from the form
        username = request.form.get('username')

        # Redirect to the additional quiz with the username included in the query string
        return redirect(url_for('additional_quiz', category=category, username=username))

    # Generate CSRF token for GET request
    csrf_token = generate_csrf()

    return render_template('quiz.html', questions=static_questions, csrf_token=csrf_token)

@app.route('/additional_quiz/<category>', methods=['GET', 'POST'])
def additional_quiz(category):
    questions = additional_questions[category]
    additional_answers = {}
    total_score = 0  # Initialize total_score with a default value

    if request.method == 'POST':
        for question_id in range(1, len(questions) + 1):
            answer = request.form.get(f'q{question_id}')
            if answer:
                additional_answers[question_id] = get_score(answer)

        # Ensure that additional_answers is not empty
        if not additional_answers:
            return redirect(url_for('additional_quiz', category=category))

        total_score = sum(additional_answers.values())
        username = request.args.get('username')  # Get the username from the query string
        return redirect(url_for('results', total_score=total_score, username=username))

    csrf_token = generate_csrf()
    return render_template('additional_quiz.html', questions=questions, csrf_token=csrf_token)

@app.route('/results/<int:total_score>')
def results(total_score):
    username = request.args.get('username')  # Get the username from the query string
    symptoms_and_recommendations, recommendations = get_recommendations(total_score)
    return render_template('results.html', total_score=total_score, username=username, symptoms_and_recommendations=symptoms_and_recommendations, recommendations=recommendations)

def get_category(score):
    if score < 16:
        return 'low'
    elif 16 <= score <= 33:
        return 'medium'
    else:
        return 'high'

def get_score(answer):
    answer = answer.lower() if answer else ''  # Convert answer to lowercase if it exists
    if answer == 'never':
        return 0
    elif answer == 'rarely':
        return 1
    elif answer == 'sometimes':
        return 2
    elif answer == 'often':
        return 3
    elif answer == 'always':
        return 4
    else:
        return 0  # Return 0 if answer is not recognized

def calculate_total_score(answers):
    # Placeholder for calculating total score based on all answers
    total_score = sum(get_score(answer) for answer in answers.values())
    return total_score

def get_recommendations(total_score):
        recommendations = []
        symptoms_and_recommendations = ""

        if total_score < 30:
            recommendations = [
                "practicing  few yoga asanas and making yourself active might be helpful for you.",
                "Walking or light jogging: Promotes relaxation and boosts mood.",
                "Swimming: Helps to reduce stress and improve overall well-being.",
                "Stretching exercises: Relieves muscle tension and promotes flexibility.",
                "Tai Chi: Combines gentle movements and deep breathing for relaxation.",
                "Child's Pose (Balasana): Calms the mind and releases tension in the back.",
                "Cat-Cow Stretch (Marjaryasana-Bitilasana): Improves flexibility and reduces stress.",
                "Legs-Up-the-Wall Pose (Viparita Karani): Relieves stress and promotes relaxation.",
                "Savasana (Corpse Pose): Helps to relax the body and quiet the mind."
            ]
            symptoms_and_recommendations = "Your health seems fine but You might feel occasionally tired or stressed. Here are some recommendations:"

        elif total_score < 50:
            recommendations = [
                "Regular aerobic exercises like running, cycling, or dancing: Boosts endorphin levels and improves mood.",
                "Strength training: Enhances physical and mental strength, reducing symptoms of anxiety.",
                "High-intensity interval training (HIIT): Releases stress and increases energy levels.",
                "Group fitness classes: Provides social interaction and reduces feelings of isolation.",
                "Tree Pose (Vrksasana): Improves balance and focus.",
                "Warrior I (Virabhadrasana I): Increases confidence and strength.",
                "Warrior II (Virabhadrasana II): Enhances concentration and stability.",
                "Triangle Pose (Trikonasana): Reduces anxiety and improves overall flexibility.",
                "Bridge Pose (Setu Bandhasana): Alleviates stress and stretches the chest and shoulders.",
                "Camel Pose (Ustrasana): Opens the heart and relieves tension in the back.",
                "Seated Forward Bend (Paschimottanasana): Calms the mind and stretches the spine.",
                "Reclining Bound Angle Pose (Supta Baddha Konasana): Relaxes the body and reduces stress."
            ]
            symptoms_and_recommendations = "You may experience mild stress or fatigue. Here are some recommendations:"

        elif total_score < 70:
            recommendations = [
                "Mindfulness meditation: Reduces stress and promotes emotional well-being.",
                "Deep breathing exercises: Activates the relaxation response and reduces anxiety.",
                "Progressive muscle relaxation: Eases physical tension and promotes relaxation.",
                "Yoga Nidra: Induces deep relaxation and improves sleep quality.",
                "Visualization or guided imagery: Reduces stress and enhances mental clarity.",
                "Journaling: Provides an outlet for emotions and helps process thoughts.",
                "Art therapy: Encourages self-expression and emotional healing.",
                "Listening to calming music: Soothes the mind and reduces stress levels.",
                "Warm baths with essential oils: Relaxes the body and calms the mind.",
                "Aromatherapy: Utilizes scents like lavender or chamomile to reduce anxiety.",
                "Practicing gratitude: Shifts focus to positive aspects of life and improves mood.",
                "Connecting with a supportive friend or family member: Provides emotional support."
            ]
            symptoms_and_recommendations = "You could be feeling moderate stress or fatigue. Here are some recommendations:"

        elif total_score < 110:
            recommendations = [
                "Seeking professional counseling or therapy: Offers guidance and support for managing mental health.",
                "Engaging in hobbies or activities you enjoy: Promotes a sense of accomplishment and joy.",
                "Setting realistic goals: Helps to manage expectations and reduce stress.",
                "Time management techniques: Improves productivity and reduces feelings of overwhelm.",
                "Practicing self-compassion: Encourages kindness towards oneself and reduces self-criticism.",
                "Limiting caffeine and sugar intake: Stabilizes mood and energy levels.",
                "Spending time in nature: Promotes relaxation and mental clarity.",
                "Connecting with support groups or online communities: Provides a sense of belonging and understanding."
            ]
            symptoms_and_recommendations = "You might be experiencing noticeable stress or tiredness. Here are some recommendations:"

        else:
            recommendations = [
                " Consider making some healthy lifestyle changes.",
                "Immediate professional help is recommended to manage your mental health.",
                "Mindfulness-based stress reduction (MBSR): Integrates mindfulness to reduce stress.",
                "Cognitive-behavioral therapy (CBT): Helps to identify and change negative thought patterns.",
                "Regular physical activity: Reduces stress hormones and promotes well-being.",
                "Healthy diet: Supports overall health and can improve mood and energy levels.",
                "Adequate sleep: Essential for physical and mental recovery.",
                "Social support: Engaging with friends and family can provide emotional support.",
                "Stress management techniques: Helps to manage and reduce stress levels.",
                "Limiting screen time: Reduces exposure to negative news and social media comparisons."
            ]
            symptoms_and_recommendations = "You might be experiencing significant stress or tiredness. Here are some recommendations:"
            # Concatenate the recommendation to consult a therapist at the end
        therapist_recommendation = "It's recommended to consult a therapist or proffesionals suggestion  before taking any action as this is just an online quiz and may not be fully accurate."
        recommendations.append(therapist_recommendation)

        return symptoms_and_recommendations, recommendations

if __name__ == '__main__':
    app.run(debug=True)