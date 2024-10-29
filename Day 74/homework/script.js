// // 1. ახალი პარაგრაფის შექმნა
// const p1 = document.createElement('p');
// p1.textContent = 'პარაგრაფი 1';
// document.body.appendChild(p1);

// // 2. ახალი სურათის ელემენტის შექმნა
// const img = document.createElement('img');
// img.src = 'image.jpg';
// img.alt = 'სურათის აღწერა';
// document.body.appendChild(img);

// // 3. ახალი ბუტონის შექმნა
// const button = document.createElement('button');
// button.textContent = 'დააჭირეთ აქ';
// document.body.appendChild(button);

// // 4. ახალი სექციის შექმნა
// const section = document.createElement('section');
// document.body.appendChild(section);

// // 5. ახალი ფორმის შექმნა
// const form = document.createElement('form');
// document.body.appendChild(form);
// // 1. ახალი ul და liის დამატება
// const ul = document.createElement('ul');
// const li = document.createElement('li');
// li1.textContent = '1';
// ul.appendChild(li);
// document.body.appendChild(ul);

// // 2. ახალი div-ის შიგნით ulის დამატება
// const nestedDiv = document.createElement('div');
// nestedDiv.appendChild(ul);

// // 3. ახალი divის შექმნა და დამატება
// const div = document.createElement('div');
// div.textContent = 'div';
// document.body.appendChild(div);

// // 4. divის შიგნით p-ის დამატება
// const p = document.createElement('p');
// p.textContent = 'p';
// div.appendChild(p);

// // 5. ახალი span-ის დამატება p-ის შიგნით
// const span = document.createElement('span');
// span.textContent = 'span';
// p.appendChild(span);
// // 1. ul და liის შექმნა
// const ul = document.createElement('ul');
// const li1 = document.createElement('li');
// li1.textContent = 'პუნქტი 1';
// const li2 = document.createElement('li');
// li2.textContent = 'პუნქტი 2';

// ul.appendChild(li1);
// ul.appendChild(li2);
// document.body.appendChild(ul);

// // 2. ახალი liის დამატება li1ის წინ
// const li0 = document.createElement('li');
// li0.textContent = '0';
// ul.insertBefore(li0, li1); // li0 li1-ის წინ

// // 3. ახალი divის შექმნა
// const div = document.createElement('div');
// div.textContent = 'div';
// document.body.appendChild(div);

// // 4. divის შიგნით pის დამატება
// const p = document.createElement('p');
// p.textContent = 'p';
// div.appendChild(p);

// // 5. ახალი pის დამატება divის შიგნით
// const p2 = document.createElement('p');
// p2.textContent = 'p';
// div.insertBefore(p2, p); // p2-ის დამატება p-ის წინ
// // 1. divის შექმნა
// const div = document.createElement('div');
// div.textContent = 'div';
// document.body.appendChild(div);

// // 2. divის ამოღება
// document.body.removeChild(div);

// // 3. ახალი ulის შექმნა და liის დამატება
// const ul = document.createElement('ul');
// const li = document.createElement('li');
// li.textContent = '0';
// ul.appendChild(li);
// document.body.appendChild(ul);

// // 4. liის ამოღება
// ul.removeChild(li);

// // 5. ისევ divის შექმნა და ამოღება
// const div1 = document.createElement('div');
// div1.textContent = 'div';
// document.body.appendChild(div1);
// document.body.removeChild(div1);
// // 1. divის შექმნა
// const div = document.createElement('div');
// div.textContent = 'div';
// document.body.appendChild(div);

// // 2. divის მშობელი ელემენტის მიღება
// const parent = div.parentNode; 
// console.log(parent);

// // 3. ulის და liის შექმნა
// const ul = document.createElement('ul');
// const li = document.createElement('li');
// li.textContent = '0';
// ul.appendChild(li);
// document.body.appendChild(ul);

// // 4. liის მშობელი ელემენტის მიღება
// const liParent = li.parentNode; 
// console.log(liParent);

// // 5. divის მშობელი ელემენტის მიღება
// const div1 = document.createElement('div');
// document.body.appendChild(div1);
// const div2 = div1.parentNode; 
// console.log(div2);
// // 1. divის შექმნა
// const div = document.createElement('div');
// div.textContent = 'div';
// document.body.appendChild(div);

// // 2. ახალი divის შექმნა
// const newDiv = document.createElement('div');
// newDiv.textContent = 'div';

// // 3. ძველი divის ჩანაცვლება ახალით
// document.body.replaceChild(newDiv, div);

// // 4. ulის შექმნა
// const ul = document.createElement('ul');
// const li = document.createElement('li');
// li.textContent = '1';
// ul.appendChild(li);
// document.body.appendChild(ul);

// // 5. liის ჩანაცვლება ახალით
// const li1 = document.createElement('li');
// li1.textContent = '2';
// ul.replaceChild(li1, li);




//ყველა დავალება ერთად გავაკეთ