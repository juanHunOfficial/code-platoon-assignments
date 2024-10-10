// let romanChars = ["I", "V", "X", "L", "C", "D", "M"];
// let romanValues = [1,   5,  10,  50,  100, 500, 1000]; references for now------------

function toRomanLazy(romanNum){
    let sum = 0
    for(let i = 0; i < romanNum.length; i++){
        switch(romanNum.charAt(i)){
            case "I":
                sum += 1
                break;
            case "V":
                sum += 5
                break;
            case "X":
                sum += 10
                break;
            case "L":
                sum += 50
                break;
            case "C":
                sum += 100
                break;
            case "D":
                sum += 500
                break;
            case "M":
                sum += 1000
                break;
        }
    }
    return sum;
}

function toRomanModern(romanNum){
    let objectOfRomanValues = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    };
    let modernSum = 0;
    for(let i = 0; i < romanNum.length; i++){
        console.log(`current value is roman num = ${romanNum.charAt(i)} and sum = ${modernSum}`)
        if (i !== romanNum.length -1){
            if(romanNum.charAt(i) === "I" && romanNum.charAt(i +1) === "V"){
                modernSum += 4;
            }else if (romanNum.charAt(i) === "I" && romanNum.charAt(i +1) === "X"){
                modernSum += 9;
            }else if (romanNum.charAt(i) === "X" && romanNum.charAt(i +1) === "L"){
                modernSum += 40;
            }else if (romanNum.charAt(i) === "C" && romanNum.charAt(i +1) === "D"){
                modernSum += 400;
            }else if (romanNum.charAt(i) === "C" && romanNum.charAt(i +1) === "M"){
                modernSum += 900;
            }else{
                modernSum += objectOfRomanValues[romanNum.charAt(i)]
            }
            if((i + 1) === romanNum.length){
                return modernSum
            }
        }else{
            console.log(`entered on index = ${romanNum.charAt(i)} and sum = ${modernSum}`)
            modernSum += objectOfRomanValues[romanNum.charAt(i)]
        }
        
    }

    return modernSum;
}

console.log(toRomanLazy("XVIIII")); //correct due to lazy formatting and no special squencing
console.log(toRomanModern("XIV")); //14

//------------------left off here---------------getting extra value unwanted from the 
//addition of the last index in line 66