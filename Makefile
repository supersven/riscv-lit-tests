run-tests: clean
	lit -v .

.PHONY: clean verbose very-verbose
verbose:
	lit -vv .

very-verbose:
	lit --show-all .

clean:
	rm -f **/*.o **/*.a.out **/*.s .lit_test_times.txt
	rm -rf **/Output
