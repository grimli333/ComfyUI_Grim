from typing import Optional, List
from dataclasses import dataclass
from folder_paths import get_folder_paths
from datetime import datetime

class GenerateFileName:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "prefix": ("STRING", ),
            "folder": ("STRING", {"default": ""}),
        }}
    
    RETURN_TYPES = ("STRING","STRING","STRING")
    RETURN_NAMES = ("full_pathname", "prefix_only", "folder_only")

    FUNCTION = "generate_filename"

    @classmethod
    def IS_CHANGED(s, prefix):
        return float("NaN")

    def generate_filename(self, prefix):
        timestamp = datetime.now().strftime("@%Y%m%d-%H%M%S")
        if(self.folder != ""):
            folder = self.folder
        else:
            folder = "{prefix}_{timestamp}".format(prefix=prefix, timestamp=timestamp)

        full_pathname = "{folder}/{prefix}_{timestamp}".format(folder=folder, prefix=prefix, timestamp=timestamp)
        return (full_pathname, prefix, folder)

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
    "GenerateFileName": GenerateFileName,
    "TwoStringsFormat": TwoStringsFormat,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GenerateFileName": "Generate a unique filename and folder name",
    "TwoStringsFormat": "Format Strings with Two Inputs",
}
