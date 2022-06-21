/*
    Array: Remove Duplicates
    Given a SORTED array of integers, dedupe the array
    Because array elements are already in order, all duplicate values will be grouped together.
    Ok to use a new array
    Bonus: do it in O(n) time (no nested loops, new array ok)
    Bonus: Do it in-place (no new array)
*/

// const nums1 = [1, 1, 1, 1]

// console.log(removeDuplicates(nums1))
// const nums2 = [1, 1, 2, 2, 3, 3]

// console.log(removeDuplicates(nums2))
// const nums3 = [1, 1, 2, 3, 3, 4]
// console.log(removeDuplicates(nums3))

// function removeDuplicates(nums) {
//     var array = []
//     for(var i = 0; i < nums.length; i++){
//         if (!array.includes(nums[i])){
//             array.push(nums[i])
//         }
//     }
//     return array;
// }

function removeDuplicates(nums) {
    if(nums.length == 0){
        return [];
    }
    var lastElement = nums[0];
    for(var i = 1; i < nums.length; i++){
        if(nums[i] == lastElement){
            nums.splice(i,1);
            i--;
        }else{
            lastElement = nums[i]
        }
    }
    return nums
}

/*****************************************************************************/

/*
    Array: Mode
    Create a function that, given an array of ints,
    returns the int that occurs most frequently in the array.
    What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
    - return empty array
*/

const nums1 = [];
// const expected1 = [];

const nums2 = [1];
// const expected2 = [1];

const nums3 = [5, 1, 4];
// const expected3 = [];

const nums4 = [5, 1, 4, 1];
// const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
// const expected5 = [5, 1];
//  - order doesn't matter

// const nums6 = [5, 1, 4, 1, 5, 4];
// const expected6 = [];

console.log(mode(nums5))


function mode(nums) {
    var obj = {};
    var array = []
    for(var i = 0; i < nums.length; i++){
        if(obj[nums[i]] == undefined){
            obj[nums[i]] = 1;
        }else{
            obj[nums[i]] += 1;
        }
    }

    return obj
    //not completed