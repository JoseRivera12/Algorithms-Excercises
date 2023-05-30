package main

import "fmt"

func main() {
	var cases int
	var QALY float64
	fmt.Scanln(&cases)
	for i := 0; i < cases; i++ {
		var qtyLife, years float64
		fmt.Scanln(&qtyLife, &years)
		QALY += qtyLife * years
	}

	fmt.Println(QALY)
}
