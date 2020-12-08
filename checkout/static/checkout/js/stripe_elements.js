const stripePublicKey = document.querySelector("#id_stripe_public_key").textContent.slice(1, -1);
const clientSecret = document.querySelector("#id_client_secret").textContent.slice(1, -1);
console.log(stripePublicKey)
console.log(clientSecret)
const stripe = Stripe(stripePublicKey)
const elements = stripe.elements();

const style = {
    base: {
        color: '#000',
        fontWeight: 500,
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
            color: '#fce883',
        },
        '::placeholder': {
            color: '#AAB7C4',
        },
    },
        invalid: {
            iconColor: '#DC3545',
            color: '#DC3545',
    },
}

const card = elements.create("card", {style: style});
card.mount("#card-element")

// Display errors after user enters card details if necessary 
card.addEventListener("change", function(e) {
    const errorDiv = document.querySelector("#card-errors");
    if (e.error) {
        const errorHtml = `
        <span class="icon" role="alert">
            <i class="fas fa-exclamation-triangle error"></i>
        </span>
        <span>${e.error.message}</span>
        `;
        errorDiv.innerHTML = errorHtml;
    } else {
        errorDiv.textContent = "";
    }
})

// Handle form submission
const form = document.querySelector("#checkout-form")

form.addEventListener("submit", function(e) {
    e.preventDefault();
    const submitBtn = document.querySelector("#checkout-button")
    card.update({"disabled": true});
    submitBtn.setAttribute("disabled", true);

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billingDetails: {
                name: form.full_name.value.trim(),
                email: form.email.value.trim(),
                address: {
                    addressLine1: form.street_address1.value.trim(),
                    addressLine2: form.street_address2.value.trim(),
                    townOrCity: form.town_or_city.value.trim(),
                    countyOrState: form.county_or_state.value.trim(),
                    country: form.country.value.trim(),
                }
            }
        },
        shipping: {
            name: form.full_name.value.trim(),
            email: form.email.value.trim(),
            address: {
                addressLine1: form.street_address1.value.trim(),
                addressLine2: form.street_address2.value.trim(),
                townOrCity: form.town_or_city.value.trim(),
                countyOrState: form.county_or_state.value.trim(),
                postCode: form.postcode.value.trim(),
                country: form.country.value.trim(),
                }
            },
    }).then(function(result) {
        if(result.error) {
            const errorDiv = document.querySelector("#card-errors");
            const errorHtml = `
            <span class="icon" role="alert">
                <i class="fas fa-exclamation-triangle error"></i>
            </span>
            <span>${result.error.message}</span>
            `;
            errorDiv.innerHTML = errorHtml;
            card.update({"disabled": true});
            submitBtn.setAttribute("disabled", true);
        } else {
            if (result.paymentIntent.status === "succeeded") {
                form.submit()
            }
        }
    })
})
