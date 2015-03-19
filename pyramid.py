def pyramid(n):
    import string;
    alphabet = (string.ascii_lowercase)*2
    a = 0;
    b = 2;
    storage = "";
    for i in range(0,n):
        for p in range(0,i+1):
            storage+=alphabet[a]
            a+=1
        for j in range(0,i):
            storage+=alphabet[a-b];
            b+=1;
        b = 2;
        print (storage.center(2*n-1,"-"))
        storage = "";
