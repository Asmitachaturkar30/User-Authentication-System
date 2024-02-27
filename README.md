# User-Authentication-System
Django User Authentication and Authorization system Implementation 

# What Is Django Authentication?
<p> Django is a free, open-source Python web framework that supports fast development and clean, functional design. It provides a ready-made infrastructure for Python web applications, allowing developers to focus on building application logic. </p>
<br>
<p> Django provides a robust user authentication system, with support for user accounts, user groups, permissions, and cookie-based user session processing.
Although it is called “Django authentication”, the Django authentication system has a broader scope and handles both authentication (ensuring users are who they say they are) and authorization (determining what a user can do in the system, once they are authenticated). </p>
<br>
<p> Django’s authentication system is very generic, by design, and does not provide many specific features commonly found in web authentication systems. You can add many of these specific features using third-party packages.</p>

# The auth system consists of:
<P> Users </P>
<P>Permissions: Binary (yes/no) flags designating whether a user may perform a certain task.</P>
<P>Groups: A generic way of applying labels and permissions to more than one user.</P>
<P>A configurable password hashing system </P>
<P>Forms and view tools for logging in users, or restricting content </P>
<P>A pluggable backend system </P>
<h3>The authentication system in Django aims to be very generic and doesn’t provide some features commonly found in web authentication systems. Solutions for some of these common problems have been implemented in third-party packages: </h3>

<P>Password strength checking </P>
<P>Throttling of login attempts </P>
<P>Authentication against third-parties (OAuth, for example) </P>
<P>Object-level permissions </P>
