const numbers = [10, 20, 30, 40, 50];

const doubled = numbers.map(num => num * 2);
console.log("Doubled Numbers:", doubled);

numbers.shift();
console.log("After Removing First Element:", numbers);

numbers.unshift(5, 15);
console.log("After Adding 5 and 15:", numbers);

const index = numbers.indexOf(30);
if (index !== -1) {
  numbers.splice(index, 2, 100, 200); 
}
console.log("After Replacing 30 and 40:", numbers);
