run-tests:
	lit -v .

.PHONY: clean
clean:
	rm -f *.o *.s .lit_test_times.txt
	rm -rf Output
