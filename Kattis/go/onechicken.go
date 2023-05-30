package main

import "fmt"

func main() {
	var n, m int
	fmt.Scanln(&n, &m)
	if m > n {
		pieces := m - n
		text := fmt.Sprintf("%d piece", pieces)
		if pieces > 1 {
			text += "s"
		}
		fmt.Printf("Dr. Chaz will have %s of chicken left over!\n", text)
		return
	}

	pieces := n - m
	text := fmt.Sprintf("%d more piece", pieces)
	if pieces > 1 {
		text += "s"
	}
	fmt.Printf("Dr. Chaz needs %s of chicken!\n", text)
}
