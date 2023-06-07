package main

import "fmt"

func find_strawberry(array []rune) bool {
	for _, val := range array {
		if val == 'S' {
			return true
		}
	}

	return false
}

func verify_horizontal(array [][]rune, x, y int) int {
	cake_pieces := 0
	for i := 0; i < x; i++ {
		if !find_strawberry(array[i]) {
			for j := 0; j < y; j++ {
				if array[i][j] == '.' {
					cake_pieces++
					array[i][j] = 'X'
				}
			}
		}
	}

	return cake_pieces
}

func verify_vertical(array [][]rune, x, y int) int {
	cake_pieces := 0
	for i := 0; i < y; i++ {
		tmpSum := 0
		for j := 0; j < x; j++ {
			if array[j][i] == 'S' {
				tmpSum = 0
				break
			}
			if array[j][i] == '.' {
				tmpSum++
			}
		}
		cake_pieces += tmpSum
	}

	return cake_pieces
}

func main() {
	var x, y int
	fmt.Scanln(&x, &y)
	array := make([][]rune, x)
	for i := range array {
		array[i] = make([]rune, y)
	}
	for i := 0; i < x; i++ {
		var value string
		fmt.Scanln(&value)
		for j := 0; j < y; j++ {
			array[i][j] = rune(value[j])
		}
	}

	horizontal_sum := verify_horizontal(array, x, y)
	vertical_sum := verify_vertical(array, x, y)

	fmt.Println(horizontal_sum + vertical_sum)
}
