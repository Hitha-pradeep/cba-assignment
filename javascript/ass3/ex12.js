// Difference Between slice() and splice()

let colors = ["Red", "Blue", "Green", "Yellow", "Pink"];

let slicedColors = colors.slice(1, 3); // from index 1 to 2

colors.splice(2, 2); // start at index 2, remove 2 elements

console.log("Sliced Array:", slicedColors);
console.log("Spliced Array:", colors);
