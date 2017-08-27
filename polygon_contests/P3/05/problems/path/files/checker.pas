{$MODE DELPHI}
uses
{$IFDEF MSWINDOWS}
  unJudge17 in '..\utils\unJudge17.pas';
{$ELSE}
  unJudge17 in '../utils/unJudge17.pas';
{$ENDIF}
const nmax=100;
var
      a:array[1..nmax,1..nmax] of integer;
      l,la:integer;
      n:integer;
      i,j:integer;
      vc,vn:integer;
      v1,v2:integer;


begin
n:=inf.readinteger;
for i:=1 to n do
  for j:=1 to n do
    a[i,j]:=inf.readinteger;
v1:=inf.readinteger;
v2:=inf.readinteger;


l:=ouf.readinteger;
la:=ans.readinteger;

if l=-1 then begin
  if la=-1 then quit(_OK,'ok, no path');
  quit(_WA,'Path actually exists');
  end;


vc:=ouf.readinteger;
if vc<>v1 then quit(_WA,'Path begins in wrong vertex');
for i:=1 to l do begin
  vn:=ouf.readinteger;
  if a[vc,vn]=0 then quit(_WA,'No such edge');
  vc:=vn;
  end;
if vc<>v2 then quit(_WA,'Path ends in wrong vertex');
if (l<la) or (la=-1) then quit(_Fail,'Answer is better than pattern');
if l>la then quit(_WA,'Path is not shortest');
quit(_OK,'ok, path exists');
end.



end.
