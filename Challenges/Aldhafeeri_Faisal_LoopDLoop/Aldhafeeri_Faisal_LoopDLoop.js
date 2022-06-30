// Q1: How do we know we need a loop here? 
// A1: we need the loop because we have to check the treadmill continuously.

// Q2: What's the starting point of the loop?
// A2: treadmill = 0 .

// Q3: When should the loop stop?
// A3: When the treadmill is equal to 6.

// Q4: How will it know to stop?
// Q5: if treadmill our conditional state is true which is treadmill == lastCandy.

// Q5: What's the incrementing for each iteration of the loop?
// A5: 1

// Q6: What variables do we need?
// A6: 3 , currDistance , i , maxDistance 



for(var treadmill = 0; treadmill < 6; treadmill++){
    if(treadmill % 2 == 0 && treadmill != 0){
        console.log('gifted a candy!');
    }
}

//Stretch Feature 1
var currSpeed = 5.6; // per hour , this variable for the Stretch Feature 1
for(var treadmill = 0; treadmill < 6; treadmill++){
    if((treadmill % 2 == 0 && treadmill != 0) && currSpeed > 5.5){
        console.log('gifted a candy!');
    }
}


