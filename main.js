// Excercise 1


let dog_string = "Hello Max, my name is Dog, and I have purple eyes!"
let dog_names = ["Max","HAS","PuRple","dog"]

function findWords(string, arr){
    for (let i of arr) {
        if (string.includes(i)) {
            console.log(i)
        }else {
            console.log('No Matches')
        }
    }
}

console.log(findWords(dog_string, dog_names));


// Exercise 2

function replaceEvens(arr){
    for (let i = 0; i < arr.length; i++) {
        if (i % 2 == 0){
            arr.splice(i, 1, 'even index')
        }
    }
    return arr;
}

let givenArr = ["Max","Baseball","Reboot","Goku","Trucks","Rodger"]

console.log(replaceEvens(givenArr));



/**Codewars 1
'Remove First and Last Character'
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.*/

function removeChar(str) {
  var new_str = str.slice(1, str.length - 1);
  return new_str;
}

console.log(removeChar('abcdefg'));


/**Codewars 2
'Find out whether the shape is a cube'

To find the volume (centimeters cubed) of a cuboid you use the formula:
volume = Length * Width * Height

But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side!

It's up to you to find out whether the cuboid has equal sides (= is a cube).

Return true if the cuboid could have equal sides, return false otherwise.

Return false for invalid numbers too (e.g volume or side is less than or equal to 0).

Note: side will be an integer
*/

function cubeChecker(volume, side) {
  if (volume <= 0 || side <= 0) {
    return false;
  }
  const possibleSideLength = Math.cbrt(volume);
  return possibleSideLength === side;
}

cubeChecker(27); // Output: true

















