from flask import Flask, render_template,request,redirect,url_for
import pymysql
import cgi
import os
import datetime
		

db= pymysql.connect('localhost','timmy','timmy00123','L')


a1='''
	<!DOCTYPE html>
	<html>
	<head>
		<title></title>
		
		

	</head>
	<body>

		<style type="text/css">
		
		#head{
			width:90%;
			padding:15px;
			}

		#head-bar{
			width:99%;
			padding:15px;
			margin-top: 1%;
			background: orange;
			}

				
			}
		#body {
			background-color:#FFFFFF;
			color:#000000;
			width: 80%;
			float: right;
			margin-top: 1%
			}

		#left{
			background-color:#FFDDAA;
			width: 20%;
			float: left;
			margin-top: 5%;
			
			}
		#right {
			background-color:#FFFFFF;
			color:#000000;
			width: 75%;
			float: right;
			margin-top: 1%
			}
	
		#linkbutton {
			background:none!important;
	 		color:inherit;
	 		border:none; 
	 		padding:0!important;
	 		font: inherit;
		 	border-bottom:1px solid #444; 
		 	cursor: pointer;
		 	color:blue
			}


	</style>
  
  	<!-- bar -->
	
	<form action="/product_s" id="head" method="post">
		<a href="/"  style="float: left;"><img src="/static/logo.png" width=50 alt="logo"></a>
		<input type="submit" value="Search" style="float: right;">
		<input type="text" name="key" placeholder="Bookname / Author / Publisher " style="float: right;">
	</form>

	<table id="head-bar">
		<tr>
		<td><a href="product" style="float: left;">Products</a></td>
		<td width=2%>&nbsp;</td>
		<td><a href="shoppingcart" style="float: left;">Shopping Cart</a></td>
		<td width=2%>&nbsp;</td>
		<td><a href="personal" style="float: left;">Personal</a></td>
		<td width=2%>&nbsp;</td>
		<td><a href="aboutus" style="float: left;">About us</a></td>
		<td width=30%>&nbsp;</td>
		<td><a href="logon" style="float: right;">Logon</a></td>
		<td width=2%>&nbsp;</td>
		<td><a href="register" style="float: right;">Register</a></td>
		</tr>
	</table>

  	'''

a2='''
	<!DOCTYPE html>
	<html>
	<head>
		<title></title>

		


	</head>
	<body>
		<style type="text/css">

		#head{
			width:90%;
			padding:15px;
			}

		#head-bar{
			width:99%;
			padding:15px;
			margin-top: 1%;
			background: orange;
			}

				
			}
		#body {
			background-color:#FFFFFF;
			color:#000000;
			width: 80%;
			float: right;
			margin-top: 1%
			}

		#left{
			background-color:#FFDDAA;
			width: 20%;
			float: left;
			margin-top: 5%;
			
			}
		#right {
			background-color:#FFFFFF;
			color:#000000;
			width: 75%;
			float: right;
			margin-top: 1%
			}

		#linkbutton {
			background:none!important;
	 		color:inherit;
	 		border:none; 
	 		padding:0!important;
	 		font: inherit;
		 	border-bottom:1px solid #444; 
		 	cursor: pointer;
		 	color:blue
			}
	</style>
  
  	<!-- bar -->
	
	<form action="/product_s" id="head" method="post">
		<a href="/"  style="float: left;"><img src="/static/logo.png" width=50 alt="logo"></a>
		<input type="submit" value="Search" style="float: right;">
		<input type="text" name="key" placeholder="Bookname / Author / Publisher " style="float: right;">
	</form>


  	<table id="head-bar">
	 	<tr>
		<td><a href="product" style="float: left;">Products</a></td>
		<td width=2%>&nbsp;</td>
   		<td><a href="shoppingcart" style="float: left;">Shopping Cart</a></td>
		<td width=2%>&nbsp;</td>
		<td><a href="personal" style="float: left;">Personal</a></td>
		<td width=2%>&nbsp;</td>
		<td><a href="aboutus" style="float: left;">About us</a></td>
		<td width=30%>&nbsp;</td>
		<td><a href="logout" style="float: right;">Logout</a></td>
		<td width=2%>&nbsp;</td>
		</tr>
  	</table>

  	'''

a3='''
	<!DOCTYPE html>
	<html>
	<head>
		<title></title>

		


	</head>
	<body>
		<style type="text/css">

		#head{
			width:90%;
			padding:15px;
			}

		#head-bar{
			width:99%;
			padding:15px;
			margin-top: 1%;
			background: orange;
			}

				
			}
		#body {
			background-color:#FFFFFF;
			color:#000000;
			width: 80%;
			float: right;
			margin-top: 1%
			}

		#left{
			background-color:#FFDDAA;
			width: 20%;
			float: left;
			margin-top: 5%;
			
			}
		#right {
			background-color:#FFFFFF;
			color:#000000;
			width: 75%;
			float: right;
			margin-top: 1%
			}

		#linkbutton {
			background:none!important;
	 		color:inherit;
	 		border:none; 
	 		padding:0!important;
	 		font: inherit;
		 	border-bottom:1px solid #444; 
		 	cursor: pointer;
		 	color:blue
			}
	</style>
  
  	<!-- bar -->
	
	
	<a href="/"  style="float: left;"><img src="/static/logo.png" width=50 alt="logo"></a>

  	<table id="head-bar">
	 	<tr>
		<td><a href="admin_product" style="float: left;">Products</a></td>
		<td width=2%>&nbsp;</td>
   		<td><a href="admin_customer" style="float: left;">Customers</a></td>
		<td width=2%>&nbsp;</td>
		<td><a href="admin_account" style="float: left;">Admin</a></td>
		<td width=30%>&nbsp;</td>
		<td><a href="logout" style="float: right;">Logout</a></td>
		<td width=2%>&nbsp;</td>
		</tr>
  	</table>

  	'''


z='''
	</body>
	</html>
	'''

logon_user=''
logon_admin=''

app = Flask(__name__)

@app.route("/",methods=['post','get'])
def home():
	if logon_user=='' and logon_admin=='':
		b="<h1>Welcome to L's Book House!</h1><br>Have a nice day!"
		return a1+b+z
	elif logon_user!='':
		b='<h1>Welcome,%s!</h1><br>Have a nice day!'%logon_user
		return a2+b+z
	elif logon_admin!='':
		b='<h1>Welcome,%s!</h1><br>You now can alter data!'%logon_admin
		return a3+b+z


@app.route("/aboutus",methods=['post','get'])
def aboutus():
	b='<p>The author is too lazy that writing noting here.</p>'
	if logon_user=='':
		return a1+b+z
	else:
		return a2+b+z


#register relate

@app.route("/register",methods=['post','get'])
def register():
	b='''<div id="body" style="margin-left: 10%">
	<h1>Register</h1>

	<form method="post" action="register_r">
		<table>
		<tr><br></tr>
		Please enter the following information:<br><br>			
		<tr>
		<td>Name:</td>
		<td><input type="text" name="name"></td>
		</tr>	
		<tr>
		<td>Email:</td>
		<td><input type="text" name="email"></td>
		</tr>
		<tr>
		<td>Phone number:</td>
		<td><input type="text" name="telephone"></td>
		</tr>
		<tr>
		<td>Address:</td>
		<td><input type="text" name="address"></td>
		</tr>
		<tr>
		<td>Username:</td>
		<td><input type="text" name="username"></td>
		</tr>
		<tr>
		<td>Password:</td>
		<td><input type="password" name="password"></td>
		</tr>
		<tr>
		<td>Input your password again:</td>
		<td><input type="password" name="password2"></td>
		</tr>
		</table>
		<br><br>
		<input type="submit" >
	</form>
	</div>
	'''
	if logon_user=='' and logon_admin=='':
		return (a1+b+z)
	elif logon_admin!='':
		return a3+b+z

@app.route("/register_r",methods=['post','get'])
def register_r():
	
	b=''
	if request.form['password']!=request.form['password2']:
		b='<h1>The passwords are not the same</h1>'
	cursor=db.cursor()
	found=False
	TNF=True
	miss=False
	for e,i in request.form.items():
		if len(i)<1:
			miss=True
			

	cursor.execute('select * from customer where 1;')
	for e in cursor.fetchall():
		if  request.form['email']==e[2]:
			b=b+'<h1>The email has been used!</h1>'
			found=True
		if request.form['telephone']==str(e[3]):
			b=b+'<h1>The phone number has been used!</h1>'
			found=True
		if request.form['username']==e[5]:
			b=b+'<h1>The username has been used!</h1>'
			found=True
		
		for i in request.form['telephone']:
			if str(i) <'0' or str(i) >'9' :
				TNF=False
			if len(request.form['telephone'])!=8:
				TNF=False
	

	if not found and TNF and not miss:
		cursor.execute("insert into customer values(%d,'%s','%s',%d,'%s','%s','%s')"%(0,request.form['name'],request.form['email'],int(request.form['telephone']),request.form['address'],request.form['username'],request.form['password']))
		db.commit()
		
	elif not TNF:
		b=b+'<h1>The format of phone number is incorrect!</h1><form action="/register"><button>Back</button></form>'
	elif miss:
		b=b+'<h1>There is/are missing data!</h1><form action="/register"><button>Back</button></form>'
	else:
		b=b+'<form action="/register"><button>Back</button></form>'
	if logon_user=='' and logon_admin=='' :
		if not miss and TNF:
			b=b+'''<h1>You can <a href="/logon">logon</a> now!</h1>'''
		return (a1+b+z)

	elif logon_admin!='':
		if not miss and TNF:
			b='''<h1>The new customer account is added!</h1>'''
		return a3+b+z

#logon relate

@app.route("/logon",methods=['post','get'])
def logon():
	b='''
	<div id="body" style="margin-left: 10%">
	<h1>Logon</h1>
	<form method="post" action="logon_r">
	Please enter your username:<br>
	<input type="text" name="username"><br><br>
	And password:<br>
	<input type="password" name="password"><br><br>
	<br><br>
	<input type="submit">
	</form>
	<br><br><br>
	<a href="admin_logon" style="color:gray">Admin Logon</a>
	</div>
		'''
	return a1+b+z

@app.route("/logon_r" ,methods=['post','get'])
def logon_r():
	cursor=db.cursor()
	cursor.execute('select * from customer where 1;')
	found=False

	for e in cursor.fetchall():
		if request.form['username']==e[5] and request.form['password']==e[6]:
			found=True
			global logon_user
			logon_user=request.form['username']
			
	if not found:
		b='<h1>Incorrect username or password!</h1><form action="/logon"><button>Back</button></form>'
		return a1+b+z
	else:
		return redirect(url_for('home'))

@app.route("/logout",methods=['post','get'])
def logout():
	global logon_user
	global logon_admin
	logon_user=''
	logon_admin=''
	return redirect(url_for('home'))


#personal relate

@app.route("/personal",methods=['post','get'])
def personal():
	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		b='''
		<table style="margin-left: 10%; margin-top:3%">
		<tr><td><a href='info'>Check personally information</a></td></tr>
		<tr><td><a href='order'>Check Order</a></td></tr>
		</table>'''
		return a2+b+z

@app.route("/info", methods=['post','get'])
def info():
	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		cursor=db.cursor()
		cursor.execute('select * from customer where 1;')
		for e in cursor.fetchall():
			if e[5]==logon_user:
				b='''
					<h1 style="margin-left: 10%;margin-top:3%">Your information:</h1>
					<form method="post" action="/info_alter">
					<table style="margin-left: 10%;">
					

					<tr><td>ID:</td>
						<td>{0}</td>
					</tr>
					<tr><td>Name:</td>
						<td>{1}</td>
						<td><input type = "submit" name="name" value='Alter'></td>
					</tr>
					<tr><td>Email:</td>
						<td>{2}</td>
						<td><input type = "submit" name="email" value='Alter'></td>

					</tr>
					<tr><td>Telephone Number:</td>
						<td>{3}</td>
						<td><input type = "submit" name="phoneNo" value='Alter'></td>
					</tr>
					<tr><td>Address:</td>
						<td>{4}</td>
						<td><input type = "submit" name="address" value='Alter'></td>
					</tr>
					<tr><td>Username</td>
						<td>{5}</td>
						<td><input type = "submit" name="username" value='Alter'></td>
					</tr>
					<tr><td>Password</td>
						<td>{6}</td>
						<td><input type = "submit" name="password" value='Alter'></td>
					</tr>
					</table>
			
					</form>
					'''.format(e[0],e[1],e[2],e[3],e[4],e[5],e[6])

		return a2+b+z

@app.route("/info_alter",methods=['post','get'])
def info_alter():
	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		cursor=db.cursor()
		cursor.execute('select * from customer where 1;')
		for e in cursor.fetchall():
			if e[5]==logon_user:

				b='''
				<form method="post" action="/info_alter_r">
				<table style="margin-left: 10%; margin-top:3%">
				'''

				if 'name' in request.form:
					b=b+'''
					<tr>
						<td>Name:</td>
						<td>{0}</td>
					</tr>
					<tr>
						<td>New name:</td>
						<td><input type = 'text' name = 'newName'></td>
					</tr>			   
					  '''.format(e[1])
				elif 'email' in request.form:
					b=b+'''
						<tr>
							<td>Email:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New Email:</td>
							<td><input type = 'text' name = 'newEmail'></td>
						</tr>			   
					  '''.format(e[2])
				elif 'phoneNo' in request.form:
					b=b+'''
						<tr>
							<td>Telephone number:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New telephone number:</td>
							<td><input type = 'text' name = 'newPhoneNo'></td>
						</tr>				   
					  '''.format(e[3])
				elif 'address' in request.form:
					b=b+'''
						<tr>
							<td>Address:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New address:</td>
							<td><input type = 'text' name = 'newAddress'></td>
						</tr>			   
					  '''.format(e[4])
				elif 'username' in request.form:
					b=b+'''
						<tr>
							<td>Username:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New username:</td>
							<td><input type = 'text' name = 'newUsername'></td>
						</tr>			   
					  '''.format(e[5])
				elif 'password' in request.form:
					b=b+'''
						<tr>
							<td>Password:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New password:</td>
							<td><input type = 'text' name = 'newPassword'></td>
						</tr>			   
					  '''.format(e[6])		

				b=b+'''
					<tr>
					<td><input type = "submit" value='Submit'></td>
					</tr>
					</table>
					</form>
					'''
				
		return a2+b+z

@app.route("/info_alter_r",methods=['post','get'])
def info_alter_r():
	miss=False
	for e,i in request.form.items():
		if len(i)<1:
			miss=True
	global logon_user
	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	elif not miss:
		cursor=db.cursor()
		cursor.execute('select * from customer where 1;')
		found=False
		TNF=True
		b=''

		for e in cursor.fetchall():
			if e[5]!=logon_user:
				if 'newEmail' in request.form and request.form['newEmail']==e[2]:
					b=b+'<h1>The email has been used!</h1>'
					found=True
				if 'newPhoneNo' in request.form and request.form['newPhoneNo']==str(e[3]):
					b=b+'<h1>The phone number has been used!</h1>'
					found=True
				if 'newUsername' in request.form and request.form['newUsername']==e[5]:
					b=b+'<h1>The username has been used!</h1>'
					found=True
		cursor.execute('select * from customer where 1;')
		for e in cursor.fetchall():
			if e[5]==logon_user and not found:
								
				if 'newName' in request.form:
					cursor.execute('''update customer set cname='{0}' where username="{1}"'''.format(request.form['newName'],logon_user))
					db.commit()
				elif'newEmail' in request.form:
					cursor.execute('''update customer set email='{0}' where username="{1}"'''.format(request.form['newEmail'],logon_user))
					db.commit()
				elif'newPhoneNo' in request.form:
					for i in request.form['newPhoneNo']:
						if str(i) <'0' or str(i) >'9' :
							TNF=False
					if len(request.form['newPhoneNo'])!=8:
						TNF=False
					if TNF:
						cursor.execute('''update customer set telno={0} where username="{1}"'''.format(int(request.form['newPhoneNo']),logon_user))
						db.commit()
					else:
						b=b+'<h1>The format of phone number is incorrect!</h1>'
				elif'newAddress' in request.form:
					cursor.execute('''update customer set address='{0}' where username="{1}"'''.format(request.form['newAddress'],logon_user))
					db.commit()
				elif'newUsername' in request.form:
					cursor.execute('''update customer set username='{0}' where username="{1}"'''.format(request.form['newUsername'],logon_user))
					db.commit()
					logon_user=request.form['newUsername']
				elif'newPassword' in request.form:
					cursor.execute('''update customer set password='{0}' where username="{1}"'''.format(request.form['newPassword'],logon_user))
					db.commit()
				if not found and TNF:
					b='<h1 style="margin-top:3%;margin-left:10%;">The update is success!</h1><form action="/info"><button>Back</button></form>'
		if found or not TNF:
			b=b+'<form action="/info"><button>Back</button></form>'

	elif miss:
		b='<h1>There is/are missing data!</h1><form action="/info"><button>Back</button></form>'
	
	return a2+b+z


#product related

@app.route("/product",methods=['post','get'])
def product():

	cat=[]
	subcat=[]

	b='''
	  	<div id ="right">
	  		<h2>The latest book</h2>
	  		<form action="/product_d" method="post">
	  	'''

	num=0
	cursor=db.cursor()
	cursor.execute('select * from product_book where 1 order by pid DESC;')
	for e in cursor.fetchall():
		num=num+1
		if e[6] not in cat:
			cat.append(e[6])
		
		if num<6:
			b=b+'''
				<button name="ID" value="{5}" type="submit" style="width:75%;margin-top:2%;margin-left:2%">
				<div style="width: 75%;">
  					<table >
  					<tr>
  					<td>Book name:</td>
  					<td>{0}</td>
  					</tr>
  					<tr>
  					<td>Author:</td>
  					<td >{1}</td>
  					</tr>
  					<tr>
  					<td>Category:</td>
  					<td>{3}/{4}</td>
  					</tr>
  					<tr>
  					<td>Price:</td>
  					<td>{2}</td>
  					</tr>
  					</table>
				</div>
				</button>
				<br><br>
				'''.format(e[1],e[2],e[5],e[6],e[7],e[0])

	b=b+'''
			</form>
			</div>
	 		<div id="left">
	 		<p>Category:</p>
	 		<br>
	 		<form action="/product_s" method="post">'''

	for i in cat:
		b=b+'''
			<li>
			<input type="submit" id="linkbutton" name="cat" value="{0}">
			<ul>
			'''.format(i)
		cursor.execute('select * from product_book where 1;')
		for e in cursor.fetchall():
			if e[6]==i and e[7] not in subcat:
				subcat.append(e[7])
				b=b+'''
					<li>
					<input type="submit" id="linkbutton" name="cat" value="{0}">
					</li>
					'''.format(e[7])

		b=b+'''
			</ul>
			</li>
			<br><br>
			'''
	b=b+'''
		</form>
		</div>
		'''

	if logon_user=='':
		
		return a1+b+z
	else:
		return a2+b+z

@app.route("/product_s",methods=['post','get'])
def product_s():
	cat=[]
	subcat=[]
	b=''
	cursor=db.cursor()
	cursor.execute('select * from product_book where 1;')
	for e in cursor.fetchall():
		if e[6] not in cat:
			cat.append(e[6])
	b=b+'''
	 		<div id="left">
	 		<p>Category:</p>
	 		<br>
	 		<form action="/product_s" method="post">
	 		'''
	for i in cat:
		b=b+'''
			<li>
				<input type="submit" id="linkbutton" name="cat" value="{0}">
			<ul>
			'''.format(i)
		cursor.execute('select * from product_book where 1;')
		for e in cursor.fetchall():
			if e[6]==i and e[7] not in subcat:
				subcat.append(e[7])
				b=b+'''
					<li>
						<input type="submit" id="linkbutton" name="cat" value="{0}">
					</li>
					'''.format(e[7])

		b=b+'''
			</ul>
			</li>
			<br><br>
			'''
	b=b+'''
		</form>
		</div>
		<div id ="right">
		'''

	if 'key' in request.form:
		key=str(request.form['key'])
	elif 'cat' in request.form:
		key=str(request.form['cat'])
	b=b+'''
		<h2 id ="body">The result of searching:{0}</h2>
		<form action="/product_d" method="post">

		'''.format(key)

	cursor=db.cursor()
	cursor.execute('select * from product_book where 1;')
	for e in cursor.fetchall():
		if (key.upper() in str(e[1]).upper()) or (key.upper() in str(e[2].upper())) or (key.upper() in str(e[4]).upper()) or (key.upper()==e[6].upper()) or (key.upper()==e[7].upper()):
			b=b+'''
				<button name="ID" value="{5}" type="submit" style="width:75%;margin-top:2%;margin-left:2%">
				<div style="width: 75%;">
  					<table >
  					<tr>
  					<td>Book name:</td>
  					<td>{0}</td>
  					</tr>
  					<tr>
  					<td>Author:</td>
  					<td >{1}</td>
  					</tr>
  					<tr>
  					<td>Category:</td>
  					<td>{3}/{4}</td>
  					</tr>
  					<tr>
  					<td>Price:</td>
  					<td>{2}</td>
  					</tr>
  					</table>
				</div>
				</button>
				<br><br>
				'''.format(e[1],e[2],e[5],e[6],e[7],e[0])


	b=b+'''
		
		</div>
		</form>
		</div>
		'''
	if logon_user=='':
		return a1+b+z
	else:
		return a2+b+z

@app.route("/product_d",methods=['post','get'])
def product_d():

	cat=[]
	subcat=[]
	b=''
	cursor=db.cursor()
	cursor.execute('select * from product_book where 1;')
	for e in cursor.fetchall():
		if e[6] not in cat:
			cat.append(e[6])
	b=b+'''
	 		<div id="left">
	 		<p>Category:</p>
	 		<br>
	 		<form action="/product_s" method="post">
	 		'''
	for i in cat:
		b=b+'''
			<li>
				<input type="submit" id="linkbutton" name="cat" value="{0}">
			<ul>
			'''.format(i)
		cursor.execute('select * from product_book where 1;')
		for e in cursor.fetchall():
			if e[6]==i and e[7] not in subcat:
				subcat.append(e[7])
				b=b+'''
					<li>
						<input type="submit" id="linkbutton" name="cat" value="{0}">
					</li>
					'''.format(e[7])

		b=b+'''
			</ul>
			</li>
			<br><br>
			'''
	b=b+'''
		</form>
		</div>
		<div id ="right">
		'''

	if 'ID' in request.form:
		ID=str(request.form['ID'])
	b=b+'''
		<div id="body">
		<form action="/product_t" method="post">
		'''
	cursor=db.cursor()
	cursor.execute('select * from product_book where 1;')
	for e in cursor.fetchall():
		if str(e[0])==ID:
			b=b+'''
				<div style="border-style: groove; width: 75%;margin-top:2%;margin-left:2%">
  				<table>
  					<tr>
  					<td>Book name:</td>
  					<td>{0}</td>
  					</tr>
  					<tr>
  					<td>Author:</td>
  					<td>{1}</td>
  					</tr>
  					<tr>
  					<td>Publisher:</td>
  					<td>{5}</td>
  					</tr>
  					<tr>
  					<td>PublishYear:</td>
  					<td>{6}</td>
  					</tr>
  					<tr>
  					<td>Category:</td>
  					<td>{3}/{4}</td>
  					</tr>
  					<tr>
  					<td>Price:</td>
  					<td>{2}</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td><button type="submit"  name="add" value="{7}">Add to shopping cart</button></td>
  					</tr>

  				</table>
		</div>
		'''.format(e[1],e[2],e[5],e[6],e[7],e[4],e[3],e[0])
	
	b=b+'''
		</form>
		</div>
		'''
	if logon_user=='':
		return a1+b+z
	else:
		return a2+b+z

@app.route("/product_t",methods=['post','get'])
def product_t():
	pid=request.form['add']
	b=''
	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		cursor=db.cursor()
		cursor.execute('select * from customer where 1;')
		for e in cursor.fetchall():
			if str(e[5])==logon_user and 'add' in request.form :
				cursor.execute("insert into cart values(%d,%d,%d)"%(0,e[0],int(pid)))
				db.commit()
				b='''<h1>Add to shopping Cart successfully!</h1>
					<form action="/product"><button>Back</button></form>'''
			
		
		return a2+b+z


#shopping cart related

@app.route("/shoppingcart",methods=['post','get'])
def shoppingcart():
	cursor=db.cursor()
	cursor.execute('select * FROM cart join customer on cart.cid=customer.cid join product_book on cart.pid=product_book.pid where 1 ')
	count=0
	found=False
	for e in cursor.fetchall():
		if logon_user==e[8]:
			found = True
	
	if not found:
		b='''
			<h2  align="center" style="margin-top:5%">There is no product in your shopping cart!</h2>
			<h3  align="center" style="margin-top:5%"><a href="/product">Go to buy now!</a></h3>
			'''
	else:
		b='''			
			<form action="shoppingcart_r" method="post">
			<div style="margin-top:5%;margin-right:15%;float:right">
			<button type="submit"  name="del">Delete</button>
			<br><br>
			<button type="submit"  name="buy" >Buy Now</button>
			</div>
			<div style="margin-top:5%;margin-left:3%;">
			<h2>The product(s) you have in shopping cart:</h2>

			'''
		cursor.execute('select * FROM cart join customer on cart.cid=customer.cid join product_book on cart.pid=product_book.pid where 1 ')
		for e in cursor.fetchall():
			count=count+1
			if logon_user==e[8]:
				b=b+'''
				<div style="border-style: groove; width: 65%;margin-top:2%;margin-left:2%">
				<input type="Checkbox" Name="{5}" ID="{6}" value={5}>
				<label for="{6}">
				<div style="width: 75%;">
  					<table >
  					<tr>
  					<td>Book name:</td>
  					<td>{0}</td>
  					</tr>
  					<tr>
  					<td>Author:</td>
  					<td >{1}</td>
  					</tr>
  					<tr>
  					<td>Category:</td>
  					<td>{3}/{4}</td>
  					</tr>
  					<tr>
  					<td>Price:</td>
  					<td>{2}</td>
  					</tr>
  					</table>
				</div>
				</label>
				</div>
				<br>
				'''.format(e[11],e[12],e[15],e[16],e[17],e[0],count)

		b=b+'''
			</form>
			</div>
			'''
	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		return a2+b+z

@app.route("/shoppingcart_r",methods=['post','get'])
def shoppingcart_r():
	b=''

	if len(request.form)==1:
		b='<h3 align="center" style="margin-top:5%">You did not select anything!</h3><form action="/shoppingcart"><button  style="margin-left:45%">Back</button></form>'

	elif 'del' in request.form and logon_user!='':
		for t in request.form:
			cursor=db.cursor()
			cursor.execute('select * FROM cart join customer on cart.cid=customer.cid join product_book on cart.pid=product_book.pid WHERE 1')
			for e in cursor.fetchall():
				if logon_user==str(e[8]) and str(t)==str(e[0]):
					cursor.execute('delete FROM cart WHERE cid={0} and scid={1}'.format(e[3],t))
					db.commit()

		b=b+"<h1>Delete successfully</h1><form action='/shoppingcart'><button>Back</button></form>"

	elif 'buy' in request.form and logon_user!='':
		b=b+'''
			<form action="/shoppingcart_rb" method="post">
			<div style="margin-top:5%;margin-left:2%;width:70%;float:left;">
			<h2>The product(s) you buy:</h2>
			<table>
			<tr>
			<td>Book name</td>
			<td width=5%>&nbsp;</td>
			<td>Author</td>
			<td width=5%>&nbsp;</td>
			<td>Price</td>
			<tr> 
			<tr><td height=5%>&nbsp;<td></tr>
			'''
		
		Total=0

		for t in request.form:
			cursor=db.cursor()
			cursor.execute('select * FROM cart join customer on cart.cid=customer.cid join product_book on cart.pid=product_book.pid WHERE 1')
			for e in cursor.fetchall():
				if logon_user==e[8] and str(t)==str(e[0]):
					b=b+'''
						<tr>
						<td>{0}</td>
						<td width=5%>&nbsp;</td>
						<td>{1}</td>
						<td width=5%>&nbsp;</td>
						<td>{2}</td>
						</tr>
						<tr>
						<td><input type="hidden" Name="{3}" value={3}></td>
						</tr>
						'''.format(e[11],e[12],e[15],e[0])
					Total=Total+int(e[15])

		b=b+'''
			</table>
			</div>
			<div style="margin-top:10%;margin-right:15%;float:right">
			<p>Total: ${0}</p>
			<button type="submit"  name="conform" >Conform</button>
			<br><br>
			<button type="submit"  name="cancel">Cancel</button>
			</div>
			</form>
			'''.format(Total)
			
	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		return a2+b+z

@app.route("/shoppingcart_rb",methods=['post','get'])
def shoppingcart_rb():
	
	b=''

	if "cancel" in request.form :
		return redirect(url_for('shoppingcart'))
	elif "conform" in request.form:
		cursor=db.cursor()
		cursor.execute('select oid FROM orders WHERE 1 group by oid')
		for e in cursor.fetchall():
			pass
		if cursor.rowcount==0:
			oid=1
		else:
			oid=int(e[0])+1

		for t in request.form:
			cursor=db.cursor()
			cursor.execute('select * FROM cart join customer on cart.cid=customer.cid join product_book on cart.pid=product_book.pid WHERE 1')
			for e in cursor.fetchall():
				if logon_user==e[8] and str(t)==str(e[0]):
					cursor.execute('delete FROM cart WHERE cid={0} and scid={1}'.format(e[3],t))
					cursor.execute('insert into orders values(%d,%d,%d,"%s")'%(oid,e[3],e[2],str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))))
					db.commit()
		b=b+'''
			<h1>Buy successfully!</h1>
			<form action='/shoppingcart'>
			<button>Back</button>
			</form>
			'''

	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		return a2+b+z

#order related
@app.route("/order",methods=['post','get'])
def order():
	order_count=[]
	order_date=[]
	cursor=db.cursor()
	cursor.execute('select orders.oid,orders.datetime, customer.username from orders join customer on customer.cid=orders.cid where 1 order by orders.oid DESC ')
	for e in cursor.fetchall():
		if e[2]==logon_user and e[0] not in order_count:
			order_count.append(e[0])
			order_date.append(e[1])
	if order_count ==[]:
		b='''
			<h2  align="center" style="margin-top:5%">You did not buy anything yet!</h2>
			<h3  align="center" style="margin-top:5%"><a href="/product">Go to buy now!</a></h3>
			'''
	else:
		b='''
			<div style="margin-top:5%;margin-left:3%;">
			<h2>The order(s) you paid before:</h2>
			<form action="/order_d" method="post">
		'''
		count=0
		for e in order_count:
			b=b+'''
				<button name="oid" value="{0}" type="submit" style="width:75%;margin-top:2%;margin-left:2%">
				<div style="width: 75%;">
				<table >
  				<tr>
  				<td>Order:</td>
  				<td style="flaot:left">{0}</td>
  				<td width=10%></td>
  				<td>Date&time:</td>
  				<td>{1}</td>
  				</tr>
  				</table>
  				</div>
  				</button>
				'''.format(e,order_date[count])
			count=count+1 

		b=b+'''
		</form>
		'''

	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		return a2+b+z

@app.route("/order_d",methods=['post','get'])
def order_d():
	b=''

	b=b+'''
			<form action="/order" method="post">
			<div style="margin-top:5%;margin-left:2%;width:70%;float:left;">
			<h2>The product(s) you bought:</h2>
			<table>
			<tr>
			<td>Book name</td>
			<td width=5%>&nbsp;</td>
			<td>Author</td>
			<td width=5%>&nbsp;</td>
			<td>Price</td>
			<tr> 
			<tr><td height=5%>&nbsp;<td></tr>
			'''
		
	Total=0

	cursor=db.cursor()
	cursor.execute('select * FROM orders join customer on orders.cid=customer.cid join product_book on orders.pid=product_book.pid WHERE 1')
	for e in cursor.fetchall():
		if logon_user==e[9] and str(request.form['oid'])==str(e[0]):
					b=b+'''
						<tr>
						<td>{0}</td>
						<td width=5%>&nbsp;</td>
						<td>{1}</td>
						<td width=5%>&nbsp;</td>
						<td>{2}</td>
						</tr>
						'''.format(e[12],e[13],e[16])
					Total=Total+int(e[16])

	b=b+'''
		</table>
		</div>
		<div style="margin-top:10%;margin-right:15%;float:right">
		<p>Total: ${0}</p>
		<br><br>
		<button type="submit">Back</button>
		</div>
		</form>
		'''.format(Total)
	
	if logon_user=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		return a2+b+z


#admin logon related

@app.route("/admin_logon",methods=['post','get'])
def admin_logon():
	b='''
	<div id="body" style="margin-left: 10%">
	<h1>Admin Logon</h1>
	<form method="post" action="admin_logon_r">
	Please enter your username:<br>
	<input type="text" name="username"><br><br>
	And password:<br>
	<input type="password" name="password"><br><br>
	<br><br>
	<input type="submit">
	</form>
	<br><br><br>
	<a href="logon" style="color:gray">Customer Logon</a>
	</div>
		'''
	return a1+b+z

@app.route("/admin_logon_r" ,methods=['post','get'])
def admin_logon_r():
	cursor=db.cursor()
	cursor.execute('select * from admin where 1;')
	found=False

	for e in cursor.fetchall():
		if request.form['username']==e[0] and request.form['password']==e[1]:
			found=True
			global logon_admin
			logon_admin=request.form['username']
			
	if not found:
		b='<h1>Incorrect username or password!</h1><form action="/admin_logon"><button>Back</button></form>'
		return a1+b+z
	else:
		return redirect(url_for('home'))


#admin product related

@app.route("/admin_product",methods=['post','get'])
def admin_product():
	key=''
	b='''
		<div align="center" style="margin:2%">
		<form action="/admin_product" id="head" method="post">
		<input type="text" name="key" placeholder="ID / Bookname / Author / Publisher " id="body" style="width:300px">
		<input type="submit" value="Search" id="body">
		</form></div>
		'''
	if 'key' in request.form:
		key=str(request.form['key'])
		b=b+'''
			<h2 id ="body">The result of searching:{0}</h2>
			'''.format(key)

	b=b+'''
		<form action="/admin_product_r" method="post">
		<table style="margin:2%">
		<tr>
		<td>PID</td>
		<td width=5%>&nbsp;</td>
		<td>Book Name</td>
		<td width=5%>&nbsp;</td>
		<td>Author</td>
		<td width=5%>&nbsp;</td>
		<td>Category:</td>
		<td width=5%>&nbsp;</td>
		<td>Publisher</td>
		<td width=5%>&nbsp;</td>
		<td><button type="submit" name="add">+</button></td>
		<td width=5%>&nbsp;</td>
		<td width=5%>&nbsp;</td>
		</tr>
		<tr><td height=5%>&nbsp;<td></tr>
		'''.format(key)

	cursor=db.cursor()
	cursor.execute('select * from product_book where 1;')
	for e in cursor.fetchall():
		if (key.upper() in str(e[0]).upper()) or (key.upper() in str(e[1]).upper()) or (key.upper() in str(e[2].upper())) or (key.upper() in str(e[4]).upper()) or (key.upper()in e[6].upper()) or (key.upper()in e[7].upper()):
			b=b+'''
					<tr>
  					<td>{0}</td>
  					<td width=5%>&nbsp;</td>
  					<td>{1}</td>
  					<td width=5%>&nbsp;</td>
  					<td>{2}</td>
  					<td width=5%>&nbsp;</td>
  					<td>{3}/{4}</td>
  					<td width=5%>&nbsp;</td>
  					<td>{5}</td>
  					<td width=20%>&nbsp;</td>
  					<td><button type="submit" name="alter" value="{0}">Detail</button></td>
  					<td width=5%>&nbsp;</td>
  					<td><button type="submit" name="delete" value="{0}">Delete</button></td>
  					</tr>
  					<tr><td height=5%>&nbsp;<td></tr>
				'''.format(e[0],e[1],e[2],e[6],e[7],e[4])


	b=b+'''
		</table>
		</form>
		'''
	if logon_admin=='':
		return a1+'<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'+z
	else:
		return a3+b+z

@app.route("/admin_product_r",methods=['post','get'])
def admin_product_r():
	
	if "alter" in request.form:
		cursor=db.cursor()
		cursor.execute('select * from product_book where 1;')
		for e in cursor.fetchall():
			if str(e[0])==str(request.form["alter"]):
				b='''
					<h1 style="margin-left: 10%;margin-top:3%">Product information:</h1>
					<form method="post" action="/admin_product_r2">
					<input type = "hidden" name="alter">
					<table style="margin-left: 10%;">
					

					<tr><td>ID:</td>
						<td>{0}</td>
						<td><input type = "hidden" name="id" value='{0}'></td>
					</tr>
					<tr><td>Book name:</td>
						<td>{1}</td>
						<td><input type = "submit" name="name" value='Alter'></td>
					</tr>
					<tr><td>Author:</td>
						<td>{2}</td>
						<td><input type = "submit" name="author" value='Alter'></td>

					</tr>
					<tr><td>Publisher:</td>
						<td>{3}</td>
						<td><input type = "submit" name="publisher" value='Alter'></td>
					</tr>
					<tr><td>Publish year:</td>
						<td>{4}</td>
						<td><input type = "submit" name="publishyear" value='Alter'></td>
					</tr>
					<tr><td>Category:</td>
						<td>{5}</td>
						<td><input type = "submit" name="cat" value='Alter'></td>
					</tr>
					<tr><td>Subcategory:</td>
						<td>{6}</td>
						<td><input type = "submit" name="subcat" value='Alter'></td>
					</tr>
					<tr><td>Price:</td>
						<td>{7}</td>
						<td><input type = "submit" name="price" value='Alter'></td>
					</tr>
					</table>
			
					</form>
					'''.format(e[0],e[1],e[2],e[4],e[3],e[6],e[7],e[5])


	elif "delete" in request.form:
		b='''
			<h2 style="width: 75%;margin-top:2%;margin-left:2%">Do you really want to delete this product?</h2>
			<form action="admin_product_r2" method="post">
			'''
		cursor=db.cursor()
		cursor.execute('select * from product_book where 1;')
		for e in cursor.fetchall():
			if str(e[0])==str(request.form["delete"]) :
				b=b+'''
				<div style="width: 75%;margin-top:2%;margin-left:2%">
  				<table>
  					<tr>
  					<td>ID:</td>
  					<td width=2%>&nbsp;</td>
  					<td>{7}</td>
  					</tr>
  					<tr>
  					<td>Book name:</td>
  					<td width=2%>&nbsp;</td>
  					<td>{0}</td>
  					</tr>
  					<tr>
  					<td>Author:</td>
  					<td width=2%>&nbsp;</td>
  					<td>{1}</td>
  					</tr>
  					<tr>
  					<td>Publisher:</td>
  					<td width=2%>&nbsp;</td>
  					<td>{5}</td>
  					</tr>
  					<tr>
  					<td>PublishYear:</td>
  					<td width=2%>&nbsp;</td>
  					<td>{6}</td>
  					</tr>
  					<tr>
  					<td>Category:</td>
  					<td width=2%>&nbsp;</td>
  					<td>{3}/{4}</td>
  					</tr>
  					<tr>
  					<td>Price:</td>
  					<td width=2%>&nbsp;</td>
  					<td>{2}</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td><button type="submit"  name="delete" value="{7}">Delete</button></td>
  					<td width=2%>&nbsp;</td>
  					<td><button type="submit"  name="cancel" >Cancel</button></td>
  					</tr>

  				</table>
		</div>
		'''.format(e[1],e[2],e[5],e[6],e[7],e[4],e[3],e[0])
	
		b=b+'''
			</form>
			</div>
			'''

	elif "add" in request.form:
		return redirect(url_for('admin_product_add'))


	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'
		return a1+b+z
	elif logon_admin!='':
		return a3+b+z

@app.route("/admin_product_r2",methods=['post','get'])
def admin_product_r2():
	b=''
	cursor=db.cursor()
	
	if "alter" in request.form:
		cursor.execute('select * from product_book where pid={0};'.format(request.form['id']))
		for e in cursor.fetchall():
			b=b+'''
				<form action="admin_product_r3" method="post">
				<input type = "hidden" name="id" value="{0}">
				<table style="margin-left: 10%; margin-top:3%">
				'''.format(request.form['id'])
			if 'name' in request.form:
				b=b+'''
					<tr>
						<td>Book Name:</td>
						<td>{0}</td>
					</tr>
					<tr>
						<td>New Book Name:</td>
						<td><input type = 'text' name = 'newName'></td>
					</tr>			   
				  	'''.format(e[1])
			elif 'author' in request.form:
				b=b+'''
					<tr>
						<td>Author:</td>
						<td>{0}</td>
					</tr>
					<tr>
						<td>New Author:</td>
						<td><input type = 'text' name = 'newAuthor'></td>
					</tr>			   
					  '''.format(e[2])
			elif 'publisher' in request.form:
				b=b+'''
					<tr>
						<td>Publisher:</td>
						<td>{0}</td>
					</tr>
					<tr>
						<td>New publisher:</td>
						<td><input type = 'text' name = 'newpublisher'></td>
					</tr>				   
					  '''.format(e[4])
			elif 'publishyear' in request.form:
				b=b+'''
					<tr>
						<td>Publish Year:</td>
						<td>{0}</td>
					</tr>
					<tr>
						<td>New Publish Year:</td>
						<td><input type = 'text' name = 'newpublishyear'></td>
					</tr>			   
				  '''.format(e[3])
			elif 'cat' in request.form:
				b=b+'''
					<tr>
						<td>Category:</td>
						<td>{0}</td>
					</tr>
					<tr>
						<td>New Category:</td>
						<td><select name = 'newCat'>
							<option value="Chinese">Chinese</option>
							<option value="English">English</option></td>
					</tr>			   
				  '''.format(e[6])
			elif 'subcat' in request.form:
				b=b+'''
					<tr>
						<td>Subcategory:</td>
						<td>{0}</td>
					</tr>
					<tr>
						<td>New Subcategory:</td>
						<td><input type = 'text' name = 'newSubcat'></td>
					</tr>			   
					'''.format(e[7])		
			elif 'price' in request.form:
				b=b+'''
					<tr>
						<td>Price:</td>
						<td>{0}</td>
					</tr>
					<tr>
						<td>New Price:</td>
						<td><input type = 'text' name = 'newPrice'></td>
					</tr>			   
					'''.format(e[5])

			b=b+'''
				<tr>
					<td><input type = "submit" value='Submit'></td>
				</tr>
				</table>
				</form>
				'''
						
	elif "delete" in request.form:
		cursor.execute('delete FROM product_book WHERE pid={0}'.format(request.form['delete']))
		db.commit()
		b="<h1>Delete successfully</h1><form action='/admin_product'><button>Back</button></form>"


	elif "cancel" in request.form:
		return redirect(url_for('admin_product'))
		

	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'
		return a1+b+z
	elif logon_admin!='':
		return a3+b+z

@app.route("/admin_product_r3",methods=['post','get'])
def admin_product_r3():
	b=''
	cursor=db.cursor()
	miss=False
	for e,i in request.form.items():
		if len(i)<1:
			miss=True
	if not miss:
		if "newName" in request.form:
			cursor.execute('''update product_book set bkname='{0}' where pid="{1}"'''.format(request.form['newName'],request.form['id']))
			db.commit()
		elif "newAuthor" in request.form:
			cursor.execute('''update product_book set author='{0}' where pid="{1}"'''.format(request.form['newAuthor'],request.form['id']))
			db.commit()
		elif "newpublisher" in request.form:
			cursor.execute('''update product_book set publisher='{0}' where pid="{1}"'''.format(request.form['newpublisher'],request.form['id']))
			db.commit()
		elif "newpublishyear" in request.form:
			cursor.execute('''update product_book set publishYear='{0}' where pid="{1}"'''.format(request.form['newpublishyear'],request.form['id']))
			db.commit()
		elif "newCat" in request.form:
			cursor.execute('''update product_book set Cat='{0}' where pid="{1}"'''.format(request.form['newCat'],request.form['id']))
			db.commit()
		elif "newSubcat" in request.form:
			cursor.execute('''update product_book set subcat='{0}' where pid="{1}"'''.format(request.form['newSubcat'],request.form['id']))
			db.commit()
		elif "newPrice" in request.form:
			cursor.execute('''update product_book set price='{0}' where pid="{1}"'''.format(request.form['newPrice'],request.form['id']))
			db.commit()	

		b='<h1 style="margin-top:3%;margin-left:10%;">The update is success!</h1><form action="/admin_product"><button>Back</button></form>'
	
	elif miss:
		b=b+'<h1>There is/are missing data!</h1><form action="/admin_product"><button>Back</button></form>'
	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'
		return a1+b+z
	elif logon_admin!='':
		return a3+b+z

@app.route("/admin_product_add",methods=['post','get'])
def admin_product_add():
	b='''<div id="body" style="margin-left: 10%">
		<h1>Adding new Product:</h1>
		<form method="post" action="admin_product_add_r">
		<table>
		<tr><br></tr>
		Please enter the following information:<br><br>			
		<tr>
		<td>Book name:</td>
		<td><input type="text" name="bookname"></td>
		</tr>	
		<tr>
		<td>Author:</td>
		<td><input type="text" name="author"></td>
		</tr>
		<tr>
		<td>Publisher:</td>
		<td><input type="text" name="publisher"></td>
		</tr>
		<tr>
		<td>Publish Year:</td>
		<td><input type="text" name="publishyear"></td>
		</tr>
		<tr>
		<td>Category:</td>
		<td><select name = 'Cat'>
			<option value="Chinese">Chinese</option>
			<option value="English">English</option></td>
		</tr>
		<tr>
		<td>Subcategory:</td>
		<td><input type="text" name="Subcat"></td>
		</tr>
		<tr>
		<td>Price:</td>
		<td><input type="text" name="price"></td>
		</tr>
		</table>
		<br><br>
		<input type="submit" >
		</form>
		</div>
		'''		
	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'
		return a1+b+z
	elif logon_admin!='':
		return a3+b+z

@app.route("/admin_product_add_r",methods=['post','get'])
def admin_product_add_r():
	b=''
	miss=False
	for e,i in request.form.items():
		if len(i)<1:
			miss=True

	if not miss:
		cursor=db.cursor()
		cursor.execute("insert into product_book values(%d,'%s','%s',%d,'%s',%f,'%s','%s')"%(0,str(request.form['bookname']),str(request.form['author']),int(request.form['publishyear']),str(request.form['publisher']),float(request.form['price']),str(request.form['Cat']),str(request.form['Subcat'])))
		db.commit()
		b='''<h1>The new product is added!</h1>
			<form action="/admin_product"><button>Back</button></form>'''
	elif miss:
		b=b+'<h1>There is/are missing data!</h1><form action="/admin_product"><button>Back</button></form>'
			
	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'
		return a1+b+z
	elif logon_admin!='':
		return a3+b+z


#admin customer related

@app.route("/admin_customer",methods=['post','get'])
def admin_customer():
	key=''
	b='''
		<div align="center" style="margin:2%">
		<form action="/admin_customer" id="head" method="post">
		<input type="text" name="key" placeholder=" Customer ID/Name/Username " id="body" style="width:300px">
		<input type="submit" value="Search" id="body">
		</form></div>
		'''
	if 'key' in request.form:
		key=str(request.form['key'])
		b=b+'''
			<h2 id ="body">The result of searching:{0}</h2>
			'''.format(key)

	b=b+'''
		<form action="/admin_customer_r" method="post">
		<table style="margin:2%">
		<tr>
		<td>CID</td>
		<td width=5%>&nbsp;</td>
		<td>Name</td>
		<td width=5%>&nbsp;</td>
		<td>Username</td>
		<td width=5%>&nbsp;</td>
		<td><button type="submit" name="add">+</button></td>
		<td width=5%>&nbsp;</td>
		<td width=5%>&nbsp;</td>
		</tr>
		<tr><td height=5%>&nbsp;<td></tr>
		'''.format(key)

	cursor=db.cursor()
	cursor.execute('select * from customer where 1;')
	for e in cursor.fetchall():
		if (key.upper() in str(e[0]).upper()) or (key.upper() in str(e[1]).upper()) or (key.upper() in str(e[5].upper())) :
			b=b+'''
					<tr>
  					<td>{0}</td>
  					<td width=5%>&nbsp;</td>
  					<td>{1}</td>
  					<td width=5%>&nbsp;</td>
  					<td>{2}</td>
  					<td width=5%>&nbsp;</td>
  					<td><button type="submit" name="alter" value="{0}">Detail</button></td>
  					<td width=5%>&nbsp;</td>
  					<td><button type="submit" name="delete" value="{0}">Delete</button></td>
  					</tr>
  					<tr><td height=5%>&nbsp;<td></tr>
				'''.format(e[0],e[1],e[5])


	b=b+'''
		</table>
		</form>
		'''
	if logon_admin=='':
		return a1+'<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'+z
	else:
		return a3+b+z

@app.route("/admin_customer_r",methods=['post','get'])
def admin_customer_r():
	
	if 'add' in request.form:
		return redirect(url_for('register'))

	
	if 'alter' in request.form:
		cursor=db.cursor()
		cursor.execute('select * from customer where 1;')
		for e in cursor.fetchall():
			if request.form['alter'] ==str(e[0]):
				b='''
					<h1 style="margin-left: 10%;margin-top:3%">The customer's information:</h1>
					<form method="post" action="/admin_customer_r2">
					<input type = "hidden" name="alter">
					<table style="margin-left: 10%;">
					

					<tr><td>ID:</td>
						<td>{0}</td>
						<td><input type = "hidden" name="id" value='{0}'></td>
					</tr>
					<tr><td>Name:</td>
						<td>{1}</td>
						<td><input type = "submit" name="name" value='Alter'></td>
					</tr>
					<tr><td>Email:</td>
						<td>{2}</td>
						<td><input type = "submit" name="email" value='Alter'></td>

					</tr>
					<tr><td>Telephone Number:</td>
						<td>{3}</td>
						<td><input type = "submit" name="phoneNo" value='Alter'></td>
					</tr>
					<tr><td>Address:</td>
						<td>{4}</td>
						<td><input type = "submit" name="address" value='Alter'></td>
					</tr>
					<tr><td>Username</td>
						<td>{5}</td>
						<td><input type = "submit" name="username" value='Alter'></td>
					</tr>
					<tr><td>Password</td>
						<td>{6}</td>
						<td><input type = "submit" name="password" value='Alter'></td>
					</tr>
					</table>
			
					</form>
					'''.format(e[0],e[1],e[2],e[3],e[4],e[5],e[6])

	if 'delete' in request.form:
		b='''
			<h2 style="width: 75%;margin-top:2%;margin-left:2%">Do you really want to delete this customer information?</h2>
			<form action="admin_customer_r2" method="post">
			'''
		cursor=db.cursor()
		cursor.execute('select * from customer where 1;')
		for e in cursor.fetchall():
			if str(e[0])==str(request.form["delete"]) :
				b=b+'''
				<div style="width: 75%;margin-top:2%;margin-left:2%">
  				<table>

					<tr><td>ID:</td>
						<td width=2%>&nbsp;</td>
						<td>{0}</td>
					</tr>
					<tr><td>Name:</td>
						<td width=2%>&nbsp;</td>
						<td>{1}</td>
					</tr>
					<tr><td>Email:</td>
						<td width=2%>&nbsp;</td>
						<td>{2}</td>
					</tr>
					<tr><td>Telephone Number:</td>
						<td width=2%>&nbsp;</td>
						<td>{3}</td>
					</tr>
					<tr><td>Address:</td>
						<td width=2%>&nbsp;</td>
						<td>{4}</td>
					</tr>
					<tr><td>Username</td>
						<td width=2%>&nbsp;</td>
						<td>{5}</td>
					</tr>
					<tr><td>Password</td>
						<td width=2%>&nbsp;</td>
						<td>{6}</td>
					</tr>
					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
					<tr>
  						<td><button type="submit"  name="delete" value="{0}">Delete</button></td>
  						<td width=2%>&nbsp;</td>
  						<td><button type="submit"  name="cancel" >Cancel</button></td>
  					</tr>
					</table>
			
					</form>
					'''.format(e[0],e[1],e[2],e[3],e[4],e[5],e[6])


	
	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'
		return a1+b+z
	elif logon_admin!='':
		return a3+b+z

@app.route("/admin_customer_r2",methods=['post','get'])
def admin_customer_r2():
	cursor=db.cursor()
	b=''
	if "alter" in request.form:
		cursor=db.cursor()
		cursor.execute('select * from customer where 1;')
		for e in cursor.fetchall():
			if str(e[0])==str(request.form['id']):

				b='''
				<form method="post" action="/admin_customer_r3">
				<input type="hidden" name="id" value="{0}">
				<table style="margin-left: 10%; margin-top:3%">
				'''.format(request.form['id'])

				if 'name' in request.form:
					b=b+'''
					<tr>
						<td>Name:</td>
						<td>{0}</td>
					</tr>
					<tr>
						<td>New name:</td>
						<td><input type = 'text' name = 'newName'></td>
					</tr>			   
					  '''.format(e[1])
				elif 'email' in request.form:
					b=b+'''
						<tr>
							<td>Email:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New Email:</td>
							<td><input type = 'text' name = 'newEmail'></td>
						</tr>			   
					  '''.format(e[2])
				elif 'phoneNo' in request.form:
					b=b+'''
						<tr>
							<td>Telephone number:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New telephone number:</td>
							<td><input type = 'text' name = 'newPhoneNo'></td>
						</tr>				   
					  '''.format(e[3])
				elif 'address' in request.form:
					b=b+'''
						<tr>
							<td>Address:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New address:</td>
							<td><input type = 'text' name = 'newAddress'></td>
						</tr>			   
					  '''.format(e[4])
				elif 'username' in request.form:
					b=b+'''
						<tr>
							<td>Username:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New username:</td>
							<td><input type = 'text' name = 'newUsername'></td>
						</tr>			   
					  '''.format(e[5])
				elif 'password' in request.form:
					b=b+'''
						<tr>
							<td>Password:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New password:</td>
							<td><input type = 'text' name = 'newPassword'></td>
						</tr>			   
					  '''.format(e[6])		

				b=b+'''
					<tr>
					<td><input type = "submit" value='Submit'></td>
					</tr>
					</table>
					</form>
					'''
				
	elif "delete" in request.form:
		cursor.execute('delete FROM customer WHERE cid={0}'.format(request.form['delete']))
		db.commit()
		b="<h1>Delete successfully</h1><form action='/admin_customer'><button>Back</button></form>"

	elif "cancel" in request.form:
		return redirect(url_for('admin_customer'))



			
	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'
		return a1+b+z
	elif logon_admin!='':
		return a3+b+z

@app.route("/admin_customer_r3",methods=['post','get'])
def admin_customer_r3():
	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	else:
		cursor=db.cursor()
		cursor.execute('select * from customer where 1;')
		found=False
		TNF=True
		b=''
		miss=False
		
		for e,i in request.form.items():
			if len(i)<1:
				miss=True

		for e in cursor.fetchall():
			if e[0]!=int(request.form['id']):
				if 'newEmail' in request.form and request.form['newEmail']==e[2]:
					b=b+'<h1>The email has been used!</h1>'
					found=True
				if 'newPhoneNo' in request.form and request.form['newPhoneNo']==str(e[3]):
					b=b+'<h1>The phone number has been used!</h1>'
					found=True
				if 'newUsername' in request.form and request.form['newUsername']==e[5]:
					b=b+'<h1>The username has been used!</h1>'
					found=True
		cursor.execute('select * from customer where 1;')
		for e in cursor.fetchall():
			if  e[0]==int(request.form['id']) and not found and not miss:
								
				if 'newName' in request.form:
					cursor.execute('''update customer set cname='{0}' where cid="{1}"'''.format(request.form['newName'],int(request.form['id'])))
					db.commit()
				elif'newEmail' in request.form:
					cursor.execute('''update customer set email='{0}' where cid="{1}"'''.format(request.form['newEmail'],int(request.form['id'])))
					db.commit()
				elif'newPhoneNo' in request.form:
					for i in request.form['newPhoneNo']:
						if str(i) <'0' or str(i) >'9' :
							TNF=False
					if len(request.form['newPhoneNo'])!=8:
						TNF=False
					if TNF:
						cursor.execute('''update customer set telno={0} where cid="{1}"'''.format(int(request.form['newPhoneNo']),int(request.form['id'])))
						db.commit()
					else:
						b=b+'<h1>The format of phone number is incorrect!</h1>'
				elif'newAddress' in request.form:
					cursor.execute('''update customer set address='{0}' where cid="{1}"'''.format(request.form['newAddress'],int(request.form['id'])))
					db.commit()
				elif'newUsername' in request.form:
					cursor.execute('''update customer set username='{0}' where cid="{1}"'''.format(request.form['newUsername'],int(request.form['id'])))
					db.commit()
					logon_user=request.form['newUsername']
				elif'newPassword' in request.form:
					cursor.execute('''update customer set password='{0}' where cid="{1}"'''.format(request.form['newPassword'],int(request.form['id'])))
					db.commit()
				if not found and TNF:
					b='<h1 style="margin-top:3%;margin-left:10%;">The update is success!</h1><form action="/admin_customer"><button>Back</button></form>'
		if found or not TNF:
			b=b+'<form action="/admin_customer"><button>Back</button></form>'
		elif miss:
			b=b+'<h1>There is/are missing data!</h1><form action="/admin_customer"><button>Back</button></form>'

		return a3+b+z


#admin account related

@app.route("/admin_account",methods=['post','get'])
def admin_account():
	key=''
	b='''
		<div align="center" style="margin:2%">
		<form action="/admin_account" id="head" method="post">
		<input type="text" name="key" placeholder=" Admin ID/Username " id="body" style="width:300px">
		<input type="submit" value="Search" id="body">
		</form></div>
		'''
	if 'key' in request.form:
		key=str(request.form['key'])
		b=b+'''
			<h2 id ="body">The result of searching:{0}</h2>
			'''.format(key)

	b=b+'''
		<form action="/admin_account_r" method="post">
		<table style="margin-left:20%;margin-right:20%">
		<tr>
		<td>AID</td>
		<td width=5%>&nbsp;</td>
		<td>Username</td>
		<td width=5%>&nbsp;</td>
		<td><button type="submit" name="add">+</button></td>
		<td width=5%>&nbsp;</td>
		<td width=5%>&nbsp;</td>
		</tr>
		<tr><td height=5%>&nbsp;<td></tr>
		'''.format(key)

	cursor=db.cursor()
	cursor.execute('select * from admin where 1;')
	for e in cursor.fetchall():
		if (key.upper() in str(e[2]).upper()) or (key.upper() in str(e[0]).upper()) :
			b=b+'''
					<tr>
  					<td>{0}</td>
  					<td width=5%>&nbsp;</td>
  					<td>{1}</td>
  					<td width=5%>&nbsp;</td>
  					<td><button type="submit" name="alter" value="{0}">Detail</button></td>
  					<td width=5%>&nbsp;</td>
  					<td><button type="submit" name="delete" value="{0}">Delete</button></td>
  					</tr>
  					<tr><td height=5%>&nbsp;<td></tr>
				'''.format(e[2],e[0])


	b=b+'''
		</table>
		</form>
		'''
	if logon_admin=='':
		return a1+'<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'+z
	else:
		return a3+b+z

@app.route("/admin_account_r",methods=['post','get'])
def admin_account_r():
	
	if 'add' in request.form:
		b='''<div id="body" style="margin-left: 10%">
		<h1>Adding new admin:</h1>
		<form method="post" action="admin_account_r2">
		<input type="hidden" name="add">
		<table>
		<tr><br></tr>
		Please enter the following information:<br><br>			
		<tr>
		<td>Userame:</td>
		<td><input type="text" name="username"></td>
		</tr>	
		<tr>
		<td>Password:</td>
		<td><input type="text" name="password"></td>
		</tr>
		</table>
		<br><br>
		<input type="submit" >
		</form>
		</div>
		'''		

	
	if 'alter' in request.form:
		cursor=db.cursor()
		cursor.execute('select * from admin where 1;')
		for e in cursor.fetchall():
			if request.form['alter'] ==str(e[2]):
				b='''
					<h1 style="margin-left: 10%;margin-top:3%">The information of admin account:</h1>
					<form method="post" action="/admin_account_r2">
					<input type = "hidden" name="alter">
					<table style="margin-left: 10%;">
					

					<tr><td>ID:</td>
						<td>{0}</td>
						<td><input type = "hidden" name="id" value='{0}'></td>
					</tr>
					<tr><td>Username:</td>
						<td>{1}</td>
						<td><input type = "submit" name="username" value='Alter'></td>
					</tr>
					<tr><td>Password:</td>
						<td>{2}</td>
						<td><input type = "submit" name="password" value='Alter'></td>

					</tr>
					</table>
			
					</form>
					'''.format(e[2],e[0],e[1])

	if 'delete' in request.form:
		b='''
			<h2 style="width: 75%;margin-top:2%;margin-left:2%">Do you really want to delete this admin account?</h2>
			<form action="admin_account_r2" method="post">
			'''
		cursor=db.cursor()
		cursor.execute('select * from admin where 1;')
		for e in cursor.fetchall():
			if str(e[2])==str(request.form["delete"]) :
				b=b+'''
				<div style="width: 75%;margin-top:2%;margin-left:2%">
  				<table>

					<tr><td>ID:</td>
						<td width=2%>&nbsp;</td>
						<td>{0}</td>
					</tr>
					<tr><td>Username</td>
						<td width=2%>&nbsp;</td>
						<td>{1}</td>
					</tr>
					<tr><td>Password</td>
						<td width=2%>&nbsp;</td>
						<td>{2}</td>
					</tr>
					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
  					<tr>
  					<td>&nbsp;</td>
  					</tr>
					<tr>
  						<td><button type="submit"  name="delete" value="{0}">Delete</button></td>
  						<td width=2%>&nbsp;</td>
  						<td><button type="submit"  name="cancel" >Cancel</button></td>
  					</tr>
					</table>
			
					</form>
					'''.format(e[2],e[0],e[1])


	
	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'
		return a1+b+z
	elif logon_admin!='':
		return a3+b+z

@app.route("/admin_account_r2",methods=['post','get'])
def admin_account_r2():
	cursor=db.cursor()
	b=''
	if "alter" in request.form:
		cursor=db.cursor()
		cursor.execute('select * from admin where 1;')
		for e in cursor.fetchall():
			if str(e[2])==str(request.form['id']):

				b='''
				<form method="post" action="/admin_account_r3">
				<input type="hidden" name="id" value="{0}">
				<table style="margin-left: 10%; margin-top:3%">
				'''.format(request.form['id'])

				if 'username' in request.form:
					b=b+'''
						<tr>
							<td>Username:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New username:</td>
							<td><input type = 'text' name = 'newUsername'></td>
						</tr>			   
					  '''.format(e[0])
				elif 'password' in request.form:
					b=b+'''
						<tr>
							<td>Password:</td>
							<td>{0}</td>
						</tr>
						<tr>
							<td>New password:</td>
							<td><input type = 'text' name = 'newPassword'></td>
						</tr>			   
					  '''.format(e[1])		

				b=b+'''
					<tr>
					<td><input type = "submit" value='Submit'></td>
					</tr>
					</table>
					</form>
					'''
				
	elif "delete" in request.form:
		cursor.execute('delete FROM admin WHERE AID={0}'.format(request.form['delete']))
		db.commit()
		b=b+"<h1>Delete successfully</h1><form action='/admin_account'><button>Back</button></form>"

	elif "cancel" in request.form:
		return redirect(url_for('admin_account'))

	elif "add" in request.form:
		miss=False
		if len(request.form['username'])<1 or len(request.form['password'])<1:
				miss=True
		if not miss:
			cursor=db.cursor()
			cursor.execute("insert into admin values('%s','%s',%d)"%(request.form['username'],request.form['password'],0))
			db.commit()
			b='''<h1>The new account is added!</h1>
				<form action="/admin_account"><button>Back</button></form>'''	
		elif miss:
			b=b+'<h1>There is/are missing data!</h1><form action="/admin_account"><button>Back</button></form>'
			
	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/admin_logon">logon</a> first!</h3>'
		return a1+b+z
	elif logon_admin!='':
		return a3+b+z

@app.route("/admin_account_r3",methods=['post','get'])
def admin_account_r3():
	b=''
	miss=False
	for e,i in request.form.items():
		if len(i)<1:
			miss=True
	
	if logon_admin=='':
		b='<h3 align="center" style="margin-top:5%">Please <a href="/logon">logon</a> first!</h3>'
		return a1+b+z
	elif not miss:
		cursor=db.cursor()
		cursor.execute('select * from admin where 1;')
		found=False
		b=''
		for e in cursor.fetchall():
			if e[2]!=int(request.form['id']):
				if 'newUsername' in request.form and request.form['newUsername']==e[0]:
					b=b+'<h1>The username has been used!</h1>'
					found=True
		cursor.execute('select * from admin where 1;')
		for e in cursor.fetchall():
			if  e[2]==int(request.form['id']) and not found:
								
				if'newUsername' in request.form:
					cursor.execute('''update admin set username='{0}' where AID="{1}"'''.format(request.form['newUsername'],int(request.form['id'])))
					db.commit()
					logon_user=request.form['newUsername']
				elif'newPassword' in request.form:
					cursor.execute('''update admin set password='{0}' where AID="{1}"'''.format(request.form['newPassword'],int(request.form['id'])))
					db.commit()
				if not found:
					b='<h1 style="margin-top:3%;margin-left:10%;">The update is success!</h1><form action="/admin_account"><button>Back</button></form>'
		if found:
			b=b+'<form action="/admin_account"><button>Back</button></form>'

		return a3+b+z

	elif miss:
		b=b+'<h1>There is/are missing data!</h1><form action="/admin_account"><button>Back</button></form>'


if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0",port=8000)
