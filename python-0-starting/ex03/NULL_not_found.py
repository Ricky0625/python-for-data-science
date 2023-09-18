def NULL_not_found(object: any) -> int:
    objectType = type(object)
    prefix = ""
    suffix = ""

    if object == None:
        prefix = "Nothing"
    elif objectType.__name__ == "float" and str(object) == "nan":
        prefix = "Cheese"
    elif object == 0:
        prefix = "Zero"
    elif object == "":
        prefix = "Empty"
    elif object == False:
        prefix = "Fake"
    
    if prefix == "" and suffix == "":
        print("Type not found")
        return 1
    elif prefix != "" and prefix == "Nothing":
        suffix = ": " + f"None {objectType}"
    else:
        suffix = ": " + f"{object} {objectType}"

    print(f"{prefix}{suffix}")
    return 0