package main

import "fmt"

func format_word(word string, lenght int) string {
	return fmt.Sprintf("%s%d%s", string(word[0]), lenght-2, string(word[lenght-1]))
}

// func main() {
// 	n_words := 0
// 	fmt.Scanf("%d\n", &n_words)
// 	words := make([]string, n_words)
// 	for i := 0; i < n_words; i++ {
// 		word := ""
// 		fmt.Scanf("%s\n", &word)
// 		words[i] = word
// 	}

// 	for i := 0; i < n_words; i++ {
// 		len_word := len(words[i])
// 		if len_word > 10 {
// 			fmt.Println(format_word(words[i], len_word))
// 		} else {
// 			fmt.Println(words[i])
// 		}
// 	}

// }

func main() {
	n_words := 0
	fmt.Scanf("%d\n", &n_words)
	for i := 0; i < n_words; i++ {
		word := ""
		fmt.Scanf("%s\n", &word)
		len_word := len(word)
		if len_word > 10 {
			fmt.Println(format_word(word, len_word))
		} else {
			fmt.Println(word)
		}
	}
}
