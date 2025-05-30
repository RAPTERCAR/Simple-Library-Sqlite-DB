from flask import Flask, render_template, request, jsonify, redirect, session
from init import sys_init
from manage import login, User
from dbmanip import viewAllUsers, viewIdUser,addUser,addItem,searchItem,checkOut,browseItem, viewChecked
app = Flask(__name__)
app.secret_key = 'your_secret_key'#necessary to create a session with flask
#sets up database for further use
with app.app_context():
    sys_init()

# sets up login page for web app
@app.route('/')
def index():
    if request.args:
        return render_template('index.html', messages =request.args['messages'])
    else:
        return render_template('index.html', messages = '')
    
@app.route('/ajaxkeyvalue', methods=['POST'])
def ajax():
    data = request.json  # Assuming the AJAX request sends JSON data
    print(data)
    # Process the data
    username = data['username']
    password = data['password']

    print(username)
    print(password)


    user = login(username, password)
    if not user:
        response_data ={'status' : 'fail'}
    else:
        session['logged_in'] = True
        session['username'] = username
        session['user'] = {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'role': user.role,
        }

        response_data = {'status' :'ok', 'user': user.to_json()}


    return jsonify(response_data)

@app.route('/library')
def profile():

    user_data = session.get('user')

    if user_data:
        # Reconstruct the user object
        user = User(user_id=user_data['id'], username=user_data['username'],
                password_hash='', first_name=user_data['first_name'],
                last_name=user_data['last_name'], role=user_data['role'])

        print(user.role)
        if(user.role == "librarian"):
            return render_template('library.html', user_info=user)
        
        else:
            return render_template('patron.html', user_info=user)
        
    else:
        return redirect('/?messages=Please login again!')
    

@app.route('/data', methods=['POST','GET'])
def accessData():
    data = request.json #get data from libScript.js or patScript.js
    print("check")
    if data:
        #view all users
        if (data['request'] == 'allUsers'):
            temp = viewAllUsers()
            response = {'output' : temp}
            return jsonify(response)
        #view user by id
        if (data['request'] == 'idUsers'):
            tid = data['id']
            print(tid)
            temp = viewIdUser(tid)
            response = {'output' : temp}
            return jsonify(response)
        #add user
        if (data['request'] == 'addUser'):
            userN = data['username']
            password = data['password']
            fName = data['fName']
            lName = data['lName']
            role = data['role']
            temp = addUser(userN,password,fName,lName,role)
            response = {'output' : temp}
            return jsonify(response)
        #add item
        if (data['request'] == 'addItem'):
            title = data['title']
            format = data['format']
            author = data['author']
            temp = addItem(title,format,author)
            response = {'output' : temp}
            return jsonify(response)
        #search item
        if (data['request'] == 'searchItem'):
            title = data['title']
            temp = searchItem(title)
            response = {'output' : temp}
            return jsonify(response)
        #browse all items
        if (data['request'] == 'browseItem'):
            temp = browseItem()
            response = {'output' : temp}
            return jsonify(response)
        #check out items
        if (data['request'] == 'checkOutItem'):
            user_data = session.get('user')
            userID= user_data['id']
            print(userID)
            title = data['title']
            temp = checkOut(title,userID)
            response = {'output' : temp}
            return jsonify(response)
        #view items checked out by some user
        if (data['request'] == 'checkUsers'):
            tid = data['id']
            print(tid)
            temp = viewChecked(tid)
            response = {'output' : temp}
            return jsonify(response)
        #patron view of own items
        if (data['request'] == 'myChecked'):
            user_data = session.get('user')
            userID= user_data['id']
            print(userID)
            temp = viewChecked(userID)
            response = {'output' : temp}
            return jsonify(response)
            

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
