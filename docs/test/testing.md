# Testing

### Setup

* Install the python3 dependencies in the virtual environment created.
  ```
  pip install -r requirements/test.txt
  ```

* Install the webdriver for Firefox used for browser automation.
    ```
    wget https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz
    mkdir geckodriver
    tar -xzf geckodriver-v0.11.1-linux64.tar.gz -C geckodriver
    rm geckodriver-v0.11.1-linux64.tar.gz
    export PATH=$PATH:$PWD/geckodriver
    ```
    
### Running

* Run the following command to test whether the server starts and the unit tests.
    ```
    python app/main.py >> log.txt 2>&1  & 
    nosetests app/tests/test.py -v --with-coverage
    ```
