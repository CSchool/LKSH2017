uses
{$IFDEF MSWINDOWS}
  unJudge17 in '..\utils\unJudge17.pas',
{$ELSE}
  unJudge17 in '../utils/unJudge17.pas',
{$ENDIF}
  sysutils;


const
  l = 1000003;
var
  h: array[0..l + 10000] of integer;
  o: integer;
  aa, bb: array[1..200000] of integer;

function hash(a, b: integer): integer;
begin
  hash := (a * 123567 + b * 13) mod l;
end;

procedure add(a, b: integer);
var
  hh: integer;
begin
  hh := hash(a, b);
  while h[hh] > 0 do begin
    assert(aa[h[hh]] <> a);
    assert(bb[h[hh]] <> b);
    assert(hh <= l + 10);
    inc(hh);
  end;
  inc(o);
  h[hh] := o;
  aa[o] := a;
  bb[o] := b; 
end;


function remove(a, b: integer): boolean;
var
  hh, hhh: integer;
begin
  hh := hash(a, b);
  if h[hh] = 0 then begin
    remove := false;
    exit;
  end;
  while (aa[h[hh]] <> a) or (bb[h[hh]] <> b) do begin
    inc(hh);
    if h[hh] = 0 then begin
      remove := false;
      exit;
    end;
  end;
  remove := true;
  h[hh] := 0;
  hhh := hh + 1;
  while (h[hhh] <> 0) do begin
    if hash(aa[h[hhh]], bb[h[hhh]]) <= hh then begin
      h[hh] := h[hhh];
      h[hhh] := 0;
      hh := hhh;
      inc(hhh);
    end else begin
      inc(hhh);
    end;
  end;
end;

var
  n, m, i, j, a, b, s, jj: integer;

 

begin
  n := inf.readinteger();
  m := inf.readInteger();

  for i := 1 to m do begin
    a := inf.readInteger();
    b := inf.readInteger();
    add(a, b);
    add(b, a);
  end;

  s := ouf.readInteger();
  if (s <> 2*m) then quit(_wa, 'Wrong length: ' + inttostr(s) + ' instead of ' + inttostr(2*m));

  jj := ouf.readInteger();
  for i := 1 to s do begin
    j := ouf.readInteger();
    if (j < 1) or (j > n) then quit(_wa, 'Incorrect number: ' + inttostr(j));
    if not remove(jj, j) then quit(_wa, 'Road ' + inttostr(jj) + '---' + inttostr(j) + ' not exist or passed twice');
    jj := j;
  end;
  quit(_ok, '');
end.