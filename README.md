## Workers
### This is a Python application powered by Django and its Object-Relational Mapper to provide convenient access to stored data. In this particular case users are able to create, read, update and delete worker profiles. 

--------------------------------------------------

### Features:
* Working with template inheritance mechanism to build a base “skeleton” template that contains all the common elements and defines blocks that child templates can override
* Taking full advantage of Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Writing as much functionality as possible in models or utility files instead of views 
* Using Model Manager - an interface through which database query operations are provided to Django models
* Performing AJAX requests from Django templates using JQuery to allow for web pages to be updated asynchronously by exchanging data with a web server behind the scenes
* Storing app’s secure credentials in environment variables
* Utilizing setUp method to handle especially expensive setup operations for all of the tests within a module
* Performing extensive selenium tests using 'page object pattern' instead of making raw WebDriver calls to have cleaner code:
  * Utilizing DRY (Don’t repeat yourself) principle to minimize code duplication by having all ID-locators in one place
  * Setting an interface between web page’s elements and tests
  * Avoiding usage of WebDriver APIs in test methods
  * Encapsulating the services of web pages, not only exposing their elements

--------------------------------------------------

### Code Coverage:
* Selenium and unit tests combined

```
coverage run -p manage.py test project && coverage run -p manage.py test rest_api && coverage run -p manage.py test tests_selenium && coverage combine && coverage html

```

<img src="https://github.com/mjaroszewski1979/workers-in/blob/main/coverage_report.png">

---------------------------------------------------

![caption](https://github.com/mjaroszewski1979/workers-in/blob/main/workers.png)
  
  Code | Technologies
  ---- | ------------
[<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/workers-in) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png">  &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/jquery_g.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/bulma_g.png">


