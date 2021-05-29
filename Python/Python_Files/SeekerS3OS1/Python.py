#The Seeker S3 OS Python interactive shell!
#Made by: xxxxxx Saggi
#Version 0.0.1
#Made for Seeker S3 OS1
version = "0.0.1"
def python():
    import sys
    print("""
    Python 3 for Seeker S3 OS1
    """)
    while True:
        code = input(">>>")
        if code == "quit()":
            break
        else:
            try:
                exec(code)
            except:
                print("Unexpected error:", sys.exc_info())