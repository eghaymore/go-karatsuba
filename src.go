package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func main() {
	// Input Handling
	if (len(os.Args) != 3) {
		fmt.Println("Only accepting two arguments")
		os.Exit(1)
	}
	var input1 = os.Args[1]
	var input2 = os.Args[2]
	// Parse input
	len_input1 := len(input1)
	len_input2 := len(input2)
	width := max(len_input1, len_input2)

	if (width % 2 != 0) {
		fmt.Println("Non-even input length!") // Debug
		width += 1
		input1 = fmt.Sprintf("%0*s", width, input1)
		input2 = fmt.Sprintf("%0*s", width, input2)
		
	}
	if (len_input1 != len_input2) {
		fmt.Println("Mismatched inputs!") // Debug
		input1 = fmt.Sprintf("%0*s", width, input1)
		input2 = fmt.Sprintf("%0*s", width, input2)
	}
	fmt.Println(fmt.Sprintf("Performing multiplication on %s and %s", input1, input2))
	
	// Define components
	idx := width/2
	a, erra := strconv.Atoi(input1[0:idx])
	b, errb := strconv.Atoi(input1[idx:])
	c, errc := strconv.Atoi(input2[0:idx])
	d, errd := strconv.Atoi(input2[idx:])
	if (erra != nil || errb != nil || errc != nil || errd != nil) {
		fmt.Println("Error converting component(s) to integer values")
	}
	fmt.Println(fmt.Sprintf("index of %d! Found components: {a: %d b: %d c: %d d: %d}", idx, a, b, c, d)) // Debug

	// Perform multiplications
	var ac = a*c
	var bd = b*d
	// Find inner term
	var inner = (a+b)*(c+d) - ac - bd 
	fmt.Println(fmt.Sprintf("Found ac: %d and bd: %d\nFound inner term: %d ", ac, bd, inner)) // Debug
	// Find output
	output := (int(math.Pow(10, float64(width))) * ac) + (inner * int(math.Pow(10,float64(width/2)))) + (bd)
	fmt.Println("Output: ", output)
	// 200538
}
