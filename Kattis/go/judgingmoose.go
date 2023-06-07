package main

import "fmt"

func main() {
	var l, r int
	fmt.Scanln(&l, &r)
	if l == 0 && r == 0 {
		fmt.Println("Not a moose")
		return
	}

	if l > r {
		fmt.Println("Odd", l*2)
		return
	} else if r > l {
		fmt.Println("Odd", r*2)
		return
	}

	fmt.Println("Even", l*2)
}
