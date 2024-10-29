const time = document.querySelector('.time');
function UpdateTime(){
    const now = new Date();
    const hours = String(now.getHours());
    const minutes = String(now.getMinutes());
    const seconds = String(now.getSeconds());
    time.textContent = `${hours}:${minutes}:${seconds}`;
}
setInterval(UpdateTime, 1000)
const colors = ['red', 'yellow', 'green', 'orange', 'purple', 'pink'];
let index = 0;

function changeBackgroundColor() {
        document.body.style.backgroundColor = colors[index];
        index = (index + 1) % colors.length;
}

setInterval(changeBackgroundColor, 3000);