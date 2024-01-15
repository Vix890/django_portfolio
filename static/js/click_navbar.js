document.addEventListener('DOMContentLoaded', function () {
    var navbarToggle = document.querySelector('#navbar_hamburger');
    var menuBg = document.querySelector('#navbar_menu_bg');
    var navbarMenu = document.querySelector('#navbar_menu');
    var userBtn = document.querySelector('#user_button');
    var userMenu = document.querySelector('#navbar_user_menu');

    navbarToggle.addEventListener('click', function () {
        navbarMenu.classList.toggle('active');
        menuBg.classList.toggle('active');
    });

    menuBg.addEventListener('click', function () {
        navbarMenu.classList.remove('active');
        menuBg.classList.remove('active');
        userMenu.classList.remove('active');
    });

    userBtn.addEventListener('click', function () {
        userMenu.classList.toggle('active');
        menuBg.classList.toggle('active');
    });
});
