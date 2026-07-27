// Array Operations Without filter() or reduce()
const numbers = [12, 5, 8, 19, 22, 7, 30];
let largest = numbers[0];
let sum = 0;
let greaterThanTen = [];
for (let i = 0; i < numbers.length; i++) {
  let num = numbers[i];
  if (num === 22) {
    console.log("Encountered 22, stopping loop.");
    break;
  }
  if (num % 2 === 0) {
    console.log("Even:", num);
  }
  if (num > largest) {
    largest = num;
  }
    sum += num;
  if (num > 10) {
    greaterThanTen.push(num);
  }
}
console.log("Largest Number:", largest);
console.log("Sum of Numbers:", sum);
console.log("Numbers > 10:", greaterThanTen);
