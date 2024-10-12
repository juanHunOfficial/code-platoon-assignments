import Users
import pytest


@pytest.mark.parametrize(
    ("name", "email", "license_number"),
    (
        ("Name", "template@code-platoon.com", "LXXX-XXX-XXX-XX-X"),
        ("Juan Hun", "juan_hun@yahoo.com", "H500-555-555-55-5"),
        ("Spongebob Squarepants", "bikini-bottom-chef@gmail.com", "H200-222-222-22-2"),
        ("Patrick Theadore Star", "under-a-rock@yahoo.com", "H111-111-123-45-6")
        ("Sandy Cheeks", "the-dome@littleTree.gov", "S233-225-124-45-7"),
        ("Squidward Tennisballs", "super-star18@compuserve.com", "S555-555-555-55-5"),
        ("Eugene Harold Krabs", "i-love-money@krustykrew.com", "K200-002-222-00-2")
        
    )
)
def test__init__(name: str , email: str, license_number: str) -> None:
    assert Users(name, email, license_number) == ""