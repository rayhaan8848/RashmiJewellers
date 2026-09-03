/* =====================================================
   ACCOUNT DROPDOWN
===================================================== */

const accountButton =
    document.getElementById("accountButton");

const accountDropdown =
    document.getElementById("accountDropdown");


accountButton.addEventListener("click", function (event) {

    event.stopPropagation();

    accountDropdown.classList.toggle("show");

});


/* Close dropdown when clicking outside */

document.addEventListener("click", function (event) {

    if (
        !accountDropdown.contains(event.target) &&
        !accountButton.contains(event.target)
    ) {

        accountDropdown.classList.remove("show");

    }

});


/* =====================================================
   MOBILE MENU
===================================================== */

const mobileToggle =
    document.getElementById("mobileToggle");

const mobileMenu =
    document.getElementById("mobileMenu");


mobileToggle.addEventListener("click", function () {

    mobileToggle.classList.toggle("active");

    mobileMenu.classList.toggle("show");

});


/* =====================================================
   MOBILE LINK CLICK
===================================================== */

const mobileLinks =
    document.querySelectorAll(".mobile-link");


mobileLinks.forEach(function (link) {

    link.addEventListener("click", function () {

        mobileToggle.classList.remove("active");

        mobileMenu.classList.remove("show");

    });

});


/* =====================================================
   NAVBAR MOUSE PARALLAX
   Very subtle 3D movement
===================================================== */

const navbar =
    document.querySelector(".luxury-navbar");


navbar.addEventListener("mousemove", function (e) {

    const rect =
        navbar.getBoundingClientRect();

    const x =
        e.clientX - rect.left;

    const y =
        e.clientY - rect.top;

    const centerX =
        rect.width / 2;

    const centerY =
        rect.height / 2;

    const rotateX =
        ((y - centerY) / centerY) * -1;

    const rotateY =
        ((x - centerX) / centerX);

    navbar.style.transform = `
        perspective(1200px)
        rotateX(${rotateX * 0.7}deg)
        rotateY(${rotateY * 0.7}deg)
    `;

});


navbar.addEventListener("mouseleave", function () {

    navbar.style.transform = `
        perspective(1200px)
        rotateX(0deg)
        rotateY(0deg)
    `;

});