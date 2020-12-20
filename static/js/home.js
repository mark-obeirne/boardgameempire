// Initialise Materialize Slider

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems, {
        duration: 700
    });
});