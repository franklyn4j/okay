function parse_ls {

	ls -la | grep -v total | awk '{print $1}' | while read line
	do
		echo $line
	done

}

parse_ls
