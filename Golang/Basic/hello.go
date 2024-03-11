package main

import "fmt"

func hello() {
	var hello = "Hello" // Implicit
	var world string = "World!" // Explicit

	var number = 222
	number2 := 2

	number += number2

	fmt.Println(hello, world, number)
	fmt.Printf("Type of hello: %T\n", hello)

	fmt.Printf("Boolean %t", true)
}