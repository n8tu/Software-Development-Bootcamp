function dismiss(ele){
    ele.parentNode.remove();
}

function changeTemperature(ele){
    
    var temp;
    var temperatures = document.querySelectorAll(".temperature-info .temperatures-container span");
    if(ele.value == "F"){
        for(var i = 0; i < temperatures.length; i++){
            temp = (parseInt(temperatures[i].innerText) * 1.8) + 32;
            temperatures[i].innerText = Math.round(temp) + "°";
        }
    }else{
        for(var i = 0; i < temperatures.length; i++){
            temp = (parseInt(temperatures[i].innerText) - 32) / 1.8;
            temperatures[i].innerText = Math.round(temp) + "°";
        }
    }
}
