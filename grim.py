from typing import Optional, List
from dataclasses import dataclass
from folder_paths import get_folder_paths

class TwoStringsFormat:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "string1": ("STRING", {"multiline": False}),
            "string2": ("STRING", {"multiline": False}),
            "format": ("STRING", {"multiline": True}),
        }}

    RETURN_TYPES = (["STRING"])
    FUNCTION = "encode"

    CATEGORY = "Grim/Variables"

    @classmethod
    def IS_CHANGED(s, clip, text):
        return True

    def encode(self, string1, string2, format):
        tmp = format.replace("$(string1)", string1)
        tmp = tmp.replace("$(string2)", string2)
        return (tmp,)


NODE_CLASS_MAPPINGS = {
    "TwoStringsFormat": TwoStringsFormat,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TwoStringsFormat": "Format Strings with Two Inputs",
}
