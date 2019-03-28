import sunau
import random
"""CS176b HW2 by Adjon Tahiraj 4487591
    I decided to use python library sunau to read/write
    the .au files.
    In order to run the program you need simple.au
    which was included in the assignment and the
    progam automatically runs main().
    The parameters which we are to experiment with are:
    packetLen -> testing effect of packet size
    threshold -> testing the effect of packet loss
    policy    -> testing different packet drop policies:
    1=silence, 2=last sample, 3=last packet"""

def main():
    #source and destination file names
    sourceFile = "simple.au"
    destFile = "test.au"
    
    #opening source and dest file
    sFile = sunau.open(sourceFile, "r")
    dFile = sunau.open(destFile, "w")
    
    #getting parameters and data from source file
    params = sFile.getparams()
    numFrames = sFile.getnframes()
    
    #setting destination parametersto the same
    dFile.setparams(params)
    
    #setting packet size in terms of frames
    packetLen = 1000
    #setting threshold (ex 20% packet loss => threshold = 80)
    threshold = 80
    #setting playback policy (1->playing silence,
    #2->playing last sample,
    #3->replaying last packet)
    policy = 1
    
    #holding emptyData for policy 1
    emptyData = bytes("  "*packetLen,'utf-8')
    #holding repeat for policy 3 and sample for policy 2
    repeat = emptyData
    sample = emptyData
    
    
    for i in range (1,numFrames+1,packetLen):
        #randomizing packet loss
        packetLoss = random.randint(1,101)
        
        #reading packet to be "received"
        packet = sFile.readframes(packetLen)
        
        if packetLoss < threshold:
            dFile.writeframes(packet)
        
        elif policy == 1:
            dFile.writeframes(emptyData)
        
        elif policy == 2:
            dFile.writeframes(sample)
        
        else:#policy 3
            dFile.writeframes(repeat)
        
        #holding sample for policy 2
        sample = packet[len(packet)-1:]*len(packet)
        
        #holding repeat for folicy 3
        repeat = packet
    
    dFile.close()
    sFile.close()
main()
