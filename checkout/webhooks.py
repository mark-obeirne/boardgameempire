from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler
import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for webhooks from Stripe """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    print(wh_secret)
    
    # Getting webhook data and verifying signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    print(sig_header)
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        print("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print("Invalid sig")
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Setup webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        "payment_intent.succeeded": handler.handle_payment_intent_succeeded,
        "payment_intent.payment_failed": handler.handle_payment_intent_failed
    }

    # Get webhook type from Stripe
    event_type = event["type"]

    # If there is a handler for this type, get it from the event map
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call event handler with the event
    response = event_handler(event)
    return response
