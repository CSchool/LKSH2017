


{$o-,q+,r+}

const
  maxn = 10000;
  maxm = 100000;

var
  n, m: integer;
  nx, ds: array[1..2*maxm] of integer;
  hd: array[1..maxn] of integer;
  z, zz: array[1..maxn] of boolean;
  l, q: integer;

procedure add(i, j: integer);
begin
  inc(l);
  ds[l] := j;
  nx[l] := hd[i];
  hd[i] := l;
end;

procedure dfs(i, p: integer);
var
  j: integer;
begin
  inc(q);
  write(i, ' ');

  if z[i] then exit;
  z[i] := true;

  j := hd[i];
  while (j <> 0) do begin
    if (ds[j] <> p) and not zz[ds[j]] then begin 
      dfs(ds[j], i);
      inc(q);
      write(i, ' ');
    end;
    j := nx[j];    
  end;

  zz[i] := true;

end;

var
  i, a, b: integer;

begin
//  reset(input, 'roads.in');
//  rewrite(output, 'roads.out');

  read(n, m);
  for i := 1 to m do begin
    read(a, b);
    add(a, b);
    add(b, a);
  end;

  writeln(2*m);

  q := 0;
  dfs(1, 0);
  assert(q = 2*m + 1);
  writeln();
end.
