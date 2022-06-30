function editProfile(id) {
    document.getElementById(id).innerText = prompt("Enter your new Name:");
}

function refuse(element){
    var card = element.parentNode.parentNode;
    var counter = document.getElementById("requestsCounter");
    counter.innerText = parseInt(counter.innerText) - 1;
    card.remove();
}

function accept(element){
    var card = element.parentNode.parentNode;

    var counter = document.getElementById("requestsCounter");
    counter.innerText = parseInt(counter.innerText) - 1;

    var counter2 = document.getElementById("connectionCounter");
    counter2.innerText = parseInt(counter2.innerText) + 1;
    
    var newConnection = card.querySelector("span");
    var connections = document.querySelector("#connection-list");
    card.remove();
    connections.innerHTML += ` <li class="card-list-item start">${newConnection.innerHTML} </li>`;
}