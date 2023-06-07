package main

import (
	"fmt"
	"strings"
)

// Aprendizajes

// Golang rune is unicode caracters
// if we need to pass string number to int number - 0 like - a or - A

func roundNumber(num string) string {
	parts := strings.Split(num, ".")
	intPart := parts[0]
	decPart := parts[1]

	lastDigit := int(intPart[len(intPart)-1] - '0')
	if lastDigit != 9 {
		fracDigit := int(decPart[0] - '0')
		if fracDigit < 5 {
			return intPart
		}
		return intPart[:len(intPart)-1] + string(lastDigit+'1')
	}

	return "GOTO Vasilisa."

}

func main() {
	var number string
	fmt.Scanln(&number)

	fmt.Println(roundNumber(number))
	fmt.Println('0')
	fmt.Println('1')
}
