package main

import "fmt"

func main() {
	n_vectors := 0
	var rx, ry, rz int
	fmt.Scanf("%d\n", &n_vectors)
	for i := 0; i < n_vectors; i++ {
		var x, y, z int
		fmt.Scanln(&x, &y, &z)
		rx += x
		ry += y
		rz += z
	}

	if rx == 0 && ry == 0 && rz == 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
