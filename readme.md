Pytest Selenium Framework

To run project install following packages

    - PyTest
    - Selenium
    - pytest-html (for html report)

PyTest rules

    Any PyTest file should start with test_ or _test
    PyTest methods must start with test
    All codes should be wrapped with method
    @pytest.mark.skip for skipping test case
    
```
To run from console just go to that directory and type:
  py.test                         plain
  py.test -v                      more detailed
  py.test -v -s                   with console output
  py.test -v -s -k credit_cart    to run only tests with name contains credit_cart
  py.test <filename>              to run specific file

-k stands for method names execution, 
-s logs in output, 
-v stands for more info metadata
-m for marks, you can mark (tag) tests and the run with -m
``` 
    
To generate HTML report:

    1. Install pytest-html
       > pip3 install pytest-html
    2. Then run following command
       > pytest --html=report.html
