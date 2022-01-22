-- nlantau, 2021-03-03

module AreaPerimeter where

areaOrPerimeter :: Double -> Double -> Double
areaOrPerimeter a b
    | a == b = a * b
    | otherwise = a*2 + b*2