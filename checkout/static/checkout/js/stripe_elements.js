// Get Stripe Public Key, Client Secret, and create an instance of Stripe
const stripePublicKey = document.querySelector("#id_stripe_public_key").textContent.slice(1, -1);
const clientSecret = document.querySelector("#id_client_secret").textContent.slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// Set style
const style = {
    base: {
        color: '#392417',
        fontWeight: 500,
        fontFamily: '"Open Sans", sans-serif',
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
};

// Create and mount card element
const card = elements.create("card", {
    style: style
});
card.mount("#card-element");

// Display errors after user enters card details if necessary 
card.addEventListener("change", function (e) {
    const errorDiv = document.querySelector("#card-errors");
    if (e.error) {
        const errorHtml = `
        <span class="icon" role="alert">
            <i class="fas fa-exclamation-triangle error"></i>
        </span>
        <span>${e.error.message}</span>
        `;
        errorDiv.innerHTML = errorHtml;
    }
    else {
        errorDiv.textContent = "";
    }
});

// Handle form submission
const form = document.querySelector("#checkout-form");

form.addEventListener("submit", function (e) {
    e.preventDefault();
    let postData;
    const submitBtn = document.querySelector("#checkout-button");
    const spinnerOverlay = document.querySelector("#spinner-overlay");
    card.update({
        "disabled": true
    });
    submitBtn.setAttribute("disabled", true);
    spinnerOverlay.classList.remove("none");

    const csrfToken = document.querySelector("input[name='csrfmiddlewaretoken']").value;
    const giftPurchase = document.querySelector("#gift_purchase").checked;
    const pointsId = document.querySelector("#id_points_used");

    if (pointsId) {
        const pointsUsed = pointsId.value;
        postData = {
            "csrfmiddlewaretoken": csrfToken,
            "client_secret": clientSecret,
            "gift_purchase": giftPurchase,
            "points_used": pointsUsed
        };
    }
    else {
        postData = {
            "csrfmiddlewaretoken": csrfToken,
            "client_secret": clientSecret,
            "gift_purchase": giftPurchase
        };
    }
    const url = "/checkout/cache_checkout_data/";

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.billing_full_name.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.billing_street_address1.value.trim(),
                        line2: form.billing_street_address2.value.trim(),
                        city: form.billing_town_or_city.value.trim(),
                        state: form.billing_county_or_state.value.trim(),
                        country: form.billing_country.value.trim(),
                    }
                }
            },
            shipping: {
                name: form.full_name.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    state: form.county_or_state.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    country: form.country.value.trim(),
                }
            },
        }).then(function (result) {
            if (result.error) {
                let errorDiv = document.getElementById('card-errors');
                let html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                spinnerOverlay.classList.add("none");
                card.update({
                    'disabled': false
                });
                $('#submit-button').attr('disabled', false);
            }
            else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
})