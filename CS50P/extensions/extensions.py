try:
    a = input('File: ').strip().lower().split('.').[-1]
except:
    print('application/octet-stream')

if a == 'gif':
    print('image/gif')
elif a == 'jpg' or a == 'jpeg':
    print('image/jpeg')
elif a == 'pdf':
    print('application/pdf')
elif a == 'png':
    print('image/png')
elif a == 'txt':
    print('text/plain')
elif a == 'zip':
    print('application/zip')
else:
    print('application/octet-stream')