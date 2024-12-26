from django.shortcuts import render,redirect
from .models import *
from .forms import *
import random
from django.core.mail import EmailMultiAlternatives


# Create your views here.
def home(request):
    global otp
    global snewreq
    if request.method == 'POST':
        if request.POST.get('signup')=='signup':
            snewreq=signForm(request.POST)
            if snewreq.is_valid():

                
                mail = request.POST['mail']
                otp = random.randint(11111, 99999)
                sub = "Your One Time Password"
                frommail = 'policyclub.com@gmail.com'
                recipient = [mail]
                
                # Plain text message
                content = f"Your OTP code is {otp}. Please use this to verify your email."
                # HTML content
                html_content = f"""
                <html>
                <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
                    <table align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; margin: 20px auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <tr>
                        <td align="center" style="padding: 20px 0; background-color: #007bff; color: #ffffff; border-radius: 8px 8px 0 0;">
                        <h1 style="margin: 0;">Verify Your Email</h1>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 20px; text-align: center;">
                        <p style="font-size: 18px; color: #333;">Your OTP code is:</p>
                        <h2 style="font-size: 36px; color: #007bff; margin: 10px 0;">{otp}</h2>
                        <p style="font-size: 14px; color: #666;">Please enter this code to verify your email address. The code will expire in 10 minutes.</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; text-align: center; background-color: #f4f4f4; color: #777; border-radius: 0 0 8px 8px;">
                        <p style="margin: 0; font-size: 12px;">If you did not request this email, please ignore it.</p>
                        </td>
                    </tr>
                    </table>
                </body>
                </html>
                """

                # Create email
                email = EmailMultiAlternatives(
                    subject=sub,
                    body=content,  # This is the plain text content
                    from_email=frommail,
                    to=recipient
                )
                email.attach_alternative(html_content, "text/html")
                email.send()  # Send the email

                print(otp)
    
        elif request.POST.get('btnotp')=='btnotp':
            if request.POST['votp'] == str(otp):
                snewreq.save()
                print("register sucessfully")
                return render(request, 'index.html')
            else:   
                print("not store")
                return render(request, 'index.html')
            
    # if request.method == 'POST':
    #     req=otpForm(request.POST)
    #     snewreq=signForm(request.POST)
    #     if req.is_valid() or snewreq.is_valid():
    #         if request.POST['votp'] == str(otp):
    #             print(snewreq)
    #             snewreq.save()
    #             return render(request,'otpverify.html')
    #     else:
    #         print("otp not valid")
    return render(request,'index.html')


                
    


