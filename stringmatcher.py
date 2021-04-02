from typing import Dict, Union


def matchString(inputStr: str, matchDict: Dict[Union[str, callable], callable]) -> (bool, tuple):
    for k, v_func in matchDict.items():
        k_val = (k(inputStr) if callable(k) else (k == inputStr))
        if k_val:
            return True, (v_func(inputStr),)
    else:
        return False, ()
