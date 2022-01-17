function narcissistic(value) {
//create results array
// split up value into array or iterate through string
  let splitUp = value.toString().split('');
  console.log(splitUp);
  let lengthy = splitUp.length;
  let basedSum = 0;
  if (lengthy === 1) {
    return true;
  }
  for (i=0;i<lengthy;i++) {
    let digit = Number(splitUp[i]);
    let basedNum=Math.pow(digit, lengthy);    
    basedSum+=basedNum;
    console.log(basedSum);
  }
  return basedSum===Number(value);
}
