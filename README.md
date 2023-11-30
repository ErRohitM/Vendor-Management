<h2 align="left">Vendor Management System</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" height="40" alt="django logo"  />
  <img width="12" />
  
</div>

<h3 align="left">Overview</h3>


###

<p align="left">Welcome to the Vendor Management System, a Django-based application designed to streamline vendor profile management, purchase order tracking, and vendor performance evaluation. This system is built using Django and Django REST Framework, providing a robust solution for effective vendor management.</p>

###

<h3 align="left">Requirements</h3>

###

<p align="left">Project Tech - Python, Django, Django REST Framework</p>

###

<h3 align="left">Project Setup</h3>

###

<h4 align="left">Clone the Repository</h4>

<h5 align="left">> git clone https://github.com/ErRohitM/Vendor-Management.git</h5>

###

<h4 align="left">Install Dependencies</h4>

<h5 align="left">>cd vendor-management-system</h5>
<h5 align="left">>pip install -r requirements.txt</h6>

###

<h4 align="left">Run Migrations</h4>

<h5 align="left">>python manage.py migrate</h5>

###

<h4 align="left">Run Development Server</h4>

###

<h5 align="left">> python manage.py runserver</h5>

###

<h4 align="left">open http://localhost:8000/api/ with your browser to access the APIs.</h4>

###

<h3 align="left">Key Features</h3>

###

<h4 align="left"> 1. Vendor Profile Management</h4>

###

<h3 align="left">> POST, GET'/api/vendors/' - List and Create a New Vendor</h3>

###

<h3 align="left">> PUT, DELETE '/api/vendors/{vendor_id}/' - Retrieve , Update and Delete Vendor:</h3>

###

<h4 align="left"> 2. Purchase Order Tracking</h4>

###

<h3 align="left">> POST, GET '/api/purchase_orders/' - List and Create a Purchase Order</h3>

###

<h3 align="left">> PUT, DELETE '/api/purchase_orders/{po_id}/' - Retrieve , Update and Delete Purchase Order</h3>

###

<h4 align="left"> 3. Vendor Performance Evaluation</h4>

###

<h3 align="left">> GET '/api/vendors/{vendor_id}/performance' - Retrieve calculated performance metrics for a specific vendor,</h3>

###

<h4 align="left"> Additional Functionalities</h4>

###

<h3 align="left">> PUT '/api/purchase_orders/{po_id}/acknowledge' - Retrieve and Update Acknowledgment of Purchase Order</h3>

###



<h3 align="left">Contributing</h3>

###

<p align="left"> Thank you for choosing the Vendor Management System. If you have any questions or feedback, please don't hesitate to reach out.</p>
    
<h3 align="left">Happy coding! 🚀</h3>
###
