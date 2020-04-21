Pytest Selenium Framework

To run project install following packages

    - PyTest
    - Selenium
    - pytest-html (for html report)

Notes

    # PyTest rules
    # Any PyTest file should start with test_ or _test
    # PyTest methods must start with test
    # All codes should be wrapped with method
    # To run from console just go to that directory and type:
    #       py.test                         plain
    #       py.test -v                      more detailed
    #       py.test -v -s                   with console output
    #       py.test -v -s -k credit_cart    to run only tests with name contains credit_cart
    # -k stands for method names execution, -s logs in output, -v stands for more info metadata
    # -m for marks, you can mark (tag) tests and the run with -m
    # @pytest.mark.skip for skipping test case
    # we can run specific file with py.test <filename>
    # to generate HTML report first install pytest-html
    # pip3 install pytest-html
    # then run following command
    # pytest --html=report.html
