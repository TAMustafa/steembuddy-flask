from steemdata import SteemData
from flask import Flask, jsonify, request 

app = Flask(__name__)

s = SteemData()

#GET steemit.com users filtered by interest 
@app.route('/steemians/<string:interest>')
def show_users(interest):

    steemians = list(s.Accounts.find({'json_metadata.profile.about': {'$regex': interest, '$options': "i"}}, 
      projection={"name": 1, "_id": 0, "profile.location": 1, "profile.about": 1, "profile.profile_image": 1}))

    return jsonify({'steemians': steemians})

if __name__ == '__main__':
    app.run(debug=True)