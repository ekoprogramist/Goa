let age = prompt("type your age");

if (age >= 18) {
    alert("Welcome to our website!");
} else {
    alert("Sorry, you are not old enough to visit our website.");
    alert("You are missing year");
    alert(18 - age);
}