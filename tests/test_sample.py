def inc(x):
        return x + 1
try:
    assert inc(4) == 666666, "InValid Operation"

except AssertionError as msg:
    print(msg)

