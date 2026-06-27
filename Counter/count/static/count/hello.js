function hello() {
  heading = document.querySelector('h1');
  if (heading.innerHTML === "Hello World") {
    heading.innerHTML = "Goodbye!";
  } else {
    heading.innerHTML = "Hello World";
  }
 
}
document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("form") = function () {
    const name = document.querySelector("#name").value;
    alert(`Hello ${name}!`)
    
  }
})
