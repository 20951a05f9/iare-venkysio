`import threading
import time
#10000 chars dummy text
s =open("text.txt","r")
s=s.read()

# s="ROHIT"
#recursive approach
def rev(s):
    n=len(s)
    if n<=1:
        return s
    return rev(s[n//2:])+rev(s[:n//2])

#iterative approach
def reverseIt(s):
    n=len(s)
    res_list=[None]*n
    for i in range(n//2+1):
        res_list[i]=s[n-i-1]
        res_list[n-1-i]=s[i]
    return "".join(res_list)


start_time=time.time()*1000 # "*1000" to get time in milli secs
print(reverseIt(s))
end_time=time.time()*1000
print("diff of :",end_time-start_time,"milliseconds")

start_time=time.time()*1000
rev(s)
end_time=time.time()*1000
print("diff:",end_time-start_time,"milliseconds")


