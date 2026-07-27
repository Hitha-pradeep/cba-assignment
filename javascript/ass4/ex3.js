// Student Report System
const students = [
  { name: "Alice", marks: [80, 85, 90] },
  { name: "Bob", marks: [60, 70, 75] },
  { name: "Charlie", marks: [95, 92, 98] }
];

students.forEach(student => {
  const total = student.marks.reduce((sum, mark) => sum + mark, 0);
  student.average = total / student.marks.length;
});
console.log("Students with Averages:", students);

const topper = students.reduce((prev, curr) =>
  curr.average > prev.average ? curr : prev
);
console.log("Topper:", topper);

const above80 = students
  .filter(student => student.average > 80)
  .map(student => student.name);
console.log("Students with Average > 80:", above80);
