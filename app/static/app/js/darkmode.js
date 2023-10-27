// Obtén el switch y el elemento body
const darkModeToggle = document.getElementById("dark-mode-toggle");
const body = document.body;

// Función para cambiar entre modos
function toggleDarkMode() {
  if (darkModeToggle.checked) {
    body.classList.add("dark-mode");
    localStorage.setItem("dark-mode", "enabled");
  } else {
    body.classList.remove("dark-mode");
    localStorage.setItem("dark-mode", "disabled");
  }
}

// Verifica la preferencia del usuario en localStorage
const darkModeLocalStorage = localStorage.getItem("dark-mode");
if (darkModeLocalStorage === "enabled") {
  darkModeToggle.checked = true;
  body.classList.add("dark-mode");
} else {
  darkModeToggle.checked = false;
}

// Habilita el switch
darkModeToggle.removeAttribute("disabled");

// Agrega un evento al switch para cambiar el modo
darkModeToggle.addEventListener("change", toggleDarkMode);