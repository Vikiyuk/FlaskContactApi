from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Welcome to My Flask App</title>
<style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                text-align: center;
                background-color: #fff;
                padding: 40px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 10px;
                color: #3498db;
            }
            p {
                font-size: 1.2em;
                margin-bottom: 20px;
            }
            a {
                display: inline-block;
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            a:hover {
                background-color: #2980b9;
            }
</style>
</head>
<body>
<div class="container">
<h1>Welcome to My Flask App</h1>
<p>This is a simple Flask web application with beautiful HTML content!</p>
<a href="https://flask.palletsprojects.com/">Learn more about Flask</a>
</div>
</body>
</html>
    '''
@app.route('/describe')
def get_description():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Flask API Description</title>
<style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                max-width: 800px;
                background-color: #fff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #4CAF50;
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2em;
                color: #555;
                margin-bottom: 20px;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                background-color: #3498db;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 5px;
            }
            a {
                color: white;
                text-decoration: none;
                font-weight: bold;
                transition: color 0.3s ease;
            }
            a:hover {
                color: #ffeb3b;
            }
            code {
                background-color: #f4f4f4;
                padding: 4px 6px;
                border-radius: 4px;
                font-size: 1.1em;
            }
</style>
</head>
<body>
<div class="container">
<h1>Flask API</h1>
<p>
                This app supports the endpoint listed below. You can change the data being sent to the API by updating the URI.
</p>
<p>The four request methods we will use are <strong>GET, POST, PUT,</strong> and <strong>DELETE</strong>. GET requests can be used in a browser. The other methods can be used via CURL or another API platform, such as Postman or Thunder Client in VS Code.</p>
<ul>
<li><a href='
http://127.0.0.1:5000/describe'>GET
This Page</a></li>
<li><a href='
http://127.0.0.1:5000/username/1'>GET
a username from ID</a></li>
<li><a href='
http://127.0.0.1:5000/users/'>GET
all user info</a></li>
</ul>
<p>The endpoints below can be accessed over CURL using the correct request method:</p>
<ul>
<li><code>curl -X POST '
http://127.0.0.1:5000/new_user/Georgina/'</code>
# POST a new user</li>
<li><code>curl -X PUT '
http://127.0.0.1:5000/update_username/1/Hazel/'</code>
# PUT updates</li>
<li><code>curl -X DELETE '
http://127.0.0.1:5000/delete_user/1/'</code>
# DELETE a user by ID</li>
</ul>
</div>
</body>
</html>
    """

# users_database = {
#     1: "Alice",
#     2: "Rachel",
#     3: "Joe"
# }
#
# @app.route("/username/<int:id>/", methods=['GET']) # notice the id is captured from the URI
# def get_username(id):
#     if id in users_database:
#         return {"username": users_database[id]}
#     else:
#         return {"error":"User not found."}
#
# @app.route("/users/", methods=['GET'])
# def get_users():
#     return users_database
#
# @app.route("/new_user/<string:username>/", methods=['POST'])
# def new_user(username):
#     if username in users_database.values():
#         return {"error": "That username already exists. Please use a different one."}
#     else:
#         new_id = len(users_database) + 1
#         users_database[new_id] = username
#         return {
#             "new_user_report": {
#                 "ID": new_id,
#                 "username": username
#             }
#         }
#
# #update an existing record
# @app.route("/update_username/<int:id>/<string:new_username>/", methods=['PUT'])
# def update_username(id, new_username):
#     if id in users_database:
#         old_name = users_database[id]
#         users_database[id] = new_username
#         return {
#             "update_report": {
#                 "ID": id,
#                 "old_username": old_name,
#                 "new_username": new_username
#             }
#         }
#     else:
#         return {"error": "Cannot update a non-existent user."}
#
# # delete an existing record
# @app.route("/delete_user/<int:id>/", methods=['DELETE'])
# def delete_user(id):
#     if id in users_database:
#         deleted_username = users_database[id]
#         del users_database[id]
#         return {
#             "delete_user_report": {
#                 "ID": id,
#                 "username": deleted_username
#             }
#         }
#     else:
#         return {"error": "Cannot delete: user not found."}
master = {}
current_id = 1
def searchContact(phonenum):
    for contact in master.values():
        if contact["phone"] == phonenum:
            return True
    return False

@app.route('/contacts', methods=['GET'])
def display_contacts():
    return jsonify(master), 200


@app.route('/create_contact', methods=['POST'])
def create_contact():
    global current_id
    name = request.args.get('name')
    phone = request.args.get('phone')
    if searchContact(phone):
        return jsonify({"error": "Contact already exists"}), 400
    master[current_id] = {
        "name": name.upper(),
        "phone": phone
    }
    current_id += 1
    return jsonify({"message": "New record crated:", "contact": master[current_id - 1]}), 201


@app.route('/delete_contact/<int:id>', methods=['DELETE'])
def delete_contact(id):
    if id not in master:
        return jsonify({"error": "The contact you are searching for does not exist"}), 404

    deleted_contact = master.pop(id)
    return jsonify({"message": "Deleting:", "contact": deleted_contact}), 200


@app.route('/update_contact/<int:id>', methods=['PUT'])
def update_contact(id):
    if id not in master:
        return jsonify({"error": "The contact does not exist"}), 404
    name = request.args.get('name')
    phone = request.args.get('phone')
    if name:
        master[id]["name"] = name
    if phone:
        master[id]["phone"] = phone
    return jsonify({"message": "Updated:", "contact": master[id]}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)