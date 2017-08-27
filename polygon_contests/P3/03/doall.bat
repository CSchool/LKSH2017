echo [INFO]: Building problem 'bipartite'.
pushd problems\bipartite
call doall.bat
popd

echo [INFO]: Building problem 'tail'.
pushd problems\tail
call doall.bat
popd

echo [INFO]: Building russian contest statement.
pushd statements\russian
call doall.bat
popd

