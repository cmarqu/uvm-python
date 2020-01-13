#//----------------------------------------------------------------------
#//   Copyright 2007-2010 Mentor Graphics Corporation
#//   Copyright 2007-2011 Cadence Design Systems, Inc.
#//   Copyright 2010-2011 Synopsys, Inc.
#//   Copyright 2019-2020 Tuomas Poikela (tpoikela)
#//   All Rights Reserved Worldwide
#//
#//   Licensed under the Apache License, Version 2.0 (the
#//   "License"); you may not use self file except in
#//   compliance with the License.  You may obtain a copy of
#//   the License at
#//
#//       http://www.apache.org/licenses/LICENSE-2.0
#//
#//   Unless required by applicable law or agreed to in
#//   writing, software distributed under the License is
#//   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#//   CONDITIONS OF ANY KIND, either express or implied.  See
#//   the License for the specific language governing
#//   permissions and limitations under the License.
#//----------------------------------------------------------------------

#from typings import Dict
from uvm import (UVMComponent, UVMConfigDb, sv, uvm_get_array_index_string,
    uvm_is_match, uvm_error)


class ClassC(UVMComponent):


    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.v = 0  # type: int
        self.s = 0  # type: int
        self.myaa = {}  # Dict[str]


    def build_phase(self, phase):
        _str = []
        super().build_phase(phase)
        arr = []
        if UVMConfigDb.get(self, "", "v", arr):
            self.v = arr[0]
        arr = []
        if UVMConfigDb.get(self, "", "s", arr):
            self.s = arr[0]

        if UVMConfigDb.get(self, "", "myaa[foo]", _str):
            self.myaa["foo"] = _str[0]
            _str = []
        else:
            uvm_error("NO_CONF_MATCH", "Did not get myaa[foo]")

        if UVMConfigDb.get(self, "", "myaa[bar]", _str):
            self.myaa["bar"] = _str[0]
            _str = []
        else:
            uvm_error("NO_CONF_MATCH", "Did not get myaa[bar]")

        if UVMConfigDb.get(self, "", "myaa[foobar]", _str):
            self.myaa["foobar"] = _str[0]
            _str = []
        else:
            uvm_error("NO_CONF_MATCH", "Did not get myaa[foobar]")


    def get_type_name(self):
        return "C"

    def do_print(self, printer):
        printer.print_field("v", self.v, 32)
        printer.print_field("s", self.s, 32)
        printer.print_array_header("myaa", len(self.myaa), "aa_string_string")
        for key in self.myaa:
            printer.print_string(sv.sformatf("myaa[%0s]", key), self.myaa[key])
        printer.print_array_footer()


    def set_string_local(self, field_name, value, recurse=1):
        index = ""
        wildcarded = 0
        #call the super function to get child recursion and any registered fields
        super().set_string_local(field_name, value, recurse)

        index = uvm_get_array_index_string(field_name, wildcarded)
        if (not wildcarded and uvm_is_match(field_name, "myaa[" + index, "]")):
            self.myaa[index] = value
