rem   *** validation ***
call scripts\run-validator-tests.bat
call scripts\run-checker-tests.bat

rem    *** tests ***
md tests
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 50 1 rain" "tests\03" 3
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 50 2 rain" "tests\04" 4
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 50 3 rain" "tests\05" 5
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 80 4 rain" "tests\06" 6
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 80 5 rain" "tests\07" 7
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 80 6 rain" "tests\08" 8
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 20 7 rain" "tests\09" 9
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 20 8 rain" "tests\10" 10
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 20 9 rain" "tests\11" 11
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 100 10 rain" "tests\12" 12
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 100 11 rain" "tests\13" 13
call scripts\gen-input-via-stdout.bat "files\generator.exe 5 100 12 rain" "tests\14" 14
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 50 13 rain" "tests\15" 15
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 50 14 rain" "tests\16" 16
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 50 15 rain" "tests\17" 17
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 80 16 rain" "tests\18" 18
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 80 17 rain" "tests\19" 19
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 80 18 rain" "tests\20" 20
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 20 19 rain" "tests\21" 21
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 20 20 rain" "tests\22" 22
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 20 21 rain" "tests\23" 23
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 100 22 rain" "tests\24" 24
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 100 23 rain" "tests\25" 25
call scripts\gen-input-via-stdout.bat "files\generator.exe 15 100 24 rain" "tests\26" 26
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 50 25 rain" "tests\27" 27
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 50 26 rain" "tests\28" 28
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 50 27 rain" "tests\29" 29
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 80 28 rain" "tests\30" 30
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 80 29 rain" "tests\31" 31
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 80 30 rain" "tests\32" 32
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 20 31 rain" "tests\33" 33
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 20 32 rain" "tests\34" 34
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 20 33 rain" "tests\35" 35
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 100 34 rain" "tests\36" 36
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 100 35 rain" "tests\37" 37
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 100 36 rain" "tests\38" 38
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 50 37 rain" "tests\39" 39
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 50 38 rain" "tests\40" 40
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 50 39 rain" "tests\41" 41
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 80 40 rain" "tests\42" 42
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 80 41 rain" "tests\43" 43
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 80 42 rain" "tests\44" 44
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 20 43 rain" "tests\45" 45
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 20 44 rain" "tests\46" 46
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 20 45 rain" "tests\47" 47
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 100 46 rain" "tests\48" 48
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 100 47 rain" "tests\49" 49
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 100 48 rain" "tests\50" 50
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

