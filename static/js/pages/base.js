// =========================================================
// MetaEstudo — tema claro/escuro + sidebar mobile
// =========================================================
(function () {
    const STORAGE_KEY = "metaestudo-theme";
    const root = document.documentElement;
    const toggleBtn = document.getElementById("theme-toggle");
    const menuBtn = document.getElementById("menu-toggle");
    const sidebar = document.getElementById("app-sidebar");
    const navLists = document.querySelectorAll(".nav-list");

    // Mantém a barra de seleção presa ao link ativo e anima a troca durante o hover.
    navLists.forEach(function (navList) {
        const links = navList.querySelectorAll(".nav-link");
        const activeLink = navList.querySelector(".nav-link.is-active");
        let indicatorLink = activeLink;
        let indicatorTimer;

        function moveIndicator(link) {
            // O link anterior recolhe enquanto o novo link expande a barra no mesmo ciclo.
            if (!link || link === indicatorLink) {
                return;
            }

            clearTimeout(indicatorTimer);
            if (indicatorLink) {
                indicatorLink.classList.remove("indicator-visible");
                indicatorLink.classList.add("indicator-hiding");
            }

            link.classList.remove("indicator-hiding");
            link.classList.add("indicator-visible");
            indicatorLink = link;

            indicatorTimer = setTimeout(function () {
                links.forEach(function (navLink) {
                    if (navLink !== indicatorLink) {
                        navLink.classList.remove("indicator-hiding", "indicator-visible");
                    }
                });
            }, 400);
        }

        if (activeLink) {
            activeLink.classList.add("indicator-visible");
        }

        links.forEach(function (link) {
            link.addEventListener("mouseenter", function () {
                moveIndicator(link);
            });
        });
        navList.addEventListener("mouseleave", function () {
            moveIndicator(activeLink);
        });
    });

    // Sidebar em telas pequenas
    if (menuBtn && sidebar) {
        menuBtn.addEventListener("click", function () {
            sidebar.classList.toggle("is-open");
        });

        document.addEventListener("click", function (event) {
            const isClickInside = sidebar.contains(event.target) || menuBtn.contains(event.target);
            if (!isClickInside && sidebar.classList.contains("is-open")) {
                sidebar.classList.remove("is-open");
            }
        });
    }
})();