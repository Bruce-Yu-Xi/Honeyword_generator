import itertools
import sys
import random
import numpy

top100 = [
    '123456',
    '12345',
    '123456789',
    'password',
    'iloveyou',
    'princess',
    '1234567',
    'rockyou',
    '12345678',
    'abc123',
    'nicole',
    'daniel',
    'babygirl',
    'monkey',
    'lovely',
    'jessica',
    '654321',
    'michael',
    'ashley',
    'qwerty',
    '111111',
    'iloveu',
    '000000',
    'michelle',
    'tigger',
    'sunshine',
    'chocolate',
    'password1',
    'soccer',
    'anthony',
    'friends',
    'butterfly',
    'purple',
    'angel',
    'jordan',
    'liverpool',
    'justin',
    'loveme',
    'fuckyou',
    '123123',
    'football',
    'secret',
    'andrea',
    'carlos',
    'jennifer',
    'joshua',
    'bubbles',
    '1234567890',
    'superman',
    'hannah',
    'amanda',
    'loveyou',
    'pretty',
    'basketball',
    'andrew',
    'angels',
    'tweety',
    'flower',
    'playboy',
    'hello',
    'elizabeth',
    'hottie',
    'tinkerbell',
    'charlie',
    'samantha',
    'barbie',
    'chelsea',
    'lovers',
    'teamo',
    'jasmine',
    'brandon',
    '666666',
    'shadow',
    'melissa',
    'eminem',
    'matthew',
    'robert',
    'danielle',
    'forever',
    'family',
    'jonathan',
    '987654321',
    'computer',
    'whatever',
    'dragon',
    'vanessa',
    'cookie',
    'naruto',
    'summer',
    'sweety',
    'spongebob',
    'joseph',
    'junior',
    'softball',
    'taylor',
    'yellow',
    'daniela',
    'lauren',
    'mickey',
    'princesa']

def makeHw(cnt, inputfile, outputfile):
  
  
  with open(inputfile) as infile:
    for line in infile:
        isLetter = any(single.isalpha() for single in line)
        line = line.replace("\n", "")
        
        if(isLetter == True):
          uplowData = map(''.join, itertools.product(*((single.upper(), single.lower()) for single in line)))
          pick = random.sample(top100, 3)
          isLetter1 = any(single.isalpha() for single in pick[0])
          isLetter2 = any(single.isalpha() for single in pick[1])
          isLetter3 = any(single.isalpha() for single in pick[2])
          if isLetter1 == True:
           pick1 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[0])))), 999)
           pick1 = random.sample(pick1, cnt)
          if isLetter2 == True:
           pick2 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[1])))), 999)
           pick2 = random.sample(pick2, cnt)
          if isLetter3 == True:
           pick3 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[2])))), 999)
           pick3 = random.sample(pick3, cnt)
          repeatData = numpy.repeat(uplowData, 999)
          honeyData = random.sample(repeatData, cnt)
          honeyPass = []
          for i in range(0, cnt):
            honeyPass.append(str(random.randint(0, 99)) + honeyData[i] + str(random.randint(0, 99)))
            honeyPass.append(pick1[i] + str(random.randint(0, 99)))
            honeyPass.append(str(random.randint(0, 99)) + pick2[i] + str(random.randint(0, 99)))
            honeyPass.append(pick3[i] + str(random.randint(0, 99)))
  
          result = random.sample(honeyPass, cnt)
          print result
          outfile = open(outputfile, "a")
          for line in result:
            outfile.write(line + "|")
          outfile.write("\n")
        
        else:
          pick = random.sample(top100, 3)
          isLetter1 = any(single.isalpha() for single in pick[0])
          isLetter2 = any(single.isalpha() for single in pick[1])
          isLetter3 = any(single.isalpha() for single in pick[2])
          if isLetter1 == True:
           pick1 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[0])))), 999)
           pick1 = random.sample(pick1, cnt)
          if isLetter2 == True:
           pick2 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[1])))), 999)
           pick2 = random.sample(pick2, cnt)
          if isLetter3 == True:
           pick3 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[2])))), 999)
           pick3 = random.sample(pick3, cnt)
          repeatData = numpy.repeat(uplowData, 999)
          honeyData = random.sample(repeatData, cnt)
          for i in range(0, cnt):
            honeyPass.append(str(random.randint(0, 99)) + honeyData[i] + str(random.randint(0, 99)))
            honeyPass.append(pick1[i] + str(random.randint(0, 99)))
            honeyPass.append(str(random.randint(0, 99)) + pick2[i] + str(random.randint(0, 99)))
            honeyPass.append(pick3[i] + str(random.randint(0, 99)))
  
          result = random.sample(honeyPass, cnt)
          print result
          outfile = open(outputfile, "a")
          for line in result:
            outfile.write(line + "|")
          outfile.write("\n")
          
        outfile.close()
        honeyPass[:] = []

if __name__ == '__main__':
  N = int(sys.argv[1])
  inputfile = sys.argv[2]
  outputfile = sys.argv[3]
  makeHw(N, inputfile, outputfile)
