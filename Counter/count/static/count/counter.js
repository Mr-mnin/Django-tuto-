let count = 0;

function counter() {
    count++;
    heading = document.querySelector("h1");
    heading.innerHTML = count
    if (count % 10 === 0) {
        alert('Count is now ${ count }');
    }

    document.addEventListener("DOMContentLoaded", function () {
        document.querySelector('button').onclick = counter;
    }); 

    
}
