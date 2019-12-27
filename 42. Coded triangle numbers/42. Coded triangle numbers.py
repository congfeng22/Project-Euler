f=open("p042_words.txt","r")
message=f.read()
wordlist = message.split(",")

triangles = [int(i*(i+1)/2) for i in range(1,40)]
code = [0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
counter=0
for i in wordlist:
    word = i[1:-1].lower()
    wordcode=0
    for letter in word:
        wordcode+=code.index(letter)
    if wordcode in triangles:
        counter+=1
print(counter)
