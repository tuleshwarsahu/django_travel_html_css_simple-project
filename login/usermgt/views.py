from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def logininfo(Request):
	temp=loader.get_template("home.html")
	return(HttpResponse(temp.render()))

def bro(Request):
	temp=loader.get_template("brochure.html")
	return(HttpResponse(temp.render({},Request)))
    
def nominal(Request):
	temp=loader.get_template("nominal.html")
	return(HttpResponse(temp.render({},Request)))


def calc(Request):
	dist=int(Request.POST["dist"])
	rs=10
	nf= dist*rs
	x11=("<b><u>Your Bill</u></b>")
	x1=("entered distance="+str(dist))
	a1=("Per km charge= rs.10\n")
	if 'class' in Request.POST:
		if 'class1'==Request.POST['class']:
			c=nf*30/100
			tf=c+nf
			a2=("\n1st class charges=30% of Nominal fare:"+str(c))
		elif 'class2'== Request.POST['class']:
			c= nf*10/100
			tf=c+nf
			a2=("\n2nd class charges=10% of Nominal Fare:"+str(c))
		elif 'class3' == Request.POST['class']:
			c= nf*5/100
			tf=c+nf
			a2=("\n3rd class charges=5% of Nominal Fare:"+str(c))
		else:
			c= nf*0
			tf=c+nf
			a2=("Normal class charges=0% of Nominal Fare:"+str(c))
	if 'age' in Request.POST:
		if "1 to 10" ==Request.POST['age']:
			f1=tf*(100/100)
			f2=tf-f1
			a3=("\nAge discount=100%:"+str(f1))
		elif "10 to 20" ==Request.POST['age']:
			f1=tf*(30/100)
			f2=tf-f1
			a3=("\nAge discount=30%:"+str(f1))
		elif "20 to 60" ==Request.POST['age']:
			f1=tf*0
			f2=tf-f1
			a3=("\nAge discount=0%:"+str(f1))
		else:
			f1=tf*(50/100)
			f2=tf-f1
			a3=("\nAge discount=50%:"+str(f1))
	a4=("<b>______________________________________</b>")
            
	b=(str(x11)+"<br>"+str(x1)+"<br>"+str(a1)+"<br>"+str(a2)+"<br>"+str(a3)+"<br>"+str(a4)+"<br>"+"\n <B>Your  Bill  Amount =</B>"+str(f2))
	return(HttpResponse(b))
    
    