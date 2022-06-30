//part 1
for(var i = 1; i <= 20; i++){
    if(i % 2 != 0){
        console.log(i);
    }
}

console.log("======== End of part 1 ========");

//part 2
for(var i = 100; i > -1; i--){
    if(i % 3 == 0){
        console.log(i);
    }
}

console.log("======== End of part 2 ========");

//part 3
for(var i = 4; i > -4; i -= 1.5){
    console.log(i);
}

console.log("======== End of part 3 ========");

//part 4
var sum = 0;
for(var i = 1; i <= 100; i++){
    sum += i;
}
console.log(sum);

console.log("======== End of part 4 ========");

//part 5 
sum = 1;
for(var i = 1; i <= 12; i++){
    sum *= i;
}
console.log(sum);

// console.log("======== End of part 5 ========");

