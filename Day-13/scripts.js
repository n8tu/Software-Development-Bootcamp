const str1 = "a x a" // const expected1 = true
const str2 = "racecar" // const expected2 = true
const str3 = "Dud" // const expected3 = false
const str4 = "oho!" // const expected4 = false

console.log(isPalindrome(str1));
console.log(isPalindrome(str2));
console.log(isPalindrome(str3));
console.log(isPalindrome(str4));



function isPalindrome(str) {
    word = "";
    for(var i = str.length-1; i > -1; i--){
        word += str[i];
    }
    return word == str;
}