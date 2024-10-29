const form = document.querySelector('form');
 

form.addEventListener('submit', function(event){
    const name = document.querySelector('.name').value;

    const email = document.querySelector('.email').value;

    const password = document.querySelector('.password').value;

    const facebook = document.querySelector('.facebook').value;

    const table = document.querySelector('table');

    event.preventDefault();

    const tr = document.createElement("tr");

    const data = [name, email, password, facebook];


    for(let i = 0; i < data.length; i++){
        const td = document.createElement("td");

        td.innerHTML = data[i];

        tr.appendChild(td);
    }
    table.appendChild(tr);
});