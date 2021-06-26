from django.shortcuts import render, redirect
from django.http import HttpResponse
from PresList.models import Sender, Product, Category, Price, Feedback



def home_page(request):
   senders = Sender.objects.all()
   return render(request, 'homepage.html',{'senders': senders})

def new_list(request):
   newsender_ = Sender.objects.create(first_name=request.POST['one'],last_name=request.POST['last'],address=request.POST['address'])
   return redirect(f'/{newsender_.id}/view_list')
    
def addsend_id(request, sender_id):
   sender_ = Sender.objects.get(id=sender_id)  
   Product.objects.create(product_name=request.POST['prodname'],product_details=request.POST['proddetails'],product_type=request.POST['prodtype'], sender=sender_)
   return redirect(f'/{sender_.id}/view_list') 
   
def view_list(request, sender_id):    
   sender_ = Sender.objects.get(id=sender_id)
   return render(request, 'registration.html', {'sender': sender_})
   
def edit(request, id):
   sender=Sender.objects.get(id=id)
   gas = {'sender':sender}
   return render(request, 'edilete.html', gas)

def update (request, id):
   sender=Sender.objects.get(id=id)
   sender.first_name=request.POST['one']
   sender.last_name=request.POST['last']
   sender.Address=request.POST['address']
   sender.save()
   return redirect('/')

def delete(request, id):
    sender=Sender.objects.get(id=id)
    sender.delete()
    return redirect('/')

'''
def home_page(request):
    senders = Sender.objects.all()
    return render(request, 'homepage.html',{'senders' : senders})

def view_list(request):
    #sender_= Sender.objects.get(id=sender_id)
    return render(request, 'registration.html')

def view3(request):
    #sender_= Sender.objects.get(id=sender_id)
    return render(request, 'model3.html')

def view4(request):
    #sender_= Sender.objects.get(id=sender_id)
    return render(request, 'model4.html')

def view5(request):
    #sender_= Sender.objects.get(id=sender_id)
    return render(request, 'model5.html')
    '''


'''def new_list(request):
    sender_= Sender.objects.create()
    #product.objects.create(Owner =request.POST['on'],fname =request.POST['od'], Sender=Sender)
    return redirect(f'/PresList/{sender_.id}/')

def add_item(request, sender_id):
    sender_ = Sender.objects.get(id=sender_id)'''
 
    #product.objects.create(fullname=request.POST['fname'],ir =request.POST['ir'],bname =request.POST['bname'],Sender=Sender)
    #return redirect(f'/PresList/{sender_.id}/')


def dataManipulation(request):
    #Creating data
    people = Sender(first_name="Ding", last_name="Manuel", address="bkl66 lt66 GreenGate" )
    people.save()

    #Read all data
    courier = Sender.objects.all()
    result = 'Printing all customers list : <br>'
    for x in courier:
        res += X.first_name+"<br>"

    #Read one data
    box = Sender.get(id="19")
    res += "Printing one customer profile : <br>"
    res += box.last_name

    #Delete data
    res+= '<br> Deletinng... <br>'
    box.delete()

    #Update data
    people = Sender.objects.get(first_name="Ding")
    people.product_name = "Packs of Briefs"
    people.save()
    res = ""

    #Filtering data
    qs = Booking.objects.filter(first_name="Ding")
    res += "found : %s result<br>"%len(qs)

    #ordering data
    qs = Sender.objects.order_by("first_name")
    for x in qs: 
        res += x.first_name + x.last_name + '<br>'



