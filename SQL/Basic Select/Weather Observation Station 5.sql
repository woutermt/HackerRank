/*

*/
select * from (
select CITY, length(city) from STATION order by length(city) asc, city asc limit 1) tblmin
UNION
select * from (
select CITY, Length(city) from STATION order by Length(city)desc, city asc limit 1) tblmax