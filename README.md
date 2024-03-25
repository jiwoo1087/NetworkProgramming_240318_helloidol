 #helloidol
  ---
1. startproject helloidol
    1. python -m pip install django~=4.2
    2. django-admin startproject _helloidol_ .
    3. [python manage.py migrate]
    4. python manage.py runserver
2. startapp _playground_ 
   1. Terminal
      1. python manager.py startapp _playground_
   2. helloidol/settings.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보 전달 : urls -> views -> (models) -> templates
   - 코드 작성 : models -> views-> template -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
      4. -> templates에 context 전달
   2. urls 
      1. _playground/hello/-> _say_hello()_
      2. _playground/hello_html/ -> _say_hello_html()
   3. templates/playground/
      1. hello.html
      2. bye.html
   4. helloidol/
      1. urls, playground/urls
         1. _playground/_ -> _hello/_ -> _say_helo()_
         2. _playground/_ -> _hello_html_ -> _say_hello_html()_
         3. _playground/_ -> _by_html/_ -> _say_bye_html()_