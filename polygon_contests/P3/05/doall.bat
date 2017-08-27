echo [INFO]: Building problem 'path-length'.
pushd problems\path-length
call doall.bat
popd

echo [INFO]: Building problem 'path'.
pushd problems\path
call doall.bat
popd

echo [INFO]: Building russian contest statement.
pushd statements\russian
call doall.bat
popd

