-- nlantau, 2021-03-04

module CodeWars.OCRMistakes where

correct :: String -> String
correct x = 
    let y '5' = 'S'
        y '0' = 'O'
        y '1' = 'I'
        y x = x
    in map y x


{-
module CodeWars.OCRMistakes where

correct :: String -> String
correct = map correctHelp

correctHelp char =
  case char of
    '5' -> 'S'
    '0' -> 'O'
    '1' -> 'I'
    c -> c

-------------------------------------------

{-# LANGUAGE LambdaCase #-}
module CodeWars.OCRMistakes where

correct :: String -> String
correct = map $ \case '0' -> 'O'; '1' -> 'I'; '5' -> 'S'; x -> x

-}