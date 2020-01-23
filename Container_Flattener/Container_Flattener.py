def container_flattener(input_list,output_list=list()):
    for item  in input_list:
        if isinstance(item,list):
            container_flattener(item,output_list)
        elif isinstance(item,tuple):
            container_flattener(item,output_list)
        elif isinstance(item,set):
            container_flattener(item,output_list)
        elif isinstance(item,range):
            container_flattener(item,output_list)
        else:
            output_list.append(item)
    return output_list

l = [1,2,[3,4,(5,6)],7,8,set([9,10]),[11],range(12)]
print(container_flattener(l))