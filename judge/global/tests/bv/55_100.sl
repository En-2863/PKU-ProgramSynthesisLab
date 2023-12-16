
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


(constraint (= (f #xa750e40d387158e2) #x4ea1c81a70e2b1c4))
(constraint (= (f #x8713aabe8cad0458) #x0e27557d195a08b0))
(constraint (= (f #x7731450c69ae79c5) #x3b98a28634d73ce2))
(constraint (= (f #x39d7863e79e2eb2b) #x1cebc31f3cf17595))
(constraint (= (f #xb968729de8d3ca6a) #x72d0e53bd1a794d4))
(constraint (= (f #xdec8233a290c3e9c) #xbd90467452187d38))
(constraint (= (f #x968ed51521183eea) #x2d1daa2a42307dd4))
(constraint (= (f #x5d89d7c1be563d4c) #xbb13af837cac7a98))
(constraint (= (f #x1e5a72d1213ddd87) #x0f2d3968909eeec3))
(constraint (= (f #xc5c1a248c94e5a18) #x8b834491929cb430))
(constraint (= (f #x0226a3e18b674926) #x044d47c316ce924c))
(constraint (= (f #x1e16309e5143a7ce) #x3c2c613ca2874f9c))
(constraint (= (f #x9dd2b22e87826110) #x3ba5645d0f04c220))
(constraint (= (f #x47d5a2c614172314) #x8fab458c282e4628))
(constraint (= (f #xeea5b46ba9ab8501) #x7752da35d4d5c280))
(constraint (= (f #x3e9a2e657caba4e6) #x7d345ccaf95749cc))
(constraint (= (f #x20767e0c29617c87) #x103b3f0614b0be43))
(constraint (= (f #x6632474db7ab9be8) #xcc648e9b6f5737d0))
(constraint (= (f #xced3e331680ccc12) #x9da7c662d0199824))
(constraint (= (f #xe7218b1229e99bd2) #xce43162453d337a4))
(constraint (= (f #x0116eee9954e3597) #x008b7774caa71acb))
(constraint (= (f #x22b68230101686c5) #x115b4118080b4362))
(constraint (= (f #x482a6b21804459a1) #x24153590c0222cd0))
(constraint (= (f #x1b0e73bbcc64e364) #x361ce77798c9c6c8))
(constraint (= (f #x669c7b4b94aca605) #x334e3da5ca565302))
(constraint (= (f #xce7762d212d378de) #x9ceec5a425a6f1bc))
(constraint (= (f #x523ee81284e35277) #x291f74094271a93b))
(constraint (= (f #x1012e10beb4c6717) #x08097085f5a6338b))
(constraint (= (f #xd379a5ee95dbde9c) #xa6f34bdd2bb7bd38))
(constraint (= (f #xb1426c2d9ded6ba5) #x58a13616cef6b5d2))
(constraint (= (f #x371c0eba756ec137) #x1b8e075d3ab7609b))
(constraint (= (f #x72a63aa46da82e7c) #xe54c7548db505cf8))
(constraint (= (f #x8c87ac00d39ea23e) #x190f5801a73d447c))
(constraint (= (f #x59e341a999cc1ada) #xb3c68353339835b4))
(constraint (= (f #x675ea51187763b0a) #xcebd4a230eec7614))
(constraint (= (f #xe56147ce651c8985) #x72b0a3e7328e44c2))
(constraint (= (f #xed171a9b9903742c) #xda2e35373206e858))
(constraint (= (f #xd4dec8db70472408) #xa9bd91b6e08e4810))
(constraint (= (f #x3468394e76c7e5e9) #x1a341ca73b63f2f4))
(constraint (= (f #x93e235aae628d79d) #x49f11ad573146bce))
(constraint (= (f #x527aae88d0d9852c) #xa4f55d11a1b30a58))
(constraint (= (f #x05435aedebe5c03b) #x02a1ad76f5f2e01d))
(constraint (= (f #x5e631117b3221785) #x2f31888bd9910bc2))
(constraint (= (f #xc72d97115c3bd6d2) #x8e5b2e22b877ada4))
(constraint (= (f #xb624e5aa3909eec0) #x6c49cb547213dd80))
(constraint (= (f #x2ec40151a2e9a1ed) #x176200a8d174d0f6))
(constraint (= (f #xcc0c12e98673db5a) #x981825d30ce7b6b4))
(constraint (= (f #x6eaad3b959e7d50a) #xdd55a772b3cfaa14))
(constraint (= (f #x3ee0e568b8026571) #x1f7072b45c0132b8))
(constraint (= (f #x92cea3c2ed99ea0c) #x259d4785db33d418))
(constraint (= (f #x01345e0694d5b894) #x0268bc0d29ab7128))
(constraint (= (f #x2d8e04e1e29e7a22) #x5b1c09c3c53cf444))
(constraint (= (f #xa254e6dce211385c) #x44a9cdb9c42270b8))
(constraint (= (f #x3b8945d7d3d8cd86) #x77128bafa7b19b0c))
(constraint (= (f #xe5b0736d8b9a96d8) #xcb60e6db17352db0))
(constraint (= (f #x413e1d93d6b1b7e6) #x827c3b27ad636fcc))
(constraint (= (f #xb24cb30be1edcd03) #x59265985f0f6e681))
(constraint (= (f #x6ca8d0a8aa11c704) #xd951a15154238e08))
(constraint (= (f #x4e8d1277a4e62025) #x2746893bd2731012))
(constraint (= (f #xcaaceaa0d10b7a34) #x9559d541a216f468))
(constraint (= (f #x4d61888cbe4ee088) #x9ac311197c9dc110))
(constraint (= (f #xb5eae9d7510de308) #x6bd5d3aea21bc610))
(constraint (= (f #x99bb77d7eaaee8a5) #x4cddbbebf5577452))
(constraint (= (f #x00ac87a09eea0116) #x01590f413dd4022c))
(constraint (= (f #xe9beb4a1235ea2b0) #xd37d694246bd4560))
(constraint (= (f #x3185579e16ce6655) #x18c2abcf0b67332a))
(constraint (= (f #x8de9a3eabd756964) #x1bd347d57aead2c8))
(constraint (= (f #xb4d7da00a4285a75) #x5a6bed0052142d3a))
(constraint (= (f #x57ba003031784ea2) #xaf74006062f09d44))
(constraint (= (f #x6e4da817ba9d2ee6) #xdc9b502f753a5dcc))
(constraint (= (f #x871c3cdd5ed6ba68) #x0e3879babdad74d0))
(constraint (= (f #x2b9654ceab22e853) #x15cb2a6755917429))
(constraint (= (f #xd6a6d48d83c86848) #xad4da91b0790d090))
(constraint (= (f #xb862e0ad18b2edb7) #x5c3170568c5976db))
(constraint (= (f #x78074547311661d6) #xf00e8a8e622cc3ac))
(constraint (= (f #xee9cc1b8c7be1d9e) #xdd3983718f7c3b3c))
(constraint (= (f #x793720e40533d56b) #x3c9b90720299eab5))
(constraint (= (f #x73ce5e578c72ad57) #x39e72f2bc63956ab))
(constraint (= (f #x05009697ed70e9e8) #x0a012d2fdae1d3d0))
(constraint (= (f #xebe0529cdd5d7722) #xd7c0a539babaee44))
(constraint (= (f #xb37aadeb59761ac9) #x59bd56f5acbb0d64))
(constraint (= (f #xac327deaced6e92e) #x5864fbd59dadd25c))
(constraint (= (f #x5e178ed10a0ee873) #x2f0bc76885077439))
(constraint (= (f #xd99d7db35c53bb0e) #xb33afb66b8a7761c))
(constraint (= (f #x2e81156923e6a9d2) #x5d022ad247cd53a4))
(constraint (= (f #xe0d9422247553ed9) #x706ca11123aa9f6c))
(constraint (= (f #xebed284952177ee7) #x75f69424a90bbf73))
(constraint (= (f #x0ee517a3748cd2a5) #x07728bd1ba466952))
(constraint (= (f #x70e4d95c61a6e9dc) #xe1c9b2b8c34dd3b8))
(constraint (= (f #x6ade54eaa00c8a0c) #xd5bca9d540191418))
(constraint (= (f #x13de3b836cee5ce2) #x27bc7706d9dcb9c4))
(constraint (= (f #x37c2b8d276bee8b2) #x6f8571a4ed7dd164))
(constraint (= (f #xecea0c842628a05a) #xd9d419084c5140b4))
(constraint (= (f #x2483b9379e672ceb) #x1241dc9bcf339675))
(constraint (= (f #x6c20b8ee5459a773) #x36105c772a2cd3b9))
(constraint (= (f #x5d845b2d3a8ec26b) #x2ec22d969d476135))
(constraint (= (f #x403604120302e344) #x806c08240605c688))
(constraint (= (f #x6b7eee630e1b1b97) #x35bf7731870d8dcb))
(constraint (= (f #xe30c312bbae09086) #xc618625775c1210c))
(constraint (= (f #x725b6179827201a3) #x392db0bcc13900d1))
(check-synth)
