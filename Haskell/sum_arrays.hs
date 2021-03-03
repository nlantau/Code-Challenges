-- nlantau, 2021-03-03

module Sum where
import Prelude hiding (sum)

sum :: Num a => [a] -> a
sum = foldr (+) 0