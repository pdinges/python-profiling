# -*- coding: utf-8 -*-

# Copyright (c) 2010--2012  Peter Dinges <pdinges@acm.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


def apply_threshold( callgraph, threshold ):
    """Prune functions with less than @p threshold percent total cost""" 
    threshold = int( threshold * callgraph.total_time() )
    insignificant_functions = [ f for f in callgraph if f.cumulative_time() < threshold ]
    for function in insignificant_functions:
        callgraph.treat_as_builtin( function )
        assert( not function.valid() )
