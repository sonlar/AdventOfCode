package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strconv"
)

func isDigit(b byte) bool {
	if b == 32 || b == 10 {
		return false
	}
	return true
}
func main() {
	num := ""
	count := 1
	even := make([]int, 0)
	odd := make([]int, 0)
	diff := 0.0

	file, err := os.ReadFile("input")
	if err != nil {
		log.Fatal(err)
	}

	for _, val := range file {
		if isDigit(val) {
			num += string(val)
		} else {
			if len(num) > 0 {
				inum, err := strconv.Atoi(num)
				if err != nil {
					log.Fatal(err)
				}

				if count&1 != 0 {
					odd = append(odd, inum)
				} else {
					even = append(even, inum)
				}
				count += 1
				num = ""
			}
		}
	}

	sort.Ints(odd)
	sort.Ints(even)
	for i := 0; i < len(odd); i++ {
		diff += math.Abs(float64(odd[i] - even[i]))
	}
	diffint := int(diff)
	fmt.Printf("%d", diffint)
}
