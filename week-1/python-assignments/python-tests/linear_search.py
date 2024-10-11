def linear_search(desired_num: int, junk_arr: list) -> int:
    for index in range(len(junk_arr)):
        if junk_arr[index] == desired_num:
            return index

print(f"See the test works fine with type annotation we got back: {linear_search(1, [3,2,4,1])}")