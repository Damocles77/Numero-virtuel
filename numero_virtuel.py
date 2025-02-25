print("Le script commence ")
# Numéro virtuel type Onnof façon là 
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

# 📩 Route pour recevoir les SMS
@app.route("/sms", methods=["POST"])
def recevoir_sms():
    from_number = request.form["From"]
    message_body = request.form["Body"]

    print(f"📩 SMS reçu de {from_number} : {message_body}")

    # Réponse automatique à l'expéditeur
    response = MessagingResponse()
    response.message("Merci pour ton message ! On te répondra bientôt.")
    return str(response)

# 📞 Route pour gérer les appels entrants
@app.route("/appel", methods=["POST"])
def recevoir_appel():
    response = VoiceResponse()
    response.say("Bonjour, ceci est un test d'appel depuis votre numéro virtuel.", voice="alice")
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    print("Le script est terminé ")