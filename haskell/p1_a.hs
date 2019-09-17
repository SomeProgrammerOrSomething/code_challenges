-- [ i | i `mod` 15 == 0 || i `mod` 3 == 0 || i `mod` 5 == 0]

isMul3 :: Int -> Bool
isMul3 x = (x `mod` 3 ) == 0

isMul5 :: Int -> Bool
isMul5 x = (x `mod` 5) == 0

isMul15 :: Int -> Bool
isMul15 x = (x `mod` 15 ) == 0

isFiltered :: Int -> Bool
isFiltered x = isMul3 x || isMul5 x || isMul15 x

value = sum $ filter (isFiltered) [ 1..1000]