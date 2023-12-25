(synth-fun findIdx ( (y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (y8 Int) (y9 Int) (y10 Int) (y11 Int) (y12 Int) (y13 Int) (y14 Int) (y15 Int) (k1 Int)) Int ((Start Int ( 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 y1 y2 y3 y4 y5 y6 y7 y8 y9 y10 y11 y12 y13 y14 y15 k1 (ite BoolExpr Start Start))) (BoolExpr Bool ((< Start Start) (<= Start Start) (> Start Start) (>= Start Start)))))

(synth-fun f ((x Int) (y Int)) Int
   ((Start Int (x
                y
                0 1 -1 2 -2
                 (+ Start Start)
                 (- Start Start)
                 (ite StartBool Start Start)))
     (StartBool Bool ((and StartBool StartBool)
                      (or  StartBool StartBool)
                      (not StartBool)
                      (<=  Start Start)
                      (=   Start Start)
                      (>=  Start Start)))))

(synth-fun max5 ((x Int) (y Int) (z Int) (w Int) (u Int)) Int
    ((Start Int (x
                 y
                 z
                 w
                 u
                 0
                 1
                 (+ Start Start)
                 (- Start Start)
                 (ite StartBool Start Start)))
     (StartBool Bool ((and StartBool StartBool)
                      (or  StartBool StartBool)
                      (not StartBool)
                      (<=  Start Start)
                      (=   Start Start)
                      (>=  Start Start)))))

(synth-fun max15 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int)
                 (x6 Int) (x7 Int) (x8 Int) (x9 Int) (x10 Int)
                 (x11 Int) (x12 Int) (x13 Int) (x14 Int) (x15 Int)) Int
    ((Start Int (x1
                 x2
                 x3
                 x4
                 x5
                 x6
                 x7
                 x8
                 x9
                 x10
                 x11
                 x12
                 x13
                 x14
                 x15
                 0
                 1
                 (+ Start Start)
                 (- Start Start)
                 (ite StartBool Start Start)))
     (StartBool Bool ((and StartBool StartBool)
                      (or  StartBool StartBool)
                      (not StartBool)
                      (<=  Start Start)
                      (=   Start Start)
                      (>=  Start Start)))))

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

(define-fun findIdx ((y1 Int) (y2 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y2) 2 1)))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y3) 3 (ite (and (> k1 y1) (< k1 y2)) 1 2))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y4) 4 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 3)))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y5) 5 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 4))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y6) 6 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 5)))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y7) 7 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 (ite (and (> k1 y5) (< k1 y6)) 5 6))))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (y8 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y8) 8 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 (ite (and (> k1 y5) (< k1 y6)) 5 (ite (and (> k1 y6) (< k1 y7)) 6 7)))))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (y8 Int) (y9 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y9) 9 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 (ite (and (> k1 y5) (< k1 y6)) 5 (ite (and (> k1 y6) (< k1 y7)) 6 (ite (and (> k1 y7) (< k1 y8)) 7 8))))))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (y8 Int) (y9 Int) (y10 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y10) 10 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 (ite (and (> k1 y5) (< k1 y6)) 5 (ite (and (> k1 y6) (< k1 y7)) 6 (ite (and (> k1 y7) (< k1 y8)) 7 (ite (and (> k1 y8) (< k1 y9)) 8 9)))))))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (y8 Int) (y9 Int) (y10 Int) (y11 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y11) 11 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 (ite (and (> k1 y5) (< k1 y6)) 5 (ite (and (> k1 y6) (< k1 y7)) 6 (ite (and (> k1 y7) (< k1 y8)) 7 (ite (and (> k1 y8) (< k1 y9)) 8 (ite (and (> k1 y9) (< k1 y10)) 9 10))))))))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (y8 Int) (y9 Int) (y10 Int) (y11 Int) (y12 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y12) 12 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 (ite (and (> k1 y5) (< k1 y6)) 5 (ite (and (> k1 y6) (< k1 y7)) 6 (ite (and (> k1 y7) (< k1 y8)) 7 (ite (and (> k1 y8) (< k1 y9)) 8 (ite (and (> k1 y9) (< k1 y10)) 9 (ite (and (> k1 y10) (< k1 y11)) 10 11)))))))))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (y8 Int) (y9 Int) (y10 Int) (y11 Int) (y12 Int) (y13 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y13) 13 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 (ite (and (> k1 y5) (< k1 y6)) 5 (ite (and (> k1 y6) (< k1 y7)) 6 (ite (and (> k1 y7) (< k1 y8)) 7 (ite (and (> k1 y8) (< k1 y9)) 8 (ite (and (> k1 y9) (< k1 y10)) 9 (ite (and (> k1 y10) (< k1 y11)) 10 (ite (and (> k1 y11) (< k1 y12)) 11 12))))))))))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (y8 Int) (y9 Int) (y10 Int) (y11 Int) (y12 Int) (y13 Int) (y14 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y14) 14 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 (ite (and (> k1 y5) (< k1 y6)) 5 (ite (and (> k1 y6) (< k1 y7)) 6 (ite (and (> k1 y7) (< k1 y8)) 7 (ite (and (> k1 y8) (< k1 y9)) 8 (ite (and (> k1 y9) (< k1 y10)) 9 (ite (and (> k1 y10) (< k1 y11)) 10 (ite (and (> k1 y11) (< k1 y12)) 11 (ite (and (> k1 y12) (< k1 y13)) 12 13)))))))))))))))

(define-fun findIdx ((y1 Int) (y2 Int) (y3 Int) (y4 Int) (y5 Int) (y6 Int) (y7 Int) (y8 Int) (y9 Int) (y10 Int) (y11 Int) (y12 Int) (y13 Int) (y14 Int) (y15 Int) (k1 Int)) Int (ite (< k1 y1) 0 (ite (> k1 y15) 15 (ite (and (> k1 y1) (< k1 y2)) 1 (ite (and (> k1 y2) (< k1 y3)) 2 (ite (and (> k1 y3) (< k1 y4)) 3 (ite (and (> k1 y4) (< k1 y5)) 4 (ite (and (> k1 y5) (< k1 y6)) 5 (ite (and (> k1 y6) (< k1 y7)) 6 (ite (and (> k1 y7) (< k1 y8)) 7 (ite (and (> k1 y8) (< k1 y9)) 8 (ite (and (> k1 y9) (< k1 y10)) 9 (ite (and (> k1 y10) (< k1 y11)) 10 (ite (and (> k1 y11) (< k1 y12)) 11 (ite (and (> k1 y12) (< k1 y13)) 12 (ite (and (> k1 y13) (< k1 y14)) 13 14))))))))))))))))

(define-fun max3 ((x Int) (y Int) (z Int)) Int (ite (and (>= x y) (>= x z)) x (ite (and (>= y x) (>= y z)) y z)))

(define-fun max4 ((x Int) (y Int) (z Int) (w Int)) Int (ite (and (>= x y) (and (>= x z) (>= x w))) x (ite (and (>= y x) (and (>= y z) (>= y w))) y (ite (and (>= z x) (and (>= z y) (>= z w))) z w))))

(define-fun max5 ((x Int) (y Int) (z Int) (w Int) (u Int)) Int (ite (and (>= x y) (and (>= x z) (and (>= x w) (>= x u)))) x (ite (and (>= y x) (and (>= y z) (and (>= y w) (>= y u)))) y (ite (and (>= z x) (and (>= z y) (and (>= z w) (>= z u)))) z (ite (and (>= w x) (and (>= w y) (and (>= w z) (>= w u)))) w u)))))

(define-fun max6 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (>= x1 x6))))) x1 (ite (and (>= x2 x1) (and (>= x2 x3) (and (>= x2 x4) (and (>= x2 x5) (>= x2 x6))))) x2 (ite (and (>= x3 x1) (and (>= x3 x2) (and (>= x3 x4) (and (>= x3 x5) (>= x3 x6))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4 x5) (>= x4 x6))))) x4 (ite (and (>= x5 x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4) (>= x5 x6))))) x5 x6))))))

(define-fun max7 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int) (x7 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (and (>= x1 x6) (>= x1 x7)))))) x1 (ite (and (>= x2 x1) (and
(>= x2 x3) (and (>= x2 x4) (and (>= x2 x5) (and (>= x2 x6) (>= x2 x7)))))) x2 (ite (and (>= x3 x1) (and (>=
x3 x2) (and (>= x3 x4) (and (>= x3 x5) (and (>= x3 x6) (>= x3 x7)))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4 x5) (and (>= x4 x6) (>= x4 x7)))))) x4 (ite (and (>= x5 x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4) (and (>= x5 x6) (>= x5 x7)))))) x5 (ite (and (>= x6 x1) (and (>= x6 x2) (and
(>= x6 x3) (and (>= x6 x4) (and (>= x6 x5) (>= x6 x7)))))) x6 x7)))))))

(define-fun max8 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int) (x7 Int) (x8 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (and (>= x1 x6) (and (>= x1 x7) (>= x1 x8))))))) x1
(ite (and (>= x2 x1) (and (>= x2 x3) (and (>= x2 x4) (and (>= x2 x5) (and (>= x2 x6) (and (>= x2 x7) (>= x2
x8))))))) x2 (ite (and (>= x3 x1) (and (>= x3 x2) (and (>= x3 x4) (and (>= x3 x5) (and (>= x3 x6) (and (>= x3 x7) (>= x3 x8))))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4 x5) (and (>= x4 x6) (and (>= x4 x7) (>= x4 x8))))))) x4 (ite (and (>= x5 x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4)
(and (>= x5 x6) (and (>= x5 x7) (>= x5 x8))))))) x5 (ite (and (>= x6 x1) (and (>= x6 x2) (and (>= x6 x3) (and (>= x6 x4) (and (>= x6 x5) (and (>= x6 x7) (>= x6 x8))))))) x6 (ite (and (>= x7 x1) (and (>= x7 x2) (and (>= x7 x3) (and (>= x7 x4) (and (>= x7 x5) (and (>= x7 x6) (>= x7 x8))))))) x7 x8))))))))

(define-fun max9 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int) (x7 Int) (x8 Int) (x9 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (and (>= x1 x6) (and (>= x1 x7) (and (>= x1 x8) (>= x1 x9)))))))) x1 (ite (and (>= x2 x1) (and (>= x2 x3) (and (>= x2 x4) (and (>= x2 x5) (and (>= x2 x6) (and (>= x2 x7) (and (>= x2 x8) (>= x2 x9)))))))) x2 (ite (and (>= x3 x1) (and (>= x3 x2) (and (>= x3 x4) (and (>= x3 x5) (and (>= x3 x6) (and (>= x3 x7) (and (>= x3 x8) (>= x3 x9)))))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4 x5) (and (>= x4 x6) (and (>= x4 x7) (and (>= x4 x8) (>= x4 x9)))))))) x4 (ite (and (>= x5 x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4) (and (>= x5 x6) (and (>= x5 x7) (and (>= x5 x8) (>= x5 x9)))))))) x5 (ite (and (>= x6 x1) (and (>= x6 x2) (and (>= x6 x3) (and (>= x6 x4) (and (>= x6 x5) (and (>= x6 x7) (and (>= x6 x8) (>= x6 x9)))))))) x6 (ite (and (>= x7 x1) (and (>= x7 x2) (and (>= x7 x3) (and (>= x7 x4) (and (>= x7 x5) (and (>= x7 x6) (and (>= x7 x8) (>= x7 x9)))))))) x7 (ite (and
(>= x8 x1) (and (>= x8 x2) (and (>= x8 x3) (and (>= x8 x4) (and (>= x8 x5) (and (>= x8 x6) (and (>= x8 x7) (>= x8 x9)))))))) x8 x9)))))))))

(define-fun max10 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int) (x7 Int) (x8 Int) (x9 Int) (x10 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (and (>= x1 x6) (and (>= x1 x7)
(and (>= x1 x8) (and (>= x1 x9) (>= x1 x10))))))))) x1 (ite (and (>= x2 x1) (and (>= x2 x3) (and (>= x2 x4)
(and (>= x2 x5) (and (>= x2 x6) (and (>= x2 x7) (and (>= x2 x8) (and (>= x2 x9) (>= x2 x10))))))))) x2 (ite
(and (>= x3 x1) (and (>= x3 x2) (and (>= x3 x4) (and (>= x3 x5) (and (>= x3 x6) (and (>= x3 x7) (and (>= x3
x8) (and (>= x3 x9) (>= x3 x10))))))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4
x5) (and (>= x4 x6) (and (>= x4 x7) (and (>= x4 x8) (and (>= x4 x9) (>= x4 x10))))))))) x4 (ite (and (>= x5
x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4) (and (>= x5 x6) (and (>= x5 x7) (and (>= x5 x8) (and (>= x5 x9) (>= x5 x10))))))))) x5 (ite (and (>= x6 x1) (and (>= x6 x2) (and (>= x6 x3) (and (>= x6 x4) (and (>= x6 x5) (and (>= x6 x7) (and (>= x6 x8) (and (>= x6 x9) (>= x6 x10))))))))) x6 (ite (and (>= x7 x1) (and (>= x7 x2) (and (>= x7 x3) (and (>= x7 x4) (and (>= x7 x5) (and (>= x7 x6) (and (>= x7 x8) (and (>= x7 x9) (>=
x7 x10))))))))) x7 (ite (and (>= x8 x1) (and (>= x8 x2) (and (>= x8 x3) (and (>= x8 x4) (and (>= x8 x5) (and (>= x8 x6) (and (>= x8 x7) (and (>= x8 x9) (>= x8 x10))))))))) x8 (ite (and (>= x9 x1) (and (>= x9 x2) (and (>= x9 x3) (and (>= x9 x4) (and (>= x9 x5) (and (>= x9 x6) (and (>= x9 x7) (and (>= x9 x8) (>= x9 x10))))))))) x9 x10))))))))))

(define-fun max11 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int) (x7 Int) (x8 Int) (x9 Int) (x10 Int) (x11 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (and (>= x1 x6) (and (>= x1 x7) (and (>= x1 x8) (and (>= x1 x9) (and (>= x1 x10) (>= x1 x11)))))))))) x1 (ite (and (>= x2 x1) (and (>= x2 x3) (and (>= x2 x4) (and (>= x2 x5) (and (>= x2 x6) (and (>= x2 x7) (and (>= x2 x8) (and (>= x2 x9)
(and (>= x2 x10) (>= x2 x11)))))))))) x2 (ite (and (>= x3 x1) (and (>= x3 x2) (and (>= x3 x4) (and (>= x3 x5) (and (>= x3 x6) (and (>= x3 x7) (and (>= x3 x8) (and (>= x3 x9) (and (>= x3 x10) (>= x3 x11)))))))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4 x5) (and (>= x4 x6) (and (>= x4 x7) (and (>= x4 x8) (and (>= x4 x9) (and (>= x4 x10) (>= x4 x11)))))))))) x4 (ite (and (>= x5 x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4) (and (>= x5 x6) (and (>= x5 x7) (and (>= x5 x8) (and (>= x5 x9) (and (>= x5 x10) (>= x5 x11)))))))))) x5 (ite (and (>= x6 x1) (and (>= x6 x2) (and (>= x6 x3) (and (>= x6 x4) (and (>= x6 x5)
(and (>= x6 x7) (and (>= x6 x8) (and (>= x6 x9) (and (>= x6 x10) (>= x6 x11)))))))))) x6 (ite (and (>= x7 x1) (and (>= x7 x2) (and (>= x7 x3) (and (>= x7 x4) (and (>= x7 x5) (and (>= x7 x6) (and (>= x7 x8) (and (>= x7 x9) (and (>= x7 x10) (>= x7 x11)))))))))) x7 (ite (and (>= x8 x1) (and (>= x8 x2) (and (>= x8 x3) (and (>= x8 x4) (and (>= x8 x5) (and (>= x8 x6) (and (>= x8 x7) (and (>= x8 x9) (and (>= x8 x10) (>= x8 x11)))))))))) x8 (ite (and (>= x9 x1) (and (>= x9 x2) (and (>= x9 x3) (and (>= x9 x4) (and (>= x9 x5) (and (>= x9 x6) (and (>= x9 x7) (and (>= x9 x8) (and (>= x9 x10) (>= x9 x11)))))))))) x9 (ite (and (>= x10 x1) (and (>= x10 x2) (and (>= x10 x3) (and (>= x10 x4) (and (>= x10 x5) (and (>= x10 x6) (and (>= x10 x7) (and (>= x10 x8) (and (>= x10 x9) (>= x10 x11)))))))))) x10 x11)))))))))))

(define-fun max12 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int) (x7 Int) (x8 Int) (x9 Int) (x10 Int) (x11 Int) (x12 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (and (>= x1
x6) (and (>= x1 x7) (and (>= x1 x8) (and (>= x1 x9) (and (>= x1 x10) (and (>= x1 x11) (>= x1 x12)))))))))))
x1 (ite (and (>= x2 x1) (and (>= x2 x3) (and (>= x2 x4) (and (>= x2 x5) (and (>= x2 x6) (and (>= x2 x7) (and (>= x2 x8) (and (>= x2 x9) (and (>= x2 x10) (and (>= x2 x11) (>= x2 x12))))))))))) x2 (ite (and (>= x3 x1)
(and (>= x3 x2) (and (>= x3 x4) (and (>= x3 x5) (and (>= x3 x6) (and (>= x3 x7) (and (>= x3 x8) (and (>= x3
x9) (and (>= x3 x10) (and (>= x3 x11) (>= x3 x12))))))))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4 x5) (and (>= x4 x6) (and (>= x4 x7) (and (>= x4 x8) (and (>= x4 x9) (and (>= x4 x10) (and (>= x4 x11) (>= x4 x12))))))))))) x4 (ite (and (>= x5 x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4)
(and (>= x5 x6) (and (>= x5 x7) (and (>= x5 x8) (and (>= x5 x9) (and (>= x5 x10) (and (>= x5 x11) (>= x5 x12))))))))))) x5 (ite (and (>= x6 x1) (and (>= x6 x2) (and (>= x6 x3) (and (>= x6 x4) (and (>= x6 x5) (and (>= x6 x7) (and (>= x6 x8) (and (>= x6 x9) (and (>= x6 x10) (and (>= x6 x11) (>= x6 x12))))))))))) x6 (ite (and (>= x7 x1) (and (>= x7 x2) (and (>= x7 x3) (and (>= x7 x4) (and (>= x7 x5) (and (>= x7 x6) (and (>= x7 x8)
(and (>= x7 x9) (and (>= x7 x10) (and (>= x7 x11) (>= x7 x12))))))))))) x7 (ite (and (>= x8 x1) (and (>= x8
x2) (and (>= x8 x3) (and (>= x8 x4) (and (>= x8 x5) (and (>= x8 x6) (and (>= x8 x7) (and (>= x8 x9) (and (>= x8 x10) (and (>= x8 x11) (>= x8 x12))))))))))) x8 (ite (and (>= x9 x1) (and (>= x9 x2) (and (>= x9 x3) (and (>= x9 x4) (and (>= x9 x5) (and (>= x9 x6) (and (>= x9 x7) (and (>= x9 x8) (and (>= x9 x10) (and (>= x9 x11) (>= x9 x12))))))))))) x9 (ite (and (>= x10 x1) (and (>= x10 x2) (and (>= x10 x3) (and (>= x10 x4) (and (>= x10 x5) (and (>= x10 x6) (and (>= x10 x7) (and (>= x10 x8) (and (>= x10 x9) (and (>= x10 x11) (>= x10 x12))))))))))) x10 (ite (and (>= x11 x1) (and (>= x11 x2) (and (>= x11 x3) (and (>= x11 x4) (and (>= x11 x5) (and (>= x11 x6) (and (>= x11 x7) (and (>= x11 x8) (and (>= x11 x9) (and (>= x11 x10) (>= x11 x12))))))))))) x11 x12))))))))))))

(define-fun max13 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int) (x7 Int) (x8 Int) (x9 Int) (x10 Int) (x11 Int) (x12 Int) (x13 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (and (>= x1 x6) (and (>= x1 x7) (and (>= x1 x8) (and (>= x1 x9) (and (>= x1 x10) (and (>= x1 x11) (and (>= x1
x12) (>= x1 x13)))))))))))) x1 (ite (and (>= x2 x1) (and (>= x2 x3) (and (>= x2 x4) (and (>= x2 x5) (and (>= x2 x6) (and (>= x2 x7) (and (>= x2 x8) (and (>= x2 x9) (and (>= x2 x10) (and (>= x2 x11) (and (>= x2 x12) (>= x2 x13)))))))))))) x2 (ite (and (>= x3 x1) (and (>= x3 x2) (and (>= x3 x4) (and (>= x3 x5) (and (>= x3 x6) (and (>= x3 x7) (and (>= x3 x8) (and (>= x3 x9) (and (>= x3 x10) (and (>= x3 x11) (and (>= x3 x12) (>= x3
x13)))))))))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4 x5) (and (>= x4 x6) (and (>= x4 x7) (and (>= x4 x8) (and (>= x4 x9) (and (>= x4 x10) (and (>= x4 x11) (and (>= x4 x12) (>= x4 x13)))))))))))) x4 (ite (and (>= x5 x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4) (and (>= x5 x6) (and (>= x5 x7) (and (>= x5 x8) (and (>= x5 x9) (and (>= x5 x10) (and (>= x5 x11) (and (>= x5 x12) (>= x5 x13)))))))))))) x5 (ite (and (>= x6 x1) (and (>= x6 x2) (and (>= x6 x3) (and (>= x6 x4) (and (>= x6 x5) (and (>= x6 x7)
(and (>= x6 x8) (and (>= x6 x9) (and (>= x6 x10) (and (>= x6 x11) (and (>= x6 x12) (>= x6 x13)))))))))))) x6 (ite (and (>= x7 x1) (and (>= x7 x2) (and (>= x7 x3) (and (>= x7 x4) (and (>= x7 x5) (and (>= x7 x6) (and (>= x7 x8) (and (>= x7 x9) (and (>= x7 x10) (and (>= x7 x11) (and (>= x7 x12) (>= x7 x13)))))))))))) x7 (ite
(and (>= x8 x1) (and (>= x8 x2) (and (>= x8 x3) (and (>= x8 x4) (and (>= x8 x5) (and (>= x8 x6) (and (>= x8
x7) (and (>= x8 x9) (and (>= x8 x10) (and (>= x8 x11) (and (>= x8 x12) (>= x8 x13)))))))))))) x8 (ite (and (>= x9 x1) (and (>= x9 x2) (and (>= x9 x3) (and (>= x9 x4) (and (>= x9 x5) (and (>= x9 x6) (and (>= x9 x7) (and (>= x9 x8) (and (>= x9 x10) (and (>= x9 x11) (and (>= x9 x12) (>= x9 x13)))))))))))) x9 (ite (and (>= x10 x1) (and (>= x10 x2) (and (>= x10 x3) (and (>= x10 x4) (and (>= x10 x5) (and (>= x10 x6) (and (>= x10 x7) (and (>= x10 x8) (and (>= x10 x9) (and (>= x10 x11) (and (>= x10 x12) (>= x10 x13)))))))))))) x10 (ite (and (>= x11 x1) (and (>= x11 x2) (and (>= x11 x3) (and (>= x11 x4) (and (>= x11 x5) (and (>= x11 x6) (and (>= x11 x7) (and (>= x11 x8) (and (>= x11 x9) (and (>= x11 x10) (and (>= x11 x12) (>= x11 x13)))))))))))) x11 (ite
(and (>= x12 x1) (and (>= x12 x2) (and (>= x12 x3) (and (>= x12 x4) (and (>= x12 x5) (and (>= x12 x6) (and (>= x12 x7) (and (>= x12 x8) (and (>= x12 x9) (and (>= x12 x10) (and (>= x12 x11) (>= x12 x13)))))))))))) x12 x13)))))))))))))

(define-fun max14 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int) (x7 Int) (x8 Int) (x9 Int) (x10 Int) (x11 Int) (x12 Int) (x13 Int) (x14 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (and (>= x1 x6) (and (>= x1 x7) (and (>= x1 x8) (and (>= x1 x9) (and (>= x1 x10) (and (>= x1 x11) (and (>= x1 x12) (and (>= x1 x13) (>= x1 x14))))))))))))) x1 (ite (and (>= x2 x1) (and (>= x2 x3) (and (>= x2
x4) (and (>= x2 x5) (and (>= x2 x6) (and (>= x2 x7) (and (>= x2 x8) (and (>= x2 x9) (and (>= x2 x10) (and (>= x2 x11) (and (>= x2 x12) (and (>= x2 x13) (>= x2 x14))))))))))))) x2 (ite (and (>= x3 x1) (and (>= x3 x2)
(and (>= x3 x4) (and (>= x3 x5) (and (>= x3 x6) (and (>= x3 x7) (and (>= x3 x8) (and (>= x3 x9) (and (>= x3
x10) (and (>= x3 x11) (and (>= x3 x12) (and (>= x3 x13) (>= x3 x14))))))))))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4 x5) (and (>= x4 x6) (and (>= x4 x7) (and (>= x4 x8) (and (>= x4 x9)
(and (>= x4 x10) (and (>= x4 x11) (and (>= x4 x12) (and (>= x4 x13) (>= x4 x14))))))))))))) x4 (ite (and (>= x5 x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4) (and (>= x5 x6) (and (>= x5 x7) (and (>= x5 x8) (and (>= x5 x9) (and (>= x5 x10) (and (>= x5 x11) (and (>= x5 x12) (and (>= x5 x13) (>= x5 x14))))))))))))) x5 (ite (and (>= x6 x1) (and (>= x6 x2) (and (>= x6 x3) (and (>= x6 x4) (and (>= x6 x5) (and (>= x6 x7) (and (>= x6 x8) (and (>= x6 x9) (and (>= x6 x10) (and (>= x6 x11) (and (>= x6 x12) (and (>= x6 x13) (>= x6 x14))))))))))))) x6 (ite (and (>= x7 x1) (and (>= x7 x2) (and (>= x7 x3) (and (>= x7 x4) (and (>= x7 x5) (and (>= x7
x6) (and (>= x7 x8) (and (>= x7 x9) (and (>= x7 x10) (and (>= x7 x11) (and (>= x7 x12) (and (>= x7 x13) (>=
x7 x14))))))))))))) x7 (ite (and (>= x8 x1) (and (>= x8 x2) (and (>= x8 x3) (and (>= x8 x4) (and (>= x8 x5)
(and (>= x8 x6) (and (>= x8 x7) (and (>= x8 x9) (and (>= x8 x10) (and (>= x8 x11) (and (>= x8 x12) (and (>=
x8 x13) (>= x8 x14))))))))))))) x8 (ite (and (>= x9 x1) (and (>= x9 x2) (and (>= x9 x3) (and (>= x9 x4) (and (>= x9 x5) (and (>= x9 x6) (and (>= x9 x7) (and (>= x9 x8) (and (>= x9 x10) (and (>= x9 x11) (and (>= x9 x12) (and (>= x9 x13) (>= x9 x14))))))))))))) x9 (ite (and (>= x10 x1) (and (>= x10 x2) (and (>= x10 x3) (and
(>= x10 x4) (and (>= x10 x5) (and (>= x10 x6) (and (>= x10 x7) (and (>= x10 x8) (and (>= x10 x9) (and (>= x10 x11) (and (>= x10 x12) (and (>= x10 x13) (>= x10 x14))))))))))))) x10 (ite (and (>= x11 x1) (and (>= x11 x2) (and (>= x11 x3) (and (>= x11 x4) (and (>= x11 x5) (and (>= x11 x6) (and (>= x11 x7) (and (>= x11 x8) (and (>= x11 x9) (and (>= x11 x10) (and (>= x11 x12) (and (>= x11 x13) (>= x11 x14))))))))))))) x11 (ite (and (>= x12 x1) (and (>= x12 x2) (and (>= x12 x3) (and (>= x12 x4) (and (>= x12 x5) (and (>= x12 x6) (and (>= x12 x7) (and (>= x12 x8) (and (>= x12 x9) (and (>= x12 x10) (and (>= x12 x11) (and (>= x12 x13) (>= x12 x14))))))))))))) x12 (ite (and (>= x13 x1) (and (>= x13 x2) (and (>= x13 x3) (and (>= x13 x4) (and (>= x13 x5) (and (>= x13 x6) (and (>= x13 x7) (and (>= x13 x8) (and (>= x13 x9) (and (>= x13 x10) (and (>= x13 x11) (and (>= x13 x12) (>= x13 x14))))))))))))) x13 x14))))))))))))))

(define-fun max15 ((x1 Int) (x2 Int) (x3 Int) (x4 Int) (x5 Int) (x6 Int) (x7 Int) (x8 Int) (x9 Int) (x10 Int) (x11 Int) (x12 Int) (x13 Int) (x14 Int) (x15 Int)) Int (ite (and (>= x1 x2) (and (>= x1 x3) (and (>= x1 x4) (and (>= x1 x5) (and (>= x1 x6) (and (>= x1 x7) (and (>= x1 x8) (and (>= x1 x9) (and (>= x1 x10) (and (>=
x1 x11) (and (>= x1 x12) (and (>= x1 x13) (>= x1 x14))))))))))))) x1 (ite (and (>= x2 x1) (and (>= x2 x3) (and (>= x2 x4) (and (>= x2 x5) (and (>= x2 x6) (and (>= x2 x7) (and (>= x2 x8) (and (>= x2 x9) (and (>= x2 x10) (and (>= x2 x11) (and (>= x2 x12) (and (>= x2 x13) (>= x2 x14))))))))))))) x2 (ite (and (>= x3 x1) (and (>= x3 x2) (and (>= x3 x4) (and (>= x3 x5) (and (>= x3 x6) (and (>= x3 x7) (and (>= x3 x8) (and (>= x3 x9) (and (>= x3 x10) (and (>= x3 x11) (and (>= x3 x12) (and (>= x3 x13) (>= x3 x14))))))))))))) x3 (ite (and (>= x4 x1) (and (>= x4 x2) (and (>= x4 x3) (and (>= x4 x5) (and (>= x4 x6) (and (>= x4 x7) (and (>= x4 x8) (and (>= x4 x9) (and (>= x4 x10) (and (>= x4 x11) (and (>= x4 x12) (and (>= x4 x13) (>= x4 x14))))))))))))) x4 (ite (and (>= x5 x1) (and (>= x5 x2) (and (>= x5 x3) (and (>= x5 x4) (and (>= x5 x6) (and (>= x5 x7) (and (>= x5 x8) (and (>= x5 x9) (and (>= x5 x10) (and (>= x5 x11) (and (>= x5 x12) (and (>= x5 x13) (>= x5 x14))))))))))))) x5 (ite (and (>= x6 x1) (and (>= x6 x2) (and (>= x6 x3) (and (>= x6 x4) (and (>= x6 x5) (and (>= x6 x7) (and (>= x6 x8) (and (>= x6 x9) (and (>= x6 x10) (and (>= x6 x11) (and (>= x6 x12) (and (>= x6 x13) (>= x6 x14))))))))))))) x6 (ite (and (>= x7 x1) (and (>= x7 x2) (and (>= x7 x3) (and (>= x7 x4) (and (>= x7 x5) (and (>= x7 x6) (and (>= x7 x8) (and (>= x7 x9) (and (>= x7 x10) (and (>= x7 x11) (and (>= x7 x12) (and (>= x7 x13) (>= x7 x14))))))))))))) x7 (ite (and (>= x8 x1) (and (>= x8 x2) (and (>= x8 x3) (and (>= x8 x4) (and (>= x8 x5) (and (>= x8 x6) (and (>= x8 x7) (and (>= x8 x9) (and (>= x8 x10) (and (>= x8 x11) (and (>= x8 x12) (and (>= x8 x13) (>= x8 x14))))))))))))) x8 (ite (and (>= x9 x1) (and (>= x9 x2) (and (>= x9 x3) (and (>= x9 x4) (and (>= x9 x5) (and (>= x9 x6) (and (>= x9 x7) (and (>= x9 x8) (and (>= x9 x10) (and (>= x9 x11) (and (>= x9 x12) (and (>= x9 x13) (>= x9 x14))))))))))))) x9 (ite (and (>= x10 x1) (and (>= x10 x2) (and (>= x10 x3) (and (>= x10 x4) (and (>= x10 x5) (and (>= x10 x6) (and (>= x10 x7) (and (>= x10 x8) (and (>= x10 x9) (and (>= x10 x11) (and (>= x10 x12) (and (>= x10 x13) (>= x10 x14))))))))))))) x10 (ite (and (>= x11 x1) (and (>= x11 x2) (and (>= x11 x3) (and (>= x11 x4) (and (>= x11 x5) (and (>= x11 x6) (and (>= x11 x7) (and (>= x11 x8) (and (>= x11 x9) (and (>= x11 x10) (and (>= x11 x12) (and (>= x11 x13) (>= x11 x14))))))))))))) x11 (ite (and (>= x12 x1) (and (>= x12 x2) (and (>= x12 x3) (and (>= x12 x4) (and (>= x12 x5) (and (>= x12 x6) (and (>= x12 x7) (and (>= x12 x8) (and (>= x12 x9) (and (>= x12 x10) (and (>= x12 x11) (and (>= x12 x13) (>= x12 x14))))))))))))) x12 (ite (and (>= x13 x1) (and (>= x13 x2) (and (>= x13 x3) (and (>= x13 x4) (and (>= x13 x5) (and (>= x13 x6) (and (>= x13 x7) (and (>= x13 x8) (and (>= x13 x9) (and (>= x13 x10) (and (>= x13 x11) (and (>= x13 x12) (>= x13 x14))))))))))))) x13 x14))))))))))))))

(define-fun f ((x Int)) Int (ite (> x 5) x (ite (= x 0) 0 (ite (= x 1) 10 (ite (= x 2) 20 (ite (= x 3) 30 (ite (= x 4) 40 50)))))))

(define-fun f ((x Int) (y Int)) Int (ite (= x y) 0 (ite (> x y) 1 -1)))

(define-fun f ((x Int) (y Int)) Int (ite (= x y) (+ x y) (ite (> x y) 1 -1)))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (if0 (bvand #x0000000000000001 (shr4 x)) (bvor x (shr16 x)) (shl1 (bvand x (shl1 x)))))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (shr16 x))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (if0 (bvand #x0000000000000001 (shr4 x)) (shl1 (bvnot x)) (bvand x (shr16 x))))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (if0 (bvand #x0000000000000001 bvnot x)) #x0000000000000000 (shr16 (shr4 (shr4 x))))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (if0 (bvand #x0000000000000001 x) (shr1 x) (shl1 x)))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (if0 (bvand #x0000000000000001 (shr16 (bvnot x))) (bvor x (bvnot #x0000000000000001)) (bvadd #x0000000000000001 (shr4 (shl1 x)))))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (let ((_let_1 (bvnot x))) (let ((_let_2 (bvand #x0000000000000001 _let_1))) (let ((_let_3 (bvadd #x0000000000000001 (shr16 x)))) (let ((_let_4 (bvand #x0000000000000001 (shr4 (shl1 x))))) (let ((_let_5 (if0 _let_4 _let_3 _let_2))) (let ((_let_6 (if0 _let_4 _let_3 #x0000000000000001))) (let ((_let_7 (if0 _let_4 _let_3 #x0000000000000001))) (let ((_let_8 (bvand #x0000000000000001 (shr16 _let_1)))) (if0 (bvand #x0000000000000001 (shr1 _let_1)) (if0 _let_8 _let_5 (if0 _let_2 _let_6 _let_7)) (if0 _let_8 (if0 (bvand #x0000000000000001 x) _let_7 _let_6) _let_5)))))))))))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (let ((_let_1 (shl1 #x0000000000000001))) (if0 (bvand #x0000000000000001 x) (bvnot _let_1) _let_1)))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (let ((_let_1 (shr4 x))) (if0 (bvand #x0000000000000001 (bvor x _let_1)) (if0 (bvand #x0000000000000001 _let_1) (shl1 (if0 (bvand #x0000000000000001 x) x #x0000000000000000)) (bvand x (shl1 (shr16 x)))) (shl1 x))))

(define-fun f ((x (_ BitVec 64))) (_ BitVec 64) (let ((_let_1 (shr1 x))) (let ((_let_2 (shr16 _let_1))) (let ((_let_3 (bvadd #x0000000000000001 _let_2))) (let ((_let_4 (shl1 x))) (let ((_let_5 (bvadd x (shr1 _let_4)))) (let ((_let_6 (shr16 x))) (let ((_let_7 (bvand #x0000000000000001 _let_1))) (let ((_let_8 (bvand #x0000000000000001 (shr1 (bvadd #x0000000000000001 x))))) (let ((_let_9 (bvnot x))) (let ((_let_10 (shr16 _let_9))) (let ((_let_11 (bvand #x0000000000000001 _let_10))) (let ((_let_12 (shr4 _let_9))) (let ((_let_13 (bvand #x0000000000000001 _let_12))) (let ((_let_14 (bvand #x0000000000000001 (shr16 _let_10)))) (let ((_let_15 (shr4 x))) (let ((_let_16 (bvand #x0000000000000001 _let_2))) (let ((_let_17 (bvand #x0000000000000001 (shr16 _let_4)))) (let ((_let_18 (bvand #x0000000000000001 (shr4 _let_15)))) (let ((_let_19 (bvand #x0000000000000001 (shr4 _let_1)))) (let ((_let_20 (bvand #x0000000000000001 (shr16 _let_15)))) (let ((_let_21 (shr1 _let_9))) (let ((_let_22 (bvand #x0000000000000001 _let_9))) (let ((_let_23 (bvand #x0000000000000001 _let_15))) (let ((_let_24 (bvand #x0000000000000001 _let_21))) (if0 (bvand #x0000000000000001 (shr4 (shl1 _let_9))) (if0 _let_19 (if0 _let_14 (if0 _let_11 (if0 _let_13 (if0 _let_22 (if0 _let_18 (if0 _let_20 _let_5 _let_3) (if0 _let_7 _let_4 _let_3)) (if0 _let_16 (if0 _let_24 _let_3 _let_5) _let_3)) (if0 _let_20 (if0 _let_16 _let_5 _let_3) _let_5)) (if0 _let_17 (if0 _let_22 _let_3 _let_5) _let_3)) (if0 _let_23 _let_5 (if0 _let_24 _let_3 (if0 (bvand #x0000000000000001 _let_6) _let_3 _let_5)))) (if0 _let_14 (if0 _let_11 (if0 _let_23 (if0 (bvand #x0000000000000001 (bvor x _let_1)) _let_3 (if0 _let_18 _let_3 _let_5)) _let_3) (if0 _let_13 (if0 _let_22 _let_4 _let_3) (if0 (bvand #x0000000000000001 (shr16 _let_21)) (if0 _let_8 _let_3 _let_4) _let_5))) (if0 _let_11 _let_3 (if0 _let_13 (if0 _let_18 (if0 (bvand #x0000000000000001 (bvand x _let_1)) _let_5 (if0 _let_20 _let_4 _let_3)) (if0 (bvand #x0000000000000001 (bvor x _let_15)) _let_3 _let_5)) _let_5)))) (if0 _let_19 (if0 _let_14 (if0 _let_11 (if0 _let_18 (if0 _let_7 (if0 _let_17 _let_3 _let_5) _let_3) (if0 _let_16 (if0 (bvand #x0000000000000001 x) _let_5 _let_3) _let_4)) (if0 (bvand #x0000000000000001 (bvadd x _let_15)) _let_5 (if0 _let_7 _let_3 _let_4))) (if0 _let_7 (if0 (shr4 (bvxor x (bvadd #x0000000000000001 (bvor #x0000000000000001 x)))) _let_3 _let_4) _let_5)) (if0 _let_14 (if0 _let_11 (if0 _let_13 (if0 _let_7 _let_5 (if0 (bvand #x0000000000000001 (shr4 _let_12)) _let_3 _let_4)) (if0 (shr1 (bvxor x (bvadd #x0000000000000001 (bvxor #x0000000000000001 x)))) _let_4 _let_3)) _let_4) (if0 _let_11 (if0 _let_8 _let_5 (if0 (bvand #x0000000000000001 (shr4 (shr4 _let_4))) _let_3 _let_5)) (if0 _let_7 (if0 (bvand #x0000000000000001 (bvadd x _let_6)) (if0 (bvand #x0000000000000001 (shr1 _let_1)) _let_3 _let_5) _let_5) _let_3))))))))))))))))))))))))))))))
