menger :: Int -> [[Bool]]
menger 0 = [[True]]
menger n
    | n < 0 = error "Invalid size."
    | n > 0 = collate 0 0 [] (menger(n-1))
        where
            collate :: Int -> Int -> [[Bool]] -> [[Bool]] -> [[Bool]]
            collate r x grid prev
                | x >= 3 = grid
                | r >= length(prev) = collate 0 (x+1) grid prev
                | otherwise = collate (r+1) x (grid++[collateRow 0 x 0 [] (prev!!r)]) prev
                    where
                        collateRow :: Int -> Int -> Int -> [Bool] -> [Bool] -> [Bool]
                        collateRow c x y row prev
                            | y >= 3 = row
                            | c >= length(prev) = collateRow 0 x (y+1) row prev
                            | x `mod` 3 == 1 && y `mod` 3 == 1 = collateRow (c+1) x y (row++[False]) prev
                            | otherwise = collateRow (c+1) x y (row++[prev!!c]) prev

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
    let grid = menger n
    putStr $ showMenger grid
