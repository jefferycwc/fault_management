# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/stage3/src/upf

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/stage3/src/upf/build

# Include any dependencies generated for this target.
include lib/knet/CMakeFiles/free5GC_knet_test.dir/depend.make

# Include the progress variables for this target.
include lib/knet/CMakeFiles/free5GC_knet_test.dir/progress.make

# Include the compile flags for this target's objects.
include lib/knet/CMakeFiles/free5GC_knet_test.dir/flags.make

lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o: lib/knet/CMakeFiles/free5GC_knet_test.dir/flags.make
lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o: ../lib/knet/test.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/stage3/src/upf/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o"
	cd /home/ubuntu/stage3/src/upf/build/lib/knet && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/free5GC_knet_test.dir/test.c.o   -c /home/ubuntu/stage3/src/upf/lib/knet/test.c

lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/free5GC_knet_test.dir/test.c.i"
	cd /home/ubuntu/stage3/src/upf/build/lib/knet && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/stage3/src/upf/lib/knet/test.c > CMakeFiles/free5GC_knet_test.dir/test.c.i

lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/free5GC_knet_test.dir/test.c.s"
	cd /home/ubuntu/stage3/src/upf/build/lib/knet && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/stage3/src/upf/lib/knet/test.c -o CMakeFiles/free5GC_knet_test.dir/test.c.s

lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o.requires:

.PHONY : lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o.requires

lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o.provides: lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o.requires
	$(MAKE) -f lib/knet/CMakeFiles/free5GC_knet_test.dir/build.make lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o.provides.build
.PHONY : lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o.provides

lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o.provides.build: lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o


# Object files for target free5GC_knet_test
free5GC_knet_test_OBJECTS = \
"CMakeFiles/free5GC_knet_test.dir/test.c.o"

# External object files for target free5GC_knet_test
free5GC_knet_test_EXTERNAL_OBJECTS =

lib/knet/home/ubuntu/stage3/src/upf/build/bin/testknet: lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o
lib/knet/home/ubuntu/stage3/src/upf/build/bin/testknet: lib/knet/CMakeFiles/free5GC_knet_test.dir/build.make
lib/knet/home/ubuntu/stage3/src/upf/build/bin/testknet: lib/utlt/libfree5GC_utlt.a
lib/knet/home/ubuntu/stage3/src/upf/build/bin/testknet: lib/knet/libfree5GC_knet.a
lib/knet/home/ubuntu/stage3/src/upf/build/bin/testknet: lib/utlt/libfree5GC_utlt.a
lib/knet/home/ubuntu/stage3/src/upf/build/bin/testknet: lib/knet/CMakeFiles/free5GC_knet_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/stage3/src/upf/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable /home/ubuntu/stage3/src/upf/build/bin/testknet"
	cd /home/ubuntu/stage3/src/upf/build/lib/knet && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/free5GC_knet_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/knet/CMakeFiles/free5GC_knet_test.dir/build: lib/knet/home/ubuntu/stage3/src/upf/build/bin/testknet

.PHONY : lib/knet/CMakeFiles/free5GC_knet_test.dir/build

lib/knet/CMakeFiles/free5GC_knet_test.dir/requires: lib/knet/CMakeFiles/free5GC_knet_test.dir/test.c.o.requires

.PHONY : lib/knet/CMakeFiles/free5GC_knet_test.dir/requires

lib/knet/CMakeFiles/free5GC_knet_test.dir/clean:
	cd /home/ubuntu/stage3/src/upf/build/lib/knet && $(CMAKE_COMMAND) -P CMakeFiles/free5GC_knet_test.dir/cmake_clean.cmake
.PHONY : lib/knet/CMakeFiles/free5GC_knet_test.dir/clean

lib/knet/CMakeFiles/free5GC_knet_test.dir/depend:
	cd /home/ubuntu/stage3/src/upf/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/stage3/src/upf /home/ubuntu/stage3/src/upf/lib/knet /home/ubuntu/stage3/src/upf/build /home/ubuntu/stage3/src/upf/build/lib/knet /home/ubuntu/stage3/src/upf/build/lib/knet/CMakeFiles/free5GC_knet_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/knet/CMakeFiles/free5GC_knet_test.dir/depend
