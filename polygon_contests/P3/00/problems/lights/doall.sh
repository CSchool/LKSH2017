#!/usr/bin/env bash
#   *** validation ***
scripts/run-validator-tests.sh
scripts/run-checker-tests.sh

#    *** tests ***
mkdir -p tests
echo "Generating test #2"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 50 1" "tests/02" 2
echo "Generating test #3"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 50 2" "tests/03" 3
echo "Generating test #4"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 50 3" "tests/04" 4
echo "Generating test #5"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 20 4" "tests/05" 5
echo "Generating test #6"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 20 5" "tests/06" 6
echo "Generating test #7"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 20 6" "tests/07" 7
echo "Generating test #8"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 0 7" "tests/08" 8
echo "Generating test #9"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 0 8" "tests/09" 9
echo "Generating test #10"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 0 9" "tests/10" 10
echo "Generating test #11"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 100 10" "tests/11" 11
echo "Generating test #12"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 100 11" "tests/12" 12
echo "Generating test #13"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 5 100 12" "tests/13" 13
echo "Generating test #14"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 50 13" "tests/14" 14
echo "Generating test #15"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 50 14" "tests/15" 15
echo "Generating test #16"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 50 15" "tests/16" 16
echo "Generating test #17"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 20 16" "tests/17" 17
echo "Generating test #18"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 20 17" "tests/18" 18
echo "Generating test #19"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 20 18" "tests/19" 19
echo "Generating test #20"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 0 19" "tests/20" 20
echo "Generating test #21"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 0 20" "tests/21" 21
echo "Generating test #22"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 0 21" "tests/22" 22
echo "Generating test #23"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 100 22" "tests/23" 23
echo "Generating test #24"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 100 23" "tests/24" 24
echo "Generating test #25"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 15 100 24" "tests/25" 25
echo "Generating test #26"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 50 25" "tests/26" 26
echo "Generating test #27"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 50 26" "tests/27" 27
echo "Generating test #28"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 50 27" "tests/28" 28
echo "Generating test #29"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 20 28" "tests/29" 29
echo "Generating test #30"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 20 29" "tests/30" 30
echo "Generating test #31"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 20 30" "tests/31" 31
echo "Generating test #32"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 0 31" "tests/32" 32
echo "Generating test #33"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 0 32" "tests/33" 33
echo "Generating test #34"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 0 33" "tests/34" 34
echo "Generating test #35"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 100 34" "tests/35" 35
echo "Generating test #36"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 100 35" "tests/36" 36
echo "Generating test #37"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 30 100 36" "tests/37" 37
echo "Generating test #38"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 50 37" "tests/38" 38
echo "Generating test #39"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 50 38" "tests/39" 39
echo "Generating test #40"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 50 39" "tests/40" 40
echo "Generating test #41"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 20 40" "tests/41" 41
echo "Generating test #42"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 20 41" "tests/42" 42
echo "Generating test #43"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 20 42" "tests/43" 43
echo "Generating test #44"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 0 43" "tests/44" 44
echo "Generating test #45"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 0 44" "tests/45" 45
echo "Generating test #46"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 0 45" "tests/46" 46
echo "Generating test #47"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 100 46" "tests/47" 47
echo "Generating test #48"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 100 47" "tests/48" 48
echo "Generating test #49"
scripts/gen-input-via-stdout.sh "wine files/generator.exe 100 100 48" "tests/49" 49
echo ""
echo "Generating answer for test #1"
scripts/gen-answer.sh tests/01 tests/01.a "tests" ""
echo ""
echo "Generating answer for test #2"
scripts/gen-answer.sh tests/02 tests/02.a "tests" ""
echo ""
echo "Generating answer for test #3"
scripts/gen-answer.sh tests/03 tests/03.a "tests" ""
echo ""
echo "Generating answer for test #4"
scripts/gen-answer.sh tests/04 tests/04.a "tests" ""
echo ""
echo "Generating answer for test #5"
scripts/gen-answer.sh tests/05 tests/05.a "tests" ""
echo ""
echo "Generating answer for test #6"
scripts/gen-answer.sh tests/06 tests/06.a "tests" ""
echo ""
echo "Generating answer for test #7"
scripts/gen-answer.sh tests/07 tests/07.a "tests" ""
echo ""
echo "Generating answer for test #8"
scripts/gen-answer.sh tests/08 tests/08.a "tests" ""
echo ""
echo "Generating answer for test #9"
scripts/gen-answer.sh tests/09 tests/09.a "tests" ""
echo ""
echo "Generating answer for test #10"
scripts/gen-answer.sh tests/10 tests/10.a "tests" ""
echo ""
echo "Generating answer for test #11"
scripts/gen-answer.sh tests/11 tests/11.a "tests" ""
echo ""
echo "Generating answer for test #12"
scripts/gen-answer.sh tests/12 tests/12.a "tests" ""
echo ""
echo "Generating answer for test #13"
scripts/gen-answer.sh tests/13 tests/13.a "tests" ""
echo ""
echo "Generating answer for test #14"
scripts/gen-answer.sh tests/14 tests/14.a "tests" ""
echo ""
echo "Generating answer for test #15"
scripts/gen-answer.sh tests/15 tests/15.a "tests" ""
echo ""
echo "Generating answer for test #16"
scripts/gen-answer.sh tests/16 tests/16.a "tests" ""
echo ""
echo "Generating answer for test #17"
scripts/gen-answer.sh tests/17 tests/17.a "tests" ""
echo ""
echo "Generating answer for test #18"
scripts/gen-answer.sh tests/18 tests/18.a "tests" ""
echo ""
echo "Generating answer for test #19"
scripts/gen-answer.sh tests/19 tests/19.a "tests" ""
echo ""
echo "Generating answer for test #20"
scripts/gen-answer.sh tests/20 tests/20.a "tests" ""
echo ""
echo "Generating answer for test #21"
scripts/gen-answer.sh tests/21 tests/21.a "tests" ""
echo ""
echo "Generating answer for test #22"
scripts/gen-answer.sh tests/22 tests/22.a "tests" ""
echo ""
echo "Generating answer for test #23"
scripts/gen-answer.sh tests/23 tests/23.a "tests" ""
echo ""
echo "Generating answer for test #24"
scripts/gen-answer.sh tests/24 tests/24.a "tests" ""
echo ""
echo "Generating answer for test #25"
scripts/gen-answer.sh tests/25 tests/25.a "tests" ""
echo ""
echo "Generating answer for test #26"
scripts/gen-answer.sh tests/26 tests/26.a "tests" ""
echo ""
echo "Generating answer for test #27"
scripts/gen-answer.sh tests/27 tests/27.a "tests" ""
echo ""
echo "Generating answer for test #28"
scripts/gen-answer.sh tests/28 tests/28.a "tests" ""
echo ""
echo "Generating answer for test #29"
scripts/gen-answer.sh tests/29 tests/29.a "tests" ""
echo ""
echo "Generating answer for test #30"
scripts/gen-answer.sh tests/30 tests/30.a "tests" ""
echo ""
echo "Generating answer for test #31"
scripts/gen-answer.sh tests/31 tests/31.a "tests" ""
echo ""
echo "Generating answer for test #32"
scripts/gen-answer.sh tests/32 tests/32.a "tests" ""
echo ""
echo "Generating answer for test #33"
scripts/gen-answer.sh tests/33 tests/33.a "tests" ""
echo ""
echo "Generating answer for test #34"
scripts/gen-answer.sh tests/34 tests/34.a "tests" ""
echo ""
echo "Generating answer for test #35"
scripts/gen-answer.sh tests/35 tests/35.a "tests" ""
echo ""
echo "Generating answer for test #36"
scripts/gen-answer.sh tests/36 tests/36.a "tests" ""
echo ""
echo "Generating answer for test #37"
scripts/gen-answer.sh tests/37 tests/37.a "tests" ""
echo ""
echo "Generating answer for test #38"
scripts/gen-answer.sh tests/38 tests/38.a "tests" ""
echo ""
echo "Generating answer for test #39"
scripts/gen-answer.sh tests/39 tests/39.a "tests" ""
echo ""
echo "Generating answer for test #40"
scripts/gen-answer.sh tests/40 tests/40.a "tests" ""
echo ""
echo "Generating answer for test #41"
scripts/gen-answer.sh tests/41 tests/41.a "tests" ""
echo ""
echo "Generating answer for test #42"
scripts/gen-answer.sh tests/42 tests/42.a "tests" ""
echo ""
echo "Generating answer for test #43"
scripts/gen-answer.sh tests/43 tests/43.a "tests" ""
echo ""
echo "Generating answer for test #44"
scripts/gen-answer.sh tests/44 tests/44.a "tests" ""
echo ""
echo "Generating answer for test #45"
scripts/gen-answer.sh tests/45 tests/45.a "tests" ""
echo ""
echo "Generating answer for test #46"
scripts/gen-answer.sh tests/46 tests/46.a "tests" ""
echo ""
echo "Generating answer for test #47"
scripts/gen-answer.sh tests/47 tests/47.a "tests" ""
echo ""
echo "Generating answer for test #48"
scripts/gen-answer.sh tests/48 tests/48.a "tests" ""
echo ""
echo "Generating answer for test #49"
scripts/gen-answer.sh tests/49 tests/49.a "tests" ""
echo ""

