function displayGreeting() {
    const message = "Hi there! Welcome to my site!";
    const greetingElement = document.getElementById("greeter");
    greetingElement.textContent = message;
}

const button = document.getElementById("greetButton");
button.addEventListener("click", displayGreeting);
