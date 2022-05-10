/**
 * This function generates triangle numbers, which are created by adding the 
 * natural terms in sequence (The third triangle number would be 6:
 * 1 + 2 + 3 = 6). Takes in a parameter that checks for a triangle number
 * with that many divisors. Returns the triangle number.
 * 
 * @param {Number} numDivisors - The number of divisors that the target
 * triangle number has
 * @returns {Number/String} - Returns the triangle number with n number of
 * divisors
 */
function triangularNumber (n) {
  let triangleNumber = 1;
  let j = 2;
  let divisors = 0;
  while (divisors < n) {
    for (let i = 0; i <= triangleNumber; i++) {
      if (triangleNumber % i === 0) {
        divisors++;
      }
      if (divisors === n) {
        return triangleNumber;
      }
    }
    divisors = 0;
    triangleNumber += j;
    j++;
  }
  return triangleNumber;
}