var
   c:array[0..201,0..201]of char;

type
   arr=array[1..40000]of byte;
var
   sp:word;
   ii,jj:^arr;

   procedure push(i,j:integer);
   begin
      if c[i,j]='#' then begin
         inc(sp);
         ii^[sp]:=i;
         jj^[sp]:=j;
         c[i,j]:='.';
      end;
   end;

   procedure pop(var i,j:integer);
   begin
      i:=ii^[sp];
      j:=jj^[sp];
      dec(sp);
   end;

   procedure paint(i,j:integer);
   begin
      sp:=0;
      push(i,j);
      while sp>0 do begin
         pop(i,j);
         push(i+1,j);
         push(i-1,j);
         push(i,j+1);
         push(i,j-1);
      end;
   end;

var
   n,m,i,j:integer;
   count:integer;
begin
   new(ii);
   new(jj);
   readln(n,m);
   for i:=0 to n+1 do
      for j:=0 to m+1 do
         c[i,j]:='.';
   for i:=1 to n do begin
      for j:=1 to m do
         read(c[i,j]);
      readln;
   end;
   count:=0;
   for i:=1 to n do
      for j:=1 to m do
         if c[i,j]='#' then begin
            paint(i,j);
            inc(count);
         end;
   writeln(count);
end.
