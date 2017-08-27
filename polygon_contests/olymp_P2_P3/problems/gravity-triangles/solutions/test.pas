var
  p1,p2,p3,m1,m2,m3,n,i:integer;
  x,y:array[1..1000] of double;
  s,max:double;
begin
  read(n);
  for i:=1 to n do read(x[i], y[i]);
  max:=-1;
  for p1:=1 to n do
    for p2:=p1 + 1 to n do
      for p3:=p2 + 1 to n do begin
        s:=sqrt((x[p1] - x[p3]) * (x[p1] - x[p3]) + (y[p1] - y[p3]) * (y[p1] - y[p3]))
          +sqrt((x[p2] - x[p3]) * (x[p2] - x[p3]) + (y[p2] - y[p3]) * (y[p2] - y[p3]))
          +sqrt((x[p1] - x[p2]) * (x[p1] - x[p2]) + (y[p1] - y[p2]) * (y[p1] - y[p2]));
        if s > max then begin
          max:=s;
          m1:=p1;
          m2:=p2;
          m3:=p3;
        end;
      end;
  writeln(x[m1]:0:6, ' ', y[m1]:0:6);
  writeln(x[m2]:0:6, ' ', y[m2]:0:6);
  writeln(x[m3]:0:6, ' ', y[m3]:0:6);
end.
