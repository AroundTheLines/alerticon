from flask import Flask, request, redirect
import twilio.twiml
import wget
 
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
    resp.say("Hello, this is 9 1 1 emergency services but not actually")
 
    resp.say("Record your concern after the tone")
    resp.record(maxLength="5", action="/handle-recording")
 
    return str(resp)


@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""
 
    recording_url = request.values.get("RecordingUrl", None)
    print recording_url
    resp = twilio.twiml.Response()
    resp.say("Take a listen to what you voiced.")
    resp.play(recording_url)

    #We can curl the url here and force it into a temp.wav
    #Using "curl recording_url -o temp.wav -s"
    #Alternatively we can use Unix piping with
    #"curl -s recording_url | whatever_function_to_get_stuff_we_want that_functions_arguments"
    #more examples: http://www.compciv.org/recipes/cli/downloading-with-curl/
    resp.say("This howl was encoded somewhere")

    resp.say("Goodbye.")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)