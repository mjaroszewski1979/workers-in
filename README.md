## Workers
### This is a Python application powered by Django and its Object-Relational Mapper to provide convenient access to stored data. In this particular case users are able to create, read, update and delete worker profiles. 

--------------------------------------------------

### Features:
* Working with template inheritance mechanism to build a base “skeleton” template that contains all the common elements and defines blocks that child templates can override
* Taking full advantage of Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Writing as much functionality as possible in models or utility files instead of views 
* Storing app’s secure credentials in environment variables

--------------------------------------------------

### Code Coverage:
* Selenium and unit tests combined

```
coverage run -p manage.py test project && coverage run -p manage.py test rest_api && coverage run -p manage.py test tests_selenium && coverage combine && coverage html

```

<img src="https://github.com/mjaroszewski1979/workers-in/blob/main/coverage_report.png">


