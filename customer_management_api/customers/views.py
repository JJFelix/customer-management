from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

# africastalking
from .sms_service import SMSService

# OIDC auth0
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

oauth  = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope":"openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)
# login endpoint
@api_view(['GET'])
def login(request):
    # redirect_uri = request.build_absolute_uri(reverse("callback"))
    redirect_uri = "https://customer-management-api-grx3.onrender.com/api/callback"
    return oauth.auth0.authorize_redirect(request, redirect_uri)

# callback endpoint after successful login
@api_view(['GET'])
def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    # send token to frontend
    return redirect(f"https://customer-management-client.onrender.com")#?token={token["access_token"]}")


def logout(request):
    request.session.clear()

    logout_url = (
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                # "returnTo": request.build_absolute_uri(reverse("index")),
                "returnTo": "https://customer-management-client.onrender.com",
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        )
    )
    return redirect(logout_url)

# homepage
@api_view(['GET'])
def index(request):
    user = request.session.get("user", None)
    if not user:
        return Response({"error": "User not logged in"}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({
        "session": user,
        "pretty": json.dumps(user, indent=4),
    })

# check login status
@api_view(['GET'])
def is_logged_in(request):
    user = request.session.get("user", None)
    if user:
        return Response({"logged_in": True, "user": user}, status=status.HTTP_200_OK)
    else:
        return Response({"logged_in": False}, status=status.HTTP_401_UNAUTHORIZED)

# test page
@api_view(['GET'])
def test(request):
    return Response({"message": "Test successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response({"message": "Customers retrieved", "data": serializer.data, }, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_customer(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    orders = Order.objects.filter(customer=customer)

    customer_serializer = CustomerSerializer(customer)
    order_serializer = OrderSerializer(orders, many=True)

    return Response({
        "message": "Customer retrieved", 
        "customer": customer_serializer.data, 
        "orders": order_serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_customer(request):
    serializer = CustomerSerializer(data=request.data)

    # check if the data provided is valid
    if serializer.is_valid():
        serializer.save() # save new customer record
        print("Customer added successfully")
        return Response({'success': 'Customer added successfully'}, status=status.HTTP_201_CREATED)

    # logging errors if data is invalid    
    print(serializer.errors)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_customer(request):
    # serializer = CustomerSerializer(data=request.data)

    # # check if the data provided is valid
    # if serializer.is_valid():
    #     serializer.save() # save new customer record
    #     print("Customer added successfully")
    #     return Response({'success': 'Customer added successfully'}, status=status.HTTP_201_CREATED)

    # # logging errors if data is invalid    
    # print(serializer.errors)
    # return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": 'Hello'})


def update_customer(request):
    pass

@api_view(['DELETE'])
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    customer.delete()
    print('Customer deleted')
    return Response({'success': 'Customer deleted'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response({"message": "Orders retrieved", "data": serializer.data, }, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_order(request):
    serializer = OrderSerializer(data=request.data)

    # check if the data provided is valid
    if serializer.is_valid():
        order = serializer.save() # save new order record

        # retrieve customer's phone number
        phone_number = order.customer.phone

        # send SMS to customer
        message = f"Dear {order.customer.name}, \
            your order for {order.item}, Amount: {order.amount}\
                has been received."

        sms_service = SMSService()
        try:
            sms_response = sms_service.send_sms([phone_number], message, settings.AFRICAS_TALKING_SENDER_CODE)
            print("SMS Sent to customer:", sms_response)
        except Exception as e:
            print(f"Failed to send SMS: {e}")

        print("Order added successfully")
        # send message to client
        return Response({'success': 'Order added successfully'}, status=status.HTTP_201_CREATED)    

    # logging errors if data is invalid    
    print(serializer.errors)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

def update_order(request):
    pass

@api_view(['DELETE'])
def delete_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    order.delete()
    print('Order deleted')
    return Response({'success': 'Order deleted'}, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def login(request):
    
#     return oauth.auth0.authorize_redirect(
#         request, request.build_absolute_uri(reverse("callback"))
#     )


# @api_view(['GET'])
# def callback(request):
#     token = oauth.auth0.authorize_access_token(request)
#     request.session["user"] = token
#     return redirect(request.build_absolute_uri(reverse("index")))


# def logout(request):
#     request.session.clear()

#     return redirect(
#         f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": request.build_absolute_uri(reverse("index")),
#                 "client_id": settings.AUTH0_CLIENT_ID,
#             },
#             quote_via=quote_plus,
#         ),
#     )


# def index(request):
#     return render(
#         request, 
#         "index.html",
#         context={
#             "session": request.session.get("user"),
#             "pretty": json.dumps(request.session.get("user"), indent=4),
#         }
#     )
