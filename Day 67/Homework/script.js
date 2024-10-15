function person(name, age){
    this.name = name;
    this.age = age;

    this.introduce = function(){
        console.log(Hi, I am ${this.name} and I am ${this.age} years old.);
    }
}
const person1 = new person("kote", 11);
person1.introduce();
function Book(title, author = "Unknown"){
    this.title = title;
    this.author = author;

    this.getDetails = function(){
        console.log(this.title + " " + this.Book);
    }
}
const Book1 = new Book("datvi");
Book1.getDetails();
function Classroom(students){
    this.students = students;
    this.countStudents = function(){
        console.log(this.students.length);
    }
}
const class1 = new Classroom(["kote", "sandro", "giorgi"]);
class1.countStudents();



function counter(){
    let num = 0;
    this.increment = function(){
        num++;
    }
    this.getValue = function(){
        console.log(num)
    }
}
const counter1 = new counter();
counter1.increment();
counter1.increment();
counter1.increment();
counter1.getValue();
function Light() {
    this.state = "off";

    this.toggle = function() {
        this.state = this.state === "off" ? "on" : "off";
    };
}

const myLight = new Light();
console.log(myLight.state);
function product(name, price){
    this.name = name;
    this.price = price;

    this.getDetails = function(){
        console.log(Product: ${this.name}, Price: ${thisprice} USD);
    }
}
const product1 = new product("bag", "99$");
product1.getDetails();
function User(userName, contact){
    this.userName = userName;
    this.contact = contact;
    this.getContactInfo = function(){
        console.log(contact);
    }
}
const User1 = new User("kote", {email: "deded@gmail.com", phone: "+995 32 33 32"});
User1.getContactInfo();
function Library(books){
    this.books = books;
    this.listBooks = function(){
    for (let i = 0; i < books.length; i++) {
        console.log((i + 1) + '. "' + this.books[i].title + '" by ' + this.books[i].author);
    }
}
}
const myLibrary = new Library([{title: "datvi", author: "ilia chavchavadze"}]);
myLibrary.listBooks();
function Cart(){
    let items = [];
    this.addItems = function(item){
        items.push(item);
    }
    this.getItems = function(){
        console.log(items)
    }
}
const myCart = new Cart();
myCart.addItems("bag");
myCart.getItems();
function Student(name, marks) {
        this.name = name;
        this.marks = marks;

        this.hasPassed = function() {
            let sum = 0;
            let count = 0;

            for (let i = 0; i < marks.length; i++) {
                sum += marks[i];
                count++;
            }

            let result = sum / count;

            return result >= 50;
        };
    }

const student1 = new Student('kote', [60, 70, 80]);
console.log(student1.hasPassed());

const student2 = new Student('gio', [40, 30, 20]);
console.log(student2.hasPassed())