// Materialize Initialisations

// Initialise Materialize Sidenav Menu

document.addEventListener('DOMContentLoaded', function() {
    const elems = document.querySelectorAll('.sidenav');
    const instances = M.Sidenav.init(elems, {
        edge: "right"
    });
});
   
// Initialise Materialize Dropdown
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
let messageCloseBtn = document.querySelector(".message-close-btn")
if (messageCloseBtn) {
    messageCloseBtn.addEventListener("click", function() {
    const message = document.querySelector(".message-container")
    message.classList.add("none")
    })
}


// Element Selectors
    // Quantity Control Spans and Input Field    
    const increaseQtyBtn = document.querySelector(".qty-increase")
    const decreaseQtyBtn = document.querySelector(".qty-decrease")
    const quantityInputField = document.querySelector(".product-qty-input")

    // Sort Dropdown Menu 
    const selectDropdown = document.querySelectorAll(".sort-select-dropdown")
    
    // Cart page - quantity adjustment buttons and input fields
    const cartIncreaseQtyBtns = document.querySelectorAll(".cart-qty-increase")
    const cartDecreaseQtyBtns = document.querySelectorAll(".cart-qty-decrease")
    const cartQuantityInputFields = document.querySelectorAll(".cart-qty-input")  


// Functions

    // Increase quantity input value when "+" button is clicked on Product Detail page

        function increaseQty() {
            const inputField = increaseQtyBtn.parentElement.previousElementSibling.firstElementChild;
            let inputValue = parseInt(inputField.value);
            const maxValue = inputField.getAttribute("max");
            if (inputValue < maxValue) {
                inputValue += 1;
                inputField.value = inputValue.toString();
            }
        }


    // Decrease quantity input value when "-" button is clicked on Product Detail page
        function decreaseQty(){
            const inputField = decreaseQtyBtn.parentElement.nextElementSibling.firstElementChild;
            let inputValue = parseInt(inputField.value);
            if (inputValue > 1) {
                inputValue -= 1;
                inputField.value = inputValue.toString();
            }
        }

    
    // Update quantity value if user tries to enter a number less than 1 or greater than max available on Product Detail page
        function updateQty() {
            let userValue = quantityInputField.value;
            const maxValue = quantityInputField.getAttribute("max");
            if (parseInt(userValue) < 1 || userValue == "" ) {
                userValue = "1";
                quantityInputField.value = userValue;
            } else if (parseInt(userValue) > maxValue) {
                userValue = maxValue.toString();
                quantityInputField.value = userValue;
            }
        }


    // Update sorting mechanic and direction on products/deals pages
        function updateSortDirection(){
            const chosenSorting = this.value;
            console.log(chosenSorting)
            const currentUrl = new URL(window.location);

            if (chosenSorting != "reset") {
                const sort = chosenSorting.split("-")[0]
                const direction = chosenSorting.split("-")[1]
                
                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);

                window.location.replace(currentUrl);
            } else {
                currentUrl.searchParams.set("sort");
                currentUrl.searchParams.set("direction");

                window.location.replace(currentUrl);
            }
        }


        // Handle quantity adjustment on Cart page
        // Increase quantity in cart input field
        function increaseCartQty() {
            const clickedBtn = this
            const productInputField = clickedBtn.parentElement.previousElementSibling.firstElementChild
            let inputValue = parseInt(productInputField.value);
            const maxValue = productInputField.getAttribute("max");
            if (inputValue < maxValue) {
                inputValue += 1;
                productInputField.value = inputValue.toString();
            }
        }

        // Decrease quantity in cart input field
        function decreaseCartQty() {
            const clickedBtn = this
            const productInputField = clickedBtn.parentElement.nextElementSibling.firstElementChild
            let inputValue = parseInt(productInputField.value);
            if (inputValue > 1) {
                inputValue -= 1;
                productInputField.value = inputValue.toString();
            }
        }

        // Update cart input field value if user tries to manually enter too many or too few
        function updateCartQty() {
            const selectedInputField = this;
            let userValue = selectedInputField.value;
            const maxValue = selectedInputField.getAttribute("max");
            if (parseInt(userValue) < 1 || userValue == "" ) {
                userValue = "1";
                selectedInputField.value = userValue;
            } else if (parseInt(userValue) > maxValue) {
                userValue = maxValue.toString();
                selectedInputField.value = userValue;
            }
        }


// Event Listeners

    // Increase quantity input value when "+" button is clicked on Product Detail page
    if (increaseQtyBtn) {
        increaseQtyBtn.addEventListener("click", increaseQty)
    }


    // Decrease quantity input value when "-" button is clicked on Product Detail page
    if (decreaseQtyBtn) {
        decreaseQtyBtn.addEventListener("click", decreaseQty)
    }


    // Update quantity value if user tries to enter a number less than 1 or greater than max available on Product Detail page
    if (quantityInputField) {
        quantityInputField.addEventListener("change", updateQty)
    }

    // Update sorting mechanic and direction on products/deals pages
    if (selectDropdown) {
        selectDropdown.forEach(dropdown => dropdown.addEventListener("change", updateSortDirection)
    )}

    // Listen for quantity adjustment of each product on cart page
    if (cartIncreaseQtyBtns) {
        cartIncreaseQtyBtns.forEach(btn => btn.addEventListener("click", increaseCartQty))
    }

    if (cartDecreaseQtyBtns) {
        cartDecreaseQtyBtns.forEach(btn => btn.addEventListener("click", decreaseCartQty))
    }

    if (cartQuantityInputFields) {
        cartQuantityInputFields.forEach(field => field.addEventListener("change", updateCartQty))
    }