from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14167006502": "Qile",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    # Get the caller's phone number from the incoming Twilio request
    from_number = request.values.get('From', None)
    
 
    # if the caller is someone we know:
    if from_number in callers:
        # Greet the caller by name
        caller = callers[from_number]
    else:
        caller = "Monkey"

 		resp = twilio.twiml.Response()
 		resp.say("Hello " + caller)
 		resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)