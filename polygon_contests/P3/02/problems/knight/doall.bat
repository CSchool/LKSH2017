rem   *** validation ***
call scripts\run-validator-tests.bat
call scripts\run-checker-tests.bat

rem    *** tests ***
md tests
call scripts\gen-input-via-stdout.bat "files\generator.exe 1" "tests\02" 2
call scripts\gen-input-via-stdout.bat "files\generator.exe 2" "tests\03" 3
call scripts\gen-input-via-stdout.bat "files\generator.exe 3" "tests\04" 4
call scripts\gen-input-via-stdout.bat "files\generator.exe 4" "tests\05" 5
call scripts\gen-input-via-stdout.bat "files\generator.exe 5" "tests\06" 6
call scripts\gen-input-via-stdout.bat "files\generator.exe 6" "tests\07" 7
call scripts\gen-input-via-stdout.bat "files\generator.exe 7" "tests\08" 8
call scripts\gen-input-via-stdout.bat "files\generator.exe 8" "tests\09" 9
call scripts\gen-input-via-stdout.bat "files\generator.exe 9" "tests\10" 10
call scripts\gen-input-via-stdout.bat "files\generator.exe 10" "tests\11" 11
call scripts\gen-input-via-stdout.bat "files\generator.exe 11" "tests\12" 12
call scripts\gen-input-via-stdout.bat "files\generator.exe 12" "tests\13" 13
call scripts\gen-input-via-stdout.bat "files\generator.exe 13" "tests\14" 14
call scripts\gen-input-via-stdout.bat "files\generator.exe 14" "tests\15" 15
call scripts\gen-input-via-stdout.bat "files\generator.exe 15" "tests\16" 16
call scripts\gen-input-via-stdout.bat "files\generator.exe 16" "tests\17" 17
call scripts\gen-input-via-stdout.bat "files\generator.exe 17" "tests\18" 18
call scripts\gen-input-via-stdout.bat "files\generator.exe 18" "tests\19" 19
call scripts\gen-input-via-stdout.bat "files\generator.exe 19" "tests\20" 20
call scripts\gen-input-via-stdout.bat "files\generator.exe 20" "tests\21" 21
call scripts\gen-input-via-stdout.bat "files\generator.exe 21" "tests\22" 22
call scripts\gen-input-via-stdout.bat "files\generator.exe 22" "tests\23" 23
call scripts\gen-input-via-stdout.bat "files\generator.exe 23" "tests\24" 24
call scripts\gen-input-via-stdout.bat "files\generator.exe 24" "tests\25" 25
call scripts\gen-input-via-stdout.bat "files\generator.exe 25" "tests\26" 26
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

