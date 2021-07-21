# Cryptocoin_CSK-Web_Scraper
-------------------------------------------------
  coinswitch kuber[CSK] - cryptocoin - notifier 
-------------------------------------------------

Web Scraping – Crypto Coin Provider Company (Coin Switch Kuber [CSK])
With the help the script written in python you can do scraping of almost all website (but one should have prior (Basic) knowledge of web-development and python)
Why have I made this?

As like many other crypto coin provider players in market CSK application not providing me any feature of alert when price goes down or up which lead me to make this 😊 To Save my Money.

Objective:

•	To Send alert @every 15 sec by means of sound (if any speaker is attached to on running script device for me, initially it was my laptop and finally get it incorporate with raspberry pi_4(SBC) with speaker which work as my DIY Server + Smart Speaker for different- different application) and email.

•	It offers you a .csv where u can name coin fallowed by price (at which u want alert to get trigger).

Setting:
1)	For sale keep it like as:  
2)	For buy chenge the operator to > (Less than)
    o	Note:- Please make change in price a/c to case u want to opt for (Inside .csv).
    
3)	Email: - Make it sure that you had enable the 2-step verification for email which you going to use for sending mails (when test case meets your fixed threshold).
  For App password creation fallow these steps:

      a.	Go to your Google Account.

      b.	Select Security.

      c.	Under "Signing into Google," select App Passwords. You may need to sign in. If you do not have this option, it might be because:

      d.	2-Step Verification is not set up for your account.

      e.	2-Step Verification is only set up for security keys.

      f.	Your account is through work, school, or other organization.

      g.	You turned on Advanced Protection.

      h.	At the bottom, choose Select app and choose the app you are using (i.e. Other) Select device and choose the device (Window/Linux) you are using Generate.

      i.	Follow the instructions to enter the App Password. The App Password is the 16-character code like (fig2 line no 92) in the yellow bar on your device.
 
Change the red doted row according to sender email with which  generated  password.

Prerequisite: After python installation completed open CLI/CMD copy and paste below line:

    •	pip install pandas
    •	pip install beautifulsoup4
    •	pip install playsound
    •	pip install requests
By default, smtplib library is present in python3.9

Working GIF:


