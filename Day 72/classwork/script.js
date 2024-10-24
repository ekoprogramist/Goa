const usertime = document.getElementById('my_p')

const time = setInterval(function() {
    usertime--;

    console.log(usertime, 'left');

    clearInterval(time);

    console.log('Time is up')
}, 1000);