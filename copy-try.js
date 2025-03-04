
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