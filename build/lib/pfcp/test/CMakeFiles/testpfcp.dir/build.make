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
include lib/pfcp/test/CMakeFiles/testpfcp.dir/depend.make

# Include the progress variables for this target.
include lib/pfcp/test/CMakeFiles/testpfcp.dir/progress.make

# Include the compile flags for this target's objects.
include lib/pfcp/test/CMakeFiles/testpfcp.dir/flags.make

lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o: lib/pfcp/test/CMakeFiles/testpfcp.dir/flags.make
lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o: ../lib/pfcp/test/test.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/stage3/src/upf/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o"
	cd /home/ubuntu/stage3/src/upf/build/lib/pfcp/test && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/testpfcp.dir/test.c.o   -c /home/ubuntu/stage3/src/upf/lib/pfcp/test/test.c

lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/testpfcp.dir/test.c.i"
	cd /home/ubuntu/stage3/src/upf/build/lib/pfcp/test && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/stage3/src/upf/lib/pfcp/test/test.c > CMakeFiles/testpfcp.dir/test.c.i

lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/testpfcp.dir/test.c.s"
	cd /home/ubuntu/stage3/src/upf/build/lib/pfcp/test && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/stage3/src/upf/lib/pfcp/test/test.c -o CMakeFiles/testpfcp.dir/test.c.s

lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o.requires:

.PHONY : lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o.requires

lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o.provides: lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o.requires
	$(MAKE) -f lib/pfcp/test/CMakeFiles/testpfcp.dir/build.make lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o.provides.build
.PHONY : lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o.provides

lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o.provides.build: lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o


# Object files for target testpfcp
testpfcp_OBJECTS = \
"CMakeFiles/testpfcp.dir/test.c.o"

# External object files for target testpfcp
testpfcp_EXTERNAL_OBJECTS =

lib/pfcp/test/home/ubuntu/stage3/src/upf/build/bin/testpfcp: lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o
lib/pfcp/test/home/ubuntu/stage3/src/upf/build/bin/testpfcp: lib/pfcp/test/CMakeFiles/testpfcp.dir/build.make
lib/pfcp/test/home/ubuntu/stage3/src/upf/build/bin/testpfcp: lib/pfcp/test/CMakeFiles/testpfcp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/stage3/src/upf/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable /home/ubuntu/stage3/src/upf/build/bin/testpfcp"
	cd /home/ubuntu/stage3/src/upf/build/lib/pfcp/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/testpfcp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/pfcp/test/CMakeFiles/testpfcp.dir/build: lib/pfcp/test/home/ubuntu/stage3/src/upf/build/bin/testpfcp

.PHONY : lib/pfcp/test/CMakeFiles/testpfcp.dir/build

lib/pfcp/test/CMakeFiles/testpfcp.dir/requires: lib/pfcp/test/CMakeFiles/testpfcp.dir/test.c.o.requires

.PHONY : lib/pfcp/test/CMakeFiles/testpfcp.dir/requires

lib/pfcp/test/CMakeFiles/testpfcp.dir/clean:
	cd /home/ubuntu/stage3/src/upf/build/lib/pfcp/test && $(CMAKE_COMMAND) -P CMakeFiles/testpfcp.dir/cmake_clean.cmake
.PHONY : lib/pfcp/test/CMakeFiles/testpfcp.dir/clean

lib/pfcp/test/CMakeFiles/testpfcp.dir/depend:
	cd /home/ubuntu/stage3/src/upf/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/stage3/src/upf /home/ubuntu/stage3/src/upf/lib/pfcp/test /home/ubuntu/stage3/src/upf/build /home/ubuntu/stage3/src/upf/build/lib/pfcp/test /home/ubuntu/stage3/src/upf/build/lib/pfcp/test/CMakeFiles/testpfcp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/pfcp/test/CMakeFiles/testpfcp.dir/depend

