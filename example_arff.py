import math

fw=open("example.arff","w")

fw.write("@RELATION test_arff\n")
#fw.write("@ATTRIBUTE relopenP_BP numeric\n")
#fw.write("@ATTRIBUTE relcloseP_BP numeric\n")
#fw.write("@ATTRIBUTE relcloseP_BP2 numeric\n")
#fw.write("@ATTRIBUTE relcloseP_BP3 numeric\n")
#fw.write("@ATTRIBUTE relcloseP_BP4 numeric\n")
#fw.write("@ATTRIBUTE relcloseP_BP5 numeric\n")
fw.write("@ATTRIBUTE t20_50 numeric\n")
fw.write("@ATTRIBUTE t20_100 numeric\n")
fw.write("@ATTRIBUTE class {H,L}\n")

fh=open("BABA4.csv")

fw.write("@DATA\n")

all_lines=fh.readlines()[1:]

N=100

for x in range(100,len(all_lines)-N):

    cur_line=all_lines[x].split(",")
    before_line=all_lines[x-1].split(",")
    tar_line=all_lines[x+N].split(",")

    before_line2=all_lines[x-2].split(",")
    before_line3=all_lines[x-3].split(",")
    before_line4=all_lines[x-4].split(",")
    before_line5=all_lines[x-5].split(",")

    cs20=[]
    for y in range(0,20):
        cs20.append(float(all_lines[x-y].split(",")[4]))
    cs50=[]
    for y in range(0,50):
        cs50.append(float(all_lines[x-y].split(",")[4]))
    cs100=[]
    for y in range(0,100):
        cs100.append(float(all_lines[x-y].split(",")[4]))

    csm20=(sum(cs20)/len(cs20))
    csm50=(sum(cs50)/len(cs50))
    csm100=(sum(cs100)/len(cs100))
    
    closeP=float(cur_line[4])
    openP=float(cur_line[1])

    closePB=float(before_line[4])
    openPB=float(before_line[1])

    closePB2=float(before_line2[4])
    closePB3=float(before_line3[4])
    closePB4=float(before_line4[4])
    closePB5=float(before_line5[4])
    
    if(float(tar_line[4])/closeP>1.2):
        my_class="H"
    else:
        my_class="L"

    if(closeP>openP and closePB<openPB):
        #fw.write("%i,%i,%i,%i,%i,%i,%i,%i,%s\n" % (100.0*openP/openPB,100.0*closeP/closePB,100.0*closeP/closePB2,100.0*closeP/closePB3,100.0*closeP/closePB4,100.0*closeP/closePB5,100.0*csm20/csm50,100.0*csm20/csm100,my_class))
        fw.write("%i,%i,%s\n" % (100.0*csm20/csm50,100.0*csm20/csm100,my_class))
    
fw.close()
