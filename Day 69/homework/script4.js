//Sort and Push: Create an array of numbers, sort it, and add a new number using push(). Log the updated array.
//Concatenate and Sort: Create two arrays, merge them with concat(), and sort the result.
//Push and Reverse: Add three new elements to an array, then reverse the entire array.
//Find and Remove Element: Use indexOf() to locate an element, then use splice() to remove it.
//Join and Include Check: Join the elements of an array into a string, split it back into an array, and check if a specific value is included using includes().
let arr = [7,5,6,8,9,3];
arr.sort();
arr.push(5);
console.log(arr);
let nums1 = [1,2];
let nums2 = [8,6,1,2,1];
console.log(nums1.concat(nums2).sort());
let arr1 = [1,2,3,4,5,9,8];
arr1.push(2,9,7);
console.log(arr1.reverse());
arr1.splice(arr1.indexOf(2), 1)
console.log(arr1);
let array = ['apple', 'banana', 'cherry'];

const joinedString = array.join('');

const splitArray = joinedString.split('');

const word = 'banana';
const included = splitArray.includes(word);
console.log(splitArray.includes(word));