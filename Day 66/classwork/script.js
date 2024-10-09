// const input_name = prompt('Enter your age:');

// if (input_name >= 18) {
//     alert('you are adult');
// }

// else {
//     alert('you are kid');
// }

// console.log(input_name);


//Task 2


let list = [];
for (let i = 1; i <= 30; i++) {
  list.push(i);
}


let evenNumbers = [];
for (let i = 0; i < list.length; i++) {
  if (list[i] % 2 === 0) {
    evenNumbers.push(list[i]);
  }
}


console.log("1-დან 30-მდე რიცხვები:", list);
console.log("ლუწი რიცხვები:", evenNumbers);
