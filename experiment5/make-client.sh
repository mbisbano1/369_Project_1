arg1=$1
arg2=$2
arg3=$3
arg4=$4

#compile
gcc -std=c89 -pedantic -Wall \
    -Wno-missing-braces -Wextra -Wno-missing-field-initializers -Wformat=2 \
    -Wswitch-default -Wswitch-enum -Wcast-align -Wpointer-arith \
    -Wbad-function-cast -Wstrict-overflow=5 -Wstrict-prototypes -Winline \
    -Wundef -Wnested-externs -Wcast-qual -Wshadow -Wunreachable-code \
    -Wlogical-op -Wfloat-equal -Wstrict-aliasing=2 -Wredundant-decls \
    -Wold-style-definition \
    -ggdb3 \
    -O0 \
    -fno-omit-frame-pointer -ffloat-store -fno-common -fstrict-aliasing \
    -lm \
    UDPClientTimer.c -o exec-UDPClientTimer


if [[ $? -eq 0 ]]; then
	valgrind --leak-check=full \
		 --show-leak-kinds=all \
		 --track-origins=yes \
		 --quiet \
		 ./exec-UDPClientTimer $arg1 $arg2 $arg3 $arg4
else
	echo Build failed, not executing
fi

