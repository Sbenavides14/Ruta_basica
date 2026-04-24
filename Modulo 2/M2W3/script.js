// script.js — Interactividad básica del portafolio (Task 5)

// ── 1. Cambiar el texto del párrafo "About me" al hacer clic ──────────────
const btnChangeText = document.getElementById("btn-change-text");
const aboutText     = document.getElementById("about-text");

// Texto alternativo que se mostrará al hacer clic
const extraText = "I'm currently learning web development and Python. " +
                  "I enjoy building projects from scratch and improving my skills every day.";

btnChangeText.addEventListener("click", function () {
    // Alterna entre el texto original y el texto extra
    if (btnChangeText.textContent === "Read more") {
        aboutText.innerHTML = extraText;
        btnChangeText.textContent = "Read less";
    } else {
        aboutText.innerHTML = "Hi! Let me tell you a little about myself.<br><br>" +
            "My name is Samuel, and I'm 24 years old. I like to describe myself as someone " +
            "focused on learning about technology, especially software development. I like to " +
            "move forward with purpose, organize my projects, and fully understand each step " +
            "to continuously improve.";
        btnChangeText.textContent = "Read more";
    }
});

// ── 2. Mostrar mensaje de bienvenida al hacer clic en Send ────────────────
const btnSend      = document.getElementById("btn-send");
const welcomeMsg   = document.getElementById("welcome-msg");

btnSend.addEventListener("click", function () {
    // Quita la clase "hidden" para mostrar el mensaje en pantalla
    welcomeMsg.classList.remove("hidden");
});
