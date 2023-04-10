run-tests:
	lit -v .

.PHONY: clean
clean:
	rm *.o *.s .lit_test_times.txt
	rm -r Output
