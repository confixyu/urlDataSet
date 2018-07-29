# This algorithm will help you to extract dataset from a  url and save to local as JSON, XLS, and CSV

def datasetFromUrl(url, filename="dataset", deslimitador = ",", separador = "\n",  encoding = "utf-8", protocol="GET",
                   mainpath="/home/confix/Desktop"):
    import urllib3
    import pandas as pd
    import os
    # url = 'http://winterolympicsmedals.com/medals.csv'

    http = urllib3.PoolManager()
    r = http.request(protocol, url)
    print ("Status: %d" %(r.status))
    response = r.data

    # The object response contains a binary string , then we enconding to UTF-8
    str_data = response.decode(encoding)

    # Split the string to array row, separate by a jump line
    lines = str_data.split(deslimitador)

    # The first line have the header, the we  extract it.
    col_names = lines[0].split(separador)
    n_cols = len(col_names)

    # Generate a empty dictionary where save proccessed information from the external URL
    counter = 0
    main_dict = {}
    for col in col_names:
        main_dict[col] = []

    # proccess row to row the informatio for filling the dictionary
    # with data like we made before
    for line in lines:
        #Jump the first line that is the header container was proccessed
        if(counter > 0):
            # Split each string by comma(,) as separator elment
            values = line.strip().split(separador)
            # Add values to their respective dictionary column
            for i in range(len(col_names)):
                main_dict[col_names[i]].append(values[i])
        counter += 1


    print("El data set tiene %d filas y %d columnas" %(counter, n_cols))

    # Convert the proccessed dictionary to data Frame and
    # check all data is correct.
    df = pd.DataFrame(main_dict)
    df.head()

    # FullPath where will save the dataSet
    fullpath = os.path.join(mainpath, filename)

    # Will save the dataset to CSV, JSON and xls
    df.to_csv(fullpath+".csv")
    df.to_json(fullpath+".json")
    df.to_excel(fullpath+".xls")
    
    print("The files is saved at " + fullpath)

    return