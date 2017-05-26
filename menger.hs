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
                | otherwise = collate (r+1) x (grid++[collateRow x (prev!!r)]) prev
                    where
                        collateRow :: Int -> [Bool] -> [Bool]
                        collateRow x prev
                            | x `mod` 3 == 1 = prev ++ (replicate (length prev) False) ++ prev
                            | otherwise = prev ++ prev ++ prev

showMenger :: [[Bool]] -> String
showMenger xs = unlines (map (concat . (map (\x -> if x then "\x2588\x2588" else "  "))) xs)

main = do
    n <- readLn :: IO Int
    let grid = menger n
    putStr $ showMenger grid
