//Find Index: Create an array with repeated values. Use indexOf() to find the first occurrence of an element.
//Find Last Index: Use lastIndexOf() to find the last occurrence of the same element.
//Check Inclusion: Use includes() to check if a specific element exists in the array.
//Invalid Index Search: Use indexOf() to search for a non-existing element. Log the result.
//Case Sensitivity: Check if includes() is case-sensitive by searching for different cases of the same string.
let arr = [1,1,2,2,3,4,4,5,5];
console.log(arr.indexOf(2));
console.log(arr.lastIndexOf(4));
console.log(arr.includes(2));
console.log(arr.indexOf(8));
let str = "hello"
console.log(str.includes("H"));