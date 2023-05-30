package main

import "fmt"

func main() {
	var easy, medium, hard, num int
	fmt.Scanln(&easy, &medium, &hard, &num)
	if easy > 0 && medium > 0 && hard > 0 && num >= 3 && easy+medium+hard >= num {
		fmt.Println("YES")
		return
	}

	fmt.Println("NO")
}
