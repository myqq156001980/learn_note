mysql -uuser -ppassword -hhost db -e "select * from table_name" | sed 's/\t/","/g;s/^/"/;s/$/"/' > test.csv
