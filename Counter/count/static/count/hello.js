document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("button").onclick = function () {
    heading = document.querySelector("h1");
    if (heading.innerHTML === "Hello World") {
      heading.innerHTML = "Goodbye!";
    } else {
      heading.innerHTML = "Hello World";
    }
  };

  document.querySelector("form").onsubmit =  () => {
    const name = document.querySelector("#name").value;
    alert(`Hello ${name}`);
  };

});

document.addEventListener("DOMContentLoaded",  () => {
  //change fontcolor 
  document.querySelectorAll('button').forEach(button => {
    button.onclick = () =>{
      document.querySelector('#hello').style.color = button.dataset.color
    }
  })
})
