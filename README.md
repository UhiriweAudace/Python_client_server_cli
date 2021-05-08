# DSSA #Building Server - CLI

Building a command line interface which handle different user's argument options while they are running the application.

## Steps to run the application

- make sure that python3 is installed on your pc

- Open your terminal and then Navigate where the project is located on your pc, after that run the following command:
  - change main app file mode
    ```shell
    chmod 744 app.py
    ```
  - change client app file mode
    ```shell
    chmod 744 client.py
    ```
  - To view different arguments options to use
    ```shell
    ./app.py --help
    ```
  - run the server application
    ```shell
    ./app.py <options argument>
    i.e ./app.py -ps 20
    ```
  - run the client application
    ```shell
    ./client.py <options argument>
    i.e ./client.py -ps 20
    ```
