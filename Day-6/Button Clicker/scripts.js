function like(element){
    var text = element.innerText;
    var number = "";
    for(var i = 0; i < text.length; i++){
        if(!isNaN(text[i])){
            number += text[i];
        }else if(text[i] = " "){
            break;
        }else{
            continue;
        }
    }
    element.innerText = ++number + " " + "likes";
    alert("Ninja was liked");
}

function remove(element){
    element.remove();
}

function isLoggedIn(element){
    if(element.innerText == "Login"){
        element.innerText = "Logout";
    }else{
        element.innerText = "Login"
    }
}

