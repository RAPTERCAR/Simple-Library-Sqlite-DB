window.onload=function(){
    //search item by title
    document.getElementById('search').addEventListener('click', function() {
        let title = document.getElementById('stitle').value;       
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
    //checkout item
    document.getElementById('checkout').addEventListener('click', function() {
        let title = document.getElementById('ptitle').value;       
        fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'request': "checkOutItem",
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
    document.getElementById('checked').addEventListener('click', function() {    
        fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'request': "myChecked",
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