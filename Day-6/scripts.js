function concat(arr1, arr2) {
    var newArray = arr1.slice();
    for(var i = 0; i < arr2.length; i++){
        newArray[newArray.length] = arr2[i];
    }
    return newArray;
}

function concatArrWithSelf(arr) {
    var limit = arr.length;
    var newArray = arr.slice();
    for(var i = 0; i < limit; i++){
        newArray[newArray.length] = arr[i];
    }
    return newArray;
}


// const arrA1 = ["a", "b"];
// const arrB1 = [1, 2, 3];
// console.log(concat(arrA1,arrB1));

console.log("=========== End of first part ===========");
console.log();

const arr1 = ["a", "b", "c"];
console.log("new Array => " , concatArrWithSelf(arr1));
console.log("Original Array => " , arr1);

