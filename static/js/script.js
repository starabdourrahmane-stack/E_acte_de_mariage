const bouton = document.getElementById("menu-btn");
const menu = document.getElementById("menu");

if (bouton && menu) {
    bouton.addEventListener("click", function () {
        menu.classList.toggle("active");

        const menuOuvert = menu.classList.contains("active");
        bouton.setAttribute("aria-expanded", menuOuvert);
    });
}
const MesImages =document.querySelectorAll(".mesimages");

let index = 0;

function afficherSlide() {
        MesImages.forEach((image, i) => {
            image.style.display = i === index ? "block" : "none";
        
        });
}
// Boutton droite images suivant 

document.getElementById("suivant").addEventListener("click", function () {
    index = (index + 1) % MesImages.length;
    afficherSlide();
});
//Boutton gauche images précédent 

document.getElementById("precedent").addEventListener("click", function() {
    index =(index -1 + MesImages.length) % MesImages.length;
    afficherSlide();
});
afficherSlide();