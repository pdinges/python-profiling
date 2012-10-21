Python3 Profiling Tools
=======================

The scripts in this repository convert [Python][python] profiling data
gathered using the `cProfile` module into the [Callgrind][callgrind]
and the [DOT][dot] formats.  This allows using more advanced tools to
inspect the profiles, for example the [KCacheGrind][kcachegrind]
interactive profile viewer.

The foundation for the scripts is the `callgraph` module, which
provies a graph interface for `pstats.Stats` compatible objects.  It
can be used, for example, to provide advanced callgraph manipulation
and aggregation functions.  It should also simplify the writing of
additional conversion scripts.

Both scripts and library are written in Python3.  They were originally
part of my
[master's thesis](https://github.com/pdinges/python-schoof/blob/master/),
but should be useful on their own.


Format Conversion Scripts
-------------------------

### `profile_to_callgrind.py`

The script converts execution profile dumps generated with the
`cProfile` module to a file in the [Callgrind][callgrind] format
(typically named `callgrind.out...`).  The Callgrind format is widely
supported in profiling tools.  For example, the excellent profile
inspection tool [KCacheGrind][kcachegrind] supports Callgrind files.
This script accepts several profile dumps as input and allows some
aggregation and grouping of the data.

**Usage:** `profile_to_callgrind.py` *<list_of_profile_file_paths>*

**Options:**
 * `-h`, `--help`: show the help message and exit `-o FILE`,
 * `--output-name=FILE`: Write output to `FILE` instead of
   `callgrind.out.FIRST_INPUT_FILE` Use `-` to have the output written
   to the terminal (stdout).
 * `-w`, `--overwrite`: Overwrite the output file if it already
   exists.


### `profile_to_dot.py`

The script creates (call) graphs in the [DOT][dot] format from
execution profile dumps generated with the `cProfile` module.  The DOT
file format is common for graph visualization tools; it comes from the
[Graphviz][graphviz] package.  The script accepts several profile
dumps as input and allows some aggregation and grouping of the data.

**Usage:** `profile_to_dot.py` *<list_of_profile_file_paths>*

**Options:**
 * `-h`, `--help`:        show this help message and exit
 * `-o FILE`, `--output-name=FILE`: Write output to `FILE` instead of
   `FIRST_INPUT_FILE.dot` Use `-` to have the output written to the
   terminal (stdout).
 * `-w`, `--overwrite`: Overwrite the output file if it already
   exists.
 * `-t PERCENT`, `--threshold=PERCENT`: Ignore all functions with less
   than `PERCENT` part in the total execution time


Call Graph Library
------------------

The class `CallGraph` in the `callgraph` module (`callgraph.py`)
implements a directed bipartite graph of functions and calls between
them.
    
A call graph represents the data of `pstats.Stats` instances: it
interprets the functions and their mutual invocations in the profile
as nodes (see the classes `Function` and `Call`).  All profiling data
is accessible via respective node methods.
    
The graph is easy to traverse both forwards (from caller to callee)
and backwards (from callee to caller). Its purpose is to support
operations that are difficult to express in the list-sorting style of
`pstats.Stats`.  Examples of such operations are pruning of execution
branches, and merging of nodes.

The class can merge multiple `pstats.Stats` objects a single call
graph.

License
-------

Copyright (c) 2010--2012 Peter Dinges <pdinges@acm.org>.

The software in this repository is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

The software is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the
[GNU General Public License][gpl3] along with this program.  If not,
see <http://www.gnu.org/licenses/>.



[callgrind]: http://valgrind.org/info/tools.html "Callgrind is part of the Valgrind tool suite"
[dot]: http://en.wikipedia.org/wiki/DOT_language "DOT Graph Description Language"
[gpl3]: http://opensource.org/licenses/GPL-3.0 "GNU General Public License, version 3"
[graphviz]: http://www.graphviz.org/ "Graph Visualization Software"
[kcachegrind]: http://kcachegrind.sourceforge.net/html/Home.html "Interactive viewer for Callgrind files."
[python]: http://python.org "Python Programming Language"
