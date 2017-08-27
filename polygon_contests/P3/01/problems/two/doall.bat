rem   *** validation ***
call scripts\run-validator-tests.bat
call scripts\run-checker-tests.bat

rem    *** tests ***
md tests
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 50 1 two" "tests\03" 3
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 50 2 two" "tests\04" 4
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 50 3 two" "tests\05" 5
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 20 4 two" "tests\06" 6
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 20 5 two" "tests\07" 7
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 20 6 two" "tests\08" 8
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 0 7 two" "tests\09" 9
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 0 8 two" "tests\10" 10
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 0 9 two" "tests\11" 11
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 100 10 two" "tests\12" 12
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 100 11 two" "tests\13" 13
call scripts\gen-input-via-stdout.bat "files\gen.exe 5 100 12 two" "tests\14" 14
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 50 13 two" "tests\15" 15
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 50 14 two" "tests\16" 16
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 50 15 two" "tests\17" 17
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 20 16 two" "tests\18" 18
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 20 17 two" "tests\19" 19
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 20 18 two" "tests\20" 20
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 0 19 two" "tests\21" 21
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 0 20 two" "tests\22" 22
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 0 21 two" "tests\23" 23
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 100 22 two" "tests\24" 24
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 100 23 two" "tests\25" 25
call scripts\gen-input-via-stdout.bat "files\gen.exe 15 100 24 two" "tests\26" 26
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 50 25 two" "tests\27" 27
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 50 26 two" "tests\28" 28
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 50 27 two" "tests\29" 29
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 20 28 two" "tests\30" 30
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 20 29 two" "tests\31" 31
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 20 30 two" "tests\32" 32
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 0 31 two" "tests\33" 33
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 0 32 two" "tests\34" 34
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 0 33 two" "tests\35" 35
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 100 34 two" "tests\36" 36
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 100 35 two" "tests\37" 37
call scripts\gen-input-via-stdout.bat "files\gen.exe 30 100 36 two" "tests\38" 38
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 50 37 two" "tests\39" 39
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 50 38 two" "tests\40" 40
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 50 39 two" "tests\41" 41
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 20 40 two" "tests\42" 42
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 20 41 two" "tests\43" 43
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 20 42 two" "tests\44" 44
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 0 43 two" "tests\45" 45
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 0 44 two" "tests\46" 46
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 0 45 two" "tests\47" 47
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 100 46 two" "tests\48" 48
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 100 47 two" "tests\49" 49
call scripts\gen-input-via-stdout.bat "files\gen.exe 100 100 48 two" "tests\50" 50
call scripts\gen-answer.bat tests\01 tests\01.a "tests" ""
call scripts\gen-answer.bat tests\02 tests\02.a "tests" ""
call scripts\gen-answer.bat tests\03 tests\03.a "tests" ""
call scripts\gen-answer.bat tests\04 tests\04.a "tests" ""
call scripts\gen-answer.bat tests\05 tests\05.a "tests" ""
call scripts\gen-answer.bat tests\06 tests\06.a "tests" ""
call scripts\gen-answer.bat tests\07 tests\07.a "tests" ""
call scripts\gen-answer.bat tests\08 tests\08.a "tests" ""
call scripts\gen-answer.bat tests\09 tests\09.a "tests" ""
call scripts\gen-answer.bat tests\10 tests\10.a "tests" ""
call scripts\gen-answer.bat tests\11 tests\11.a "tests" ""
call scripts\gen-answer.bat tests\12 tests\12.a "tests" ""
call scripts\gen-answer.bat tests\13 tests\13.a "tests" ""
call scripts\gen-answer.bat tests\14 tests\14.a "tests" ""
call scripts\gen-answer.bat tests\15 tests\15.a "tests" ""
call scripts\gen-answer.bat tests\16 tests\16.a "tests" ""
call scripts\gen-answer.bat tests\17 tests\17.a "tests" ""
call scripts\gen-answer.bat tests\18 tests\18.a "tests" ""
call scripts\gen-answer.bat tests\19 tests\19.a "tests" ""
call scripts\gen-answer.bat tests\20 tests\20.a "tests" ""
call scripts\gen-answer.bat tests\21 tests\21.a "tests" ""
call scripts\gen-answer.bat tests\22 tests\22.a "tests" ""
call scripts\gen-answer.bat tests\23 tests\23.a "tests" ""
call scripts\gen-answer.bat tests\24 tests\24.a "tests" ""
call scripts\gen-answer.bat tests\25 tests\25.a "tests" ""
call scripts\gen-answer.bat tests\26 tests\26.a "tests" ""
call scripts\gen-answer.bat tests\27 tests\27.a "tests" ""
call scripts\gen-answer.bat tests\28 tests\28.a "tests" ""
call scripts\gen-answer.bat tests\29 tests\29.a "tests" ""
call scripts\gen-answer.bat tests\30 tests\30.a "tests" ""
call scripts\gen-answer.bat tests\31 tests\31.a "tests" ""
call scripts\gen-answer.bat tests\32 tests\32.a "tests" ""
call scripts\gen-answer.bat tests\33 tests\33.a "tests" ""
call scripts\gen-answer.bat tests\34 tests\34.a "tests" ""
call scripts\gen-answer.bat tests\35 tests\35.a "tests" ""
call scripts\gen-answer.bat tests\36 tests\36.a "tests" ""
call scripts\gen-answer.bat tests\37 tests\37.a "tests" ""
call scripts\gen-answer.bat tests\38 tests\38.a "tests" ""
call scripts\gen-answer.bat tests\39 tests\39.a "tests" ""
call scripts\gen-answer.bat tests\40 tests\40.a "tests" ""
call scripts\gen-answer.bat tests\41 tests\41.a "tests" ""
call scripts\gen-answer.bat tests\42 tests\42.a "tests" ""
call scripts\gen-answer.bat tests\43 tests\43.a "tests" ""
call scripts\gen-answer.bat tests\44 tests\44.a "tests" ""
call scripts\gen-answer.bat tests\45 tests\45.a "tests" ""
call scripts\gen-answer.bat tests\46 tests\46.a "tests" ""
call scripts\gen-answer.bat tests\47 tests\47.a "tests" ""
call scripts\gen-answer.bat tests\48 tests\48.a "tests" ""
call scripts\gen-answer.bat tests\49 tests\49.a "tests" ""
call scripts\gen-answer.bat tests\50 tests\50.a "tests" ""

