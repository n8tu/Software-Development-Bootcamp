function review(element){
    if(element.src.includes("assets/succulents-1.jpg")){
        element.src = "assets/succulents-2.jpg";
    }else{
        element.src = "assets/succulents-1.jpg"
    }
}

function hide(element){
    element.parentNode.remove();
}