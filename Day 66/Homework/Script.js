num = 4;
if(num % 2 === 0){
    console.log("even")
}
else{
    console.log("odd")
}
list = [1, 2, 3]
let sum = 0;
if (list.length === 0){
    console.log("list is empty")
}
else{
    for (let i = 0; i < list.length; i++) {
        sum += list[i];
    }
    console.log(sum);
}
function Multiply(numbers) {
    const result = [];

    for (let i = 0; i < numbers.length; i++) {
        const multiplied = numbers[i] * 3;

        if (multiplied > 20) {
            result.push(multiplied);
        }
    }

    return result;
}

const numbers = [1, 2, 4, 10, 6];
const result = Multiply(numbers);
console.log(result);
let numbers = [3, 5, 7, 2, 8];
let maxNum = numbers[0];

    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > maxNum) {
            maxNum = numbers[i];
        }
    }

console.log(maxNum);