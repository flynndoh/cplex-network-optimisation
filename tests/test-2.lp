Minimize
  obj:  r

Subject To
  demflow111:  2 x111 - 3 bin111 = 0
  demflow112:  2 x112 - 4 bin112 = 0
  demflow113:  2 x113 - 5 bin113 = 0
  demflow114:  2 x114 - 6 bin114 = 0
  demflow121:  2 x121 - 3 bin121 = 0
  demflow122:  2 x122 - 4 bin122 = 0
  demflow123:  2 x123 - 5 bin123 = 0
  demflow124:  2 x124 - 6 bin124 = 0
  demflow211:  2 x211 - 5 bin211 = 0
  demflow212:  2 x212 - 6 bin212 = 0
  demflow213:  2 x213 - 7 bin213 = 0
  demflow214:  2 x214 - 8 bin214 = 0
  demflow221:  2 x221 - 5 bin221 = 0
  demflow222:  2 x222 - 6 bin222 = 0
  demflow223:  2 x223 - 7 bin223 = 0
  demflow224:  2 x224 - 8 bin224 = 0
  demflow311:  2 x311 - 7 bin311 = 0
  demflow312:  2 x312 - 8 bin312 = 0
  demflow313:  2 x313 - 9 bin313 = 0
  demflow314:  2 x314 - 10 bin314 = 0
  demflow321:  2 x321 - 7 bin321 = 0
  demflow322:  2 x322 - 8 bin322 = 0
  demflow323:  2 x323 - 9 bin323 = 0
  demflow324:  2 x324 - 10 bin324 = 0
  srccap11:    x111 + x112 + x113 + x114 - c11 <= 0
  srccap12:    x121 + x122 + x123 + x124 - c12 <= 0
  srccap21:    x211 + x212 + x213 + x214 - c21 <= 0
  srccap22:    x221 + x222 + x223 + x224 - c22 <= 0
  srccap31:    x311 + x312 + x313 + x314 - c31 <= 0
  srccap32:    x321 + x322 + x323 + x324 - c32 <= 0
  transload1:  x111 + x112 + x113 + x114 + x211 + x212 + x213 + x214 + x311 + x312 + x313 + x314 - r <= 0
  transload2:  x121 + x122 + x123 + x124 + x221 + x222 + x223 + x224 + x321 + x322 + x323 + x324 - r <= 0
  destcap11:   x111 + x211 + x311 - d11 <= 0
  destcap12:   x112 + x212 + x312 - d12 <= 0
  destcap13:   x113 + x213 + x313 - d13 <= 0
  destcap14:   x114 + x214 + x314 - d14 <= 0
  destcap21:   x121 + x221 + x321 - d21 <= 0
  destcap22:   x122 + x222 + x322 - d22 <= 0
  destcap23:   x123 + x223 + x323 - d23 <= 0
  destcap24:   x124 + x224 + x324 - d24 <= 0
  dmndvol11:   x111 + x121 = 3
  dmndvol12:   x112 + x122 = 4
  dmndvol13:   x113 + x123 = 5
  dmndvol14:   x114 + x124 = 6
  dmndvol21:   x211 + x221 = 5
  dmndvol22:   x212 + x222 = 6
  dmndvol23:   x213 + x223 = 7
  dmndvol24:   x214 + x224 = 8
  dmndvol31:   x311 + x321 = 7
  dmndvol32:   x312 + x322 = 8
  dmndvol33:   x313 + x323 = 9
  dmndvol34:   x314 + x324 = 10
  util11:      bin111 + bin121 = 2
  util12:      bin112 + bin122 = 2
  util13:      bin113 + bin123 = 2
  util14:      bin114 + bin124 = 2
  util21:      bin211 + bin221 = 2
  util22:      bin212 + bin222 = 2
  util23:      bin213 + bin223 = 2
  util24:      bin214 + bin224 = 2
  util31:      bin311 + bin321 = 2
  util32:      bin312 + bin322 = 2
  util33:      bin313 + bin323 = 2
  util34:      bin314 + bin324 = 2

Bounds
  x111 >= 0
  x112 >= 0
  x113 >= 0
  x114 >= 0
  x121 >= 0
  x122 >= 0
  x123 >= 0
  x124 >= 0
  x211 >= 0
  x212 >= 0
  x213 >= 0
  x214 >= 0
  x221 >= 0
  x222 >= 0
  x223 >= 0
  x224 >= 0
  x311 >= 0
  x312 >= 0
  x313 >= 0
  x314 >= 0
  x321 >= 0
  x322 >= 0
  x323 >= 0
  x324 >= 0
  c11  >= 0
  c12  >= 0
  c21  >= 0
  c22  >= 0
  c31  >= 0
  c32  >= 0
  d11  >= 0
  d12  >= 0
  d13  >= 0
  d14  >= 0
  d21  >= 0
  d22  >= 0
  d23  >= 0
  d24  >= 0
  r    >= 0

Binaries
  bin111  bin112  bin113  bin114
  bin121  bin122  bin123  bin124
  bin211  bin212  bin213  bin214
  bin221  bin222  bin223  bin224
  bin311  bin312  bin313  bin314
  bin321  bin322  bin323  bin324

End
