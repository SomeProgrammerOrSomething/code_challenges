fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
val' = takeWhile (<4000000) fibs
val'' = filter even val'
val''' = sum val''
val = sum $ filter even $ takeWhile (<4000000) fibs