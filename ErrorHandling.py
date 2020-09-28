# float("123.4") -> 123.4
# float("#N/A") -> error

keyword = "Hello"
# try:
#     print(int(keyword))
# except:
#     pass # do nothing

# try:
#     print(int(keyword))

# except Exception as e:
#     print(str(e))
#     pass # do nothing


# try:
#     print(int(keyword))

# except ValueError:
#     print("Got a value error")
#     pass # do nothing

# except:
#     print("other type of exception")

# finally:
#     print("finally")

try:
    print(int(keyword))

# except ValueError:
#     print("Got a value error")
#     pass # do nothing

except Exception as e:
    print("other type of exception")
    print(str(e))

finally:
    print("finally")

print("Past exception")
