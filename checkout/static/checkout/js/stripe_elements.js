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