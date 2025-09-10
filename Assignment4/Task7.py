try:
    file1 = open('sample.txt','r')
    read_file1 = file1.readline()
    read_file2 = file1.readline()
    print("Reading file content:\nLine 1:", read_file1+"Line 2:", read_file2)
    file1.close()
    

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")

    