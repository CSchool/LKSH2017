{
Written by Fyodor Menshikov 22.05.2002
10:06-10:27
Modified into checker 02.08.2002
I/O filename changed 20.01.2004
I/O filename changed 10.12.2004
}
const
   space=0;
   wall=-1;
   way=-2;
   deltai:array[1..8]of integer=(2,-2,2,-2,1,-1,1,-1);
   deltaj:array[1..8]of integer=(1,1,-1,-1,2,2,-2,-2);
var
   a:array[-1..52,-1..52]of integer;
   n:integer;
   fi,fj:integer;

   procedure ac;
   begin
      writeln('ok');
      halt(0);
   end;

   procedure wa;
   begin
      writeln('wa');
      halt(1);
   end;

   procedure pe;
   begin
      writeln('pe'{,id});
      halt(2);
   end;

   procedure ie(message:string);
   begin
      writeln('Internal error: ',message);
      halt(3);
   end;

   procedure check;
   var
      firstline:string;
      u:array[-1..52,-1..52]of char;
      i,j,q:integer;
      ii,jj:integer;
      moves:integer;
      cnt:integer;
   begin
      assign(input,paramstr(2));
      reset(input);
      readln(firstline);
      if firstline='Impossible' then begin
         if not eof then
            pe;
         if a[fi,fj]=space then
            ac
         else
            wa;
      end;
      for i:=-1 to 52 do
         for j:=-1 to 52 do
            u[i,j]:='.';
      reset(input);
      for i:=1 to n do begin
         for j:=1 to n do begin
            if eoln then
               pe;
            read(u[i,j]);
         end;
         if not eoln then
            pe;
         readln;
      end;
      if not eof then
         pe;
      for i:=1 to n do
         for j:=1 to n do begin
            if not(u[i,j] in ['@','.','#']) then
               pe;
            if (a[i,j]=wall)xor(u[i,j]='#') then
               pe;
         end;
      for i:=1 to n do
         for j:=1 to n do
            if a[i,j]=1 then begin
               if u[i,j]<>'@' then
                  pe;
               ii:=i;
               jj:=j;
            end;
      moves:=1;
      while true do begin
         cnt:=0;
         for q:=1 to 8 do
            if u[ii+deltai[q],jj+deltaj[q]]='@' then
               inc(cnt);
         case cnt of
         0:break;
         1:begin
            inc(moves);
            u[ii,jj]:='.';
            for q:=1 to 8 do
               if u[ii+deltai[q],jj+deltaj[q]]='@' then begin
                  ii:=ii+deltai[q];
                  jj:=jj+deltaj[q];
                  break;
               end;
         end;
         else
            pe;
         end;
      end;
      u[ii,jj]:='.';
      for i:=1 to n do
         for j:=1 to n do
            if u[i,j]='@' then
               pe;
      if (ii<>fi)or(jj<>fj) then
         pe;
      if moves<>a[ii,jj] then
         wa;
      ac;
   end;

var
   i,j,q:integer;
   wasstart:boolean;
   c:char;
   changed:boolean;
   pass:integer;
begin
   assign(input,paramstr(1));
   reset(input);
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
   check;
end.
