package main
import "fmt"

func conditions() {
	var num1 = 2
	var num2 = 4

	if num1 * num2 == 8 { 
		fmt.Println("num1 * num2 = 8") 
	} else if num1 + num2 == 8 { 
		fmt.Println("num1 + num2 = 8") 
	}
}