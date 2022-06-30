function reverseString(str) {
    var word = "";
    for(var i = str.length-1; i >= 0 ; i--){
        word += str[i];
    }
    return word;
  }
  
  /*****************************************************************************/

  function acronymize(str) {
   
    var array = str.split(" ");
      var word = "";
      for(var i = 0; i < array.length; i++){
          if(array[i][0] == undefined){
              continue;
          }else{
              word += array[i][0];
          }
      }
      return word.toUpperCase();
  }
  
  /*****************************************************************************/
  
  function caseInsensitiveStringCompare(strA, strB) {
      return strA.toLowerCase() == strB.toLowerCase();
  }



var str1 = "creature"
var str2 = "dog";
console.log(reverseString(str1));
console.log(reverseString(str2));

console.log("=============================================");

str1 = " there's no free lunch - gotta pay yer way. ";
str2 = "Live from New York, it's Saturday Night!";
console.log(acronymize(str1));
console.log(acronymize(str2));

console.log("=============================================");


const strA1 = "ABC";
const strB1 = "abc";

const strA2 = "ABC";
const strB2 = "abd";

const strA3 = "ABC";
const strB3 = "bc";

console.log(caseInsensitiveStringCompare(strA1,strB1));
console.log(caseInsensitiveStringCompare(strA2,strB2));
console.log(caseInsensitiveStringCompare(strA3,strB3));
