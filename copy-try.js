
// switch cse code in js


var day = "mon";
		switch(day){
			case "mon":
			case "Mon":
			console.log("Working Day");
			break;
			case "Sat":
			case "Sun":
            console.log("Holiday");
			break;
			default:
            console.log("Wrong");
		}

// Addition code of three numbers 

var a  = 10
var b = 20
var c = 30
console.log(a+b+c) 


var result = 70;
		if(result <= 30)
		console.log("Fail");
		else if (result <= 40 )
        console.log("Pass");
		else if (result <= 60)
        console.log("Good");
		else
		console.log("Very Good");


//  loop code in js 
//  example 1

for(i=0; i<5; i++)
    {
        console.log(i);
        
    }

    //  example 2

var i = 0;
for(; i<5; i++)
{
    console.log(i);
}


//  example 3

var i = 0;
		for(; i<5;)
		{
			console.log(i);
			i++;
			
		}

//  example 4

var i = 0;
		for(; ; i++)
		{
			if(i==3)
			{
				break;
			}
			console.log(i);
		}

//  example 5


var i = 0;
		while(i<5)
		{
			console.log(i);
			i++;
			
		}

//  example 6

var i = 0;
		while(true)
		{
			if(i==3)
			{
				break;
			}
			console.log(i);
			i++;
			
		}


//  example 7

var i = 0;
		do 
		{
			console.log(i);
			i++;
			
		} 
        while(i<5);


//  example 8

var i = 0;
		do 
		{
			if(i==3)
			{
				break;
			}
			console.log(i); 
			i++;
			
		} 
        while(true);


//  example 9


for(i=1; i<=10; i++)
    {
        if(i==8)
        {
            break;	// stop loop
        }
        console.log(i);
       
    }


//  example 10


for(i=1; i<=10; i++)
    {
        if(i==8)
        {
            continue;	// skip loop
        }
       console.log(i);
        
    }


    // example 11

for(i=0; i<3; i++)
    {
        console.log("<strong>Outer Loop </strong>");
        console.log(i);
        for(j=0; j<5; j++)
        {
            console.log("Inner Loop ");
            console.log(j);
        }
    }


    // function example 1

function add()
{
    var a = 1;
    var b = 2;
    return a + b;
}
console.log(add());


// function example 2

function add(a,b){
    return a+b;
}
a = add(23,45)
console.log(a);


// function example 3

// Default Parameter
			// Array
			function add(num, a=["Geeky", "Shows"]){
				console.log("A0= " + a[0] );
				console.log("A1= " + a[1] );
				console.log("Num= " + num );
			}
			add(20, [10, 40]);
			add(20);
			add();   // hare functio are calling three times with different parameter



// function example 4


function display(name)
			{
				console.log(name);
				console.log(arguments[0]);
			}
display("GeekyShows");


// function example 5

function display(name1, name2)
			{
				//document.write(name1, name2);
				console.log(arguments[0] + " " + arguments[1]);
			}
display("GeekyShows", "World");


// function example 6

function display(name1, name2)
			{
				arguments[0] = "Hello";
				console.log(arguments[0] + " " + arguments[1]);
			}
			display("GeekyShows", "World");


// function example 7

function display(name1 , name2)
{
    console.log(arguments.length);
}
display("GeekyShows", "Hello", "World");


// function example 8

function display()
			{
				console.log(arguments.length);
			}
display("GeekyShows", "Hello", "World");


// function example 9


function display(name1, name2)
			{
				for(var i = 0; i<arguments.length; i++)
				{
					console.log(arguments[i] + " ");
				}
			}
display("GeekyShows", "World");



// function example 10

function display()
			{
				arguments[0] = "Hello";
				for(var i = 0; i<arguments.length; i++)
				{
					console.log(arguments[i] + " ");
				}
			}
display("GeekyShows", "World");



// function example 11

// Rest Parameters
function show(...args){
    console.log(args);
}
show(10,20,30,40,50,89,56,43);


// function example 12


// Rest Parameters one
function show(a, ...args){
    console.log(a);
    console.log(args);
}
show(10,20,30,40,50);


// function example 13


// Rest Parameters 2
function show(a, ...args){
    console.log(a);
    console.log(args[0] + " " + args[1] + " " + args[2]);
}
show(10,20,30,40,50);


// function example 14

// Rest Parameters vs arguments parameter
function restShow(...args){
    console.log(args);
}
restShow(10,20,30,40,50);

// Arguments Object
function show(){
    console.log(arguments);
}
show(10,20,30,40,50);


// function example 15

// Rest Parameters
function restShow(a, ...args){
    console.log("a: " + a);
    console.log(args);
}
restShow(10,20,30,40,50);

// Arguments Object
function show(a){
    console.log("a: " + a);
    console.log(arguments);
}
show(10,20,30,40,50);



// function example 16

function add(a, b){
    return (a+b);
}
console.log(add(10, 20));


// function example 17 block scope



if(true){
    var i = 10;	// accesssible from anywhere
    console.log(i );
}
// in other programming i is not accessible outside block
// but in javascript it is accessible
console.log(i);	// i accessible outside block

if(true){
    let j = 10;	// only accessible within block
    console.log(j);
}
// when we declare variable with let
// it is only accessible within block
console.log(j );	// j not accessible 


// function example 18   , Global Variable 


// accessible from anywhere 
var i = "I am global Variable";	// Global Variable
			
function show(){
    console.log(i);	// accessible in function
}
show();

console.log(i);	// accessible outside

function disp(){
    console.log(i);	// accessible in function
}
disp();

if(true){
    console.log(i);	// accessible in block

}


// function example 19, Local Variable 


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


// function example 20, Local Variable




function show(){
    var j = "J a Local Vari of Outer Function"; // Local Variable
    console.log(j);	// j accessible in function
    function innerFun(){
        var k = "K a Local Vari of inner fun";	// Local variable
        console.log(k);	// k accessible in function
        console.log(j);	// j accessible in function
    }
    innerFun();
    console.log(j);	// j accessible in function
    console.log(k);	// k not accessible for outer fun
}
show();


// function example 21, Local Variable


// Variable Hoisting
var i = "Hello";
console.log(i);
function show(){
    console.log(i);
    var i = "GeekyShows";
    console.log(i);
}
show();

/*
    var i; 
    i = "Hello";
    document.write(i + "<br>");
    function show(){
        var i;
        document.write(i + "<br>");
        i = "GeekyShows";
        document.write(i + "<br>");
    }
    show();
*/



// function example 22, Local Variable


var i = 10;
			function show(){
				var j = 20;
				console.log(j);
				console.log(i);
			}
			show();


// function example 23, Local Variable



function show(){
    var j = "J a Local Vari of Outer Function"; // Local Variable
    console.log(j);	// j accessible in function
    function innerFun(){
        var k = "K a Local Vari of inner fun";	// Local variable
        console.log(k);	// k accessible in function
        console.log(j );	// j accessible in function
    }
    innerFun();
    console.log(j);	// j accessible in function
    console.log(k);	// k not accessible for outer fun
}
show();


// function example 24, function expression

// Function Expression
		// You can't use function expressions before you define them:
        var disp = function show(){
            console.log("Hello GeekyShows");
        };
        disp();




// Storing Anonymous Function in variable
var disp = function(){
    console.log("Hello GeekyShows");
};
disp();



// Passing Anonymous Function
function disp(myfun){
    return myfun();
}

console.log(disp(function(){
    return "GeekyShows";
}));



// Returning Anonymous Function
function disp(a){
    return function(b){
        return a+b;
    };
}
var af = (disp(10));
console.log(af(20));


//  arrow functions 


// Function Expression
var myfun1 = function show(){
    console.log("GeekyShows");
};
myfun1();
// Anonymous Function 
var myfun2 = function(){
    console.log("GeekyShows");
};
myfun2();
// Arrow Function 
var myfun = () => {
    console.log("GeekyShows");
};

myfun();





// Arrow Function with parameter 
			// One Parameter () optional  
			var myfun1 = a => {			// var myfun = (a) => {
				console.log(a);
			};
			myfun1(10);
				
			// More than One Parameter () required  
			var myfun2 = (a, b) => {
				console.log(a + b);
				};
				
				myfun2(10, 20);
	
			// No Parameter () required  
			var myfun0 = () => {
				console.log("Geekyshows");
				};
				myfun0();



// Arrow Function 
var myfun1 = a => {
    console.log(a);
};
myfun1(108);
// Arrow Function 
// use curly brackets when more than one statement			
var myfun = a => {
console.log(a);
console.log("Hello"); };
myfun(10);






// Arrow Function


// Function Expression
var myfun1 = function show(a){
    return a;
};

// Anonymous Function 
var myfun2 = function(b){
    return b;
};

// Arrow Function 
var myfun = (c) => {
    return c;
};

// a bit more shorter Arrow Function 
var myfunN = (c) => c;	

console.log(myfun1(10));
console.log(myfun2(20));
console.log(myfun(30));
console.log(myfunN(40));
/*
var myfunN = (c) => { c };
if you put curly bracket it wont work 
if you want to put curly bracket then
you have to write return c 
More Example
var myfunN=(c)=>c;		// Work, It automatically returns c
var myfunN=(c)=>{c};	// Won't Work
var myfunN=(c)=>{return c};	// Work

var myfunN=(a,b)=> a+b;		// Work, It automatically returns a+b
var myfunN=(a,b)=>{a+b};	// Won't Work
var myfunN=(a,b)=>{return a+b};	// Work
*/			





// Arrow Function


// Arrow Function with default para
var myfunD = (a, b=20) => {
    console.log(a + " " + b);
};
myfunD(10, 50);

// Arrow Function with default para
var myfunR = (a, ...args) => {
    console.log(a + " " + args);
};
myfunR(10, 50, 60, 70);






//  infoked function IIFE

(function(){
    var a = 10;
    console.log(a);
})();


//  type of operator


var	a = 13;	
			console.log(typeof(a));	
			console.log(typeof("Hello"));





//  unfined in js 


var	a;	
			// Value not assigned Undefined
			console.log(a);	
			
			// b doesnt exist undefined
			console.log(typeof(b));	

			// Undefined Error			
			console.log(b);	

		





var	a = null;	
console.log(a);	
console.log(typeof(a));






    











 
