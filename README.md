
# Web Scraping using two methods

Hi, I'm [Sumit Khobragade](https://github.com/SumitK69), a passionate self-taught data scientist/analyst and a student studying Bachelor's in Computer Application.
## 1: using UI automation tool Selenium

Packages:

<img src="./readme files/selenium_imports.png">

Using Selenium's webdriver to open Chrome Browser fill the username and password input section with the credentials. Navigating to the page which contains the table of account holders' holdings.


To simply run the program download the zip file unzip it in a directory on that particular directory run the code.

<code>python Main.py</code>

<img src="./readme files/selenium_output.png">

## 2:Using Requests and BeautifulSoup4

Packages:

<img src="./readme files/requests_imports.png">

Using requests to get the required website and post/send the encrypted username and password to the website directly.

The encryption process is taken care of by pycryptodome package.

Then using BeautifulSoup4 to get particular web elements to work on it directly.

Using this method does not consume as much RAM as using the Selenium method.

this method can provide results in two ways that are:

<ol>
<li>Saving the Excel file in the local directory and displaying it on Console.</li>
<li>Directly displaying it to the Console using BeautifulSoup.</li>
</ol>

To simply run the program download the zip file unzip it in a directory on that particular directory run the code.

<code>python usingrequests.py</code>

### Excel file

<img src="./readme files/Excel_Requests_output.png">


### WebView 
<img src="./readme files/WebView_Requests_output.png">