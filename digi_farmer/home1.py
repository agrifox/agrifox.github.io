import cgi, config
print ('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Home</title>
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.py"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>
	<p><a href="index.html">Select Language</a></p><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="=right"><a href="home1.py">HOME</a> | | <a href="flogin1.py">FARMER</a> | | <a href="wlogin1.py">WHOLESALER</a> | | <a href="alogin1.py">ADMIN</a> | | <a href="contact1.html"> CONTACT US</a></nav>
	''')
import marq1
print ('''

	<blockquote><div id="div1" align="center" style="background-image: url('images/field_arable_land_agriculture_hills_road_day_60181_1920x1080.jpg'); color: white; width: 100%; height: 300px; font-family: 'Algerian';"><br><br><br><h1>"Investment in Agriculture are the best weapon against hunger and poverty,<br> and they have made life better for billions of people"</h1>
	<h2><a href="flogin1.py">Sell</a> | | | | | <a href="wlogin1.py">Buy</a></div></h2>
''')
print ('''
	<p align="left" style=" font-family: Comic Sans MS; font-size: 20px;">Agriculture is a major part of our country as well as economic and the livelihood of many people in India. Both and the farmers can sell their crop directly to the wholesale market from their field and they will get their money in real time in their linked bank account. The website has respective regional language options for your compatibility. This website have 2 user interfaces: one is for farmer and another is for wholesaler. Farmer and Seller can find and choose each others location using google map.</p>
	<p align="left" style=" font-family: Comic Sans MS; font-size: 20px;">We know that the agent gives much low price of the crop to the farmer than the allotted amount by the Govt. of India. By this website the farmers can see the real time price of their crop in wholesale market. Farmers also have the flexibility to pre-book the slot regarding their crop cutting time and they can contact to their nearby local wholesaler to sell the crop and receive the online payment from the wholesaler and vice-versa. Now our rural area can also make more contributions towards Digital India. For the availability of pre booking slot service, farmers/wholesalers are facilitating with proper planning of transportation for their crop from field to market. By this method Govt. can get the information of the income of the farmers as well as the wholesalers. The Govt. can even get the figure of exact quantity of crops produced within the season and black marketing of unlawfully storing crops in cold storage can be reduced.</p>
	</blockquote>
	''')
print ('''
  <center><footer id="footer" style="background-color: darkgrey; height: 80px">
      <div class="row text-center">
        <div class="small-18 medium-8 medium-offset-8 columns">
         <br> <p center:id="copyright">Copyright &copy; 2020 | Agri Fox</p>
        </div>
      </div>
    </footer>
  </center>
</body>
</html>
''')