// Required specification to ride a rollercoaster.
var minmumheightInInches = 52;
var minmumAge = 10;

// Variables to determine the rider specifications , if higher than required specifion it will allow him to ride.
var height = 53; // rider height in inches.
var age = 12;


// Main required app.
function original(height){
    if(height >= minmumheightInInches){
        console.log("Get on that ride, kiddo!");
    }else{
        console.log("Sorry kiddo. Maybe next year.");
    }
}

// Features.
function stretchFeature1(height,age){
    if(height >= minmumheightInInches && age > minmumAge){
        console.log("Get on that ride, kiddo!");
    }else{
        console.log("Sorry kiddo. Maybe next year.");
    }
}

function stretchFeature2(height,age){
    if(height >= minmumheightInInches || age > minmumAge){
        console.log("Get on that ride, kiddo!");
    }else{
        console.log("Sorry kiddo. Maybe next year.");
    }
}

// Mains ( Lunchers ), choose the wanted function and uncomment it!.

original(height);
// stretchFeature1(height,age);
// stretchFeature2(height,age);





