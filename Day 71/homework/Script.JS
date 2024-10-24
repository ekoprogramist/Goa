let pi = Math.PI;
let sqrt = Math.sqrt(16);
let power = Math.pow(2, 3);
let ceiling = Math.ceil(4.2);
let floor = Math.floor(4.8);
let random = Math.random();
let abs = Math.abs(-5);
let max = Math.max(1, 2, 3, 4, 5); 
let min = Math.min(1, 2, 3, 4, 5); 
let trunc = Math.trunc(4.9);
function RandomInteger() {
    return Math.trunc(Math.random() * 100) + 1;
}
function CircleArea(radius) {
    return Math.PI * Math.pow(radius, 2);
}
console.log(CircleArea(5))