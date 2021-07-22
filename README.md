# Cryptocoin_CSK-Web_Scraper
-------------------------------------------------
  coinswitch kuber[CSK] - cryptocoin - notifier 
-------------------------------------------------

Web Scraping(web data extraction) – One can choose any website to do scraping like me. I had chosen Crypto Coin Provider Company (Coin Switch Kuber [CSK]) and used python and its library to do data harvesting.

Why have I made this?

As like many other crypto coin provider players in the market CSK application does not providing any feature of alert to let us determine when the price goes down or up which leads me to make this 😊 To Save $Money$.

**Objective:**

  •	To Send alert @every 15 sec by means of sound (if any speaker is attached to on running script device for me, initially it was my laptop and finally get it incorporate with raspberry pi_4(SBC) with speaker which work as my DIY Server + Smart Speaker for different- different application) and email.

  •	It offers you a .csv where you can name coin fallowed by price (at which you want alert to get invoke).

**Setting:**
1)	For sale keep it like as:  
![image](https://user-images.githubusercontent.com/65926581/126496465-36fd2761-8aa2-4ad9-8fce-3bd7b4cd4587.png)
3)	For buy chenge the operator to > (Less than)
    o	Note:- Please make change in price according to case you want to opt for (Inside .csv).
    
3)	Email: - Make it sure that you have enable the 2-step verification for email which you are going to use for sending mails (when test case meets your fixed threshold).
  For App password creation fallow these steps:

      a.	Go to your Google Account.

      b.	Select Security.

      c.	Under "Signing into Google," select App Passwords. You may need to sign in. If you do not have this option, it might be because:

      d.	2-Step Verification is not set up for your account.

      e.	2-Step Verification is only set up for security keys.

      f.	Your account is through work, school, or other organization.

      g.	You have turned on Advanced Protection.

      h.	At the bottom, choose Select app and choose the app you are using (i.e. Other) Select device and choose the device (Window/Linux) you are using to Generate.

      i.	Follow the instructions to enter the App Password. The App Password is the 16-character code like (fig2 line no 91) in the yellow bar on your device.
      
      ![image](https://user-images.githubusercontent.com/65926581/126496755-c7fd693c-44af-4b98-b507-6e1547a713ca.png)
 
Change the red doted row according to sender email with which  generated  password.

**Prerequisite:** After python installation completed open CLI/CMD copy and paste below line:

    •	pip install pandas
    •	pip install beautifulsoup4
    •	pip install playsound
    •	pip install requests
By default, smtplib library is present in python3.9

**Working GIF:**
![CSK-W](https://user-images.githubusercontent.com/65926581/126498941-19283747-4573-440d-be01-f8dca971e436.gif)


