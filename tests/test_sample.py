def inc(x):
        return x + 1
try:
    assert inc(4) == 5, "InValid Operation"

except AssertionError as msg:
    print(msg)

