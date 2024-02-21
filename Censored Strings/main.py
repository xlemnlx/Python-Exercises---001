from unittest import main
from censored_string_func import censored_string

test_one = ("Today is a Wednesday!", ["Today", "a"], "-")

print(censored_string(test_one))

main(module="test_module_censored_string")