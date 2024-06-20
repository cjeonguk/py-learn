import time

print(time.ctime(time.time()))

time_obj = time.localtime()
# time_obj = time.gmtime()

print(time_obj)
print(time.strftime('%Y-%m-%d %H:%M:%S', time_obj))

time_1 = "January 1, 1970"

print(time.strptime(time_1, '%B %d, %Y'))

print(time.asctime(time_tuple := (2020, 1, 1, 0, 0, 0, 0, 0, 0)))
print(time.mktime(time_tuple))