## Workers
### This is a Python application powered by Django and its Object-Relational Mapper to provide convenient access to stored data. In this particular case users are able to create, read, update and delete worker profiles. 

--------------------------------------------------

### Features:
* One of the key tasks of a proficient software developer is to create a user interface that is not only visually appealing but also easy to use. One way to achieve this is through the use of **template inheritance mechanism**. Template inheritance mechanism involves building a base "skeleton" template that contains all the common elements and defines blocks that child templates can override. This approach saves time by avoiding the need to recreate common elements in each template. With this technique, it is possible to create a consistent and cohesive design for a website or application. Moreover, if there are any updates or changes needed, it can be done easily and quickly as they only need to be made in the base template. In addition, this mechanism can also enhance code readability and maintainability. By having a central location for common elements, it is easier to manage and modify the code.
* One way to ensure that data is transferred safely is by using Django's built-in features, **including Cross-Site Request Forgery Protection**. Cross-site request forgery (CSRF) attacks occur when a malicious website tricks a user's browser into making a request to another website without their knowledge or consent. This type of attack can result in data theft or corruption, making it essential to protect against. Django's CSRF protection works by including a unique token in each form submission. This token is validated on the server-side to ensure that the request came from the correct user and not from a malicious source. By using this feature, developers can ensure that web forms are safe and secure, and that data is transferred safely to the database. In addition to CSRF protection, Django also includes other built-in security features, such as user authentication and authorization, password hashing, and SSL encryption. These features are designed to protect against common security threats and make it easier for developers to build secure web applications.
* **Breaking down logic into smaller, manageable parts** is crucial to ensuring the success of any project. One way to achieve this is by adding various new Django applications to an existing project. By creating smaller, more focused applications within a larger project, developers can improve code organization, maintainability, and scalability. Each application can handle a specific task or feature of the project, such as user authentication, data management, or payment processing. This approach can also make it easier to debug and test individual parts of the codebase. When adding new applications to an existing Django project, it's important to consider the functionality and purpose of each application. Each application should be responsible for a specific feature or function within the project, making it easier to modify and maintain the codebase in the long run. However, it's important to keep in mind that adding too many applications can also have drawbacks. It can increase the complexity of the codebase and slow down the overall performance of the project. Therefore, it's crucial to strike a balance between breaking down the logic of the project and keeping it manageable.
* **Breaking down logic into smaller, manageable parts** is crucial to ensuring the success of any project. One way to achieve this is by adding various new Django applications to an existing project. By creating smaller, more focused applications within a larger project, developers can improve code organization, maintainability, and scalability. Each application can handle a specific task or feature of the project, such as user authentication, data management, or payment processing. This approach can also make it easier to debug and test individual parts of the codebase. When adding new applications to an existing Django project, it's important to consider the functionality and purpose of each application. Each application should be responsible for a specific feature or function within the project, making it easier to modify and maintain the codebase in the long run. However, it's important to keep in mind that adding too many applications can also have drawbacks. It can increase the complexity of the codebase and slow down the overall performance of the project. Therefore, it's crucial to strike a balance between breaking down the logic of the project and keeping it manageable.
* One of the standout features of my Django application is its **use of Model Manager**. This interface plays a crucial role in providing database query operations to Django models. Essentially, the Model Manager acts as a mediator between the database and the models in the application. By leveraging the Model Manager, my application gains access to a variety of helpful query methods, such as filter(), all(), and exclude(). These methods make it much easier to manipulate and retrieve data from the database in a way that is both efficient and effective. Additionally, the Model Manager can be customized to suit the specific needs of the application. This means that developers can define their own query methods or modify existing ones to better suit the application's requirements. This level of flexibility is essential when it comes to building robust, scalable applications that can evolve over time.
* I have incorporated into my Django application the ability to perform AJAX requests using JQuery from Django templates. This allows web pages to be updated in real-time, without the need for a full page refresh, making for a smoother user experience. By leveraging the power of asynchronous communication between the web browser and the server, data can be exchanged behind the scenes, without the user being aware of it. This is particularly useful for web applications that require frequent updates, such as chat applications or social media platforms, as it reduces the load on the server and minimizes the time it takes for data to be displayed on the user's screen. With this feature, users can enjoy a more seamless and efficient browsing experience.
* Understanding the importance of keeping sensitive information secure, we always store API keys, database passwords, and other credentials in environment variables. Environment variables are values that can be set in the operating system and accessed by applications. By **storing sensitive information in environment variables**, developers can keep this information separate from the codebase, reducing the risk of accidental exposure. Storing sensitive information in environment variables also makes it easier to manage and maintain credentials across multiple environments. Rather than hard-coding credentials into the application, environment variables can be set differently for each environment, such as development, staging, and production. This helps to ensure that sensitive information is not accidentally exposed in a non-production environment. However, it's important to keep in mind that environment variables are not a foolproof security measure. They are still vulnerable to potential security breaches if not properly secured or if accessed by unauthorized users. Therefore, it's important to follow best practices for securing sensitive information, such as using strong passwords, limiting access to credentials, and regularly monitoring and auditing access to environment variables.
* Writing efficient and fast tests is essential for a successful project. In Django, one way to optimize tests is by **utilizing the setUp method** to handle especially expensive setup operations for all of the tests within a module. The setUp method is a method that is called before each test in a module. It is used to set up any test data or other resources needed for the tests. By using the setUp method to handle expensive setup operations, such as creating database records or generating test data, we can save time and resources in our test suite. Using the setUp method not only saves time, but it also makes our tests more reliable. By setting up the necessary data and resources before each test, we ensure that our tests are always running with the correct environment and data. This helps to prevent false positives or negatives in our test results, which can be time-consuming and frustrating to debug. However, it's important to keep in mind that the setUp method should be used judiciously. While it can be tempting to use the setUp method to handle all setup operations, doing so can actually slow down our tests. This is because the setUp method is called before each test, and if it is too complex or time-consuming, it can add significant overhead to our test suite.
* When it comes to software testing, it's essential to ensure that the code is clean, efficient, and easy to understand. One way to achieve this is by **utilizing the 'page object pattern'** while conducting extensive selenium tests instead of using raw WebDriver calls. The page object pattern allows for a cleaner codebase by following the DRY (Don't Repeat Yourself) principle, where all ID-locators are in one place. This practice minimizes code duplication and makes maintenance and updates more manageable. Another advantage of the page object pattern is that it sets up an interface between web page elements and tests. This separation helps to avoid the usage of WebDriver APIs in test methods, making the tests more robust and less prone to failure. Additionally, encapsulating the services of web pages, rather than exposing their elements, leads to better test organization and helps to prevent code duplication. Overall, using the page object pattern can help to streamline your selenium testing process and result in a more efficient, effective, and maintainable codebase.

--------------------------------------------------

### Docker info:
* Compose is a tool for defining and running multi-container Docker applications
* With a single command, you create and start all the services from your configuration
* In this example Compose command line tool allows you to create and start separate containers for each dependency with a single command (docker-compose up)
* Included custom shell script creates a superuser and runs initial database migrations

```
docker-compose up

```


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
[<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/workers-in) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png">  &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/jquery_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/bulma_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/js1.png">


