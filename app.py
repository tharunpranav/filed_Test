from flask import Flask
from flask_restful import Api,Resource,request
from gateway import ProcessPayment

app=Flask(__name__)
api=Api(app)



api.add_resource(ProcessPayment,"/api/details")

@app.before_request
def checking_url():
    try:
        data=request.get_json()
    except:
        return "userdefind exception:Invalid input please enter input in given format"

app.run(port=5000)