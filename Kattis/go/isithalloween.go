package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	line, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	line = strings.TrimSuffix(line, "\n")
	if line == "OCT 31" || line == "DEC 25" {
		fmt.Println("yup")
		return
	}
	fmt.Println("nope")
}
