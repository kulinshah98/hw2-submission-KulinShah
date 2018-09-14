import os
import time

all_flags = "-targetlibinfo -tti -tbaa -scoped-noalias -assumption-cache-tracker -forceattrs -inferattrs -ipsccp -globalopt -domtree -mem2reg -deadargelim -basicaa -aa -domtree -instcombine -simplifycfg -aa -loops -lazy-branch-prob -basiccg -globals-aa -prune-eh -inline -functionattrs -domtree -sroa -early-cse -lazy-value-info -jump-threading -correlated-propagation -simplifycfg -basicaa -aa -domtree -instcombine -tailcallelim -simplifycfg -reassociate -domtree -loops -loop-simplify -lcssa -loop-rotate -basicaa -aa -licm -loop-unswitch -simplifycfg -basicaa -aa -domtree -instcombine -loops -scalar-evolution -loop-simplify -lcssa -indvars -aa -loop-idiom -loop-deletion -loop-unroll -basicaa -aa -mldst-motion -aa -memdep -gvn -basicaa -aa -memdep -memcpyopt -sccp -domtree -demanded-bits -bdce -basicaa -aa -instcombine -lazy-value-info -jump-threading -correlated-propagation -domtree -basicaa -aa -memdep -dse -loops -loop-simplify -lcssa -aa -licm -adce -simplifycfg -basicaa -aa -domtree -instcombine -barrier -basiccg -rpo-functionattrs -elim-avail-extern -basiccg -globals-aa -float2int -domtree -loops -loop-simplify -lcssa -loop-rotate -branch-prob -block-freq -scalar-evolution -basicaa -aa -loop-accesses -demanded-bits -loop-vectorize -instcombine -scalar-evolution -aa -slp-vectorizer -simplifycfg -basicaa -aa -domtree -instcombine -loops -loop-simplify -lcssa -scalar-evolution -loop-unroll -basicaa -aa -instcombine -loop-simplify -lcssa -aa -licm -scalar-evolution -alignment-from-assumptions -strip-dead-prototypes -globaldce -constmerge -verify"

arr = list(set(all_flags.split(' ')))
print len(arr)

#cur_files = os.listdir('../Coyote/.')
cur_files = ['fftbench.c', 'lpbench.c', 'treebench.c']

print arr
for f in cur_files:
    print f
    str1 = "clang -c -emit-llvm " + f + " -o intermediate.bc"
    os.system(str1)

    for cnt in range(len(arr)):
        com = "opt -S "

        for ind,i in enumerate(arr):
            if(cnt != ind):
                com = com + i
		com = com + " "

        com += "intermediate.bc -o intermediate"
        #print com
        #os.system(com)

        os.system("llc intermediate.bc")
        os.system("clang intermediate.s -lm")

        st_time = time.time()
        os.system("./a.out")
        en_time = time.time()
        print (f, end-start, arr[cnt])
	if cnt%10 == 0:
	    time.sleep(20)

    time.sleep(10)
