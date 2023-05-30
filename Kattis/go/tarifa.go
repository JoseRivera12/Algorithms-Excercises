package main

import "fmt"

func main() {
	// Version 1
	// var plan int
	// var months int
	// var dataUsed int
	// fmt.Scanln(&plan)
	// fmt.Scanln(&months)
	// for i := 0; i < months; i++ {
	// 	var monthData int
	// 	fmt.Scanln(&monthData)
	// 	dataUsed += monthData
	// }

	// fmt.Println((months+1)*plan - dataUsed)

	var plan int
	var months int
	var remaingData int
	fmt.Scanln(&plan)
	fmt.Scanln(&months)
	for i := 0; i < months; i++ {
		monthData := plan + remaingData
		var dataUsed int
		fmt.Scanln(&dataUsed)
		remaingData = monthData - dataUsed
	}

	fmt.Println(plan + remaingData)
}
