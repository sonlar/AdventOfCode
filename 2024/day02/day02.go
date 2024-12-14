package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func checkRequirements(line []float64) bool {

	if line[0] > line[1] {
		for key := range line {
			if key+1 < len(line) {
				if line[key] <= line[key+1] {
					// fmt.Print("Not decreasing:")
					// fmt.Printf("key:%v key+1:%v\n", line[key], line[key+1])
					return false
				}
				if math.Abs(line[key]-line[key+1]) > 3 {
					// fmt.Print("Too big of a difference:")
					// fmt.Printf("key:%v key+1:%v\n", line[key], line[key+1])
					return false
				}
			}
		}
	}
	if line[0] < line[1] {
		for key := range line {
			if key+1 < len(line) {
				if line[key] >= line[key+1] {
					// fmt.Print("Not increasing:")
					// fmt.Printf("key:%v key+1:%v\n", line[key], line[key+1])
					return false
				}
				if math.Abs(line[key]-line[key+1]) > 3 {
					// fmt.Print("Too big of a difference:")
					// fmt.Printf("key:%v key+1:%v\n", line[key], line[key+1])
					return false
				}
			}
		}
	}
	fmt.Println(line)
	return true
}
func main() {
	safe_reports := 0

	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		text := scanner.Text()
		stringLine := strings.Split(text, " ")
		floatLine := []float64{}
		for _, value := range stringLine {
			if f, err := strconv.ParseFloat(value, 64); err == nil {
				floatLine = append(floatLine, f)
			}
		}
		if checkRequirements(floatLine) == true {
			safe_reports++
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Number of safe reports: %v", safe_reports)
}
