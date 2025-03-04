//  console.log
// accessible from anywhere 
var i = "I am global Variable";	// Global Variable
			
function show(){
    var j = "I am Local Variable";	// Local Variable
    console.log(i);	// i accessible in function
    console.log(j);	// j accessible in function
    
}
show();

console.log(i);	// i accessible outside
console.log(j);	// j not accessible outside

function disp(){
    console.log(i);	// i accessible in function
    console.log(j);	// j not accessible in other function
}
disp();

if(true){
    console.log(i);	// accessible in block
    console.log(j);	// j not accessible in block
}










    











 