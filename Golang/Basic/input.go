package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func input() {
	// Get user input
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Printf("Type something: ")
	scanner.Scan()

	input := scanner.Text()
	fmt.Printf("You typed: %q\n\n", input)

	
	// Check user age
	fmt.Printf("Type your birth year: ")
	scanner.Scan()

	age, _ := strconv.ParseInt(scanner.Text(), 10, 64)
	fmt.Printf("You will be %d by the end of 2023", 2023 - age)
}