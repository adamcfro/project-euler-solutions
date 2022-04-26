/**
 * This function determines how many numbers are in a chain in a 
 * Collatz Sequence, and returns the count.
 * 
 * @param {Number} num - A number parameter
 * @returns {Number} - Returns a count of the numbers in the chain
 */
function lengthOfCollatzSequence (num) {
  let count = 1;
  while (num > 1) {
    if (num % 2 === 0) {
      num = num / 2;
    } else {
      num = num * 3 + 1;
    }
    count++;
  }
  return count;
}