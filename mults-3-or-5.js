/**
 * Returns the sum of all the multiples of 3 or 5 below 'num'.
 * 
 * @param {Number} num - A number parameter
 * @returns {Number} - Returns a sum
 */
function multiples (num) {
  let sum = 0;
  for (let i = 0; i < num; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      sum += i;
    }
  }
  return sum;
}