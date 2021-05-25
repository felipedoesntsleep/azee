let submitButton = document.getElementById("submit");
const Http = new XMLHttpRequest();
const HttpGet = new XMLHttpRequest();
const url='http://localhost:8080/';

let table = document.getElementById("table");

function updateTable(){
    console.log("update");
    HttpGet.open("GET", url + "games");
    HttpGet.send();
}
updateTable();

HttpGet.onreadystatechange = (e) => {
    console.log("here");

    // console.log(Http.response)
    // console.log(Http.responseText);  
    // table.remove();
    let response = HttpGet.responseText;
    response = response.slice(12, response.length-4);
    let split_ = response.split(")");
    console.log(split_);
    let games = [];
    for (let i = 0; i < split_.length-1; i++){
        // console.log(split_[i]);
        let short = split_[i].split("(")[1];
        console.log(short);
        let game = short.split(",");
        console.log(game);
        games.push(game);
        var row = table.insertRow(1);
        var cell0 = row.insertCell(0);
        var cell1 = row.insertCell(1);
        var cell2 = row.insertCell(2);
        var cell3 = row.insertCell(3);
        var cell4 = row.insertCell(4);
        var cell5 = row.insertCell(5);
        var link = document.createElement("a");
        console.log(game[6]);
        link.setAttribute("href", game[6]);
        // link.className = "someCSSclass";
        // For IE only, you can simply set the innerText of the node.
        // The below code, however, should work on all browsers.
        var linkText = document.createTextNode(game[0]);
        link.appendChild(linkText);

        // Add the link to the previously created TableCell.
        cell0.appendChild(link);
        // cell0.href = "https://azee.mattle.online/room/q82jgWtmZbAsM797W";
        // cell0.innerHTML = game[0];
        cell1.innerHTML = game[1];
        cell2.innerHTML = game[2];
        cell3.innerHTML = game[3];
        cell4.innerHTML = game[4];
        cell5.innerHTML = game[5];
    }
    for (let i = table.rows.length-1; i > games.length; i--){
        table.deleteRow(i);
    }
}

p1 = document.getElementById("p1");
p2 = document.getElementById("p2");
p3 = document.getElementById("p3");
p4 = document.getElementById("p4");
winner = document.getElementById("winner");
link = document.getElementById("link");

submitButton.addEventListener('click', function(){
    console.log(link.value);
    Http.open("POST", url + "game", false);
    Http.setRequestHeader('Content-Type', 'application/json');
    
    Http.send(JSON.stringify({
        "p1": p1.value, 
        "p2": p2.value, 
        "p3": p3.value, 
        "p4": p4.value, 
        "winner": winner.value, 
        "link": link.value
    }));
    updateTable();
});

let updateButton = document.getElementById("update");
updateButton.addEventListener('click', function(){
    updateTable();
});

// updateButton.addEventListener('click', async _ => {
//     try {     
//       const response = await fetch(url+"games", {
//         method: 'get',
//       });
//       console.log('Completed!', response);
//     } catch(err) {
//       console.error(`Error: ${err}`);
//     }
//   });

