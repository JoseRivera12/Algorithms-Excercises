package main

import "fmt"

func main() {
	n := 0
	fmt.Scanln(&n)
	for i := 1; i <= n; i++ {
		fmt.Printf("%d Abracadabra\n", i)
	}
}
