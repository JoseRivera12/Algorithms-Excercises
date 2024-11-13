func isValid(s string) bool {
	mapping := map[rune]rune{'}': '{', ']': '[', ')': '('}
	stack := make([]rune, 0)
	for _, c := range s {
		if val, ok := mapping[c]; ok {
			topElement := '#'
			if len(stack) != 0 {
				topElement, stack = stack[len(stack)-1], stack[:len(stack)-1]
			}
			if topElement != val {
				return false
			}
		} else {
			stack = append(stack, c)
		}
	}

	return len(stack) == 0
}
