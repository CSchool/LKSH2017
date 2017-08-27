const
   free=-1;
   wall=-2;
var
   a:array[1..30,1..30,1..30]of integer;
   n:integer;
type
   tqueue=array[1..30*30*30]of byte;
var
   first,last:integer;
   ii,jj,kk:^tqueue;

   procedure initQueue;
   begin
      new(ii);
      new(jj);
      new(kk);
      first:=1;
      last:=0;
   end;

   procedure put(i,j,k:byte);
   begin
      inc(last);
      ii^[last]:=i;
      jj^[last]:=j;
      kk^[last]:=k;
   end;

   procedure get(var i,j,k:byte);
   begin
      i:=ii^[first];
      j:=jj^[first];
      k:=kk^[first];
      inc(first);
   end;

   function queueNotEmpty:boolean;
   begin
      queueNotEmpty:=first<=last;
   end;

var
   wasS:boolean;
   c:char;
   i,j,k:byte;
   min:integer;
begin
   readln(n);
   wasS:=false;
   for i:=1 to n do begin
      readln;
      for j:=1 to n do begin
         for k:=1 to n do begin
            read(c);
            case c of
            '.':a[i,j,k]:=free;
            '#':a[i,j,k]:=wall;
            'S':begin
               if wasS then
                  halt(1);
               a[i,j,k]:=0;
               initQueue;
               put(i,j,k);
               wasS:=true;
            end;
            else
               halt(1);
            end;
         end;
         readln;
      end;
   end;
   if not wasS then
      halt(1);
   while queueNotEmpty do begin
      get(i,j,k);
      if (i>1)and(a[i-1,j,k]=free) then begin
         a[i-1,j,k]:=a[i,j,k]+1;
         put(i-1,j,k);
      end;
      if (j>1)and(a[i,j-1,k]=free) then begin
         a[i,j-1,k]:=a[i,j,k]+1;
         put(i,j-1,k);
      end;
      if (k>1)and(a[i,j,k-1]=free) then begin
         a[i,j,k-1]:=a[i,j,k]+1;
         put(i,j,k-1);
      end;
      if (i<n)and(a[i+1,j,k]=free) then begin
         a[i+1,j,k]:=a[i,j,k]+1;
         put(i+1,j,k);
      end;
      if (j<n)and(a[i,j+1,k]=free) then begin
         a[i,j+1,k]:=a[i,j,k]+1;
         put(i,j+1,k);
      end;
      if (k<n)and(a[i,j,k+1]=free) then begin
         a[i,j,k+1]:=a[i,j,k]+1;
         put(i,j,k+1);
      end;
   end;
   min:=maxint;
   for j:=1 to n do
      for k:=1 to n do
         if (a[1,j,k]>=0) and (a[1,j,k]<min) then
            min:=a[1,j,k];
   if min=maxint then
      halt(1);
   writeln(min);
end.