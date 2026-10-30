const bouton = document.getElementById("menu-btn");
const menu = document.getElementById("menu");

if (bouton && menu) {
    bouton.addEventListener("click", function () {
        menu.classList.toggle("active");

        const menuOuvert = menu.classList.contains("active");
        bouton.setAttribute("aria-expanded", menuOuvert);
    });
}