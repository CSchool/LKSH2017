echo [INFO]: Building problem 'connectivity'.
pushd problems\connectivity
call doall.bat
popd

echo [INFO]: Building problem 'forest'.
pushd problems\forest
call doall.bat
popd

echo [INFO]: Building problem 'knight'.
pushd problems\knight
call doall.bat
popd

echo [INFO]: Building problem 'roads'.
pushd problems\roads
call doall.bat
popd

echo [INFO]: Building russian contest statement.
pushd statements\russian
call doall.bat
popd

