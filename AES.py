from audioop import mul
from os import stat
from pydoc import plain
import time


def convertHexToDec(hex):
    if hex == "A":
        return 10
    elif hex == "B":
        return 11
    elif hex == "C":
        return 12
    elif hex == "D":
        return 13
    elif hex == "E":
        return 14
    elif hex == "F":
        return 15
    else:
        return int(hex)

def convertDecToHex(dec):
    if dec == 10:
        return "A"
    elif dec == 11:
        return "B"
    elif dec == 12:
        return "C"
    elif dec == 13:
        return "D"
    elif dec == 14:
        return "E"
    elif dec == 15:
        return "F"
    else:
        return str(dec)

def sBox(key): #substitute bytes
    
    sBox = [
    [["63"], ["7C"], ["77"], ["7B"], ["F2"], ["6B"], ["6F"], ["C5"], ["30"], ["01"], ["67"], ["2B"], ["FE"], ["D7"], ["AB"], ["76"]],
    [["CA"], ["82"], ["C9"], ["7D"], ["FA"], ["59"], ["47"], ["F0"], ["AD"], ["D4"], ["A2"], ["AF"], ["9C"], ["A4"], ["72"], ["C0"]],
    [["B7"], ["FD"], ["93"], ["26"], ["36"], ["3F"], ["F7"], ["CC"], ["34"], ["A5"], ["E5"], ["F1"], ["71"], ["D8"], ["31"], ["15"]],
    [["04"], ["C7"], ["23"], ["C3"], ["18"], ["96"], ["05"], ["9A"], ["07"], ["12"], ["80"], ["E2"], ["EB"], ["27"], ["B2"], ["75"]],
    [["09"], ["83"], ["2C"], ["1A"], ["1B"], ["6E"], ["5A"], ["A0"], ["52"], ["3B"], ["D6"], ["B3"], ["29"], ["E3"], ["2F"], ["84"]],
    [["53"], ["D1"], ["00"], ["ED"], ["20"], ["FC"], ["B1"], ["5B"], ["6A"], ["CB"], ["BE"], ["39"], ["4A"], ["4C"], ["58"], ["CF"]],
    [["D0"], ["EF"], ["AA"], ["FB"], ["43"], ["4D"], ["33"], ["85"], ["45"], ["F9"], ["02"], ["7F"], ["50"], ["3C"], ["9F"], ["A8"]],
    [["51"], ["A3"], ["40"], ["8F"], ["92"], ["9D"], ["38"], ["F5"], ["BC"], ["B6"], ["DA"], ["21"], ["10"], ["FF"], ["F3"], ["D2"]],
    [["CD"], ["0C"], ["13"], ["EC"], ["5F"], ["97"], ["44"], ["17"], ["C4"], ["A7"], ["7E"], ["3D"], ["64"], ["5D"], ["19"], ["73"]],
    [["60"], ["81"], ["4F"], ["DC"], ["22"], ["2A"], ["90"], ["88"], ["46"], ["EE"], ["B8"], ["14"], ["DE"], ["5E"], ["0B"], ["DB"]],
    [["E0"], ["32"], ["3A"], ["0A"], ["49"], ["06"], ["24"], ["5C"], ["C2"], ["D3"], ["AC"], ["62"], ["91"], ["95"], ["E4"], ["79"]],
    [["E7"], ["C8"], ["37"], ["6D"], ["8D"], ["D5"], ["4E"], ["A9"], ["6C"], ["56"], ["F4"], ["EA"], ["65"], ["7A"], ["AE"], ["08"]],
    [["BA"], ["78"], ["25"], ["2E"], ["1C"], ["A6"], ["B4"], ["C6"], ["E8"], ["DD"], ["74"], ["1F"], ["4B"], ["BD"], ["8B"], ["8A"]],
    [["70"], ["3E"], ["B5"], ["66"], ["48"], ["03"], ["F6"], ["0E"], ["61"], ["35"], ["57"], ["B9"], ["86"], ["C1"], ["1D"], ["9E"]],
    [["E1"], ["F8"], ["98"], ["11"], ["69"], ["D9"], ["8E"], ["94"], ["9B"], ["1E"], ["87"], ["E9"], ["CE"], ["55"], ["28"], ["DF"]],
    [["8C"], ["A1"], ["89"], ["0D"], ["BF"], ["E6"], ["42"], ["68"], ["41"], ["99"], ["2D"], ["0F"], ["B0"], ["54"], ["BB"], ["16"]]
    ]

    ans=[]

    for i in range(len(key)): #for each byte
        temp=[]
        k=str(key[i][0])
        row = convertHexToDec(k[0])
        col = convertHexToDec(k[1])
        temp.append(sBox[row][col])
        ans.append(sBox[row][col])
    return ans

def invsBox(key): #substitute bytes
    
    sBox = [
    [["52"], ["09"], ["6A"], ["D5"], ["30"], ["36"], ["A5"], ["38"], ["BF"], ["40"], ["A3"], ["9E"], ["81"], ["F3"], ["D7"], ["FB"]],
    [["7C"], ["E3"], ["39"], ["82"], ["9B"], ["2F"], ["FF"], ["87"], ["34"], ["8E"], ["43"], ["44"], ["C4"], ["DE"], ["E9"], ["CB"]],
    [["54"], ["7B"], ["94"], ["32"], ["A6"], ["C2"], ["23"], ["3D"], ["EE"], ["4C"], ["95"], ["0B"], ["42"], ["FA"], ["C3"], ["4E"]],
    [["08"], ["2E"], ["A1"], ["66"], ["28"], ["D9"], ["24"], ["B2"], ["76"], ["5B"], ["A2"], ["49"], ["6D"], ["8B"], ["D1"], ["25"]],
    [["72"], ["F8"], ["F6"], ["64"], ["86"], ["68"], ["98"], ["16"], ["D4"], ["A4"], ["5C"], ["CC"], ["5D"], ["65"], ["B6"], ["92"]],
    [["6C"], ["70"], ["48"], ["50"], ["FD"], ["ED"], ["B9"], ["DA"], ["5E"], ["15"], ["46"], ["57"], ["A7"], ["8D"], ["9D"], ["84"]],
    [["90"], ["D8"], ["AB"], ["00"], ["8C"], ["BC"], ["D3"], ["0A"], ["F7"], ["E4"], ["58"], ["05"], ["B8"], ["B3"], ["45"], ["06"]],
    [["D0"], ["2C"], ["1E"], ["8F"], ["CA"], ["3F"], ["0F"], ["02"], ["C1"], ["AF"], ["BD"], ["03"], ["01"], ["13"], ["8A"], ["6B"]],
    [["3A"], ["91"], ["11"], ["41"], ["4F"], ["67"], ["DC"], ["EA"], ["97"], ["F2"], ["CF"], ["CE"], ["F0"], ["B4"], ["E6"], ["73"]],
    [["96"], ["AC"], ["74"], ["22"], ["E7"], ["AD"], ["35"], ["85"], ["E2"], ["F9"], ["37"], ["E8"], ["1C"], ["75"], ["DF"], ["6E"]],
    [["47"], ["F1"], ["1A"], ["71"], ["1D"], ["29"], ["C5"], ["89"], ["6F"], ["B7"], ["62"], ["0E"], ["AA"], ["18"], ["BE"], ["1B"]],
    [["FC"], ["56"], ["3E"], ["4B"], ["C6"], ["D2"], ["79"], ["20"], ["9A"], ["DB"], ["C0"], ["FE"], ["78"], ["CD"], ["5A"], ["F4"]],
    [["1F"], ["DD"], ["A8"], ["33"], ["88"], ["07"], ["C7"], ["31"], ["B1"], ["12"], ["10"], ["59"], ["27"], ["80"], ["EC"], ["5F"]],
    [["60"], ["51"], ["7F"], ["A9"], ["19"], ["B5"], ["4A"], ["0D"], ["2D"], ["E5"], ["7A"], ["9F"], ["93"], ["C9"], ["9C"], ["EF"]],
    [["A0"], ["E0"], ["3B"], ["4D"], ["AE"], ["2A"], ["F5"], ["B0"], ["C8"], ["EB"], ["BB"], ["3C"], ["83"], ["53"], ["99"], ["61"]],
    [["17"], ["2B"], ["04"], ["7E"], ["BA"], ["77"], ["D6"], ["26"], ["E1"], ["69"], ["14"], ["63"], ["55"], ["21"], ["0C"], ["7D"]]
    ]

    ans=[]

    for i in range(len(key)): #for each byte
        temp=[]
        k=str(key[i][0])
        row = convertHexToDec(k[0])
        col = convertHexToDec(k[1])
        temp.append(sBox[row][col])
        ans.append(sBox[row][col])
    return ans


def XOR(a,hex): #XOR with a hex value
  
    p1=hex[0] #first hex value
    p2=hex[1] #second hex value

    
    p1=bin(int(p1,16))[2:] #convert to binary
    p2=bin(int(p2,16))[2:]  #convert to binary

    
    if len(p1)<4:
        p1="0"*(4-len(p1))+p1
    if len(p2)<4:
        p2="0"*(4-len(p2))+p2

    
    binaryOfHex=p1+p2 #binary of hex value

    p1=a[0]
    p2=a[1]

    
    p1=bin(int(p1,16))[2:] #convert to binary
    p2=bin(int(p2,16))[2:] #convert to binary

    if len(p1)<4:
        p1="0"*(4-len(p1))+p1
    if len(p2)<4:
        p2="0"*(4-len(p2))+p2

    binaryOfA=p1+p2
    

    
    if len(binaryOfA)<8: #if binary of a is less than 8 bits
        binaryOfA="0"*(8-len(binaryOfA))+binaryOfA

    
    ans=""
    for i in range(len(binaryOfA)): #XOR
        if binaryOfA[i]==binaryOfHex[i]:
            ans+="0"
        else:
            ans+="1"

    

    p1=ans[0:4] #first 4 bits
    p2=ans[4:8] #last 4 bits

    p1=int(p1,2) #convert to decimal
    p2=int(p2,2) #convert to decimal

    p1=convertDecToHex(p1) #convert to hex
    p2=convertDecToHex(p2) #convert to hex

    ans=p1+p2 #final answer
    return ans
    


def generateRoundKeys(key): #generate round keys
    currRound=0
    roundConstant=[["01"], ["02"], ["04"], ["08"], ["10"], ["20"], ["40"], ["80"], ["1B"], ["36"]] #round constants
    roundKeys = [] #round keys
    roundKeys.append(key) #first round key is the key itself
    
    while currRound<10: #for 10 rounds
        words=[]
        
        last4vals = key[len(key)-4:len(key)].copy() #last 4 values of key
        
        last4vals = last4vals[1:] + last4vals[:1] #circular shift left
        last4vals=sBox(last4vals) #sbox
        
        temp=last4vals.copy() #copy of last 4 values
        
        ans1=XOR(roundConstant[currRound][0],last4vals[0][0]) #XOR with round constant
         
        last4vals.clear() #clear last 4 values
        last4vals=[] #clear last 4 values
        for i in range(4): #append to last 4 values
            if i>0:
                last4vals.append(temp[i])
            else:
                t=[]
                t.append(ans1)
                last4vals.append(t)
        
        
        for i in range(0,len(key),4): #for each word
            w=key[i:i+4]
            for i in range(len(last4vals)):
                ans=[]
                ans.append(XOR(w[i][0],last4vals[i][0]))
                last4vals[i]=ans
                words.append(ans)
        key=words.copy()
        currRound+=1
        roundKeys.append(words) #append round key
    return roundKeys,currRound+1 #return round keys and number of rounds

def shiftRows(state): #shift rows
    
    temp=[] #temp array
    for i in range(0,len(state),4): #for each row
        temp.append(state[i:i+4]) #append to temp array
    state=temp

    
    state = list(map(list, zip(*state))) #transpose matrix
    
    for i in range(1,len(state)): #for each row
        state[i]=state[i][i:]+state[i][:i] #circular shift left

    
    state = list(map(list, zip(*state))) #transpose matrix
    
    ans=[] #final answer
    for i in range(len(state)): #for each row
        for j in range(len(state[i])): #for each column
            ans.append(state[i][j])  
    return ans

def inverseShiftRows(state): #inverse shift rows

    temp=[]
    for i in range(0,len(state),4): #for each row
        temp.append(state[i:i+4]) #append to temp array
    state=temp

    
    state = list(map(list, zip(*state))) #transpose matrix
    
    for i in range(1,len(state)): #for each row
        
        state[i]=state[i][len(state[i])-i:]+state[i][:len(state[i])-i] #circular shift right

    state = list(map(list, zip(*state))) #transpose matrix
    ans=[] 
    for i in range(len(state)): #for each row
        for j in range(len(state[i])): #for each column
            ans.append(state[i][j]) 
    return ans

def giveBinaryin8bit(state): #convert to binary
    p1=state[0]
    p2=state[1]

    p1=bin(int(p1,16))[2:]
    p2=bin(int(p2,16))[2:]

    if len(p1)<4:
        p1="0"*(4-len(p1))+p1
    if len(p2)<4:
        p2="0"*(4-len(p2))+p2
    ans=p1+p2

    return ans

def giveHexFromBinary(binary): #convert to hex
    p1=binary[0:4]
    p2=binary[4:8]

    
    p1=int(p1,2)
    p2=int(p2,2)

    p1=convertDecToHex(p1)
    p2=convertDecToHex(p2)

    ans=p1+p2
    return ans

def getLeftShit(binary): #get left shift
    if binary[0]=='0':
        binary=binary[1:]+"0"
    else:
        binary=binary[1:]+"0"
        binary=giveHexFromBinary(binary)
        binary=XOR("1B",binary)
        binary=giveBinaryin8bit(binary)
    
    return binary

def multiply(mixColumRow,stateColumn): #multiply
    ans=[]
    for i in range(len(mixColumRow)): #for each row

        if mixColumRow[i]=='02':
            binary=giveBinaryin8bit(stateColumn[i][0])
            if binary[0]=='0':
                binary=binary[1:]+"0"
            else:
                binary=binary[1:]+"0"
                binary=giveHexFromBinary(binary)
                binary=XOR("1B",binary)
                binary=giveBinaryin8bit(binary)
            ans.append(giveHexFromBinary(binary))
        elif mixColumRow[i]=='03':
            temp_binary=giveBinaryin8bit(stateColumn[i][0])
            binary=giveBinaryin8bit(stateColumn[i][0])
            if binary[0]=='0':
                binary=binary[1:]+"0"
                binary=giveHexFromBinary(binary)
            else:                
                binary=binary[1:]+"0"
                binary=giveHexFromBinary(binary)
                binary=XOR("1B",binary)
                binary=giveBinaryin8bit(binary)
                binary=giveHexFromBinary(binary)
            
        
            temp_binary=giveHexFromBinary(temp_binary)
            binary=XOR(binary,temp_binary)
            ans.append(binary)        
            

            
        elif mixColumRow[i]=='01':
            ans.append(stateColumn[i][0])

        elif mixColumRow[i]=='0E':
            
            temp=[]
            binary=giveBinaryin8bit(stateColumn[i][0])
            

            binary=getLeftShit(binary)         
            temp.append(giveHexFromBinary(binary))
            
            binary=getLeftShit(binary)  

            temp.append(giveHexFromBinary(binary))
            binary=getLeftShit(binary)
            temp.append(giveHexFromBinary(binary))
            
            for i in range(1,len(temp)):
                temp[0]=XOR(temp[0],temp[i])
            ans.append(temp[0])

        elif mixColumRow[i]=='0B':
            temp=[]
            
            binary=giveBinaryin8bit(stateColumn[i][0])
            temp.append(giveHexFromBinary(binary))

            binary=getLeftShit(binary)
            temp.append(giveHexFromBinary(binary))

            binary=getLeftShit(binary)
            binary=getLeftShit(binary)
            temp.append(giveHexFromBinary(binary))

            

            for i in range(1,len(temp)):
                temp[0]=XOR(temp[0],temp[i])
            ans.append(temp[0])

        elif mixColumRow[i]=='0D':
            temp=[]
            binary=giveBinaryin8bit(stateColumn[i][0])

            temp.append(giveHexFromBinary(binary))
            binary=getLeftShit(binary)
            binary=getLeftShit(binary)
            temp.append(giveHexFromBinary(binary))
            binary=getLeftShit(binary)
            temp.append(giveHexFromBinary(binary))
            for i in range(1,len(temp)):
                temp[0]=XOR(temp[0],temp[i])
            # print(temp[0])
            ans.append(temp[0])


        elif mixColumRow[i]=='09':   
            temp=[]
            binary=giveBinaryin8bit(stateColumn[i][0])
            temp.append(giveHexFromBinary(binary))
            binary=getLeftShit(binary)
            binary=getLeftShit(binary)
            binary=getLeftShit(binary)
            temp.append(giveHexFromBinary(binary))

            for i in range(1,len(temp)):
                temp[0]=XOR(temp[0],temp[i])
            ans.append(temp[0])       

        
    
    for i in range(1,len(ans)):
        ans[0]=XOR(ans[0],ans[i])
    return ans[0]


def mixColumns(state): #mix columns
    answer=[]
    mixColunmsMatrix=[
    ["02","03","01","01"],
    ["01","02","03","01"],
    ["01","01","02","03"],
    ["03","01","01","02"]
    ]

    temp=[]
    for i in range(0,len(state),4): #for each column
        temp.append(state[i:i+4])
    state=temp.copy()
    
    for i in range(len(mixColunmsMatrix)): #for each row
        for j in range(len(state)):
            ans=multiply(mixColunmsMatrix[i].copy(),state[j].copy())
            answer.append(ans)
            

    temp=[]
    for i in range(0,len(answer),4): #for each column
        temp.append(answer[i:i+4])

    temp = list(map(list, zip(*temp))) #transpose
    ans1=[]
    for i in range(len(temp)): #for each row
        for j in range(len(temp[i])):
            t=[]
            t.append(temp[i][j])
            ans1.append(t)

    
    return ans1


def invmixColumns(state): #inverse mix columns
    
    answer=[]
    mixColunmsMatrix=[
    ["0E","0B","0D","09"],
    ["09","0E","0B","0D"],
    ["0D","09","0E","0B"],
    ["0B","0D","09","0E"]
    ]
   
    

    temp=[]
    for i in range(0,len(state),4): #for each column
        temp.append(state[i:i+4])
    state=temp.copy()
    

    
        

    for i in range(len(mixColunmsMatrix)): #for each row
        for j in range(len(state)): 
            
            ans=multiply(mixColunmsMatrix[i].copy(),state[j].copy())
            answer.append(ans)
            
    
    temp=[] 
    for i in range(0,len(answer),4): #for each column
        temp.append(answer[i:i+4])

    
    temp = list(map(list, zip(*temp))) #transpose
    
    
    ans1=[]
    for i in range(len(temp)): #for each row
        for j in range(len(temp[i])):
            t=[]
            t.append(temp[i][j])
            ans1.append(t)
    
    
    return ans1

def workFromRound1(stateMatrix,roundKeys,lengthOfRoundKeys): #for round 1 to round 9
    currRound=1 #current round
    while 1:
        
        sBoxStateMatrix=sBox(stateMatrix) #sbox
                
        sBoxStateMatrix=shiftRows(sBoxStateMatrix) #shift rows
        
        if(currRound==10): #for round 10
            
            for i in range(len(sBoxStateMatrix)): #for each row
                sBoxStateMatrix[i][0]=XOR(sBoxStateMatrix[i][0],roundKeys[currRound][i][0])
            break   

        
        sBoxStateMatrix=mixColumns(sBoxStateMatrix) #mix columns
        
        for i in range(len(sBoxStateMatrix)): #for each row
            sBoxStateMatrix[i][0]=XOR(sBoxStateMatrix[i][0],roundKeys[currRound][i][0])
            
        
        stateMatrix=sBoxStateMatrix.copy() #copy to state matrix
        currRound+=1   

    return sBoxStateMatrix

def decrypt(cipherTextis,roundKeys): #decrypt
    for i in range(len(cipherTextis)): #for each row
        cipherTextis[i][0]=XOR(cipherTextis[i][0],roundKeys[10][i][0])
       

    cipherTextis=inverseShiftRows(cipherTextis) #inverse shift rows
    
    
    cipherTextis=invsBox(cipherTextis) #inverse sbox
    
    currRound=9
    while 1: #for round 9 to round 1
        ans=[] #for each row
        for i in range(len(cipherTextis)): #for each row
            temp=[]
            temp.append(XOR(cipherTextis[i][0],roundKeys[currRound][i][0]))
            ans.append(temp)
        

        cipherTextis=ans.copy() #copy to cipher text
        
        
        currRound-=1
        if(currRound==-1):
            break

        cipherTextis=invmixColumns(cipherTextis.copy()) #inverse mix columns

        cipherTextis=inverseShiftRows(cipherTextis.copy()) #inverse shift rows
        
        cipherTextis=invsBox(cipherTextis.copy()) #inverse sbox
        
   
    return cipherTextis

#Create main
def encrypt(keys,plainText,roundKeys,length): #encrypt
    #calculate encryptiuon time
    start_time = time.time()
   
    stateMatrix=[]
    for i in range(len(plainText)): #for each row
        ans=[]
        ans.append(XOR(plainText[i][0],roundKeys[0][i][0]))
        stateMatrix.append(ans)

    cipherTextis = workFromRound1(stateMatrix,roundKeys,length) #for round 1 to round 9
    answer=[]
    for i in range(len(cipherTextis)): #for each row
        t=[]
        t.append(cipherTextis[i][0])
        answer.append(t)
    

    #End time
    end_time = time.time()
    # calculate MB/s
    print("Encryption MB/s = ",(len(plainText)*16)/(end_time-start_time)/1000000)

    #calculate decryption time
    start_time = time.time()



    dec=decrypt(cipherTextis,roundKeys)   #decrypt

    #End time
    end_time = time.time()
    print("Decryption MB/s = ",(len(plainText)*16)/(end_time-start_time)/1000000)
    
    f = open("cipherText.enc", "a+")
    for i in range(len(cipherTextis)):
        f.write(cipherTextis[i][0])
    f.write("\n")
    f.close()

    
    f = open("decrypt.dec", "a+")
    for i in range(len(dec)):
        f.write(dec[i][0])
    f.write("\n")
    f.close()

    return answer

def readKey():
    f = open("key.key", "r")
    key=f.read()
    keyis=[]
    for i in range(0,len(key),2):
        temp=[]
        temp.append(key[i:i+2])
        keyis.append(temp)
    return keyis


def readPlainText():
    f = open("plaintext.pt", "r")
    plainTextis=[]
    for line in f:
        line=line[:-1]
        if (len(line)-1) !=32:
            while len(line)!=32:
                line+="0" 
        line+="\n" 
        tempo=[]
        for i in range(0,len(line),2):
            temp=[]
            if line[i:i+2] == '\n':
                continue
            temp.append(line[i:i+2])
            tempo.append(temp)
        plainTextis.append(tempo)
    return plainTextis

def main():

    f = open("cipherText.enc", "w")
    f.close()

    f = open("decrypt.dec", "w")
    f.close()

    keys=readKey()
    plainText=readPlainText()



    roundKeys,length=generateRoundKeys(keys)
    for i in range(len(plainText)):
        print("Encrypting Plain text in line ", i+1 )
        cipherText=encrypt(keys,plainText[i],roundKeys,length)
        print()
        print()
    


    return

if __name__ == "__main__":
    main()
