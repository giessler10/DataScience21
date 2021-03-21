class ListKeeper:
    #Init-Methode
    def __init__(self):
        self.dicListKeeper = {}
        self.dicListKeeper['Example'] = [1,2,3,4,5]
    #Show-Methode - Key-Werte als Return
    def show(self):
        #View durch Methode keys() erzeugen
        keys = self.dicListKeeper.keys()
        #Temporäre Liste
        tempListKeys = []
        for i in keys:
            tempListKeys.append(i)
        return tempListKeys
    #Add-Methode - Key-Value-Paar als Zip-Objekt
    def add(self,name,list):
        self.dicListKeeper[name] = list
    #Delete-Methode - Gelöschte Liste als Return
    def delete(self,name):
        return self.dicListKeeper.pop(name)
    #Sort-Methode - Sortiere Liste wird zurück gegeben
    def sort(self,name):
        tempList = self.dicListKeeper[name]
        tempList.sort()
        return tempList
    #Append-Methode - Die Liste hinter "name" wird um die Werte in "list" erweitert
    def append(self,name,list):
        for i in list:
            self.dicListKeeper[name].append(i)