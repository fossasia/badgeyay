# Testing

### Setup

* Install the python3 dependencies in the virtual environment created.
  ```
  pip install -r requirements/test.txt
  ```

* Install the webdriver for Chrome used for browser automation.
    ```
    wget https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip
    mkdir chromedriver
    unzip chromedriver_linux64.zip -d chromedriver
    rm chromedriver_linux64.zip
    export PATH=$PATH:$PWD/chromedriver
    ```
  _*Make the changes in the download link of chromedriver if you are using a 32-bit machine*_
    
### Running

* Run the following command to test whether the server starts and the unit tests.
    ```
    python app/main.py >> log.txt 2>&1  & 
    nosetests app/tests/test.py -v --with-coverage
    ```
  _*Make sure to run the server before running tests*_
