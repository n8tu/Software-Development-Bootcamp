// Recursion

// Base case(s)
// Forward movement

// return value or function call
// Call Stack
// Pass by value/reference

/* ******************************************************************************** */

/*
Recursively sum an arr of ints
*/

const nums0 = [1, 2, 3]
// const expected1 = 6
console.log(sumArr(nums0))
// add params if needed for recursion

function sumArr(nums) {
    if(nums.length == 0){
        return 0;
    }else{
        return nums.pop() + sumArr(nums);
    }
}

/* ******************************************************************************** */

/*
        Recursive Sigma
        
        Input: integer
        Output: sum of integers from 1 to Input integer
        
        */

const num1 = 5
// const expected1 = 15
// // Explanation: (1+2+3+4+5)

const num2 = 2.5
// const expected2 = 3
// // Explanation: (1+2)

const num3 = -1
// const expected3 = 0

console.log(recursiveSigma(num1),recursiveSigma(num2),recursiveSigma(num3))

function recursiveSigma(n) {
    if(n <= 0){
        return 0;
    }else{
        return Math.floor(n) + recursiveSigma(Math.floor(n)-1);
    }
}