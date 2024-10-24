//Get Length: Create an array with 5 items. Log the length of the array.
//Convert to String: Convert the same array to a string using toString() and log the result.
//Access Element: Use the at() method to access the second element and log it.
//Join Elements: Use join() to combine the array elements with - between them.
//Push & Pop: Add two new elements to the array using push(), then remove the last element using pop().
let arr = [1,2,3,4,5];
console.log(arr.length);
console.log(arr.toString());
console.log(arr.at(1));
console.log(arr.join("-"));
arr.push(8,9);
console.log(arr.pop);