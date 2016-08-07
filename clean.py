def clear_file(file_path):
    with open(file_path, 'w+') as sf:
        sf.write("")
        sf.close()
clear_file("shared/cache1/seek_cache.txt")
clear_file("shared/cache2/seek_cache.txt")
clear_file("shared/log1/access.log")
clear_file("shared/log1/error.log")
clear_file("shared/log2/access.log")
clear_file("shared/log2/error.log")
