from flask import Flask, jsonify, request
app = Flask(__name__)

unames = [{'name' : 'BlueWaters'}, {'name' : 'JCChin'}, {'name' : 'RecycleBin007'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works'})

@app.route('/unames', methods=['GET'])
def returnAll():
	return jsonify({'Usernames' : unames})

@app.route('/unames', methods=['POST'])
def addOne():
	Usernames = {'name' : request.json['name']}

	unames.append(Usernames)
	return jsonify({'Usernames' : unames})

@app.route('/unames/<string:name>', methods=['PUT'])
def editOne(name):
	Usernames = [usernames for usernames in unames if usernames['name'] == name]
	Usernames[0]['name'] = request.json['name']
	return jsonify({'name' : Usernames[0]})

@app.route('/unames/<string:name>', methods=['DELETE'])
def deleteOne(name):
	Username = [usernames for usernames in unames if usernames['name'] == name]
	unames.remove(Username[0])
	return jsonify({'Usernames': unames})

if __name__=='__main__':
	app.run(debug=True, port=8080)