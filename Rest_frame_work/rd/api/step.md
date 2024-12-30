# Step-by-Step Guide to Create a Django Project with REST API

## Step 1: Create and Activate Virtual Environment
1. Create a virtual environment.
2. Activate the virtual environment.

---

## Step 2: Install Django and Django REST Framework
1. Install Django.
2. Install Django REST Framework.

---

## Step 3: Start a Django Project
- Use the `django-admin` command to create a project named `rd`.

---

## Step 4: Navigate into the Project Directory
- Use the `cd` command to enter the project directory.

---

## Step 5: Create an Application
- Use the `python manage.py startapp api` command to create an app named `api`.

---

## Step 6: Create Models
- Define your models in the `models.py` file of the `api` app.

---

## Step 7: Run Migrations
1. Run `python manage.py makemigrations` to create migration files.
2. Run `python manage.py migrate` to apply the migrations and create the model in the database.

---

## Step 8: Create a Superuser
- Use the `python manage.py createsuperuser` command to create a superuser.

---

## Step 9: Add Models to the Admin Panel
- Register your models in the `admin.py` file of the `api` app to manage them in the admin interface.

---

## Step 10: Add Manual Entries via Admin Panel
- Use the admin panel to manually add entries for the model.

---

## Step 11: Create Serializers
- Create a `serializers.py` file in the `api` app.
- Add a class named `StudentSerializers` for data serialization.

---

## Step 12: Create Views
### **Student_details View**
- Fetches a specific student record based on the primary key (pk).
- Serializes the student data using `StudentSerializers`.
- Converts the serialized data into JSON format.
- Returns the JSON data as an HTTP response.

### **Student_list View**
- Fetches all student records.
- Serializes the data using `many=True` for multiple objects.
- Converts the serialized data into JSON format.
- Returns the JSON data as an HTTP response.

### Additional Notes:
- Views utilize Django REST Framework (DRF) for serialization and JSON conversion.
- `JSONRenderer` is used to render serialized data into JSON format.
- `HttpResponse` is used to send the JSON response with the correct content type.

---

## Step 13: Configure URLs
This Django URL configuration file defines three routes:

1. **Admin Interface:**
   - Path: `admin/`
   - Maps to Django's built-in admin site.

2. **Single Student Details:**
   - Path: `stuinfo/<int:pk>`
   - Calls the `Student_details` view from the `api` app.
   - Expects an integer `pk` (primary key) in the URL to fetch details of a specific student.

3. **All Students List:**
   - Path: `stuinfo/`
   - Calls the `Student_list` view from the `api` app.
   - Fetches and displays the details of all students.

**Notes:**
- `path()` is used to map URLs to specific views.
- `<int:pk>` captures an integer from the URL to be passed to the `Student_details` view.
- All paths are linked to views from the `api` app.

---

## Step 14: Run the Server
- Run the command `python manage.py runserver` to start the Django server.

---

## Step 15: Create a `myapp.py` File (Optional)
- Create a `myapp.py` file to demonstrate how to communicate with the API.
- This file fetches data from the Django running application.
- Run the `myapp.py` file after starting the Django server.
