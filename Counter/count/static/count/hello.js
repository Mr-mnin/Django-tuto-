function hello() {
  heading = document.querySelector('h1');
  if (heading.innerHTML === "Hello World") {
    heading.innerHTML = "Goodbye!";
  } else {
    heading.innerHTML = "Hello World";
  }
}
