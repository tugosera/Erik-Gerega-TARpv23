for i in range(5):

    import smtplib, ssl

    smtp_server = "smtp.gmail.com"
    port = 587
    to_email = "erik.gerega@gmail.com"
    sender_email = "erik.gerega@gmail.com"
    password = "dplj cluh drnm exef"

    #Create a secure SSL context
    context = ssl.create_default_context()
    msg="HUI"
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() #Can be omitted
        server.starttls(context=context)
        server.ehlo() #Can be omitted
        server.login(sender_email,password)
        server.sendmail(sender_email,to_email,msg)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


    "dplj cluh drnm exef"