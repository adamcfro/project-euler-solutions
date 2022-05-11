/**
 * This function takes the factorial of a number, then adds up all the digits
 * from the factorial and returns their sum.
 * 
 * @param {Number} num - A number parameter
 * @returns {Number} - Returns a sum
 */
function factorialDigitSum (num) {
  let factorialSum = num > 0 ? 1 : 0;
  for (let i = 1; i <= num; i++) {
    factorialSum *= i;
  }
  let digitSum = 0;
  let numArr = factorialSum.toString().split('');
  for (let i = 0; i < numArr.length; i++) {
    digitSum += parseInt(numArr[i]);
  }
  return digitSum;
}