setInterval(function() {
    var seconds = new Date().getSeconds();
    var minutes = new Date().getMinutes()
    var hours = new Date().getHours();

    document.getElementById("hour").style.transform = `rotate(${(hours+3)*30}deg)`;
    document.getElementById("minutes").style.transform = `rotate(${(minutes+30)*6}deg`;
    document.getElementById("seconds").style.transform = `rotate(${(seconds+30)*6}deg`;
}, 1000);