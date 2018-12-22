import os
import matplotlib.pyplot as plt

Source = os.getcwd()
Subfolder = os.listdir(Source)

record = []
number = []
Generator = []
Discriminator = []
Classifier = []
k=0
idPosition = 0

for i in range(0, len(Subfolder)):
    if (Subfolder[i] == 'log2.txt'):
        filea = open(Subfolder[i], "r+")
        fileaString = filea.read()
        idFilter = 'GL: '

# Generator
        while(fileaString.find(idFilter, idPosition) != -1):
            idPosition = fileaString.find(idFilter, idPosition)
            idPosition += 4
            
            while(fileaString[idPosition] != ':' and fileaString[idPosition] != ','):
                record.append(fileaString[idPosition])
                idPosition += 1
                k += 1

            k = 0
            number.append("".join(record))
            record.clear()

        for k in range(0, len(number)):
            Generator.append(float(number[k]))

# Discriminator
        number.clear()
        idFilter = 'DL: '
        k=0
        idPosition = 0

        while(fileaString.find(idFilter, idPosition) != -1):
            idPosition = fileaString.find(idFilter, idPosition)
            idPosition += 4
            
            while(fileaString[idPosition] != ':' and fileaString[idPosition] != ','):
                record.append(fileaString[idPosition])
                idPosition += 1
                k += 1

            k = 0
            number.append("".join(record))
            record.clear()

        for k in range(0, len(number)):
            Discriminator.append(float(number[k]))

# Classifier
        number.clear()
        idFilter = 'CL: '
        k=0
        idPosition = 0

        while(fileaString.find(idFilter, idPosition) != -1):
            idPosition = fileaString.find(idFilter, idPosition)
            idPosition += 4
            
            while(fileaString[idPosition] != ':' and fileaString[idPosition] != ','):
                record.append(fileaString[idPosition])
                idPosition += 1
                k += 1

            k = 0
            number.append("".join(record))
            record.clear()

        for k in range(0, len(number)):
            Classifier.append(float(number[k]))

#for k in range(0, len(Classifier)): 
#print(len(Discriminator), len(Classifier), len(Generator))

plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.plot(Discriminator,"-",color = "R",label = "Discriminator")
plt.plot(Classifier,"-",color = "G",label = "Generator")
plt.plot(Generator,"-",color = "B",label = "Classifier")

plt.xlim(1,120000)
plt.legend(loc = "upper right")
plt.show()
