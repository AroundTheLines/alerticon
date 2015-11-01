from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    from_number = request.values.get('From', None)
    if from_number in callers:
        caller = callers[from_number]
    else:
        caller = "Monkey"
 
    resp = twilio.twiml.Response()
    # Greet the caller by name
    resp.say("Hello " + caller)
    # Play an mp3
    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
 
    resp.say("Record your monkey howl after the tone.")
    resp.record(maxLength="10", action="/handle-recording")
 
    return str(resp)


@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""
 
    recording_url = request.values.get("RecordingUrl", None)
    resp = twilio.twiml.Response()
    resp.say("Thanks for howling... take a listen to what you howled.")
    resp.play(recording_url)
    resp.say("This howl was encoded at the url: " + recording_url)
    resp.say("Goodbye.")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)