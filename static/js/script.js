// Materialize Initialisations

// Initialise Materialize Sidenav Menu

document.addEventListener('DOMContentLoaded', function() {
    const elems = document.querySelectorAll('.sidenav');
    const instances = M.Sidenav.init(elems, {
        edge: "right"
    });
});
   
// Initialise Materialize Dropdown for larger devices with hover

document.addEventListener('DOMContentLoaded', function() {
    const elems = document.querySelectorAll('.dropdown-trigger');
    const instances = M.Dropdown.init(elems, {
        coverTrigger: false,
        hover: true
    });
});

// Initialise Materialize Dropdown for mobile navigation and top bar icons
document.addEventListener('DOMContentLoaded', function() {
    const elems = document.querySelectorAll('.click-dropdown-trigger');
    const instances = M.Dropdown.init(elems, {
        coverTrigger: false,
        hover: false
    });
});

// Initialise Materialize Dropdown with specific options for search dropdown on mobile
document.addEventListener('DOMContentLoaded', function() {
    const elems = document.querySelectorAll('.search-dropdown-trigger');
    const instances = M.Dropdown.init(elems, {
        coverTrigger: false,
        constrainwidth: false,
        closeOnClick: false,
    });
});
            

// Messages

// Close message container
const closeBtn = document.querySelector(".message-close-btn")
if (closeBtn) {
    closeBtn.addEventListener("click", function() {
    const message = document.querySelector(".message-container")
    message.classList.add("none")
    })
}

