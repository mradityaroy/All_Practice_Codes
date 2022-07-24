given_string="asvdaaavsxsvxsxgcagvsvxavvaavcvaaavvscsvavsacvcavsbcvcvcvsxhahaxbhaaahsbbsvchsahachsaaahhaacvcchchabajvavvhvjcgftcdyusfvavvvavvaayvyvvacvsvdaahfghffgygefyvyueaadgfuegfeuuccwgewg"
search_string="aa"
L=[]
start_index=0
while search_string in given_string[start_index :]:
    i = given_string.index(search_string, start_index)
    L.append (i)
    start_index = i + 1
print (L)


print ("How many times occur :",len(L))
