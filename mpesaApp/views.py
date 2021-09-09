from django.http import HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from .models import Transactions
import json
# Create your views here.


def lipa_na_mpesa_online(request):
    amount_paid  = 1
    customer_phone_number = 254719199065
    Business_short_code = "174379"
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount_paid,
        "PartyA": customer_phone_number,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": customer_phone_number,  # replace with your phone number to get stk push
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Nelson",
        "TransactionDesc": "Nelson stk push test"
    }

    response = requests.post(api_url, json=request, headers=headers)
    data =  response.json()
    status = int(data["ResponseCode"])
    if status == 0:
        try:
            payment = Transactions(
                company_phone_number_db=customer_phone_number,
                customer_phone_number_db=customer_phone_number,
                customer_amount=amount_paid,
                Business_short_code_db=Business_short_code,
            )
            payment.save()
            return HttpResponse('saved sucessfull')
        except:
            return HttpResponse(status)
    else:
        return HttpResponse('failed computing')


# def get_data(companynumber1,customernumber2,amountpaid,short_code,):
#     payment = Transactions(
#                 company_phone_number_db=companynumber1,
#                 customer_phone_number_db=customernumber2,
#                 customer_amount=amountpaid,
#                 Business_short_code_db=short_code,
#             )
#     payment.save()

# @csrf_exempt
# def confirmation(request):
#     mpesa_body =request.body.decode('utf-8')
#     mpesa_payment = json.loads(mpesa_body)

#     payment = Transactions(
#         first_name=mpesa_payment['FirstName'],
#         last_name=mpesa_payment['LastName'],
#         middle_name=mpesa_payment['MiddleName'],
#         description=mpesa_payment['TransID'],
#         phone_number=mpesa_payment['MSISDN'],
#         amount=mpesa_payment['TransAmount'],
#         reference=mpesa_payment['BillRefNumber'],
#     )
#     payment.save()

#     return HttpResponse('sucessfull')