from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    print("✅ Rendering index.html")
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message').lower()

    # Disease logic (symptom-based)
    if "fever" in user_message:
        response = (
            "🌡️ It sounds like you may have a fever.\n"
            "🔹 Rest well and stay hydrated.\n"
            "🔹 Take paracetamol if needed.\n"
            "📞 Visit a doctor if fever continues for more than 2 days."
        )
    elif "diarrhea" in user_message or "loose motion" in user_message:
        response = (
            "💧 It seems like you're experiencing diarrhea.\n"
            "🔹 Drink ORS or clean boiled water frequently.\n"
            "🔹 Avoid spicy and oily foods.\n"
            "🔹 Eat curd, rice, banana.\n"
            "📞 If symptoms persist, consult a health worker."
        )
    elif "cold" in user_message or "cough" in user_message:
        response = (
            "🤧 It looks like you have a cough or cold.\n"
            "🔹 Drink warm fluids (like ginger tea).\n"
            "🔹 Gargle with salt water.\n"
            "🔹 Avoid cold drinks and rest well.\n"
            "📞 If it lasts more than 3 days, see a doctor."
        )
    elif "malaria" in user_message or "mosquito" in user_message:
        response = (
            "🦟 Malaria is spread by mosquito bites.\n"
            "🔹 Sleep under mosquito nets.\n"
            "🔹 Use mosquito repellents and wear full clothes.\n"
            "🔹 Get a blood test if you have chills and fever.\n"
            "📞 Visit a health center immediately if positive."
        )
    elif "headache" in user_message:
        response = (
            "🧠 You seem to have a headache.\n"
            "🔹 Rest in a quiet, dark room.\n"
            "🔹 Drink water and avoid screen time.\n"
            "🔹 Avoid skipping meals.\n"
            "📞 If severe or regular, consult a doctor."
        )
    elif "stomach pain" in user_message or "abdominal pain" in user_message:
        response = (
            "🍽️ You may be having stomach pain.\n"
            "🔹 Avoid spicy or oily food.\n"
            "🔹 Drink warm water.\n"
            "🔹 Eat small and soft meals.\n"
            "📞 Visit a clinic if pain is severe or with vomiting."
        )
    elif "skin rash" in user_message or "itching" in user_message:
        response = (
            "🧴 It looks like you're having a skin problem.\n"
            "🔹 Keep the affected area clean and dry.\n"
            "🔹 Avoid scratching.\n"
            "🔹 Apply calamine lotion or mild antiseptic.\n"
            "📞 If rash spreads or burns, visit a health worker."
        )
    elif "vomiting" in user_message:
        response = (
            "🤢 Vomiting can cause dehydration.\n"
            "🔹 Sip ORS or electrolyte drinks slowly.\n"
            "🔹 Avoid solid food temporarily.\n"
            "🔹 Rest and avoid strong smells.\n"
            "📞 If vomiting continues or has blood, visit a doctor."
        )
    else:
        response = (
            "🤖 I'm here to help with common symptoms like fever, cough, diarrhea, headache, etc.\n"
            "Please describe your symptoms in simple words.\n"
            "Example: 'I have stomach pain' or 'fever and vomiting'."
        )

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
