document.addEventListener("DOMContentLoaded", function () {

  document.querySelector('button').onclick = function () {
    heading = document.querySelector('h1');
    if (heading.innerHTML === "Hello World") {
      heading.innerHTML = "Goodbye!";
    } else {
      heading.innerHTML = "Hello World";
    }
  }

  document.querySelector('form').onsubmit = function () {
    const name = document.querySelector('#name').value;
    alert(`Hello ${name}`);
  }

});