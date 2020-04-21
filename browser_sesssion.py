session = ['google', 'youtoube', 'netsave', 'downloader']
f_session = []
n_session = []
# enter back to go previous version and enter to go to the next version

print("kindly type 'a' to go back to previous session or 'b'to go to next session")
click = input('>')
if click == 'a':
    a = session.pop()
    b = f_session.append(a)
    print(f_session)

elif click == 'b':
    c = session[1]
    n_session.append(c)
    print(n_session)
