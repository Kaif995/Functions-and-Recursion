def list_print(list, index=0):
    if(index == len(list)):
        return
    print(list[index])
    list_print(list, index+1)
    
Movies=["World war Z","Playlist", "The Social Network", "Source Code"]
print(list_print(Movies)) 