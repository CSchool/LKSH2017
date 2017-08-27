label
   01;
const
   space=0;
   wall=-1;
   way=-2;
   deltai:array[1..8]of integer=(2,-2,2,-2,1,-1,1,-1);
   deltaj:array[1..8]of integer=(1,1,-1,-1,2,2,-2,-2);
var
   n,i,j,k,q:integer;
   a:array[-1..52,-1..52]of integer;
   wasstart:boolean;
   fi,fj:integer;
   c:char;
   changed:boolean;
   pass:integer;
begin
   readln(n);
   for i:=-1 to n+2 do
      for j:=-1 to n+2 do
         a[i,j]:=wall;
   wasstart:=false;
   for i:=1 to n do begin
      for j:=1 to n do begin
         read(c);
         case c of
         '@':begin
            if not wasstart then begin
               a[i,j]:=1;
               wasstart:=true;
            end
            else begin
               a[i,j]:=space;
               fi:=i;
               fj:=j;
            end;
         end;
         '.':a[i,j]:=space;
         '#':a[i,j]:=wall;
         else
            halt(1);
         end;
      end;
      readln;
   end;
   pass:=0;
   repeat
      inc(pass);
      changed:=false;
      for i:=1 to n do
         for j:=1 to n do
            if a[i,j]=pass then
               for q:=1 to 8 do
                  if a[i+deltai[q],j+deltaj[q]]=space then begin
                     a[i+deltai[q],j+deltaj[q]]:=pass+1;
                     changed:=true;
                  end;
   until not changed;
   if a[fi,fj]=space then begin
      writeln('Impossible');
      halt;
   end;
01:
   for q:=1 to 8 do
      if a[fi+deltai[q],fj+deltaj[q]]=a[fi,fj]-1 then begin
         a[fi,fj]:=way;
         fi:=fi+deltai[q];
         fj:=fj+deltaj[q];
         goto 01;
      end;
   a[fi,fj]:=way;{first}
   for i:=1 to n do begin
      for j:=1 to n do begin
         case a[i,j] of
         wall:write('#');
         way:write('@');
         else
            write('.');
         end;
      end;
      writeln;
   end;
end.