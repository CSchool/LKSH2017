echo [INFO]: Building problem 'rain'.
pushd problems\rain
call doall.bat
popd

echo [INFO]: Building problem 'complete'.
pushd problems\complete
call doall.bat
popd

echo [INFO]: Building problem 'gold'.
pushd problems\gold
call doall.bat
popd

echo [INFO]: Building problem 'mockery'.
pushd problems\mockery
call doall.bat
popd

echo [INFO]: Building problem 'two'.
pushd problems\two
call doall.bat
popd

echo [INFO]: Building problem 'nodes'.
pushd problems\nodes
call doall.bat
popd

echo [INFO]: Building russian contest statement.
pushd statements\russian
call doall.bat
popd

