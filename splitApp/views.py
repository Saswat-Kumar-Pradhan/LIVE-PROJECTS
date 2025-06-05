from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from datetime import datetime

# Predefined recipient list (could also be put in settings)
RECIPIENT_LIST = [
    'saswatkumar059@gmail.com',
    'msiddharthkumar2000@gmail.com',
    'soma756126@gmail.com',
    'rajxid836@gmail.com',
    'nayaksubrat030247@gmail.com',
    'mangesh.mane95@gmail.com',
    'sumankumarpradhan789@gmail.com'
]
def send_youtube_monthly_split(request):
    if request.method == 'POST':
        selected_month = request.POST.get('month', '')
        formatted_month = datetime.strptime(selected_month, "%Y-%m").strftime("%B %Y")
        if formatted_month:
            subject = f"YouTube Premium plans in {formatted_month}."
            message = f"""
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>

            <body style="font-family: Arial, sans-serif; margin: 0; padding: 2px;">
                <div class="container" style="max-width: 650px; margin: auto;">
                    <div class="mainPic" style="margin: 40px auto 0px; text-align: left;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/YouTube_Premium_logo.svg/2560px-YouTube_Premium_logo.svg.png"
                            alt="Youtube Premium" style="width: 130px;">
                    </div>
                    <h1 style="font-size: 35px; margin-top: 15px; text-align: left;">Split Revenue <br />For <span
                            style="color: green;">{formatted_month}</span></h1>
                    <div class="block"
                        style="border: 1px solid #ddd; border-radius: 8px; width: calc(100% - 40px); padding: 20px; margin-bottom: 20px;">
                        <h2 style="margin-top: 0; font-size: 25px;">Expense Split</h2>
                        <div style="display: flex;">
                            <div style="border-right: 1px solid #ddd; padding-right: 20px;">
                                <p style="font-size: 12px; margin: 5px 0px;"><a href="mailto:saswatkumar059@gmail.com"
                                        style="color: black; margin-right: 5px; text-decoration: none;">Saswat Kumar Pradhan</a>(50)</p>
                                <p style="font-size: 12px; margin: 5px 0px;"><a href="mailto:saswatkumar059@gmail.com"
                                        style="color: black; margin-right: 5px; text-decoration: none;">M. Siddharth Kumar</a>(50)</p>
                                <p style="font-size: 12px; margin: 5px 0px;"><a href="mailto:saswatkumar059@gmail.com"
                                        style="color: black; margin-right: 5px; text-decoration: none;">Mangesh mane</a>(50)</p>
                                <p style="font-size: 12px; margin: 5px 0px;"><a href="mailto:saswatkumar059@gmail.com"
                                        style="color: black; margin-right: 5px; text-decoration: none;">Somanath Mohapatra</a>(50)</p>
                                <p style="font-size: 12px; margin: 5px 0px;"><a href="mailto:saswatkumar059@gmail.com"
                                        style="color: black; margin-right: 5px; text-decoration: none;">Subrat Prasad Nayak</a>(50)</p>
                                <p style="font-size: 12px; margin: 5px 0px;"><a href="mailto:saswatkumar059@gmail.com"
                                        style="color: black; margin-right: 5px; text-decoration: none;">Suman Kumar Pradhan</a>(50)</p>
                            </div>
                            <div style="margin-left: auto; margin-top: 5px; font-size: 12px; text-align: right;">
                                <p>YT Plan: ₹300</p>
                                <p style="margin-bottom: 6px;">Total Members: 6</p>
                                <hr style="margin-top: 13px;">
                                <p>Per Member : ₹50</p>
                            </div>
                        </div>
                        <a href="https://saswatkumar.com/pages/youtube" class="btn" style="text-decoration: none;">
                            <div
                                style="width: 40%; margin: 20px calc(30%) 0; background-color: red; padding: 10px 0px; color: white; text-align: center; border-radius: 6px;">
                                Check Status
                            </div>
                        </a>
                        <p style="text-align: center; font-size: 8px; margin-bottom: 0; color: gray;">View detailed monthly payment status here.</p>
                    </div>
                    <div class="block"
                        style="border: 1px solid #ddd; border-radius: 8px; width: calc(100% - 40px); padding: 20px; margin-bottom: 20px;">
                        <h2 style="margin-top: 0; font-size: 25px;">Payment Option</h2>
                        <div class="row"
                            style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <div class="desc"
                                style="width: 500px; border-right: 1px solid #ddd; margin-right: 15px; padding-right: 10px;">
                                <p style="margin: 0; font-size: 12px;">Scan the QR Code displayed here using any UPI-enabled app Or
                                    use the UPI ID: saswatkumar@upi</p><br>
                                <p style="margin: 0; font-size: 12px;">Click on the "Pay Now" button below to proceed with direct
                                    payment.</p>
                            </div>
                            <img class="qr" src="https://saswatkumar.com/pages/GooglePay_QR%20(2).jpg" alt="qr code"
                                style="width: 150px; height: 150px;">
                        </div>
                        <a href="https://saswatkumar.com/pages/youtubePayment" class="btn2" style="text-decoration: none;">
                            <div
                                style="width: 40%; margin: 20px calc(30%) 0; background-color: royalblue; padding: 10px 0px; color: white; text-align: center; border-radius: 6px;">
                                Pay Now</div>
                        </a>
                        <p style="text-align: center; font-size: 10px; color: gray;">supported by</p>
                        <div style="font-size: 12px; text-align: center; margin-top: 6px;">
                            <img style="height: 15px; margin: auto 5px;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Google_Pay_Logo.svg/1200px-Google_Pay_Logo.svg.png" alt="">
                            <img style="height: 14px; margin: auto 5px;" src="https://upload.wikimedia.org/wikipedia/commons/4/42/Paytm_logo.png" alt="">
                            <img style="height: 11px; margin: auto 5px;" src="https://tinuiti.com/wp-content/uploads/legacysitecontent/cpcs/posts_01/2018/12/23161707/Amazon-Pay-logo-1024x197.png" alt="">
                            <img style="height: 15px; margin: auto 5px;" src="https://cdn2.downdetector.com/static/uploads/logo/apple-pay.png" alt="">
                        </div>
                        <p style="text-align: center; font-size: 8px; margin-bottom: 0; color: gray;">Support for PhonePe and BHIM app coming soon.</p>

                    </div>
                    <p class="footerDesc" style="text-align: center; margin: 30px 20px 20px; font-size: 12px;">Unlock endless joy
                        with YouTube
                        Premium, YouTube Kids, and YouTube Music! Dive into ad-free content and limitless entertainment today!</p>
                    <img class="footerImage" src="https://miro.medium.com/v2/resize:fit:1400/1*vNWQi_uRDnm4Y5uYqq9zkw.png" alt=""
                        style="width: 100%; margin: 0px auto;">
                </div>
            </body>

            </html>
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            email = EmailMessage(subject, message, from_email, RECIPIENT_LIST)
            email.content_subtype = "html"  # Specify the email content type as HTML
            email.send()

            messages.success(request, f"Email sent for {formatted_month}!")
            return redirect('send_youtube_monthly_split')  # Replace with your desired redirect

    return render(request, 'month_form.html')

def send_youtube_monthly_receipt(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        for_month = request.POST.get('month', '')
        amount = request.POST.get('amount', '')
        transaction_id = request.POST.get('transactionId', '')
        received_date = request.POST.get('receivedDate', '')
        received_time = request.POST.get('receivedTime', '')
        payment_from = request.POST.get('paymentFrom', '')
        # formatted_month = datetime.strptime(selected_month, "%Y-%m").strftime("%B %Y")
        if email:
            subject = f"Payment Receipts for YouTube Premium."
            message = f"""
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>

            <body style="font-family: Arial, sans-serif; margin: 0; padding: 2px;">
                <div class="container" style="max-width: 650px; margin: auto;">
                    <div class="mainPic" style="margin: 40px auto 0px; text-align: left;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/YouTube_Premium_logo.svg/2560px-YouTube_Premium_logo.svg.png"
                            alt="Youtube Premium" style="width: 130px;">
                    </div>
                    <h1 style="font-size: 20px; margin: 25px 0 5px; text-align: left;">Hi {name}</h1>
                    <p class="footerDesc" style="text-align: left; margin: 0px 20px 20px 0; font-size: 12px;">Thank you for being a
                        valued part of our YouTube Premium family. Your support means the world to us. We're thrilled to have you
                        with us on this ad-free, entertainment-filled journey!</p>
                    <div style="text-align: center;">
                        <p style="font-size: 23px; font-weight: bold; margin: 10px;">Recieved</p>
                        <p style="font-size: 40px; font-weight: bolder; color: green; margin: 0;">₹{amount}</p>
                        <p style="font-size: 13px; font-weight: bold; margin: 10px 0 5px; color: rgb(66, 66, 66);">for the month of
                        </p>
                        <p style="font-size: 25px; font-weight: bold; margin: 0px 0 30px; color: royalblue;">{for_month}</p>
                    </div>
                    <div class="block"
                        style="border: 1px solid #ddd; border-radius: 8px; width: calc(100% - 20px); padding: 10px; margin-bottom: 20px; font-weight: bold; color: grey;">
                        <table spacing="0" cellpadding="0" cellspacing="10">
                            <tbody style="font-size: 12px;">
                                <tr>
                                    <td>Transaction ID</td>
                                    <td>: {transaction_id}</td>
                                </tr>
                                <tr>
                                    <td>Recieved On</td>
                                    <td>: {received_date} ({received_time})</td>
                                </tr>
                                <tr>
                                    <td>Payment From</td>
                                    <td>: {payment_from}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <p class="footerDesc" style="text-align: center; margin: 30px 20px 20px; font-size: 12px;">If you have any
                        questions about the payment, just reply to this message
                        <br /><br />we’re here to help!
                        We want to make sure everything is smooth and hassle-free for you.
                        Thanks again for being a part of our YouTube Premium family.
                        Sit back, relax, and enjoy top-notch entertainment with no interruptions!
                    </p>
                    <img class="footerImage" src="https://miro.medium.com/v2/resize:fit:1400/1*vNWQi_uRDnm4Y5uYqq9zkw.png" alt=""
                        style="width: 100%; margin: 0px auto;">
                </div>
            </body>

            </html>

            """
            from_email = settings.DEFAULT_FROM_EMAIL
            email = EmailMessage(subject, message, from_email, [email])
            email.content_subtype = "html"  # Specify the email content type as HTML
            email.send()

            messages.success(request, f"Email sent to {name}!")
            return redirect('send_youtube_monthly_receipt')  # Replace with your desired redirect

    return render(request, 'receipt_form.html')
