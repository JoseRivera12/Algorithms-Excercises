package main

import (
	"fmt"
	"math"
)

func main() {
	for {
		var num1, num2 float64
		_, err := fmt.Scanln(&num1, &num2)
		if err != nil {
			return
		}
		fmt.Printf("%d\n", int(math.Abs(num1-num2)))
	}
}
