rem   *** validation ***
call scripts\run-validator-tests.bat
call scripts\run-checker-tests.bat

rem    *** tests ***
md tests
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 10 0 1 forest" "tests\03" 3
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 10 5 2 forest" "tests\04" 4
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 10 -5 3 forest" "tests\05" 5
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 10 100 4 forest" "tests\06" 6
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 10 -100 5 forest" "tests\07" 7
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 30 0 6 forest" "tests\08" 8
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 30 5 7 forest" "tests\09" 9
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 30 -5 8 forest" "tests\10" 10
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 30 100 9 forest" "tests\11" 11
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 30 -100 10 forest" "tests\12" 12
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 0 0 11 forest" "tests\13" 13
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 0 5 12 forest" "tests\14" 14
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 0 -5 13 forest" "tests\15" 15
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 0 100 14 forest" "tests\16" 16
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 0 -100 15 forest" "tests\17" 17
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 85 0 16 forest" "tests\18" 18
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 85 5 17 forest" "tests\19" 19
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 85 -5 18 forest" "tests\20" 20
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 85 100 19 forest" "tests\21" 21
call scripts\gen-input-via-stdout.bat "files\generator.exe 20 85 -100 20 forest" "tests\22" 22
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 10 0 21 forest" "tests\23" 23
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 10 5 22 forest" "tests\24" 24
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 10 -5 23 forest" "tests\25" 25
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 10 100 24 forest" "tests\26" 26
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 10 -100 25 forest" "tests\27" 27
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 30 0 26 forest" "tests\28" 28
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 30 5 27 forest" "tests\29" 29
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 30 -5 28 forest" "tests\30" 30
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 30 100 29 forest" "tests\31" 31
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 30 -100 30 forest" "tests\32" 32
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 0 0 31 forest" "tests\33" 33
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 0 5 32 forest" "tests\34" 34
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 0 -5 33 forest" "tests\35" 35
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 0 100 34 forest" "tests\36" 36
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 0 -100 35 forest" "tests\37" 37
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 85 0 36 forest" "tests\38" 38
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 85 5 37 forest" "tests\39" 39
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 85 -5 38 forest" "tests\40" 40
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 85 100 39 forest" "tests\41" 41
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 85 -100 40 forest" "tests\42" 42
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

