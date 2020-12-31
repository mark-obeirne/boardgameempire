// Materialize Initialisation
document.addEventListener('DOMContentLoaded', function () {
    let elems = document.querySelectorAll('select');
    let instances = M.FormSelect.init(elems, {});
});


// Element Selectors

const billingCheckbox = document.querySelector("#same-billing-shipping");
const pointsToUse = document.querySelector("#id_points_used");
const inputFields = document.querySelectorAll(".delivery-input-field");

// Functions

// Show or hide billing details section based on checkbox to indicate that billing details match delivery details
function toggleBillingDetails() {
    const billingDetails = document.querySelector(".billing-details");
    if (billingCheckbox.checked) {
        billingDetails.classList.add("none");
        autofillBilling();
    }
    else {
        billingDetails.classList.remove("none");
        autofillBilling();
    }
}

// Autofill billing details if user checks box to indicate that billing details match delivery details
function autofillBilling() {
    if (billingCheckbox.checked) {
        form.billing_full_name.value = form.full_name.value;
        form.billing_street_address1.value = form.street_address1.value;
        form.billing_street_address2.value = form.street_address2.value;
        form.billing_town_or_city.value = form.town_or_city.value;
        form.billing_county_or_state.value = form.county_or_state.value;
        form.billing_country.value = form.country.value;
    }
    else {
        form.billing_full_name.value = "";
        form.billing_street_address1.value = "";
        form.billing_street_address2.value = "";
        form.billing_town_or_city.value = "";
        form.billing_county_or_state.value = "";
        form.billing_country.value = "";
    }
}

// Update grand total as user opts to use loyalty points

function updateGrandTotal() {
    // Get cart total and points user has opted to use
    const cartTotal = document.querySelector(".cart-total");
    let cartTotalText = cartTotal.innerText;
    const regex = /[€\s]/g;
    let totalToPay = parseFloat(cartTotalText.replace(regex, ""));
    const userInputPoints = pointsToUse.value;
    const pointsCashEquivalent = userInputPoints / 500;

    // Get delivery cost
    let deliveryCost = 0;
    const deliveryText = document.querySelector(".delivery-cost");
    if (deliveryText.innerText === "€6.00") {
        deliveryCost = 6;
    }

    // Calculate cart total remaining
    const cartTotalRemaining = (totalToPay - pointsCashEquivalent + deliveryCost).toFixed(2);
    const cartTotalRemainingText = "€" + cartTotalRemaining.toString();

    // Change grand total text values
    let grandTotal = document.querySelectorAll(".grand-total");
    grandTotal.forEach(total => total.innerText = cartTotalRemainingText);
}


// Update points available to use number select limits

function setPointsAvailable() {
    const pointsToUse = document.querySelector("#id_points_used");
    if (pointsToUse) {
        const pointsAvailable = document.querySelector(".user-loyalty-points").textContent;
        pointsToUse.setAttribute("min", "0");
        pointsToUse.setAttribute("max", pointsAvailable);
        pointsToUse.setAttribute("step", "50");
    }
}


// Check loyalty points entered are valid if user enters number manually
function checkValidPointsUsed() {
    const pointsAvailable = parseInt(document.querySelector(".user-loyalty-points").textContent);
    const userEnteredPoints = parseInt(pointsToUse.value);

    // Check if user enters a points value that is less than 0 or greater than loyalty points earned
    if (userEnteredPoints < 0) {
        pointsToUse.value = 0;
    }
    else if (userEnteredPoints > pointsAvailable) {
        // Check if user enters a points value greater than what is available
        if (pointsAvailable === 0) {
            pointsToUse.value = 0;
        }
        else {
            // Check if pointsAvailable is divisible by 50 and remove remainder to use a multiple of 50 if not
            const remainder = pointsAvailable % 50;
            if (remainder) {
                pointsToUse.value = pointsAvailable - remainder;
            }
        }
    }
    else if (userEnteredPoints % 50 != 0) {
        const excessPoints = userEnteredPoints % 50;
        pointsToUse.value = userEnteredPoints - excessPoints;
    }
}


// Event Listeners

// Show or hide billing details section based on checkbox to indicate that they match delivery details
billingCheckbox.addEventListener("change", toggleBillingDetails);

// Check loyalty points entered are valid if user enters number manually
if (pointsToUse) {
    pointsToUse.addEventListener("change", checkValidPointsUsed);
}

// Update grand total as user opts to use loyalty points
if (pointsToUse) {
    pointsToUse.addEventListener("change", updateGrandTotal);
}

// Update points available to use number select limits
if (pointsToUse) {
    document.addEventListener('DOMContentLoaded', setPointsAvailable);
}

// Update billing details as delivery details filled in
inputFields.forEach(inputField => inputField.addEventListener("change", autofillBilling));