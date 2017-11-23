select * from appropriation as ap
where exists (select 1
from appropriation as other
where ap.rowid <> other.rowid
and ap.tas_with_sub = other.tas_with_sub);