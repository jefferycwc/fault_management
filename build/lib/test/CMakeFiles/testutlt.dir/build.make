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
include lib/test/CMakeFiles/testutlt.dir/depend.make

# Include the progress variables for this target.
include lib/test/CMakeFiles/testutlt.dir/progress.make

# Include the compile flags for this target's objects.
include lib/test/CMakeFiles/testutlt.dir/flags.make

lib/test/CMakeFiles/testutlt.dir/test.c.o: lib/test/CMakeFiles/testutlt.dir/flags.make
lib/test/CMakeFiles/testutlt.dir/test.c.o: ../lib/test/test.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/stage3/src/upf/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object lib/test/CMakeFiles/testutlt.dir/test.c.o"
	cd /home/ubuntu/stage3/src/upf/build/lib/test && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/testutlt.dir/test.c.o   -c /home/ubuntu/stage3/src/upf/lib/test/test.c

lib/test/CMakeFiles/testutlt.dir/test.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/testutlt.dir/test.c.i"
	cd /home/ubuntu/stage3/src/upf/build/lib/test && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/stage3/src/upf/lib/test/test.c > CMakeFiles/testutlt.dir/test.c.i

lib/test/CMakeFiles/testutlt.dir/test.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/testutlt.dir/test.c.s"
	cd /home/ubuntu/stage3/src/upf/build/lib/test && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/stage3/src/upf/lib/test/test.c -o CMakeFiles/testutlt.dir/test.c.s

lib/test/CMakeFiles/testutlt.dir/test.c.o.requires:

.PHONY : lib/test/CMakeFiles/testutlt.dir/test.c.o.requires

lib/test/CMakeFiles/testutlt.dir/test.c.o.provides: lib/test/CMakeFiles/testutlt.dir/test.c.o.requires
	$(MAKE) -f lib/test/CMakeFiles/testutlt.dir/build.make lib/test/CMakeFiles/testutlt.dir/test.c.o.provides.build
.PHONY : lib/test/CMakeFiles/testutlt.dir/test.c.o.provides

lib/test/CMakeFiles/testutlt.dir/test.c.o.provides.build: lib/test/CMakeFiles/testutlt.dir/test.c.o


# Object files for target testutlt
testutlt_OBJECTS = \
"CMakeFiles/testutlt.dir/test.c.o"

# External object files for target testutlt
testutlt_EXTERNAL_OBJECTS =

lib/test/home/ubuntu/stage3/src/upf/build/bin/testutlt: lib/test/CMakeFiles/testutlt.dir/test.c.o
lib/test/home/ubuntu/stage3/src/upf/build/bin/testutlt: lib/test/CMakeFiles/testutlt.dir/build.make
lib/test/home/ubuntu/stage3/src/upf/build/bin/testutlt: lib/utlt/libfree5GC_utlt.a
lib/test/home/ubuntu/stage3/src/upf/build/bin/testutlt: lib/test/libfree5GC_utlt_test.a
lib/test/home/ubuntu/stage3/src/upf/build/bin/testutlt: lib/utlt/libfree5GC_utlt.a
lib/test/home/ubuntu/stage3/src/upf/build/bin/testutlt: lib/test/CMakeFiles/testutlt.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/stage3/src/upf/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable /home/ubuntu/stage3/src/upf/build/bin/testutlt"
	cd /home/ubuntu/stage3/src/upf/build/lib/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/testutlt.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/test/CMakeFiles/testutlt.dir/build: lib/test/home/ubuntu/stage3/src/upf/build/bin/testutlt

.PHONY : lib/test/CMakeFiles/testutlt.dir/build

lib/test/CMakeFiles/testutlt.dir/requires: lib/test/CMakeFiles/testutlt.dir/test.c.o.requires

.PHONY : lib/test/CMakeFiles/testutlt.dir/requires

lib/test/CMakeFiles/testutlt.dir/clean:
	cd /home/ubuntu/stage3/src/upf/build/lib/test && $(CMAKE_COMMAND) -P CMakeFiles/testutlt.dir/cmake_clean.cmake
.PHONY : lib/test/CMakeFiles/testutlt.dir/clean

lib/test/CMakeFiles/testutlt.dir/depend:
	cd /home/ubuntu/stage3/src/upf/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/stage3/src/upf /home/ubuntu/stage3/src/upf/lib/test /home/ubuntu/stage3/src/upf/build /home/ubuntu/stage3/src/upf/build/lib/test /home/ubuntu/stage3/src/upf/build/lib/test/CMakeFiles/testutlt.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/test/CMakeFiles/testutlt.dir/depend
