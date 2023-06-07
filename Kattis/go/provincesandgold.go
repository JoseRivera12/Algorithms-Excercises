package main

import "fmt"

func main() {
	var g, s, c, money int
	fmt.Scanln(&g, &s, &c)
	money += g*3 + s*2 + c

	switch {
	case money >= 8:
		fmt.Println("Province or Gold")
	case money >= 6:
		fmt.Println("Duchy or Gold")
	case money == 5:
		fmt.Println("Duchy or Silver")
	case money >= 3:
		fmt.Println("Estate or Silver")
	case money == 2:
		fmt.Println("Estate or Copper")
	default:
		fmt.Println("Copper")
	}
}
