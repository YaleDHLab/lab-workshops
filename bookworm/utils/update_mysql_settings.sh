echo "" >> ~/.my.cnf
echo "[client]" >> ~/.my.cnf
echo "max_allowed_packet=1073741824" >> ~/.my.cnf

echo "" >> ~/.my.cnf
echo "[mysqld]" >> ~/.my.cnf
echo "max_allowed_packet=1073741824" >> ~/.my.cnf
echo "myisam_sort_buffer_size = 512M" >> ~/.my.cnf
echo "read_rnd_buffer_size = 8M" >> ~/.my.cnf
echo "read_buffer_size = 4M" >> ~/.my.cnf
echo "max_heap_table_size = 1024M" >> ~/.my.cnf
echo "tmp_table_size = 1024M" >> ~/.my.cnf

echo "" >> ~/.my.cnf
echo "character_set_server = utf8" >> ~/.my.cnf
echo "query_cache_size = 128M" >> ~/.my.cnf
echo "query_cache_type = 1" >> ~/.my.cnf
echo "query_cache_limit = 2M" >> ~/.my.cnf

echo "" >> ~/.my.cnf
echo "bulk_insert_buffer_size = 512M" >> ~/.my.cnf
echo "myisam_max_sort_file_size = 1500G" >> ~/.my.cnf
echo "sort_buffer_size = 8M" >> ~/.my.cnf

echo "" >> ~/.my.cnf
echo "key_buffer_size=1500M" >> ~/.my.cnf
