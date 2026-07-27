// Exercise 11: Custom Implementations

// 1. myPush()
Array.prototype.myPush = function(element) {
  this[this.length] = element; // place element at next index
  return this.length;          // return new length (like push)
};

// 2. myPop()
Array.prototype.myPop = function() {
  if (this.length === 0) return undefined;
  const last = this[this.length - 1];
  this.length = this.length - 1; // shrink array
  return last;                   // return removed element
};

// 3. myMap()
Array.prototype.myMap = function(callback) {
  const result = [];
  for (let i = 0; i < this.length; i++) {
    result[i] = callback(this[i], i, this);
  }
  return result;
};

// 4. myForEach()
Array.prototype.myForEach = function(callback) {
  for (let i = 0; i < this.length; i++) {
    callback(this[i], i, this);
  }
};

// 5. myObjectKeys()
Object.myObjectKeys = function(obj) {
  const keys = [];
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      keys.push(key);
    }
  }
  return keys;
};

// ------------------ Testing ------------------

let arr = [1, 2, 3];

// myPush
arr.myPush(4);
console.log("After myPush:", arr);

// myPop
console.log("myPop:", arr.myPop());
console.log("After myPop:", arr);

// myMap
const doubled = arr.myMap(x => x * 2);
console.log("myMap (doubled):", doubled);

// myForEach
arr.myForEach((val, idx) => console.log(`Index ${idx}: ${val}`));

// myObjectKeys
const user = { name: "Rahul", age: 25, email: "rahul@example.com" };
console.log("myObjectKeys:", Object.myObjectKeys(user));
