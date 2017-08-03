import datetime as dt
from steemdata import SteemData
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

s = SteemData()
time_constraints = {
    '$gte': dt.datetime.now() - dt.timedelta(days=28)}

#GET steemit.com users filtered by interest 
@app.route('/steemians/<string:interest>')
def show_users(interest):

    steemians = list(s.Accounts.find({'json_metadata.profile.about': {'$regex': interest, '$options': "i"}, 'last_post': time_constraints},
      projection={'name': 1, '_id': 0, 'profile.location': 1, 'profile.about': 1, 'last_post': 1,'profile.profile_image': 1}))

    return jsonify({'steemians': steemians})

if __name__ == '__main__':
    app.run(debug=True)