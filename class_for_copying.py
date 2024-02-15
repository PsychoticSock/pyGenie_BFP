from __future__ import annotations

from copy import deepcopy

class DatFileObject:
    def __deepcopy__(self, memo):
        print(f"Class: {self.__class__.__name__} \n\t Dict options: {self.__dict__.keys()} \n memo: {memo}")
        #exit()
        cls =    self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            #print(f"key is {k}, value is {v}, name is {k.title()}")
            entry = self._deepcopy_entry(k, v)
            #print("ENTRY", entry)
            if entry is None:
                continue
            setattr(result, k, entry)
        return result

    def _deepcopy_entry(self, k, v):
        #print(f"Getting Key {k}, Value {v}")
        if k in ['_sections', '_link_list']:  #'_resource_storage', '_damage_graphics',
            val = getattr(self, k)
        else:
            val = deepcopy(v)
            #print(val)
        return val