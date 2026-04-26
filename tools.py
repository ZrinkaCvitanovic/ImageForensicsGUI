def parseParameters(path):
    params = dict()
    remove_ext = path.split(".")
    real_path = remove_ext[0]
    extension = remove_ext[1]
    split_real_path = real_path.split("-")
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
    print(params)

parseParameters("inserted_elephant-edges-30-200-robust.jpg")
