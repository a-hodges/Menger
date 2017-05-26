menger :: Int -> [[Boo ]
menger 0 = [[True]]
menger n
    | n < 0 = error "Invalid size."
    | n > 0 = collate 0 0 [] (menger(n-1))
        where
            collate :: Int -> Int -> [[Bool]] -> [[Bool]] -> [[Bool]]
            collate r x grid prev
                | x >= 3 = grid
                | r >= length(prev) = collate 0 (x+1) grid prev
                | otherwise = collate (r+1) x (grid++[collateRow x (prev!!r)]) prev
                    where
                        collateRow :: Int -> [Bool] -> [Bool]
                        collateRow x prev
                            | x `mod` 3 == 1 = prev ++ (replicate (length prev) False) ++ prev
                            | otherwise = prev ++ prev ++ prev

showMenger :: [[Bool]] -> String
showMenger m = mengerStr "" m
    where
        mengerStr :: String -> [[Bool]] -> String
        mengerStr str [] = str
        mengerStr str (x:xs) = mengerStr (str++(mengerLine "" x)) xs
            where
                mengerLine :: String -> [Bool] -> String
                mengerLine str [] = str++"\n"
                mengerLine str (x:xs)
                    | x = mengerLine (str++"\x2588\x2588") xs
                    | otherwise = mengerLine (str++"  ") xs

main = do
    n <- readLn :: IO Int
    let grid = menge
    putStr $ showMenger grid
