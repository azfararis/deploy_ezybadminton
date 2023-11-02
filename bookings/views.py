from django.shortcuts import render, redirect
from .models import User, Court, Booking
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

def index(request):
    courts = Court.objects.all()
    return render(request, 'index.html', {'courts': courts})

from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)  # Add this line


        if user is not None:
            login(request, user)
            return redirect('homepage')  # Replace with your desired redirect
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')



def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        phoneNo = request.POST['phoneNo']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            signup_error = "Passwords do not match"
            return render(request, 'login.html', {'signup_error': signup_error})

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            signup_error = "Username is already taken"
            return render(request, 'login.html', {'signup_error': signup_error})

        # Create a new user
        user = User.objects.create(username=username, address=address, phoneNo=phoneNo, password=password)
        user.save()

        return redirect('login_user')  # Replace with the name of your login view

    return render(request, 'login.html')



def login_page(request):
    return render(request, 'login.html')



def homepage(request):
    courts = Court.objects.all()
    return render(request, 'homepage.html', {'courts': courts})



def booking_page(request):
    if request.user.is_authenticated:

        user = request.user

        courts = Court.objects.all()

        if request.method == 'POST':
            user = request.POST['userId']
            court_id = request.POST['courtId']
            date = request.POST['date']
            time = request.POST['time']
            hours = request.POST['hours']
            

            price_per_hour = float(Court.objects.get(courtId=court_id).price_per_hour)
            total_price = price_per_hour * int(hours)

            court = Court.objects.get(courtId=court_id)

            booking = Booking(
                courtId=court,
                userId=user,  
                date=date,
                time=time,
                hours=hours,
                totalPrice=total_price
            )

            booking.save()

            return redirect('receipt', booking_id=booking.id)

        return render(request, 'booking_page.html', {'courts': courts})
    else:
        return redirect('login_user')




def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

def receipt(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'receipt.html', {'booking': booking})



def create_booking(request, user_id, court_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        court = Court.objects.get(pk=court_id)
        date = request.POST['date']
        time = request.POST['time']
        hours = int(request.POST['hours'])
        
        # Calculate totalPrice based on price_per_hour and hours
        price_per_hour = court.price_per_hour
        total_price = price_per_hour * hours

        booking = Booking(userId=user, courtId=court, date=date, time=time, hours=hours, totalPrice=total_price)
        booking.save()

        return redirect('booking_list')

    return render(request, 'booking_page.html', {'user_id': user_id, 'court_id': court_id})




from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Booking

def update_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        new_hours = request.POST.get('new_hours')

        booking = get_object_or_404(Booking, pk=booking_id)
        booking.hours = new_hours
        booking.save()

        return JsonResponse({'message': 'Booking updated successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

def delete_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')

        booking = get_object_or_404(Booking, pk=booking_id)
        booking.delete()

        return JsonResponse({'message': 'Booking deleted successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
