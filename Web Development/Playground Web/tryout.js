list = []

var meric = {
  name: "Meriç Aşkın",
  age: 17,
  specialty: "speed",
  maths: 7 + 9,
  arraytest: list.push(5),
  muchmore: {
    favoritenumber: [7, 9],
    favoritemeal: "koka"
  },
};


console.log(meric);
console.log(meric.maths);
console.log(meric.arraytest);

var meruc = new Object();
meruc.name = "Meriççç Aşkın";
meruc.age = 18;

console.warn(meruc.name);
console.warn(meruc.age);
