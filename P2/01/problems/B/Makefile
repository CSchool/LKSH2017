### BEGIN ejudge auto-generated makefile ###
EJUDGE_PREFIX_DIR ?= /opt/ejudge
EJUDGE_CONTESTS_HOME_DIR ?= /home/judges
EJUDGE_SERVER_BIN_PATH ?= /opt/ejudge/bin

CXX = /usr/bin/g++-6
CXXFLAGS = -O2 -std=gnu++11
CXXLIBCHECKERFLAGS = -Wall -g -O2 -I${EJUDGE_PREFIX_DIR}/include/ejudge -L${EJUDGE_PREFIX_DIR}/lib64 -Wl,--rpath,${EJUDGE_PREFIX_DIR}/lib64
CXXLIBCHECKERLIBS = -lchecker -lm

EXECUTE = ${EJUDGE_PREFIX_DIR}/bin/ejudge-execute
EXECUTE_FLAGS =  --use-stdin --use-stdout --test-pattern=%03d.dat --corr-pattern=%03d.ans

NORMALIZE = ${EJUDGE_SERVER_BIN_PATH}/ej-normalize
NORMALIZE_FLAGS = --workdir=tests --test-pattern=%03d.dat --corr-pattern=%03d.ans

all : check
check_settings : all normalize


check : check.cpp
	${CXX} -DEJUDGE ${CXXLIBCHECKERFLAGS} check.cpp -ocheck ${CXXLIBCHECKERLIBS}


normalize :
	${NORMALIZE} ${NORMALIZE_FLAGS} --all-tests

clean :
	-rm -f *.o *.class *.exe *~ *.bak check

### END ejudge auto-generated makefile ###
