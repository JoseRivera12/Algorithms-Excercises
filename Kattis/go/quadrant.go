package main

import "fmt"

func get_cuadrant(x, y int) int {
	if x > 0 {
		if y > 0 {
			return 1
		}
		return 4
	}

	if y > 0 {
		return 2
	}

	return 3
}

func main() {
	var x, y int
	fmt.Scanln(&x)
	fmt.Scanln(&y)
	fmt.Println(get_cuadrant(x, y))

}
