CC=gcc
CFLAGS=-O0 -fno-pie -no-pie -fno-stack-protector -fcf-protection=none -z execstack

BIN=cs101-hw1
SRC=shellcodebasic.c

all: $(BIN)

$(BIN): $(SRC)
	$(CC) -o $@ $(CFLAGS) $^

clean:
	rm $(BIN)
