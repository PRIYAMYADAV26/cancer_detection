from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
import pickle  # For loading the model
from django.shortcuts import render
from .models import User
import numpy as np

# Load the model
with open(r'C:\Users\priya\OneDrive\Desktop\Priti Minor\minorproject\core\core\model (5).pkl', 'rb') as file:
    breast_model = pickle.load(file)

def breast(request):
    value = None  # Initialize value to None to handle GET request

    if request.method == 'POST':
        try:
            # Retrieve input values from the form
            mean_radius = float(request.POST.get('mean_radius', 0))
            mean_texture = float(request.POST.get('mean_texture', 0))
            mean_perimeter = float(request.POST.get('mean_perimeter', 0))
            mean_area = float(request.POST.get('mean_area', 0))
            mean_concavity = float(request.POST.get('mean_concavity', 0))

            # Combine the features into a numpy array
            features = np.array([mean_radius, mean_texture, mean_perimeter, mean_area, mean_concavity])

            # Ensure that we have exactly 5 features
            assert features.shape[0] == 5, f"Expected 5 features, but got {features.shape[0]}."

            # Reshape the input to match the model's expected input shape
            user_data = features.reshape(1, -1)

            # Make prediction
            prediction = breast_model.predict(user_data)

            # Determine the result based on the prediction
            if int(prediction[0]) == 1:
                value = 'You have not breast cancer.'
            else:
                value = 'You have breast cancer.'
        except Exception as e:
            value = f"Error in processing the data: {e}"

    # Render the template with the result
    return render(request, 'breast.html', {'result': value})

# Load the trained model from the .pkl file
with open(r'C:\Users\priya\OneDrive\Desktop\Priti Minor\minorproject\core\core\logistic_regression_model.pkl', 'rb') as file:
    logistic_model = pickle.load(file)

def lung(request):
    prediction_result = None
    if request.method == 'POST':
        # Example of expected input data
        input_data = {
            'GENDER': request.POST.get('GENDER'),
            'AGE': int(request.POST.get('AGE')),
            'SMOKING': int(request.POST.get('SMOKING')),
            'YELLOW_FINGERS': int(request.POST.get('YELLOW_FINGERS')),
            'ANXIETY': int(request.POST.get('ANXIETY')),
            'PEER_PRESSURE': int(request.POST.get('PEER_PRESSURE')),
            'CHRONIC_DISEASE': int(request.POST.get('CHRONIC_DISEASE')),
            'FATIGUE': int(request.POST.get('FATIGUE')),
            'ALLERGY': int(request.POST.get('ALLERGY')),
            'WHEEZING': int(request.POST.get('WHEEZING')),
            'ALCOHOL_CONSUMING': int(request.POST.get('ALCOHOL_CONSUMING')),
            'COUGHING': int(request.POST.get('COUGHING')),
            'SHORTNESS_OF_BREATH': int(request.POST.get('SHORTNESS_OF_BREATH')),
            'SWALLOWING_DIFFICULTY': int(request.POST.get('SWALLOWING_DIFFICULTY')),
            'CHEST_PAIN': int(request.POST.get('CHEST_PAIN'))
        }

        # Preprocess input data
        gender_mapping = {'M': 1, 'F': 0}
        input_data['GENDER'] = gender_mapping.get(input_data['GENDER'], -1)

        input_values = np.array([list(input_data.values())])

        # Make prediction
        prediction = logistic_model.predict(input_values)
        prediction_result = 'You have lung cancer' if prediction[0] == 1 else 'You have not Lung cancer '

    return render(request, 'lung.html', {'prediction_result': prediction_result})

def Sign_in(request):
    if request.method == 'POST':
        # Get username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Authenticate user
        # user = authenticate(request, username=username, password=password)
        print(username,password,email)
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another one.")
            return redirect('signin1')  # Redirect back to the registration page
       
        # Create the user securely with hashed password
        user = User.objects.create(username=username, password=password,email=email)
        user.save()

        # Redirect to the breast cancer page after successful registration
        return redirect('prediction') 
    if request.method == "POST":
        email = request.POST.get('email')
        # Add other form data processing here

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, 'Sign_in.html')  

        # Proceed to create a new user if the email doesn't exist
        user = User(email=email)
        user.save()  # Adjust this as per your form handling logic
        messages.success(request, "User registered successfully!")
        return render(request, 'prediction.html') 
    return render(request, 'Sign_in.html')



def home(request):
    if not request.user.is_authenticated:
        return redirect('Sign_in')  # Redirect to the sign-in page if not logged in
    return render(request, 'base.html', {'username': request.user.username})
    
def login(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user exists and verify the password
        print("testerrror0")
        user = authenticate(email=email,password=password)
        print("testerrror1")
        try:
            print("testerrror2")
            user = User.objects.get(email=email)
            if user.password == password:
                print("testerrror3")
                return redirect('prediction')  # Redirect to the home page after successful login
            else:
                error = "Invalid username or password"
        except User.DoesNotExist:
            error = "User Does not exist"

    print("testerrror4")
    error = "Invalid username or password"
    return render(request, 'login.html', {'error': error})

def home(request): 
    return render(request, 'base.html') 

def prediction(request): 
    return render(request, 'prediction.html') 
