// Initialise Materialize Slider

document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('.slider');
    let instances = M.Slider.init(elems, {
        duration: 700
    });
});