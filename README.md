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
   
---
5. startapp 데이식스 
   1. Terminal
      1. python manage.py startapp day6
   2. helloidol/settings.py
      1. 'day6', in INSTALLED_APPS
   3. 데이식스/
      1. views
         1. show_성진()
         2. show_young.K()
         3. show_원필()
         4. show_도운()
         5. -> templates에 context 전달
      2. templates/데이식스/
         1. ~~성진.html~~
            1. title: 데이식스 - 성진
            2. h1 : 데이식스
            3. h2 : 성진
            4. img : 성진 프로필 사진
               1. border-radius.50%
         2. 멤버.html
            1. group_name, name, img_src
         3. ~~young.k.html~~
         4. ~~원필.html~~
         5. ~~도운.html~~
      3. urls
         1. 데이식스/ -> 성진/ -> show_성진()
         2. 데이식스/ -> young.k/ -> show_young.k()
         3. 데이식스/ -> 원필/ -> show_원필()
         4. 데이식스/ -> 도운/ -> show_도운()