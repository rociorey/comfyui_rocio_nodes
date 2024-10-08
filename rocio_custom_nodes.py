import math
import re

class RocioBranchNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "caption": ("STRING", {"forceInput": True}),  # Input string: "yes" or "no"
                "image_yes": ("IMAGE",),  # Image if caption indicates "yes"
                "image_no": ("IMAGE",),  # Image if caption indicates "no"
            }
        }

    RETURN_TYPES = ("IMAGE",)  # Output: The selected image
    FUNCTION = "select_image"
    
    CATEGORY = "Image Processing"

    def select_image(self, caption, image_yes, image_no):
        # Check if the caption indicates "yes" (case insensitive)
        if caption.strip().lower() == "yes":
            return (image_yes,)  # Output the first image if caption is "yes"
        else:
            return (image_no,)  # Output the second image if caption is anything else
        


class RocioConditionalPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_string": ("STRING", {"default": "", "multiline": False}),
                "prompt_for_brown": ("STRING", {"default": "Prompt if brown", "multiline": True}),
                "prompt_for_other": ("STRING", {"default": "Prompt if not brown", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "check_string"

    CATEGORY = "Conditionals"

    def check_string(self, input_string, prompt_for_brown, prompt_for_other):
        # Ensure string comparison is case-insensitive
        if input_string.strip().lower() == "brown":
            return (prompt_for_brown,)
        else:
            return (prompt_for_other,)

class RocioResizeImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "width": ("INT", {"forceInput": True}),
                "height": ("INT", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "process_resize"


    def process_resize(self, images, width, height):
        return (process_resize_image(images, width, height),)
    

NODE_CLASS_MAPPINGS = {
    "RocioBranchNode": RocioBranchNode,
    "RocioConditionalPrompt": RocioConditionalPrompt,
    "RocioResizeImage": RocioResizeImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RocioBranchNode": "Rocio Image Branch",
    "RocioConditionalPrompt": "Rocio Conditional Prompt",
    "RocioResizeImage": "Rocio Resize Image"
}
