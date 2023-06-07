package main

import (
	"fmt"
	"strings"
)

func is_pangram(word string) bool {
	word = strings.ToLower(word)
	var letters [26]int

	for _, letter := range word {
		letters[letter-'a']++
	}

	for _, letter := range letters {
		if letter == 0 {
			return false
		}
	}

	return true
}

func main() {
	n_caracters := 0
	word := ""
	fmt.Scanln(&n_caracters)
	fmt.Scanln(&word)

	if n_caracters < 26 {
		fmt.Println("NO")
		return
	}

	if is_pangram(word) {
		fmt.Println("YES")
		return
	}

	fmt.Println("NO")
}
