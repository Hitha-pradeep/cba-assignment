// Stop at First Negative 

const numbers = [10, 25, 18, -4, 30, 50];
for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] < 0) {
    console.log("Encountered negative number:", numbers[i]);
    break; // stop the loop immediately
  }
  console.log(numbers[i]);
}
