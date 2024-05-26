const logo = document.querySelector('#logo');
const burgerMenu = document.querySelector('#burger-menu');
const burgerBlock = document.querySelector('#burger-block');

const more = document.querySelector('#more');
const moreMenu = document.querySelector('#more-menu');

burgerMenu.addEventListener('click', () => {
    burgerBlock.classList.toggle('hide');
});

more.addEventListener('click', () => {
    moreMenu.classList.toggle('hide');
});