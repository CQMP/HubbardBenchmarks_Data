#this script generates the file names
from os import system

for t in ["1"]:
  for tprime in ["-0.2","0","0.2"]:
    ttprime="t"+t+"_tprime"+tprime
    print ttprime
    system("mkdir -p "+ttprime)
    for U in ["2","4","6","8","12"]:
      for n in ["1","0.875","0.8","0.6","0.3"]:
        for T in ["0","0.125","0.25","0.5"]:
          print "t"+t+"_tprime"+tprime+"_U"+U+"_n"+n+"_T"+T
          system("mkdir -p "+ttprime+"/t"+t+"_tprime"+tprime+"_U"+U+"_n"+n+"_T"+T)
