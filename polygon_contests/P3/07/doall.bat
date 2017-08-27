echo [INFO]: Building problem 'dijkstra'.
pushd problems\dijkstra
call doall.bat
popd

echo [INFO]: Building problem 'gas'.
pushd problems\gas
call doall.bat
popd

echo [INFO]: Building problem 'beds'.
pushd problems\beds
call doall.bat
popd

echo [INFO]: Building russian contest statement.
pushd statements\russian
call doall.bat
popd

