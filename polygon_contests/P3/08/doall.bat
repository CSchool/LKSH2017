echo [INFO]: Building problem 'floyd'.
pushd problems\floyd
call doall.bat
popd

echo [INFO]: Building problem 'floyd-max'.
pushd problems\floyd-max
call doall.bat
popd

echo [INFO]: Building russian contest statement.
pushd statements\russian
call doall.bat
popd

