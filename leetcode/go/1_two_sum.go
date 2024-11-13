func twoSum(nums []int, target int) []int {
	memory := make(map[int]int)
	for i, value := range nums {
		search := target - value
		if _, exists := memory[search]; exists {
			return []int{i, memory[search]}	
		} else {
			memory[value] = i
		}
	}

	return []int{-1,-1}
}
