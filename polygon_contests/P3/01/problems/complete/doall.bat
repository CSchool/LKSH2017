rem   *** validation ***
call scripts\run-validator-tests.bat
call scripts\run-checker-tests.bat

rem    *** tests ***
md tests
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 95 1 complete" "tests\02" 2
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 95 2 complete" "tests\03" 3
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 95 3 complete" "tests\04" 4
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 40 4 complete" "tests\05" 5
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 40 5 complete" "tests\06" 6
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 40 6 complete" "tests\07" 7
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 1 7 complete" "tests\08" 8
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 1 8 complete" "tests\09" 9
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 1 9 complete" "tests\10" 10
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 70 10 complete" "tests\11" 11
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 70 11 complete" "tests\12" 12
call scripts\gen-input-via-stdout.bat "files\generator.exe 10 70 12 complete" "tests\13" 13
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 95 13 complete" "tests\14" 14
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 95 14 complete" "tests\15" 15
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 95 15 complete" "tests\16" 16
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 40 16 complete" "tests\17" 17
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 40 17 complete" "tests\18" 18
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 40 18 complete" "tests\19" 19
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 1 19 complete" "tests\20" 20
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 1 20 complete" "tests\21" 21
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 1 21 complete" "tests\22" 22
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 70 22 complete" "tests\23" 23
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 70 23 complete" "tests\24" 24
call scripts\gen-input-via-stdout.bat "files\generator.exe 30 70 24 complete" "tests\25" 25
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 95 25 complete" "tests\26" 26
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 95 26 complete" "tests\27" 27
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 95 27 complete" "tests\28" 28
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 40 28 complete" "tests\29" 29
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 40 29 complete" "tests\30" 30
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 40 30 complete" "tests\31" 31
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 1 31 complete" "tests\32" 32
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 1 32 complete" "tests\33" 33
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 1 33 complete" "tests\34" 34
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 70 34 complete" "tests\35" 35
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 70 35 complete" "tests\36" 36
call scripts\gen-input-via-stdout.bat "files\generator.exe 100 70 36 complete" "tests\37" 37
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

