ifeq ($(test),testcase0)
	delay = 5
else ifeq ($(test),testcase1)
	delay = 10
else ifeq ($(test),testcase2)
	delay = 10
else ifeq ($(test),testcase3)
	delay =  15
	error = sleep error
else
	delay = 3
endif

clean:
	echo "this is clean task"

build:
	echo $(test)
	sleep $(delay)
	$(error)
	echo "this is build task"

compiler:
	echo $(test)
	sleep $(delay)
	$(error)
	echo "this is compiler task"

run:
	echo $(test)
	sleep $(delay)
	$(error)
	echo "this is run task"