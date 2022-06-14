from csv import reader

def importCSV(path):
    tMap = []
    with open(path) as levelMap:
        # reads the , in comma seperated file (csv)
        layout = reader(levelMap, delimiter= ',')
        for row in layout:
            tMap.append(list(row))
        return tMap
            