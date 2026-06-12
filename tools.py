def parseParameters(path):
    params = dict()
    remove_ext = path.split(".")
    real_path = remove_ext[0]
    extension = "." + remove_ext[1]
    split_real_path = real_path.split("-")
    image_title = split_real_path[0]
    params.update({"Original image": image_title + extension})
    try:
        algorithm = split_real_path[1]
        params.update({"Algorithm": algorithm.capitalize()})
        match algorithm:
            case "ELA":
                quality = split_real_path[2]
                params.update({"Quality": quality})
            case "HSV":
                params.update({"Algorithm": "Hue-Saturation-Value"})
            case "LUM":
                params.update({"Algorithm": "Luminence gradient"})
            case "Edge_Detection":
                lower = split_real_path[2]
                higher = split_real_path[3]
                params.update({"Algorithm": "Edge detection"})
                params.update({"Lower threshold": lower})
                params.update({"Higher threshold": higher})
            case "PatchMatch":
                mask_color = split_real_path[2]
                params.update({"Mask color": mask_color.capitalize()})
            case "resize":
                method = split_real_path[2].capitalize()
                height_scale = split_real_path[3]
                width_scale = split_real_path[4]
                params.update({"Method": method.capitalize()})
                params.update({"Height scale": height_scale})
                params.update({"Width scale": width_scale})
            case "sharpen":
                method = split_real_path[2]
                params.update({"Method": method.capitalize()})
            case "contrast":
                method = split_real_path[2]
                params.update({"Method": "Increasing contrast"})
            case "Telea":
                params.update({"Algorithm": "Telea's inpainting"})
                radius = split_real_path[2]
                params.update({"Radius": radius})
            case "Gaussian_blur":
                params.update({"Algorithm": "Gaussian filter"})
            case "Median_blur":
                params.update({"Algorithm": "Median filter"})
        
    except:
        return params
    return params