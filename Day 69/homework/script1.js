//Shift Element: Create an array and remove the first element using shift().
//Unshift Element: Add a new element at the beginning using unshift().
//Delete Element: Use the delete operator to remove the second element. Log the array and observe the result.
//Concatenate Arrays: Create two arrays and use concat() to merge them.
//Explore Unshift & Length: After using unshift(), log the new length of the array.
let arr = [1,2,3,4,5];
console.log(arr.shift());
console.log(arr.unshift(0));
console.log(arr.length);
delete arr.at(1);
console.log(arr);
let nums1 = [1,2];
let nums2 = [3,4,5,6,7];
console.log(nums1.concat(nums2));
