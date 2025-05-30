window.onload=function(){
    //librarian functions
    //view all users
    document.getElementById('allU').addEventListener('click', function() {
        console.log("test");
        fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'request': "allUsers"
                                }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('test');
            document.getElementById('output').innerHTML = data.output;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    //view user by id
    document.getElementById('sID').addEventListener('click', function() {
        let id = document.getElementById('idU').value;
        console.log(id);
        fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'request': "idUsers",
            'id': id
                                }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('test');
            document.getElementById('output').innerHTML = data.output;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    //add user
    document.getElementById('addU').addEventListener('click', function() {
        let userN = document.getElementById('username').value;
        let pass = document.getElementById('password').value;
        let fName = document.getElementById('fName').value;
        let lName = document.getElementById('lName').value;
        let role = document.getElementById('role').value;
        
        //console.log(id);
        fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'request': "addUser",
            'username': userN,
            'password': pass,
            'fName': fName,
            'lName': lName,
            'role': role
                                }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('test');
            document.getElementById('output').innerHTML = data.output;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    //add items
    document.getElementById('addI').addEventListener('click', function() {
        let title = document.getElementById('title').value;
        let format = document.getElementById('format').value;
        let author = document.getElementById('author').value;
        
        //console.log(id);
        fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'request': "addItem",
            'title': title,
            'format': format,
            'author': author,
                                }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('test');
            document.getElementById('output').innerHTML = data.output;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    //search item by title
    document.getElementById('search').addEventListener('click', function() {
        let title = document.getElementById('stitle').value;       
        //console.log(id);
        fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'request': "searchItem",
            'title': title,
                                }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('test');
            document.getElementById('output').innerHTML = data.output;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    //view all items
    document.getElementById('browse').addEventListener('click', function() {    
        fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'request': "browseItem",
                                }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('test');
            document.getElementById('output').innerHTML = data.output;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    //view items checked out by a user
    document.getElementById('cID').addEventListener('click', function() {
        let id = document.getElementById('cidU').value;
        console.log(id);
        fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'request': "checkUsers",
            'id': id
                                }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('test');
            document.getElementById('output').innerHTML = data.output;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

}