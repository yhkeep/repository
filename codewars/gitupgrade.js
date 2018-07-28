/*
function toBinary(decNumber) {
    var decStack = [];
    var rem;
    var decString = '';

    while (decNumber > 0) {
        rem = decNumber % 2;
        decStack.push(rem);
        decNumber = Math.floor(decNumber / 2);
    }

    while (decStack.length != 0) {
        decString += decStack.pop().toString();
    }
	//转为int类型
    return parseInt(decString);
}
console.log(toBinary(10)); //1010*/
function finalGrade (exam, projects) {
   if( exam>=90 || projects>=10){
       return 100;
   }else if (90>exam>=75 && 10>projects>=5) {
       return 90;
   }else if (90>exam>=50 && 5>projects>=2){
       return 75;
   }else{
       return 0;
   }
}
console.log(finalGrade(85, 5));
