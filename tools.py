def parseParameters(path):
    params = dict()
    remove_ext = path.split(".")
    real_path = remove_ext[0]
    extension = "." + remove_ext[1]
    split_real_path = real_path.split("-")
    image_title = split_real_path[0]
    params.update({"original_image_title": image_title + extension})
    algorithm = split_real_path[1]
    params.update({"algorithm": algorithm})
    match algorithm:
        case "ela":
            quality = split_real_path[2]
            params.update({"quality": quality})
        case "edges":
            lower = split_real_path[2]
            higher = split_real_path[3]
            if len(split_real_path) > 4:
                robust = True
            else:
                robust = False
            params.update({"lower": lower})
            params.update({"higher": higher})
            params.update({"robust": robust})
        case "PatchMatch":
            mask_color = split_real_path[2]
            params.update({"mask_color": mask_color})
        case "resize":
            method = split_real_path[2]
            height_scale = split_real_path[3]
            width_scale = split_real_path[4]
            params.update({"method": method})
            params.update({"height_scale": height_scale})
            params.update({"width_scale": width_scale})
        case "sharpen":
            method = split_real_path[2]
            params.update({"method": method})
    print(params)

parseParameters("blurry-sharpen-histogram.jpg")
