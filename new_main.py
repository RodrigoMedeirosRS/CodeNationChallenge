#Code made by R.M.Lehnemann into 24/03/2018, published into 25/03/2018

class myResult:
    first = True
    nationalities = []
    clubs = []
    names = []
    richPay = {}
    agePeople = {}
    howMuchAge = {}

    myResponse1 = 0
    myResponse2 = 0
    myResponse4 = []
    myResponse5 = []
   
    def data_read(self, line):
        result = []
        infoCounter = 0;
        output = ""
        for i in range(0, len(line)):
            if line[i] == ",":
                infoCounter += 1
                if infoCounter  ==  3:
                    result.append(output)
                elif infoCounter  ==  4:
                    result.append(output)
                elif infoCounter  ==  7:
                    result.append(float(output))
                elif infoCounter  ==  15:
                    result.append(output)
                elif infoCounter  ==  18:
                    result.append(float(output))
                    return result
                output = ""
            else:
                output += line[i]


    def __init__(self):
        with open('./python-1/data.csv') as the_file:
            for line in the_file:
                if self.first == False:
                    current_data = self.data_read(line)
                    self.rq_1(current_data[3], self.nationalities, False)
                    self.rq_2(current_data[1], self.clubs, False)
                    self.rq_3(current_data[0], self.names, False)
                    self.rq_4(current_data[0], current_data[4], self.richPay, False)
                    self.rq_5(current_data[0], current_data[2], self.agePeople, False)
                    self.rq_6(current_data[2], self.howMuchAge, False)
                else:
                    self.first = False
        self.myResponse1 = self.rq_1(current_data[3], self.nationalities, True)
        self.myResponse2 = self.rq_2(current_data[1], self.clubs, True)
        self.myResponse4 = self.rq_4(current_data[0], current_data[4], self.richPay, True)
        self.myResponse5 = self.rq_5(current_data[0], current_data[2],  self.agePeople, True)

        the_file.close()
    
    def rq_1(self, current_nationality, nationalities, last):
        if last  == False:
            for i in range(0, nationalities.__len__()):
                if nationalities[i] == current_nationality:
                    return False
            nationalities.append(current_nationality)
        else:
            return nationalities.__len__()
    
    def rq_2(self,current_club, clubs, last):
        if last  == False:
            for i in range(0, clubs.__len__()):
                if clubs[i] == current_club:
                    return False
            clubs.append(current_club)
        else:
            return clubs.__len__()

    def rq_3(self, current_names, names, last):
        if last == False:
            if names.__len__() < 20:
                names.append(current_names)
    
    def rq_4(self, current_names, current_pays, richPay, last):
        if last == False:
            if current_pays in richPay.keys():
                current_pays -= 0.1
            richPay[current_pays] = current_names
        
        else:
            sortedDict = {k: richPay[k] for k in sorted(richPay)}
            orderedList = list(sortedDict.values())
            result = []
            for i in range(1, 11):
                result.append(orderedList[i*-1])
            return result
    
    def rq_5(self, current_names, current_ages, agePeople, last):
        if last == False:
            currentAge = current_ages
            while currentAge in agePeople.keys():
                currentAge -= 0.001
            currentName = current_names
            agePeople[currentAge] = currentName
        
        else:
            sortedDict = {k: agePeople[k] for k in sorted(agePeople)}
            orderedList = list(sortedDict.values())
            result = []
            for i in range(1, 11):
                result.append(orderedList[i*-1])
            
            return result

    def rq_6(self, current_ages, howMuchAge, last):
        if last == False:
            currentAge = int(current_ages)
            if howMuchAge.__len__() > 1:
                if currentAge in howMuchAge.keys():
                    howMuchAge[currentAge] += 1
                else:
                    howMuchAge[currentAge] = 1
            else:
                howMuchAge[currentAge] = 1

# coding: utf-8
# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

myProgram = myResult()

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
myProgram.myResponse1

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
myProgram.myResponse2

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
myProgram.names

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
myProgram.myResponse4

# **Q5.** Quem são os 10 jogadores mais velhos?
myProgram.myResponse5

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
myProgram.howMuchAge
