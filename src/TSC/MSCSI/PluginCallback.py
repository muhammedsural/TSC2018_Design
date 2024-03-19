

from dataclasses import dataclass


@dataclass
class PluginCallback:
    ErrorFlag : int
    Finished  : bool

    def Finish(self,iVal : int) ->None:
        pass
