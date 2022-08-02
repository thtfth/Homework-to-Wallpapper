import homework_to_wallpaper

tick_homework_txt = homework_to_wallpaper.file_loc_folder + '\\homeworks.txt'

f = open(tick_homework_txt, 'r+')

file = f.read()

subject = input("What subject did you complete?: ")

search_key = subject + ':'

content = file.split('\n')

#if search_key.upper() in content:
#    content[subject] = subject + '    #COMPLETE'
#    print(content)

indices = [i for i, s in enumerate(content) if search_key.upper() in s]

index_num = ''.join(str(e) for e in indices)

content[int(index_num)] = subject + '    #COMPLETE'

print(index_num)

print(content)

print(file)





