                                                        ** 11 July 2026 **


## WHAT IS A COOKIE?

A cookie is a small piece of data stored in the browser by a website.

Whenever you visit that website again, the browser automatically sends the cookie back to the website, allowing it to recognize you or remember information such as whether you're logged in.

( Real life Example-
You visit a library. The librarian gives you a identity card. So if u visit again in future and show the card to hom the librarian will remember you.)


## Why session imp?
A session is a way for Flask to remember information about a user across different requests.

Like to prevent- for example if someone opens my website and to avoide password inputing they can enter the url directly like /home and jump to taht page without password. -- Session prevents that from happening.


## Render_tenplate Vs Redirect

>>Render - it sends the html file to the browser and the browser opens it.

>>Redirect - it send only the URL to the BROWSER and then the browser sends that url to the Flask if will then match the address(url) and execute the function if url matched matched 