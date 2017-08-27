echo [INFO]: Building problem 'checkboard'.
pushd problems\checkboard
call doall.bat
popd

echo [INFO]: Building problem 'numgame'.
pushd problems\numgame
call doall.bat
popd

echo [INFO]: Building problem 'primesum'.
pushd problems\primesum
call doall.bat
popd

echo [INFO]: Building problem 'lights'.
pushd problems\lights
call doall.bat
popd

echo [INFO]: Building problem 'multiplication'.
pushd problems\multiplication
call doall.bat
popd

echo [INFO]: Building problem 'list'.
pushd problems\list
call doall.bat
popd

echo [INFO]: Building russian contest statement.
pushd statements\russian
call doall.bat
popd

