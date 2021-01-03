fw=open("example.arff","w")

fw.write("@RELATION test_arff\n")
fw.write("@ATTRIBUTE word string\n")
fw.write("@ATTRIBUTE count numeric\n")

fw.write("@DATA\n")
fw.write("A1,1\n")
fw.write("A1,2\n")
fw.write("B1,1\n")
fw.write("C1,3\n")
fw.write("D1,1\n")
fw.write("E1,4\n")
fw.write("A1,5\n")
fw.write("B1,1\n")
fw.write("C1,6\n")
fw.write("A1,1\n")

fw.close()
