import sys

if (len(sys.argv)!=2):
    print ("usage %s filename"%(sys.argv[0]))

file1 = open ('./%s.abi'%sys.argv[1],"rb+")
data = file1.read()
#print (data)
file1.close()
file1 = open ('./%s.abi'%sys.argv[1],"wb+")
data = "var simpleContract = eth.contract(" + data + ")"
file1.write (data);
file1.close()

file2 = open ("./%s.bin"%sys.argv[1],'rb+')
data2 = file2.read()
#print (data2)
file2.close()
file2 = open('./%s.bin'%sys.argv[1],'wb+')
data2 = data2
data2 = '''
personal.unlockAccount(eth.accounts[0])

var simple = simpleContract.new(
{ from: eth.accounts[0],
data: "0x''' + data2 + '''",
gas: 3000000
}
)
'''
file2.write(data2)
file2.close()

