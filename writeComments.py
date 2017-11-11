import csv

GraderName = "foo"
GraderEmail = "bla@bu.edu"

with open('test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='|')
    columnProperties = next(reader)
    columnProperties[0] = 'username'
    latex = 0
    total = 0
    #get total index and latex index:
    for i in range(len(columnProperties)):
        if columnProperties[i] == 'latex':
            latex = i
        if columnProperties[i] == 'total':
            total = i
    perfect = next(reader)
    text = "------------\n"
    #where the magic happens
    for row in reader:
        arr = row
        length = len(arr)
        comment = ''
        totaldeduc = 0
        for i in range(1,total):
            #there's a comment
            if(len(arr[i]) > 3):
                st = arr[i].split(' ')
                #find how much I substracted
                sub = float(st[0]) - int(perfect[i])
                totaldeduc += sub
                fro = 2
                if st[2] == '-':
                    fro = 3
                comment += columnProperties[i]+") " + ' '.join(st[fro:]) + ' (' + str(sub) + 'pts)' + "\n"
        finalGrade = float(arr[total])
        okay = ''
        if int(arr[latex]):
            finalGrade += 8
            okay = "Used LaTeX +8pts \n"
        comment = arr[0] + ': ' + str(finalGrade) + '\n' + comment + okay + '\n' + GraderName + '\n' + GraderEmail
        if (float(arr[total]) == (float(perfect[total]) + totaldeduc)):
            text += comment
        else:
            text += "STOP SOMETHING WENT WRONG\ncheck: " + arr[0] + "\ngrade:{}, deduction:{}".format(arr[total],totaldeduc)
        text += "\n------------\n"
    f = open('comments.txt', 'w')
    f.write(text)
    f.close()



