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
        


class RocioImageSizer:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_type": (["SD","SDXL"],),
                "aspect_ratio_width": ("INT",{
                    "default": 1,
                    "step":1,
                    "display": "number"
                }),
                "aspect_ratio_height": ("INT",{
                    "default": 1,
                    "step":1,
                    "display": "number"
                })
            }
        }

    RETURN_TYPES = ("INT","INT")
    RETURN_NAMES = ("Width", "Height")

    FUNCTION = "run"

    CATEGORY = "CodyCustom"

    def run(self, model_type, aspect_ratio_width, aspect_ratio_height):
        # Define the total pixel counts for SD and SDXL
        total_pixels = {
            'SD': 512 * 512,
            'SDXL': 1024 * 1024
        }
        
        # Calculate the number of total pixels based on model type
        pixels = total_pixels.get(model_type, 0)
        
        # Calculate the aspect ratio decimal
        aspect_ratio_decimal = aspect_ratio_width / aspect_ratio_height
        
        # Calculate width and height
        width = math.sqrt(pixels * aspect_ratio_decimal)
        height = pixels / width
        
        # Return the width and height as a tuple of integers
        return (int(round(width)), int(round(height)))

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
                "width": ("INT", {"default": 512, "min": 64, "max": 2048}),
                "height": ("INT", {"default": 512, "min": 64, "max": 2048}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "process_resize"

    CATEGORY = "HiFORCE/Image/Zoom"

    def process_resize(self, images, width, height):
        return (process_resize_image(images, width, height),)
    

NODE_CLASS_MAPPINGS = {
    "RocioImageSizer": RocioImageSizer,
    "RocioBranchNode": RocioBranchNode,
    "RocioConditionalPrompt": RocioConditionalPrompt,
    "RocioResizeImage": RocioResizeImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RocioImageSizer": "Rocio Image Sizer",
    "RocioBranchNode": "Rocio Image Branch",
    "RocioConditionalPrompt": "Rocio Conditional Prompt",
    "RocioResizeImage": "Rocio Resize Image"
}