function like(id){
    var element = document.querySelector("."+id);
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
    element.innerText = ++number + " " + "like(s)";
}

function jump(element){
    element.classList.add("jump");
}

function unjump(element){
    element.classList.remove("jump");
}