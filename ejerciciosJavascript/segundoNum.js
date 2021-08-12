function secondLargesNumber(numbers){
    let first = numbers[0]
    let second = 0;
    for(let i=0; i < numbers.length; i++){
        if (numbers[i] > first){
            second = first;
            first = numbers[i];
        }
        if(numbers[i] > second && numbers[i] < first){
            second = numbers[i];
        }
    }

    return second;
    
}
let nums = [8, 9, 6, 7, 11];
console.log(secondLargesNumber(nums));
var segundo = secondLargesNumber(nums)
document.write("El segundo numero es:  <strong> " + segundo);