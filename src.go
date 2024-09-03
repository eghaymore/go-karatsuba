package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"math/big"
)

func main() {
	// Input Handling
	if (len(os.Args) != 3) {
		fmt.Println("Only accepting two arguments")
		os.Exit(1)
	}
	var input1 = os.Args[1]
	var input2 = os.Args[2]
	result := karatsuba(input1, input2)
	fmt.Println(result)
}

// TODO: This works but encounters int overflow with operands longer than 10 digits (base 10)
// Maybe try to make it work using big int?
func karatsuba(_i1 string, _i2 string) int {
	// Parse input
	i1 := strings.TrimLeft(_i1, "0")
	i2 := strings.TrimLeft(_i2, "0")
	len_i1 := len(i1)
	len_i2 := len(i2)
	width := max(len_i1, len_i2)
	fmt.Println("width of %d found!", width) // Debug
	
	fmt.Println(fmt.Sprintf("Performing multiplication on %s and %s", i1, i2))
	if (width < 2) { // Base Case
		_i1, err1 := strconv.Atoi(i1)
		_i2, err2 := strconv.Atoi(i2)
		if (err1 != nil || err2 != nil) {
			fmt.Println("Error converting component(s) to integer values")
			return 0
		}
		return _i1 * _i2
	}

	if (width % 2 != 0) {
		fmt.Println("Non-even input length!") // Debug
		width += 1
		i1 = fmt.Sprintf("%0*s", width, i1)
		i2 = fmt.Sprintf("%0*s", width, i2)
		
	}
	if (len_i1 != len_i2) {
		fmt.Println("Mismatched inputs!") // Debug
		i1 = fmt.Sprintf("%0*s", width, i1)
		i2 = fmt.Sprintf("%0*s", width, i2)

	}
	// Define components
	idx := width/2
	_a := i1[0:idx]
	_b := i1[idx:]
	_c := i2[0:idx]
	_d := i2[idx:]
	a, erra := strconv.Atoi(_a)
	b, errb := strconv.Atoi(_b)	
	c, errc := strconv.Atoi(_c)	
	d, errd := strconv.Atoi(_d)
	
	biga := new(big.Int)
	bigb := new(big.Int)
	bigc := new(big.Int)
	bigd := new(big.Int)
	biga, aok:= biga.SetString(_a, 10)
	bigb, bok:= bigb.SetString(_b, 10)
	bigc, cok:= bigc.SetString(_c, 10)
	bigd, dok:= bigd.SetString(_d, 10)
	if (erra != nil || errb != nil || errc != nil || errd != nil ||
	!aok || !bok || !cok || !dok) {
		fmt.Println("Error converting component(s) to integer values")
		return 0
	}
	fmt.Println(fmt.Sprintf("index of %d! Found components: {a: %d b: %d c: %d d: %d}", idx, a, b, c, d)) // Debug
	
	// Perform multiplications
	var ac = karatsuba(_a, _c)
	var bd = karatsuba(_b, _d)
	// Find inner term
//	fmt.Println("test: ", n)
//	a_b := strconv.Itoa(a+b)
//	c_d := strconv.Itoa(c+d)
	a_b := new(big.Int)
	c_d := new(big.Int)
	
	a_b.Add(biga, bigb)
	c_d.Add(bigc, bigd)
//	fmt.Println("a+b:", a_b) // Debug
//	fmt.Println("c+d:", c_d) // Debug
	var inner = (karatsuba(a_b.String(), c_d.String()) - ac - bd) 
	ac_bd := new(big.Int).Add( big.NewInt(int64(ac)), big.NewInt(int64(bd))) // This is just ac + bd
//	fmt.Println("ac+bd: ", ac_bd) // Debug
	inner2 := new(big.Int).Sub(big.NewInt(int64(karatsuba(a_b.String(), c_d.String()))), ac_bd) // This is just (a + b) * (c + d) - ac - bd
	fmt.Println("inner using bigint: ", inner2) // Debug
	fmt.Println("inner using int: ", inner) // Debug
	// Find output
	output := (int(math.Pow(10, float64(width))) * ac) + (inner * int(math.Pow(10,float64(width/2)))) + (bd)
	powerOfTen := new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(width)), nil) // This is just 10^(width)
	powerOfTen2 := new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(width/2)), nil) // This is just 10^(width/2), needed for inner term
	fmt.Println("Pwr of 10: ", powerOfTen) // Debug
	output2 := new(big.Int).Add(new(big.Int).Mul(powerOfTen, big.NewInt(int64(ac))), new(big.Int).Add(new(big.Int).Mul(inner2, powerOfTen2), big.NewInt(int64(bd))))
	fmt.Println("Output recursive: ", output) // Debug
	fmt.Println("Output recursive using bigInt: ", output2) // Debug
	return output
}
