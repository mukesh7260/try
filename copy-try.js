
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



// ---------------------     	OBJECT TOPICS IN JS		-------------------------------------------


var fees = { };		// Declaring empty object
			fees['Rahul'] = 100;	// initializing 
			fees['Sumit'] = 200;
			fees['Rohan'] = 300;
		/*
			fees.Rahul = 100;
			fees.Sumit = 200;
			fees.Rohan = 300;
		*/
            console.log(fees['Sumit']);	// Accessing value




    
var fees = { };	
fees['Rahul'] = 100;
fees['total'] = function () {return(100+200+300);};
// fees.total = function(){return(100+200+300);};
document.write(fees.total());



var fees = {Rahul:100, Sumit:200, Rohan:300};
		/*
			var fees = {
						Rahul:100, 
						Sumit:200, 
						Rohan:300
					   };
		*/
        console.log(fees['Rahul']);



var fees = {Rahul:100, Sumit:200, Rohan:300, total: function(){return(100+200+300)}};
/*
	var fees = {
				Rahul:100, 
				Sumit:200, 
				Rohan:300,
				total: function(){return(100+200+300)}
				};
*/
console.log(fees.total());



// declare objects using conostuctor 



var fees = new Object();
			fees['Rahul'] = 100;
			fees['Sumit'] = 200;
			fees['Rohan'] = 300;
		/*
			fees.Rahul = 100;
			fees.Sumit = 200;
			fees.Rohan = 300;
		*/	
            console.log(fees['Rahul']);







var fees = new Object();
fees['Rahul'] = 100;
fees['Sumit'] = 200;
fees['Rohan'] = 300;
fees['total'] = function (){return(100+200+300);};
/*
fees.Rahul = 100;
fees.Sumit = 200;
fees.Rohan = 300;
fees.total = function(){return(100+200+300);};
*/	
console.log(fees.total());





//  object constructor
var fees = {Rahul:100, Sumit:200, Rohan:300};
		/*
			var fees = {
						Rahul:100, 
						Sumit:200, 
						Rohan:300
					   };
		*/
            console.log(fees['Rahul']);



var fees = {Rahul:100, Sumit:200, Rohan:300, total: function(){return(100+200+300)}};
/*
	var fees = {
				Rahul:100, 
				Sumit:200, 
				Rohan:300,
				total: function(){return(100+200+300)}
				};
*/
	console.log(fees.total());





var fees = new Object();
	fees['Rahul'] = 100;
	fees['Sumit'] = 200;
	fees['Rohan'] = 300;
/*
	fees.Rahul = 100;
	fees.Sumit = 200;
	fees.Rohan = 300;
*/	
	console.log(fees['Rahul']);






var fees = new Object();
	fees['Rahul'] = 100;
	fees['Sumit'] = 200;
	fees['Rohan'] = 300;
	fees['total'] = function (){return(100+200+300);};
/*
	fees.Rahul = 100;
	fees.Sumit = 200;
	fees.Rohan = 300;
	fees.total = function(){return(100+200+300);};
*/	
console.log(fees.total());





var fees = {Rahul:100, Sumit:200, Rohan:300};
    console.log(fees['Rahul'] );
    console.log(fees["Rahul"] );
    console.log(fees.Rahul);





var fees = {Rahul:100, "Super Man": 400};
    console.log(fees['Super Man']);
    console.log(fees["Super Man"]);
   // console.log(fees.Super Man); // We Cannt access multiword key by dot notation






var fees = {
    Rahul: 100, 
    Sumit: 200, 
    Rohan: 300, 
    total: function () { return(100+200+300); }			
};
console.log(fees.total());
console.log(fees['total']());




var fees = {Rahul:100, Sumit:200};
			
            console.log(fees.Rahul + " "+ fees.Sumit );
			
			fees.Sonam = 600;	// fees.['Sonam'] = 600;
			
			console.log(fees.Sonam + " " + fees.Rahul + " "+ fees.Sumit);
			
			fees.show = function () {};
			
			console.log(fees);



var fees = {Rahul:100, Sumit:200};

	console.log(fees.Rahul + " "+ fees.Sumit );

	delete fees.Rahul;
	console.log(fees.Rahul + " "+ fees.Sumit);
	console.log(fees);




function mobile( ) {
	return {
		model: 'Galaxy',
		price: function(){return "Price Rs. 3000";} 
	};
}
var samsung = mobile( );
console.log(samsung.model + " "+samsung.price( ));
	




function mobile(model_no) {
    return {
        model: model_no,
        price: function(){
            return "Price is Rs. 3000";
        } 
    };
}
var samsung = mobile('galaxy');
var nokia = mobile('3310');
console.log(samsung.model + " "+samsung.price( ));
console.log(nokia.model + " "+nokia.price( ));





function Mobile(){
    this.model = '3310';
    this.price = function(){
        console.log(this.model + " Price Rs. 3000");
    }
}

var samsung = new Mobile();
samsung.price();





function Mobile(model_no){
    this.model = model_no;
    this.price = function(){
        console.log(this.model + " Price Rs.3000");
    }
}
var samsung = new Mobile('Galaxy');
var nokia = new Mobile('3310');
samsung.price();
nokia.price();




function Mobile(model_no){
    this.model = model_no;
    this.color = 'white';
    this.ram = '4GB';
    this.price = function(){
        console.log(this.model + " Price Rs.3000 ");
    };
}
var samsung = new Mobile('Galaxy');
var nokia = new Mobile('3310');
for(var key in nokia)
{
    console.log(nokia[key]);
}






function Mobile(model_no){
    this.model = model_no;
    this.color = 'white';
    this.ram = '4GB';
    this.price = function(){
        console.log(this.model + " Price Rs.3000 ");
    };
}
var samsung = new Mobile('Galaxy');
var nokia = new Mobile('3310');
// Method wont display
for(var key in nokia){
    if(typeof nokia[key] !== 'function'){
        console.log(nokia[key]);
    }	
}

/* value with key, Method wont display
for(var key in nokia){
    if(typeof nokia[key] !== 'function'){
    console.log(key + " : " + nokia[key] + "<br>"); 
    }
}
*/



function Mobile(model_no){
    this.model = model_no;
    this.memory = 4;
}

var samsung = new Mobile('Galaxy');
var nokia = new Mobile('3310');

if(typeof nokia.memory !== 'undefined'){
    console.log("Available");
} else {
    console.log("Doesnt Exist");
}






function Mobile(model_no){
    this.model = model_no;
    this.memory = 4;
}

var samsung = new Mobile('Galaxy');
var nokia = new Mobile('3310');

if('memory' in nokia){
    console.log("Available");
} else {
    console.log("Doesnt Exist");
}





function Mobile(model_no){
    this.model = model_no;
    this.color = 'white';
}

var samsung = new Mobile('Galaxy');
var nokia = new Mobile('3310');

if(nokia.hasOwnProperty('color')){
    console.log("Available");
} else {
    console.log("Doesnt Exist");
}







var  Mobile = function(model_no, sprice){
    this.model = model_no;
    this.color = 'white';
    this.price = 3000;
    this.sp = sprice;
    this.sellingprice = function(){
        return (this.price + this.sp);
    };
    this.data = function(){
        console.log(" Model No: " + this.model + " Price: " + this.sellingprice());
    }
};
var samsung = new Mobile('Galaxy', 2000);
var nokia = new Mobile('3310', 1000);
nokia.data();




var  Mobile = function(model_no, sprice){
    this.model = model_no;
    this.color = 'white';
    var price = 3000;	// private property
    this.sp = sprice;
    // Private Method
    var show = function() { return "Hello World";};
};
var samsung = new Mobile('Galaxy', 2000);
var nokia = new Mobile('3310', 1000);
console.log(nokia.price);
console.log(nokia.show());





var  Mobile = function(model_no, sprice){
    this.model = model_no;
    this.color = 'white';
    var price = 3000;	// private property
    this.sp = sprice;
    // Private Method
    var show = function shows() { return show;};
};
var samsung = new Mobile('Galaxy', 2000);
var nokia = new Mobile('3310', 1000);
console.log(nokia.price);
console.log(nokia.show);





var  Mobile = function(model_no, sprice){
    this.model = model_no;
    this.color = 'white';
    var price = 3000;	// private property
    this.sp = sprice;
    // Public Method
    this.sellingprice = function(){		
        return (price);
    };
};
var samsung = new Mobile('Galaxy', 2000);
var nokia = new Mobile('3310', 1000);
console.log(nokia.price);
console.log(nokia.sellingprice());




var  Mobile = function(model_no){
    // Instance Member
    this.model = model_no;
    this.price = 3000;
};
var samsung = new Mobile('Galaxy');
var nokia = new Mobile('3310');			
// classname.prototype.key = 'value';
// Prototype Member
Mobile.prototype.color = 'white';

console.log(samsung.color);
console.log(samsung);







var  Mobile = function(model_no){
    // Instance Member
    this.model = model_no;
    this.price = 3000;
};
var samsung = new Mobile('Galaxy');
var nokia = new Mobile('3310');			
// classname.prototype.key = 'value';
// Prototype Member
Mobile.prototype.color = 'white';
for (var key in samsung){
    console.log(key);
}






// It will return Object.prototype
console.log(Object.prototype);

// creating an empty object and prototype object of this 
// object is Object.prototype
var b = {};

// We are checking what is the Prototype Object of b which 
// should be Object.prototype
// b will inherit all properties of Object.prototype Object
console.log(Object.getPrototypeOf(b)); 

// Further check what is the Prototype Object of Object.prototype it should be null
console.log(Object.getPrototypeOf(Object.prototype)); 

// Check the above stuff with new operator
var b1 = new Object();
console.log(Object.getPrototypeOf(b1));

// checking with Array
// First check what is the Array.prototype
console.log(Array.prototype);

// creating empty Array Object
var b2 = new Array();

// check what is the Prototype of Object b2
// it will be Array.Prototype
console.log(Object.getPrototypeOf(b2));

// Now check what is the Prototype Object of Array.prototype
console.log(Object.getPrototypeOf(Array.prototype));









function Mobile(){

}
// Mobile is the object created by Function which is actually Function itself
console.log(Mobile);

// prototype is a property of Mobile which points to the Prototype Object of Mobile
console.log(Mobile.prototype);  // it will show Prototype Object of Mobile Function

// Creating a new Object using new keyword
var lg = new Mobile();

// When you create a new object of that function using new keyword JS Engine creates an object and sets a property named __proto__ which points to its function’s prototype object
console.log(lg.__proto__);                // Mobile.prototype

// Verifying all stuffs
console.log(lg.__proto__ === Mobile.prototype);     // true
console.log(Mobile === lg.__proto__.constructor);      // true
console.log(Mobile === Mobile.prototype.constructor);   // true
    






function Mobile(){
}
// Creating a new Object using new keyword
var lg = new Mobile();
// This will show undefined becoz a is neither defined in the funtion nor in the function's prototype
// it first checks if lg object have property a as it doesn't have it so it go to its prototype object pointed by __proto__ and ask him if he has property a as it also doesn't have it so finally we receive undefined. This is how it works behind the browser and JS Engine is the responsible for this task
console.log(lg.a);
console.log(lg);







function Mobile(){
            
}
 // This property is defined in Function's Prototype Object so all Objects will have access to this property and this is just one single property for all objects. It doesn't make copies for objects separately. usually we defined methods as a prototype method member rather than Prototype variable memeber
 Mobile.prototype.a = 10;   

// Creating a new Object using new keyword
var lg = new Mobile();

// It first checks if lg object have property a as it doesn't have it so it go to its prototype object pointed by __proto__ and ask him if he has property a as it has so finally we receive 10. This is how it works behind the browser and JS Engine is the responsible for this task
console.log(lg.a);





function Mobile(){
    this.a = 20;
}
 // This property is defined in Function's Prototype Object so all Objects will have access to this property and this is just one single property for all objects. It doesn't make copies for objects separately. usually we defined methods as a prototype method member rather than Prototype variable memeber
 Mobile.prototype.a = 10;   

// Creating a new Object using new keyword
var lg = new Mobile();

// It first checks if lg object have property a as it has so it will return 10 and will stop checking further in the prototype object
console.log(lg.a);      // 20







// Super Class
var Mobile = function(){
    this.a = 10;
}

// Prototype Property of Mobile
Mobile.prototype.z = 30;

// Sub Class
var Samsung = function(){
    // It initialize and call Super class constructor without this you can not access super class property using sub class object
    Mobile.call(this);      
    this.b = 20;
}

// Prototype Inheritance
Samsung.prototype = Object.create(Mobile.prototype);
Samsung.prototype.constructor = Samsung;

var s = new Samsung();
console.log(s.a);
console.log(s.b);
console.log(s.z);






var Mobile = function(){

}
Mobile.prototype.getModel = function(){ return this.model; }

var Samsung = function(model, price){
    this.model = model;
    this.price = price;
}

var Lenovo = function(model){
    this.model = model;
}

// inheritance 
Samsung.prototype = Object.create(Mobile.prototype);
Samsung.prototype.constructor = Samsung;
Lenovo.prototype = Object.create(Mobile.prototype);
Lenovo.prototype.constructor = Lenovo;

// always write child prototype after inheritance else it wont work
Samsung.prototype.getPrice = function(){ return this.price; }

var galaxy = new Samsung("Galaxy", 3000);
var  phab2 = new Lenovo('Phab 2')

console.log(galaxy.getModel());
console.log(galaxy.getPrice());
console.log(phab2.getModel());






// Function for inheritance
function extend(Child, Parent) {
    Child.prototype = Object.create(Parent.prototype);
    Child.prototype.constructor = Child;
}
var Mobile = function () {

}
Mobile.prototype.getModel = function () {
    return this.model;
}

var Samsung = function (model, price) {
    this.model = model;
    this.price = price;
}

var Lenovo = function (model) {
    this.model = model;
}

// inheritance 
extend(Samsung, Mobile);
extend(Lenovo, Mobile);

// always write child prototype after inheritance else it wont work
Samsung.prototype.getPrice = function () {
    return this.price;
}

var galaxy = new Samsung("Galaxy", 3000);
var phab2 = new Lenovo('Phab 2')

console.log(galaxy.getModel());
console.log(galaxy.getPrice());
console.log(phab2.getModel());







var Mobile = function(model){
    this.model = model;
}
Mobile.prototype.getModel = function(){ return this.model; }

var Samsung = function(model, price){
Mobile.call(this, model)
this.price = price;
}

// inheritance 
Samsung.prototype = Object.create(Mobile.prototype);
Samsung.prototype.constructor = Samsung;


var galaxy = new Samsung("Galaxy", 3000);

console.log(galaxy.getModel());
console.log(galaxy.model);









// Function for inheritance
function extend(Child, Parent){
    Child.prototype = Object.create(Parent.prototype);
    Child.prototype.constructor = Child;
}

// Super Class
var Mobile = function() {
    
}
// Prototype Member
Mobile.prototype.show = function(){
    return "Super Class Method";
}

// Sub Class
var Samsung = function(){

}

// sub class Samsung extending super class Mobile
extend(Samsung, Mobile);

// Prototype Member for Sub Class
Samsung.prototype.show = function(){
    return "Sub Class Method";
}

// Creating object of sub class Samsung
var sam = new Samsung();

// Accessing super class property model
// using sub class object
console.log(sam.show());	





                                    //  ARRAY IN JAVA SCRIPTS 


var stu = ["Rahul", "Raj" ];
console.log(stu);
console.log(typeof(stu));     




var geek = [];	// empty array
			geek[0] = "Rahul";
			geek[1] = "Ram";
			geek[2] = 56;
			geek[3] = "Jay";
			console.log(geek);

var stu = ["Rahul", "Raj" ];
console.log(stu[0]);
console.log(typeof(stu)); 


var geek = ["Rahul", "Ram", 56, "Jay"];
console.log(geek); 




// var geek = [];
var geek = new Array();		// empty array
geek[0] = "Rahul";
geek[1] = "Ram";
geek[2] = 56;
geek[3] = "Jay";
console.log(geek[2]);



// var geek = ["Rahul", "Ram", 56, "Jay"];
var geek = new Array("Rahul", "Ram", 56, "Jay");
console.log(geek[3])



var geek = new Array(10);
console.log(geek);



/*
				var geek = ["Rahul", "Ram", 56, "Jay"];
				console.log(geek);

			*/
			var geek = [];
			geek[0] = "Rahul";
			geek[1] = "Ram";
			geek[2] = 56;
			geek[3] = "Jay";
			geek[4] = "Extra";
			console.log(geek);




var geek = ["Rahul", "Ram", 56, "Jay"];
console.log (geek);
geek[0] = "Rohit";
console.log(geek);




var geek = ["Rahul", "Ram", 56, "Jay"];
			var geekyshows = geek;
			console.log(geekyshows);
			console.log(geek);
			geekyshows[0] = "Rohit";
			console.log(geek);



var geek = ["Rahul", "Ram", 56, "Jay"];
console.log(geek);
delete geek[0];
console.log(geek);
console.log(geek[0]);




var geek = ["Rahul", "Ram", 56, "Jay"];
console.log(geek.length); 





var geek = ["Rahul", "Ram", 56, "Jay"];
		//  var geek = new Array("Rahul", "Ram", 56, "Jay");
			for(let i=0; i<=3; i++){
				console.log(geek[i]);
			}
			
			/* In case if you dont know array length use length property with for loop 
			for(let i=0; i<geek.length; i++){
				document.write(geek[i] + "<br>");
			}
			*/



var geek = ["Rahul", "Ram", 56, "Jay"];
geek.forEach(function (value, index) {
    console.log(value + " " + index);
});




var geek = ["Rahul", "Ram", 56, "Jay"];
			for(let value of geek){
				console.log(value);
			}








// Defining Array         install this one packege for user input in JAVA SCRIPT : npm install prompt-sync

const prompt = require('prompt-sync')();
var elements = prompt("Enter number of Elements: ");
var geek= [];

// Input for Array
for(var i = 0; i<=elements; i++){
    geek[i] = prompt("Enter Name: ");
}
// Display Values
for(var value of geek){
    console.log(value);
}








/*	
// Defining Array
var geek = new Array(3);		// length of array 3

// Array Length
var ln = geek.length;

// Input 
for(let i =0; i<= ln; i++){
    geek[i] = prompt("Enter Name: ");
}

// Display Values
for(var value of geek){
    document.write(value + "<br>");
}

*/	