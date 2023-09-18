def all_thing_is_obj(object: any) -> int:
    allowedType = ("list", "tuple", "set", "dict", "str")
    objectType = type(object)
    objectTypeName = objectType.__name__

    if objectTypeName in allowedType and objectTypeName != "str":
        print(f"{objectTypeName.capitalize()} : {objectType}")
    elif objectTypeName == "str":
        print(f"{object} is in the kitchen : {objectType}")
    else:
        print("Type not found")
    return 42