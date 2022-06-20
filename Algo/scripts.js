/*
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted.
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
// const expected1 = false

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;

// const expected2 = true

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
// const expected3 = true

const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
// const expected4 = true

console.log(
    binarySearch(nums1, searchNum1),
    binarySearch(nums2, searchNum2),
    binarySearch(nums3, searchNum3),
    binarySearch(nums4, searchNum4)
);

function binarySearch(sortedNums, searchNum) {
    if (sortedNums.length == 0) {
        return false;
    }

    index = Math.floor(sortedNums.length / 2); // start from center
    previous = null;
    while (index > -1 && index < sortedNums.length) {
        
        if (sortedNums[index] == searchNum) {
            return true;

            // checking if searchNum are between previous and current value or no 
            // otherwise change previous and decrease index ;
        } else if (sortedNums[index] > searchNum) {
            if (previous < searchNum && previous != null) {
                return false;
            } else {
                previous = sortedNums[index];
                index--;
            }
            // checking if searchNum are between previous and current value or no 
            // otherwise change previous and increase index ;
        } else {
            if (previous > searchNum && previous != null) { 
                return false;
            } else {
                previous = sortedNums[index];
                index++;
            }
        }
    }
    return false;
}
