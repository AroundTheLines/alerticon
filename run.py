from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

#Try adding your own number to this list!
callers = {
	"+14158675309": "Curious George",
	"+14167006502": "Qile",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	#Respond to incoming calls with a simple text message.

	from_number = request.values.get('From',None)
	if from_number in callers:
		message = callers[from_number] + ", thanks for the message!"
	else:
		message = "Monkey, thanks for the message!"

	resp = twilio.twiml.Response()
	resp.message(message)

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)