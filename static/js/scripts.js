
// ...existing code...

document.addEventListener('DOMContentLoaded', function() {
    var dropdownSubmenus = document.querySelectorAll('.dropdown-submenu .dropdown-toggle');
    dropdownSubmenus.forEach(function(el) {
        el.addEventListener('click', function(e) {
            e.stopPropagation();
            var submenu = el.nextElementSibling;
            if (submenu) {
                submenu.classList.toggle('show');
            }
        });
    });
});

// ...existing code...