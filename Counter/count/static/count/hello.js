document.addEventListener("DOMContentLoaded", function () {
  // Click me button
  document.querySelector("button").onclick = function () {
    heading = document.querySelector("h1");
    if (heading.innerHTML === "Hello World") {
      heading.innerHTML = "Goodbye!";
    } else {
      heading.innerHTML = "Hello World";
    }
  };

  // Form submit
  document.querySelector("form").onsubmit = function () {
    const name = document.querySelector("#name").value;
    alert(`Hello ${name}`);
  };

  // Color buttons
  document.querySelectorAll("button").forEach((button) => {
    button.onclick = () => {
      document.querySelector("#hello").style.color = button.dataset.color;
    };
  });

  // Dropdown select
  document.querySelector("select").onchange = (event) => {
    document.querySelector("#hello").style.color = event.target.value;
  };
});
