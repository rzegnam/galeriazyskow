Skrobak
==============
**Skrobak** - celem aplikacji jest zebranie artykułów z portalu galeriazyskow.pl, przetworzenie i zaprezentowanie ich w formie serwisu typu REST zwracającego zgromadzone posty.

**Prezentacja projektu**
----------
http://bit.ly/2HI7k18

Wymagania funkcjonalne
----------
- Pobieranie treści artykułów ze strony galeriazyskow.pl
- Serwis typu REST zwracający zgromadzone posty

Wymagania niefunkcjonalne
----------
- Komputer
- Os: Linux lub Windows
- Połączenie z internetem
- Docker

Użycie
----------
Po sklonowaniu repozytorium i wywołaniu komendy docker-compose up, aplikacja jest dostępna na porcie 8080

Jeśli nie masz zainstalowanego docker'a, użyj https://labs.play-with-docker.com/

::

    $ git clone https://github.com/rzegnam/galeriazyskow
    $ cd galeriazyskow
    $ docker-compose up -d db
    $ docker-compose up api
