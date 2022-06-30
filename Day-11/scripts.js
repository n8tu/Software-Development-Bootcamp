/*
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  No trailing separator at the end
  Bonus: Default the separator to a comma with a space after it if no separator is provided
*/

// const arr1 = [1, 2, 3]
// const separator1 = ", "
// console.log(join(arr1,separator1));
// const expected1 = "1, 2, 3"

// const arr2 = [1, 2, 3]
// const separator2 = "-"
// const expected2 = "1-2-3"
// console.log(join(arr2,separator2));

// const arr3 = [1, 2, 3]
// const separator3 = " - "
// const expected3 = "1 - 2 - 3"
// console.log(join(arr3,separator3));

// const arr4 = [1]
// const separator4 = ", "
// console.log(join(arr4,separator4))
// const expected4 = "1"

// const arr5 = []
// const separator5 = ", "
// console.log(join(arr5,separator5))
// const expected5 = ""

// const arr6 = [1, 2, 3]
// separator is not given
// console.log(join(arr6))
// const expected 6 = "1, 2, 3"
function join(arr, separator = ",") {
  if (arr.length == 0) {
    return "";
  }
  var word = "";
  for (var i = 0; i < arr.length - 1; i++) {
    word += arr[i] + separator;
  }
  word += arr[arr.length - 1];
  return word;
}
/*****************************************************************************/

/*
      Book Index
    
      Given an array of ints representing page numbers
      return a string with the page numbers formatted as page ranges when the nums span a consecutive range
    */

const nums1 = [1, 13, 14, 15, 16, 17, 18, 37, 38, 70, 71];
console.log(bookIndex(nums1));
// const expected1 = "1, 13-15, 37-38, 70";

function bookIndex(pageNums) {
  var newArray = [];
  var seris = false;
  for (var i = 0; i < pageNums.length; i++) {
    if (pageNums[i + 1] == pageNums[i] + 1) {
      seris = true;
      if (seris) {
        for (var j = i + 1; j < pageNums.length; j++) {
          if (pageNums[j + 1] == pageNums[j] + 1) {
            continue;
          } else {
            newArray.push(pageNums[i] + "-" + pageNums[j]);
            seris = false;
            i = j;
            break;
          }
        }
      }
    } else {
      newArray.push(pageNums[i]);
    }
  }
  return newArray;
}
