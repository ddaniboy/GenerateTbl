class GenerateTable():
    def __init__(self, table, parametros):
        self.nameTable = table
        self.tables = {}
        self.info = {}

        self.tables[table] = []
        self.info[table] = []
        
        for par in parametros:
            self.tables[table].append(par)
        
    
    def add(self, *parametros):
        table = self.nameTable
        parametros = list(parametros)

        count = 0

        val = {}

        for item in self.tables[table]:
            try:
                val[item] = parametros[count]
                count += 1
            except:
                val[item] = ""
                count += 1
                

        self.info[table].append(val)


    def merge(self):
        table = self.nameTable

        result = ""

        stringd = ""
        count = 0

        values = self.info[table]

        tablesLen = {}

        for tab in self.tables[table]:
            tablesLen[tab] = len(tab)

        for tab in values:
            for item in tab:
                itemv = item

                item = tab[item]


                if len(str(item)) > tablesLen[itemv]:
                    tablesLen[itemv] = len(item)

    
                
        

        for item in self.tables[table]:


            tlen = len(self.tables[table])-1

            tblen = len(item)

            tblen = tablesLen[item] - tblen

            

            spaceLen = " "*tblen

            if tlen != count:
                stringd += "| " + item +spaceLen+ " "
            else:
                stringd += "| " + item +spaceLen+ " |"

            count += 1

        result += "_"*len(stringd)+"\n"
        result += stringd+"\n"
        result += "-"*len(stringd)+"\n"






        for valores in values:

            count = 0
            countFinal = len(valores)-1

            for item in valores:

                tlen = len(str(valores[item]))
                lenCount = tablesLen[item] - tlen
                spacelen = " "*lenCount

                if count != countFinal:
                    result += "| " + str(valores[item]) + spacelen + " "
                else:
                    result += "| " + str(valores[item]) + spacelen + " |\n"

                count += 1

        result += "-"*len(stringd)+"\n"

        return result
