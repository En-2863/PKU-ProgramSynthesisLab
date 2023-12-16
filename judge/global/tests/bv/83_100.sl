
(set-logic BV)

(define-fun shr1 ((x (_ BitVec 64))) (_ BitVec 64) (bvlshr x #x0000000000000001))
(define-fun shr4 ((x (_ BitVec 64))) (_ BitVec 64) (bvlshr x #x0000000000000004))
(define-fun shr16 ((x (_ BitVec 64))) (_ BitVec 64) (bvlshr x #x0000000000000010))
(define-fun shl1 ((x (_ BitVec 64))) (_ BitVec 64) (bvshl x #x0000000000000001))
(define-fun if0 ((x (_ BitVec 64)) (y (_ BitVec 64)) (z (_ BitVec 64))) (_ BitVec 64) (ite (= x #x0000000000000001) y z))

(synth-fun f ( (x (_ BitVec 64))) (_ BitVec 64)
(

(Start (_ BitVec 64) (#x0000000000000000 #x0000000000000001 x (bvnot Start)
                    (shl1 Start)
 		    (shr1 Start)
		    (shr4 Start)
		    (shr16 Start)
		    (bvand Start Start)
		    (bvor Start Start)
		    (bvxor Start Start)
		    (bvadd Start Start)
		    (if0 Start Start Start)
 ))
)
)


(constraint (= (f #x0acd09c5a975c111) #x0acf09c7ad7fe119))
(constraint (= (f #x7640c320cb13baee) #x42846dc2723b1925))
(constraint (= (f #xc2cb7649acb76e28) #x6d92728971272df6))
(constraint (= (f #x02eab4d8531eaa88) #x01a405b9aec13fec))
(constraint (= (f #xe28712501a800edd) #xe3871a501ac00eff))
(constraint (= (f #xe67ed79a8acd24b9) #xe77ff79ececf24bd))
(constraint (= (f #x2a217052ddc89ade) #x17b2cf2e9cc0d71c))
(constraint (= (f #xe01eb63c7831d9ee) #x7e114682039c0a95))
(constraint (= (f #x7e0bd9c1d2a36b8b) #x7f0bddc1dab37bcf))
(constraint (= (f #xee2232b953028a68) #x85f33c883eb16dda))
(constraint (= (f #x2016ece1da8b3e26) #x120ce53f0aee52f5))
(constraint (= (f #x1e543cb3e7eaa7dd) #x1e763cf3f7fff7ff))
(constraint (= (f #x0239c0851e5d1534) #x01407c4ae1145bed))
(constraint (= (f #xc15e44b985bd6ee0) #x6cc506a85b3a8e5e))
(constraint (= (f #x5d956c712bda6d76) #x34a40cffa8aadd92))
(constraint (= (f #x47480e23de58c3d1) #x47680e33de78c3d9))
(constraint (= (f #x5086646b90bd6749) #x5086766bd8bde769))
(constraint (= (f #x969c6e63be80914a) #x54b7fe181b2851b9))
(constraint (= (f #xb0e300ee9506e4aa) #x637fb08633d3e09f))
(constraint (= (f #xa0e4c35d28dc7e0c) #x5a80ade466fc06e6))
(constraint (= (f #x4d00826d8c256c52) #x2b50495d9ed50cee))
(constraint (= (f #xce3709c16c83718d) #xce3789c16ec3798d))
(constraint (= (f #x7702cb254e7485d1) #x7782cf356e7685f9))
(constraint (= (f #x2178dac156e6e946) #x12d3fb0cc0e1e337))
(constraint (= (f #x1e776e1d27a5aa61) #x1e77ff1da7b5af71))
(constraint (= (f #x457ee2cc8dd55346) #x27175f930fc7fed7))
(constraint (= (f #x2e7eb23435cb9817) #x2f7ff33435efdc17))
(constraint (= (f #x90e158e3e92beb33) #x90e158e3fd2bff3b))
(constraint (= (f #xa75e28394ba86ee2) #x5e24f6a03a8ebe5f))
(constraint (= (f #xedc42416a80986ae) #x85be544cbe855bc1))
(constraint (= (f #xe7614d4164d3add3) #xe7714f6166f3bdfb))
(constraint (= (f #x9e01664b61b2d136) #x58e0c98a66f495ae))
(constraint (= (f #x4828c868c7e4a7e5) #x4828cc68c7f6a7f7))
(constraint (= (f #x8142ebe06bae1138) #x48b5a4ae3c91e9af))
(constraint (= (f #xc559978d6e4eee70) #x6f02653f8e0c661f))
(constraint (= (f #x0430ac615182951a) #x025b60f6bdd973de))
(constraint (= (f #x4c26d7beee0b69c6) #x2ad5d95b65e66b7f))
(constraint (= (f #x7308de58802cd66e) #x40b4fd11c819389d))
(constraint (= (f #x2ea71496941abe94) #x1a3dfb94b34f0b33))
(constraint (= (f #xa8b87978346a03ba) #x5ee7c4539d7ba218))
(constraint (= (f #x091ee5d365b1a8d4) #x05216146e933eef7))
(constraint (= (f #xe44179e810c73bee) #x8064d492897011b5))
(constraint (= (f #xb1e71b94947388e1) #xb1e71bdc94738ce1))
(constraint (= (f #xda9b819e9e717bee) #x7af778e9391fd5b5))
(constraint (= (f #x953b280783d7671a) #x53f146843a2929fe))
(constraint (= (f #xc8359b18609e2ce3) #xcc359f98609e3ce3))
(constraint (= (f #xead2e2ae58621b7d) #xefd2f3bf78631bff))
(constraint (= (f #xc62c997a45238a8d) #xc63cddfb47238ecd))
(constraint (= (f #x8b6aa407d85995dd) #x8f7bf407fc59ddff))
(constraint (= (f #x6c677dec6b1d9163) #x6e677fee6b1dd9e3))
(constraint (= (f #x10e7ec87513c163b) #x10e7fec779bc163b))
(constraint (= (f #xdb8e89e89754bee3) #xdfcecdecd7febff3))
(constraint (= (f #xc02e86ed55916aa8) #x6c1a2be58021cbfe))
(constraint (= (f #xab5189454e704393) #xaf598d476e70439b))
(constraint (= (f #xbd5be170eece648e) #x6a83aecf8654188f))
(constraint (= (f #xed9638e8cbe3a642) #x85a48002f2b00d85))
(constraint (= (f #x35a34eb539dc2cea) #x1e2bdc45f08bd943))
(constraint (= (f #x825b772c57e8e7b7) #x825bffbc77fce7bf))
(constraint (= (f #x4375e9ecaa702135) #x437fedeeef70213d))
(constraint (= (f #x6579ceca76ac2696) #x39148451e2c0d5b4))
(constraint (= (f #xa2b7ee77c891b2e1) #xa3b7ff77ecd1bbf1))
(constraint (= (f #xba6a39ee309372e5) #xbf7b39ef3093fbf7))
(constraint (= (f #x4d280b16dad33aee) #x2b66863cdb16d125))
(constraint (= (f #xb276392c8617e0ab) #xb37739acc617f0af))
(constraint (= (f #xa05282d9638534a3) #xa05282dde3853ca3))
(constraint (= (f #xeee72e4dadeca9e9) #xeff73f6fedeeeded))
(constraint (= (f #x1a9e9b8e035eb845) #x1adedfce035efc47))
(constraint (= (f #xe25b4d98d80d1485) #xe35bcfdcdc0d1c85))
(constraint (= (f #x1a90cb686b85a87a) #x0ef1726abc7b2ec4))
(constraint (= (f #x101925d2e531b2b8) #x090e2546a0ebf487))
(constraint (= (f #x3d99eabb42641cc2) #x22a694095558502d))
(constraint (= (f #xd2eee612e85d652d) #xd2fff712fc5fe72d))
(constraint (= (f #xb6d36b2742ee500c) #x66d6ec4615a60d06))
(constraint (= (f #x71b22104b7c29aa3) #x71bb3104b7e29ef3))
(constraint (= (f #x885eee2d2ea2dc80) #x4cb565f96a3b9c08))
(constraint (= (f #x51da7922438dcee3) #x51de79a3438deef3))
(constraint (= (f #x031aeb8e81ec4420) #x01bf24802914e652))
(constraint (= (f #x372144b9d1790db6) #x1f02b6a885d417b6))
(constraint (= (f #x469248e53236ec3c) #x27b24900ec3ee4e1))
(constraint (= (f #x290e46419a2bc586) #x17180784e6b89f1b))
(constraint (= (f #x039b8126e7a24c63) #x039fc127f7b34e63))
(constraint (= (f #x3e7a42a90d000748) #x2324c57f17500418))
(constraint (= (f #xacb8920eeee79a94) #x6127d228666246f3))
(constraint (= (f #xb512b498d270d1c9) #xb59ab49cd270d1cd))
(constraint (= (f #xc742b96b359c2b81) #xc762bdeb3d9c2bc1))
(constraint (= (f #x3dec67671573865c) #x22d4fa29fc10fb93))
(constraint (= (f #x949b88e6581b4c31) #x949fcce7781bce31))
(constraint (= (f #xe459800a2514edbd) #xe679c00a351ceffd))
(constraint (= (f #xe28c52951b736ebe) #x7f6eee73df70ee4a))
(constraint (= (f #xae868459ab19d230) #x622baa72703e863b))
(constraint (= (f #xebd4931bae3a4b31) #xefde939bff3b4b39))
(constraint (= (f #xdb55277927b84a0d) #xdfdfa779a7bc4a0d))
(constraint (= (f #x449a81c038c814de) #x2696e8fc1ff08bbc))
(constraint (= (f #x505cdd01440073d4) #x2d343c50b6404127))
(constraint (= (f #x9c77679abc0c49e9) #x9c77f79efc0c69ed))
(constraint (= (f #x838d63be4b6d0091) #x838d63bf6b7f0091))
(constraint (= (f #xd11ce6539dacb840) #x75a0418f08b127a4))
(constraint (= (f #x7cee6623e311e7ee) #x464619742fba1275))
(constraint (= (f #xe1eaeb8e76c4080c) #x7f14248022ce4486))
(constraint (= (f #x3ecd7ce750b59ec9) #x3fef7ee778b59eed))
(check-synth)
