package main

import "fmt"

func main() {
	var x, y float64
	fmt.Scanln(&x, &y)

	if x == 0 && y == 1 {
		fmt.Println("ALL GOOD")
	} else if y == 1 {
		fmt.Println("IMPOSSIBLE")
	} else {
		fmt.Println(x / (1 - y))
	}
}
