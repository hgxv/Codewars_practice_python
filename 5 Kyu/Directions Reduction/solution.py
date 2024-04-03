opposites = {
    "NORTH": "SOUTH",
    "SOUTH": "NORTH",
    "EAST": "WEST",
    "WEST": "EAST",
}

def dir_reduc(arr):
    index = 0

    while True:

        try:
            if arr[index + 1] == opposites[arr[index]]:
                del arr[index + 1]
                del arr[index]
                index = 0
                continue
                
        except IndexError:
            return arr
            
        index += 1
