import cv2



test_list = [[3], [[['f']]], [8]]

def replace_entry(tl: list, pos_new: int, new_entry):
    ctr = 0
    for entry in tl:
        if isinstance(entry, list):
            replace_entry(entry, pos_new, new_entry)
        else:
            print(type(entry[0]))


            if ctr == pos_new:
                entry = new_entry
                print(tl)
                
            else:
                ctr += 1
    return tl

replace_entry(test_list, 2, 10)