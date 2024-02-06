/** product: calculate the product of an array of numbers. */

function product(nums, i=0) {
  if(i === nums.length) return 1;

  return nums[i] * product(nums, i + 1);
}
// console.log(product([2,2,2]));
/** longest: return the length of the longest word in an array of words. */

function longest(words, len = 0, i = 0) {
  if(i === words.length) return len;

  if(words[i].length > len) len = words[i].length;

  if(i !== words.length) return longest(words, len, i + 1);
}
// console.log(longest(["tiny","short","longest"]))
/** everyOther: return a string with every other letter. */

function everyOther(str, i = 0) {
  if(i >= str.length) return '';

  if(i % 2 === 0) {
    console.log(`Recursion ${i}: char = ${str[i]}, remainder = ${i % 2}`);
    return str[i] + everyOther(str, i+1);
  };

  return everyOther(str, i+1);
}
// console.log(everyOther("Hello"));
/** isPalindrome: checks whether a string is a palindrome or not. */

function isPalindrome(str, i = 0) {
  if(i === str.length) return true;

  if(str[i] !== str[str.length - (i + 1)]) return false;

  return isPalindrome(str, i+1);
}
// console.log(isPalindrome('racekar'));
/** findIndex: return the index of val in arr (or -1 if val is not present). */

function findIndex(arr, val, i = 0) {
  if(i === arr.length) return -1;

  if(arr[i] === val) return i;

  return findIndex(arr, val, i+1);
}
// console.log(findIndex([0,0,2,0], 1));
/** revString: return a copy of a string, but in reverse. */

function revString(str, i = 0) {
  if(i === str.length) return '';

  return revString(str, i+1) + str[i];
}

// console.log(revString('Caleb'));
/** gatherStrings: given an object, return an array of all of the string values. */

function gatherStrings(obj) {
  let strArr = [];

  Object.keys(obj).forEach(key => {
    if (typeof obj[key] === 'string') {
      strArr.push(obj[key]);
    } else if (typeof obj[key] === 'object') {
      strArr = strArr.concat(gatherStrings(obj[key]));
    }
  });

  return strArr;
}
// console.log(gatherStrings({width : 5, height : 6, catchphrase : "hello", words : {greeting : "yo", favorite: "love"}}));
/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */

function binarySearch(arr, val) {
  
}

module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch
};
