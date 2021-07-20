def bubble_sort(list1):  

    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  


a = [1, 8, 3, 4, 5, 6]

print(bubble_sort(a))