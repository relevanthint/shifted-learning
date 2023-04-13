const hamburger = document.querySelector(".hamburger");
const menu = document.querySelector(".menu");
const menuItems = document.querySelectorAll(".menu li");

function toggleMenu() {
  menu.classList.toggle("menu-open");
  menu.classList.toggle("menu");
}

hamburger.addEventListener("click", toggleMenu);

menuItems.forEach(item => {
  item.addEventListener("click", toggleMenu);
});
