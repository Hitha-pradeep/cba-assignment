const operation = (a,b,op) => {
    switch(op){
        case '+':
            return a+b;
        case '-':
            return a-b;
        case '*':
            return a*b;
        case '/':
            return b!==0 ?a/b:"zero / error";
    }
}
console.log(operation(10,5,'+'));
console.log(operation(10,5,'-'));
console.log(operation(10,5,'*'));
console.log(operation(10,0,'/'));
console.log(operation(10,5,'/'));