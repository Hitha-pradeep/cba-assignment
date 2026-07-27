// Total Marks Using forEach()
const marks = [75, 82, 91, 68, 88];
let total = 0;
marks.forEach(mark => {
  total += mark;
});

let average = total / marks.length;
console.log("Total Marks:", total);
console.log("Average Marks:", average.toFixed(2));
