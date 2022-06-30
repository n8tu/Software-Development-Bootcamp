function zipArraysIntoMap(keys, values) {
  var map = {};
  for (var i = 0; i < values.length; i++) {
    map[keys[i]] = values[i];
  }
  return map;
}

/*****************************************************************************/

function invertObj(obj) {
  var newObj = {};
  var keys = Object.keys(obj);
  var values = Object.values(obj);
  for (var i = 0; i < keys.length; i++) {
    newObj[values[i]] = keys[i];
  }
  return newObj;
}






const obj1 = {
    name: "Zaphod",
    charm: "high",
    morals: "dicey",
};
const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
console.log(zipArraysIntoMap(keys1, vals1));
console.log(invertObj(obj1));
