
inputFilename = r"C:\Users\Matz\Downloads\Small_Cubicuboctahedron_V1_L1.123caf69009d-5438-4d39-b990-e0265e2bfb8f\Small_Cubicuboctahedron_V1_L1.123caf69009d-5438-4d39-b990-e0265e2bfb8f\20775_Small_Cubicuboctahedron_V1.obj"
outputFilename = r"c:\temp\output.obj"

f = open(inputFilename, "r")
#print(f.read()) 

data = f.readlines()
dataCopy=[]

for line in data:
    #words = line.split()
    if line.startswith('vn'):
        elements = line.split(' ')[1:]
        x = - + float(elements[0])
        y = - + float(elements[1])
        z = - + float(elements[2])
        line = "vn {} {} {}\n".format(x,y,z)
    if line.startswith('f'):

        #f 1/1/1 2/2/1 3/3/1 4/4/1 



    dataCopy.append(line)

f.close()
print 'writing to output {}'.format(outputFilename)
f = open(outputFilename, "w")

for line in dataCopy:
    f.write(line)
f.close()
    
print 'finished'
