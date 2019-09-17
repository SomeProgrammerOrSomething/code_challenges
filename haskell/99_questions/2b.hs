-- Find the last but one element of a list.

myButLast :: [a] -> a
myButLast [] = error "Does not work for empty list."
myButLast [_] = error "Does not work for singletons."
myButLast [x,_] = x
myButLast (_:y:xs) = myButLast (y:xs)