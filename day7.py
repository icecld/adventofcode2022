class elfile():
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

class dir():
    def __init__(self, name: str) -> None:
        self.name = name
        self.size = 0
        self.files = []
        self.child_dirs = {}

    def add_dir(self, name: dir) -> None:
        self.child_dirs[name] = dir(name)
    
    def add_file(self, f: elfile) -> None:
        self.files.append(f)
        self.size += f.size        
    
    def update_sizes(self):
        if self.child_dirs == {}:
            return self.size
        else:
            for d_name in self.child_dirs:
                s = self.child_dirs[d_name].update_sizes()
                self.size += s
            return self.size
    
    def sum_dirs_leq_size(self, n: int) -> int:
        total = 0
        if self.size <= n:
            total += self.size
        for d_name in self.child_dirs:
            total += self.child_dirs[d_name].sum_dirs_leq_size(n)
        return total
    
    
    #THIS BIT DOESNT WORK YET
    
    def smallest_dir_leq_size(self, n: int) -> str:
        self.smallest_dir_leq_size_helper(n, (70000000, ""))

    def smallest_dir_leq_size_helper(self, n: int, prev_best) -> str:
        if self.size >= n:
            if self.size < best[0]:
                best = (self.size, self.name)
            else:
                best = prev_best

        for d_name in self.child_dirs:
            best_child = self.child_dirs[d_name].smallest_dir_leq_size_helper(n)
            if best_child[0] < best[0]:
                best = best_child
        return best


def parse_filesystem(input: str) -> dir:
    filesystem = dir("/")
    parent_dir_path = []
    current_dir = None
    for i, line in enumerate(input.splitlines()):
        if "$" in line:
            if line == "$ ls":
                pass
            elif line == "$ cd /":
                current_dir = filesystem
            elif line == "$ cd ..":
                current_dir = parent_dir_path.pop()
            elif line[0:5] == "$ cd ":
                parent_dir_path.append(current_dir)
                current_dir = current_dir.child_dirs[line[5:]]
        elif "dir " in line[0:4]:
            if line[4:] not in current_dir.child_dirs:
                current_dir.add_dir(line[4:])
        else:
            file_attrs = line.split(" ")
            current_dir.add_file(elfile(file_attrs[1], int(file_attrs[0])))

    filesystem.update_sizes()

    return filesystem
    


def main():
    fs = parse_filesystem(INPUT)
    print(fs.sum_dirs_leq_size(100000))
    print(fs.smallest_dir_leq_size(30000000))

INPUT = """$ cd /
$ ls
dir brdsppd
dir dnjqmzgg
126880 fmftdzrp.fwt
173625 hhfqgzfj.qvt
dir lbbcfjl
dir mzdqcb
dir npppw
dir plmb
6337 rfgtcj.tdn
dir szfw
230140 vmc.cdf
$ cd brdsppd
$ ls
dir gjc
dir lcz
218543 ndqmcv
dir qnj
dir rrdd
dir zppsglq
$ cd gjc
$ ls
dir bvctghh
262132 cbczvmdf
111855 dnltsq.fwv
22416 fnrwscz.vwb
dir gwd
dir lsprzlbf
$ cd bvctghh
$ ls
dir lsprzlbf
dir lwfgnzz
dir tjslbpb
$ cd lsprzlbf
$ ls
182522 hhfqgzfj.qvt
dir hts
229288 jtpdh
dir lwfgnzz
284594 szfw
89639 tgdsjl
$ cd hts
$ ls
11158 dnltsq.fwv
52582 tchv
$ cd ..
$ cd lwfgnzz
$ ls
dir tjslbpb
$ cd tjslbpb
$ ls
58586 jtzmjgw.bql
$ cd ..
$ cd ..
$ cd ..
$ cd lwfgnzz
$ ls
199598 rlhz.pbs
$ cd ..
$ cd tjslbpb
$ ls
119666 fmzfs.glg
$ cd ..
$ cd ..
$ cd gwd
$ ls
dir bcfqd
1631 hhfqgzfj.qvt
$ cd bcfqd
$ ls
197168 cqvwnslp.ltw
$ cd ..
$ cd ..
$ cd lsprzlbf
$ ls
dir jwznh
$ cd jwznh
$ ls
dir lpm
dir ncs
dir vqprn
$ cd lpm
$ ls
15172 bnw.rqm
215818 flpbspn.stt
$ cd ..
$ cd ncs
$ ls
dir rzdbw
$ cd rzdbw
$ ls
15150 cvjldjt.gdc
$ cd ..
$ cd ..
$ cd vqprn
$ ls
23882 njjjh
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd lcz
$ ls
37587 gwcvttb.dhc
195583 lsprzlbf.vng
152648 tchv
$ cd ..
$ cd qnj
$ ls
dir bpvl
275640 cfvznj.bqc
dir lwfgnzz
213007 nwbt.mct
135231 twpf.pft
165501 vmc.cdf
88097 vmvs.hnr
dir znbdpp
$ cd bpvl
$ ls
dir nmzbpb
$ cd nmzbpb
$ ls
129477 pjlvs.zcp
$ cd ..
$ cd ..
$ cd lwfgnzz
$ ls
dir lwfgnzz
dir rsbdcwjr
dir sgh
dir wvwmf
$ cd lwfgnzz
$ ls
33186 ftcrfnmd
$ cd ..
$ cd rsbdcwjr
$ ls
dir lsprzlbf
$ cd lsprzlbf
$ ls
dir jvcgnbs
288445 pjmqm
111585 szfw.drf
dir vnftvqf
$ cd jvcgnbs
$ ls
dir ctlwjnjz
dir lwfgnzz
dir tjslbpb
$ cd ctlwjnjz
$ ls
72087 zmhnsmmf
$ cd ..
$ cd lwfgnzz
$ ls
151358 sqs
$ cd ..
$ cd tjslbpb
$ ls
112471 mftdzhwj.zvt
$ cd ..
$ cd ..
$ cd vnftvqf
$ ls
120421 lsprzlbf.tqc
$ cd ..
$ cd ..
$ cd ..
$ cd sgh
$ ls
228239 szfw.dzv
$ cd ..
$ cd wvwmf
$ ls
dir bcjfz
$ cd bcjfz
$ ls
26284 bzhqwdjq.nzn
$ cd ..
$ cd ..
$ cd ..
$ cd znbdpp
$ ls
dir szfw
$ cd szfw
$ ls
dir nthzqpws
dir snfmt
$ cd nthzqpws
$ ls
96382 twhdbvtw.lbj
$ cd ..
$ cd snfmt
$ ls
133360 bjmgtpgh
134215 vmc.cdf
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd rrdd
$ ls
185903 cpgpgntt.tfn
$ cd ..
$ cd zppsglq
$ ls
41689 jvcgnbs.hrt
169754 wgnpq
$ cd ..
$ cd ..
$ cd dnjqmzgg
$ ls
dir lsprzlbf
dir lwfgnzz
dir nmvj
dir sfpg
$ cd lsprzlbf
$ ls
dir lbw
141416 sqs
$ cd lbw
$ ls
48758 cjv
235522 dnltsq.fwv
$ cd ..
$ cd ..
$ cd lwfgnzz
$ ls
36709 bcmtmwcz
$ cd ..
$ cd nmvj
$ ls
dir dqpw
dir tjslbpb
$ cd dqpw
$ ls
10608 hhfqgzfj.qvt
$ cd ..
$ cd tjslbpb
$ ls
261140 qfzb
$ cd ..
$ cd ..
$ cd sfpg
$ ls
8543 szfw
69248 tjslbpb
$ cd ..
$ cd ..
$ cd lbbcfjl
$ ls
dir csnjp
dir drwpfn
301956 hhfqgzfj.qvt
dir jvcgnbs
dir lsprzlbf
dir pdzlnm
161886 tchv
153858 vmc.cdf
87849 wghtg
dir zhgchnld
$ cd csnjp
$ ls
dir ffgfmcm
dir gtd
dir lbjvqv
dir lwfgnzz
11312 sqs
$ cd ffgfmcm
$ ls
dir bcnvw
dir lcf
dir lsprzlbf
$ cd bcnvw
$ ls
111692 ftcvs.tcz
173665 jpfh.hrs
120561 lwfgnzz.zvd
dir ngtbzz
29479 tchv
dir tjslbpb
$ cd ngtbzz
$ ls
dir czrqmh
dir jrhpnpw
dir lsprzlbf
$ cd czrqmh
$ ls
225055 hhfqgzfj.qvt
$ cd ..
$ cd jrhpnpw
$ ls
206497 tjslbpb.zbv
$ cd ..
$ cd lsprzlbf
$ ls
66627 szfw.wtd
$ cd ..
$ cd ..
$ cd tjslbpb
$ ls
dir cgzlp
116060 lsprzlbf
dir szfw
128885 zht.ptf
$ cd cgzlp
$ ls
18201 sqs
$ cd ..
$ cd szfw
$ ls
104128 tchv
$ cd ..
$ cd ..
$ cd ..
$ cd lcf
$ ls
137662 lwfgnzz
$ cd ..
$ cd lsprzlbf
$ ls
151745 fmcgs.tvh
37707 gszw.jlm
dir lsprzlbf
178133 rjw.wrq
dir szw
267875 tchv
198852 vmc.cdf
$ cd lsprzlbf
$ ls
54734 lsprzlbf.hcq
81537 lwfgnzz
120990 qppfdrf
$ cd ..
$ cd szw
$ ls
dir jtvschrd
dir zcnpls
$ cd jtvschrd
$ ls
dir gtz
$ cd gtz
$ ls
dir rdzzlm
$ cd rdzzlm
$ ls
55063 tchv
8813 zfwvvpvz.zzb
$ cd ..
$ cd ..
$ cd ..
$ cd zcnpls
$ ls
282808 dpmd
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd gtd
$ ls
148653 cmchsg.zdr
66537 hhfqgzfj.qvt
125493 mdtmqbml.gnt
dir rwjdjqcs
dir tjslbpb
$ cd rwjdjqcs
$ ls
77026 zpt.gfp
$ cd ..
$ cd tjslbpb
$ ls
dir dfl
$ cd dfl
$ ls
203731 qpsmsjgh.gvs
dir tjslbpb
84386 vmc.cdf
dir zgh
$ cd tjslbpb
$ ls
dir lwfgnzz
140021 qnp
312305 svh.vqt
$ cd lwfgnzz
$ ls
49701 lgffdn.gmr
$ cd ..
$ cd ..
$ cd zgh
$ ls
138627 tchv
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd lbjvqv
$ ls
dir bnl
$ cd bnl
$ ls
dir gbv
dir lwfgnzz
$ cd gbv
$ ls
dir lsprzlbf
36406 lsprzlbf.cfd
$ cd lsprzlbf
$ ls
168615 hlhp.rvp
$ cd ..
$ cd ..
$ cd lwfgnzz
$ ls
149511 cdpwjbpd
$ cd ..
$ cd ..
$ cd ..
$ cd lwfgnzz
$ ls
232898 dnltsq.fwv
181665 hhfqgzfj.qvt
62529 qfmhhvvq.prh
57822 sqs
$ cd ..
$ cd ..
$ cd drwpfn
$ ls
dir fvgw
dir lsprzlbf
dir lwfgnzz
104745 nqvlqd.mdb
203189 qqpmz
159549 tchv
dir tjslbpb
dir wnrns
$ cd fvgw
$ ls
dir tlzmplfl
$ cd tlzmplfl
$ ls
29740 vmc.cdf
30062 wgrm.dst
181738 zqr
$ cd ..
$ cd ..
$ cd lsprzlbf
$ ls
dir lcqhctjl
dir ldr
dir tjslbpb
$ cd lcqhctjl
$ ls
209114 bcfr.gpf
$ cd ..
$ cd ldr
$ ls
148649 fzh.pqm
$ cd ..
$ cd tjslbpb
$ ls
241013 dnltsq.fwv
$ cd ..
$ cd ..
$ cd lwfgnzz
$ ls
288335 cdctnn
67277 tchv
$ cd ..
$ cd tjslbpb
$ ls
dir pblzrspg
dir qqgddb
86103 sqs
183539 tjslbpb.wrs
$ cd pblzrspg
$ ls
dir pgl
$ cd pgl
$ ls
305421 lwfgnzz.jdz
114244 tjslbpb
dir vzff
$ cd vzff
$ ls
80591 rlww.htq
86968 sqs
$ cd ..
$ cd ..
$ cd ..
$ cd qqgddb
$ ls
dir szfw
$ cd szfw
$ ls
dir jtw
$ cd jtw
$ ls
263 szfw.lzp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd wnrns
$ ls
203725 dnltsq.fwv
77752 qrg.fnt
$ cd ..
$ cd ..
$ cd jvcgnbs
$ ls
296356 lwfgnzz.svf
294928 ptvdsngf
$ cd ..
$ cd lsprzlbf
$ ls
dir lwfgnzz
dir tjslbpb
$ cd lwfgnzz
$ ls
105095 tchv
$ cd ..
$ cd tjslbpb
$ ls
53558 hhfqgzfj.qvt
189180 szfw
$ cd ..
$ cd ..
$ cd pdzlnm
$ ls
76426 jwttcp.rjj
dir lsprzlbf
dir qldhzf
dir rtdsjf
dir sfdtljj
69033 slhl.jst
$ cd lsprzlbf
$ ls
71362 vgdr
$ cd ..
$ cd qldhzf
$ ls
303106 lsprzlbf.rbq
$ cd ..
$ cd rtdsjf
$ ls
45781 pzbgwrdm.lwt
dir rzc
$ cd rzc
$ ls
297081 qqvlp
86015 zthlr
$ cd ..
$ cd ..
$ cd sfdtljj
$ ls
254377 ftw.fwg
dir jvcgnbs
153393 lwfgnzz.dws
dir pnphc
220821 wslttcn
$ cd jvcgnbs
$ ls
92642 bzpvvlsn.gvt
$ cd ..
$ cd pnphc
$ ls
288388 lwfgnzz
$ cd ..
$ cd ..
$ cd ..
$ cd zhgchnld
$ ls
16588 ftgrpj.srl
112044 vmc.cdf
$ cd ..
$ cd ..
$ cd mzdqcb
$ ls
dir bfphcs
dir cgjmj
dir jgcqqsh
dir jvcgnbs
dir lccjbtqs
dir lwfgnzz
dir pprvjm
dir szfw
dir tjslbpb
dir ztc
$ cd bfphcs
$ ls
124148 wzt.qtr
$ cd ..
$ cd cgjmj
$ ls
28095 ddjdbdf
dir jvcgnbs
169536 sqs
dir svbsrj
159511 vmc.cdf
$ cd jvcgnbs
$ ls
dir crmsnch
dir jvcgnbs
$ cd crmsnch
$ ls
195745 lsprzlbf.prh
271424 tjslbpb
227054 vmc.cdf
$ cd ..
$ cd jvcgnbs
$ ls
294249 vmc.cdf
$ cd ..
$ cd ..
$ cd svbsrj
$ ls
49038 cspzcpqs
dir czltsqrg
98084 ljhljcw
dir ntdjg
202570 szfw.lpj
$ cd czltsqrg
$ ls
207690 dnltsq.fwv
208745 lnns.hsv
40703 rgmjszf.vtd
$ cd ..
$ cd ntdjg
$ ls
dir szfw
$ cd szfw
$ ls
284994 qzwptr.ggb
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jgcqqsh
$ ls
2462 djfwggvp
$ cd ..
$ cd jvcgnbs
$ ls
dir ftjprdj
289965 zhlrstpt
$ cd ftjprdj
$ ls
dir wnmhs
$ cd wnmhs
$ ls
dir tjslbpb
$ cd tjslbpb
$ ls
dir jvcgnbs
$ cd jvcgnbs
$ ls
160761 dnltsq.fwv
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd lccjbtqs
$ ls
dir jjrdbgtg
77186 sqs
116398 szfw.qjt
182665 vmc.cdf
248366 vqdjwsh
$ cd jjrdbgtg
$ ls
237358 bdvbjs.sjp
$ cd ..
$ cd ..
$ cd lwfgnzz
$ ls
dir ggptdvr
dir jnb
dir lcpmzpr
222506 lsprzlbf
293605 qbjfqh
dir smvwg
291643 tchv
247095 vwdstb.pdw
dir wghpmnm
dir wtrbfrj
$ cd ggptdvr
$ ls
184198 vmc.cdf
$ cd ..
$ cd jnb
$ ls
296536 dnltsq.fwv
91419 jvcgnbs.cvq
279635 rwt.wth
$ cd ..
$ cd lcpmzpr
$ ls
184769 hhfqgzfj.qvt
dir qwqcbdms
236533 tjslbpb.bnc
162397 vmvctfnw
dir wcc
$ cd qwqcbdms
$ ls
232132 jgm.tfm
dir jnfmcnfh
173727 mwrbndt
dir qshphcb
dir tjslbpb
$ cd jnfmcnfh
$ ls
dir rngnt
$ cd rngnt
$ ls
236114 hhfqgzfj.qvt
$ cd ..
$ cd ..
$ cd qshphcb
$ ls
78407 lsprzlbf.hpd
$ cd ..
$ cd tjslbpb
$ ls
30200 brbz
171368 jvcgnbs.vwl
236158 sqs
285872 srfwnmb
dir znr
$ cd znr
$ ls
108194 hhfqgzfj.qvt
$ cd ..
$ cd ..
$ cd ..
$ cd wcc
$ ls
167768 jvcgnbs
289640 lgthn.cjn
28517 lwfgnzz.chf
dir nvgfwn
43738 rrg
81011 sqs
$ cd nvgfwn
$ ls
270370 hgnv.ssj
98235 lwfgnzz.nfv
$ cd ..
$ cd ..
$ cd ..
$ cd smvwg
$ ls
dir jvcgnbs
77510 tchv
dir tgrm
$ cd jvcgnbs
$ ls
287955 bqcnj.zzv
119021 bsrtmzd
3391 cnngp.mbf
68540 qjmb.vjz
149062 tchv
$ cd ..
$ cd tgrm
$ ls
112315 qzth
277566 scqp
$ cd ..
$ cd ..
$ cd wghpmnm
$ ls
dir hpm
$ cd hpm
$ ls
113354 hhfqgzfj.qvt
$ cd ..
$ cd ..
$ cd wtrbfrj
$ ls
dir ggrsgzvv
dir mvzzsl
dir szfw
dir vsqjb
$ cd ggrsgzvv
$ ls
dir dpv
dir gqtsmnr
dir lsprzlbf
dir pcjcm
137203 tchv
84711 tns.sdh
$ cd dpv
$ ls
233264 dmd
dir fzlchpb
293097 gwmspnm.qtp
100283 jbbnssc.nnv
$ cd fzlchpb
$ ls
150431 pdmzrs.rll
$ cd ..
$ cd ..
$ cd gqtsmnr
$ ls
dir jdml
dir jfqtjt
dir lwfgnzz
dir tjslbpb
$ cd jdml
$ ls
148333 bwm.dnt
dir lsprzlbf
$ cd lsprzlbf
$ ls
dir cslvm
dir lwfgnzz
dir rllt
265856 sqs
dir szfw
56452 tchv
$ cd cslvm
$ ls
266380 vmc.cdf
$ cd ..
$ cd lwfgnzz
$ ls
dir tzghdrd
$ cd tzghdrd
$ ls
dir tjslbpb
dir vhv
$ cd tjslbpb
$ ls
dir jvcgnbs
$ cd jvcgnbs
$ ls
18188 sqs
$ cd ..
$ cd ..
$ cd vhv
$ ls
95547 jhhblnn.vzt
dir srgh
$ cd srgh
$ ls
299624 lsprzlbf.dnr
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd rllt
$ ls
dir crpcbl
308185 dnltsq.fwv
dir szfw
$ cd crpcbl
$ ls
209445 dfds.mzh
$ cd ..
$ cd szfw
$ ls
dir lsprzlbf
159720 vmc.cdf
$ cd lsprzlbf
$ ls
291090 tzrvpv
$ cd ..
$ cd ..
$ cd ..
$ cd szfw
$ ls
113605 fbrtbfjm
$ cd ..
$ cd ..
$ cd ..
$ cd jfqtjt
$ ls
119124 hhfqgzfj.qvt
251412 jvcgnbs.zfm
dir rbv
dir tjslbpb
142371 tjslbpb.czt
65455 vmc.cdf
47786 zjmtjsv
$ cd rbv
$ ls
300632 dzssgm.pqn
$ cd ..
$ cd tjslbpb
$ ls
221545 pswrb.bsw
$ cd ..
$ cd ..
$ cd lwfgnzz
$ ls
34086 wshbr.spm
$ cd ..
$ cd tjslbpb
$ ls
118394 djfwjd.fvl
65377 qmgcpdr.qjz
146317 tchv
$ cd ..
$ cd ..
$ cd lsprzlbf
$ ls
195086 clqmgmq.gbw
dir cpgjgbdf
109787 jmwshtg.snl
305108 lsprzlbf
dir szfw
174614 szfw.qjq
105247 vmcf.rsm
$ cd cpgjgbdf
$ ls
dir vzddwsr
$ cd vzddwsr
$ ls
91787 nwgfs
$ cd ..
$ cd ..
$ cd szfw
$ ls
193316 tjslbpb
$ cd ..
$ cd ..
$ cd pcjcm
$ ls
dir lsprzlbf
$ cd lsprzlbf
$ ls
210834 hvrpj.cdc
29497 wcnf
$ cd ..
$ cd ..
$ cd ..
$ cd mvzzsl
$ ls
dir rnrtf
$ cd rnrtf
$ ls
221025 btwgwrp.ctj
$ cd ..
$ cd ..
$ cd szfw
$ ls
dir jvcgnbs
dir szfw
31365 tjslbpb
$ cd jvcgnbs
$ ls
250409 lwfgnzz.nvf
66638 tchv
dir tlms
$ cd tlms
$ ls
84192 lsprzlbf.pcm
107549 nwqzqcmw.rls
97234 svdqvwcz
$ cd ..
$ cd ..
$ cd szfw
$ ls
45362 zsflqrtc
$ cd ..
$ cd ..
$ cd vsqjb
$ ls
dir vvnzdcbb
$ cd vvnzdcbb
$ ls
144027 tchv
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pprvjm
$ ls
dir hvst
137237 lwfgnzz.qfp
dir szfw
$ cd hvst
$ ls
100531 svmvncf
$ cd ..
$ cd szfw
$ ls
233868 hhfqgzfj.qvt
$ cd ..
$ cd ..
$ cd szfw
$ ls
14971 tchv
$ cd ..
$ cd tjslbpb
$ ls
283684 lwfgnzz.wzv
$ cd ..
$ cd ztc
$ ls
dir bwhfncdm
161420 jvcgnbs
135102 tchv
$ cd bwhfncdm
$ ls
108615 lwfgnzz.msn
$ cd ..
$ cd ..
$ cd ..
$ cd npppw
$ ls
94593 cwdz.tlb
258598 jsswljc
245674 nmmfzscz
$ cd ..
$ cd plmb
$ ls
dir dwnpl
dir lwfgnzz
$ cd dwnpl
$ ls
15993 hhfqgzfj.qvt
264944 vmc.cdf
$ cd ..
$ cd lwfgnzz
$ ls
154801 cnbmh.hsh
$ cd ..
$ cd ..
$ cd szfw
$ ls
173334 lsprzlbf
dir lwfgnzz
70693 szfw
$ cd lwfgnzz
$ ls
dir jgwzcgd
dir qgdcjq
dir spwcmrl
$ cd jgwzcgd
$ ls
dir jvcgnbs
dir nvtvcf
$ cd jvcgnbs
$ ls
131852 cntlhf.mqq
217305 dnltsq.fwv
174110 jvcgnbs.njb
179602 lwfgnzz.mth
dir pzcssdhv
dir qcmqmnpn
227361 szfw
dir wmhhl
$ cd pzcssdhv
$ ls
187518 gjfwbwnv
115671 lsprzlbf
$ cd ..
$ cd qcmqmnpn
$ ls
197002 dlns
40030 mmpp.ggt
198158 tchv
$ cd ..
$ cd wmhhl
$ ls
168011 hhfqgzfj.qvt
$ cd ..
$ cd ..
$ cd nvtvcf
$ ls
dir rrzjjjhc
$ cd rrzjjjhc
$ ls
33548 sqs
$ cd ..
$ cd ..
$ cd ..
$ cd qgdcjq
$ ls
252274 prshd.qdj
$ cd ..
$ cd spwcmrl
$ ls
dir lslmr
dir szfw
135076 tchv
265608 vmc.cdf
$ cd lslmr
$ ls
172247 rrvwsbl
$ cd ..
$ cd szfw
$ ls
192729 rnq"""

if __name__ == "__main__":
    main()
