Web scraper
==============
**Pajączek** - celem aplikacji jest zebranie artykułów z portalu galeriazyskow.pl, przetworzenie i zaprezentowanie ich w formie serwisu typu REST zwracającego zgromadzone posty.

Wymagania funkcjonalne
----------
- Pobieranie treści artykułów ze strony galeriazyskow.pl
- Serwis typu REST zwracający zgromadzone posty

Wymagania niefunkcjonalne
----------
- Komputer.
- Os: Linux lub Windows
- Połączenie z internetem.

Użycie
----------

Jeśli nie masz zainstalowanego docker'a, użyj https://labs.play-with-docker.com/

::

    $ docker-compose up -d db
    $ docker-compose up api
