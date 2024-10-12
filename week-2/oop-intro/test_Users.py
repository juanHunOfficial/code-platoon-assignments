import Users
import pytest


@pytest.mark.parametrize(
    ("name", "email", "license_number", "expected"),
    (
        #test 1:
        ("Name", "template@code-platoon.com", "LXXX-XXX-XXX-XX-X", 
        "Congradulations! Your account has been created, your ID number is: 1000"),
        #test 2:
        ("Juan Hun", "juan_hun@yahoo.com", "H500-555-555-55-5",
         "Congradulations! Your account has been created, your ID number is: 1001"),
        #test 3:
        ("Spongebob Squarepants", "bikini-bottom-chef@gmail.com", "H200-222-222-22-2",
         "Congradulations! Your account has been created, your ID number is: 1002"),
        #test 4:
        ("Patrick Theadore Star", "under-a-rock@yahoo.com", "H111-111-123-45-6",
         "Congradulations! Your account has been created, your ID number is: 1003"),
        #test 5:
        ("Sandy Cheeks", "the-dome@littleTree.gov", "S233-225-124-45-7",
         "Congradulations! Your account has been created, your ID number is: 1004"),
        #test 6:
        ("Squidward Tennisballs", "super-star18@compuserve.com", "S555-555-555-55-5",
         "Congradulations! Your account has been created, your ID number is: 1005"),
        #test 7:
        ("Eugene Harold Krabs", "i-love-money@krustykrew.com", "K200-002-222-00-2",
         "Congradulations! Your account has been created, your ID number is: 1006")
        
    )
)
def test__init__(name: str , email: str, license_number: str, expected: str) -> str:
    assert Users.Users(name, email, license_number) == expected