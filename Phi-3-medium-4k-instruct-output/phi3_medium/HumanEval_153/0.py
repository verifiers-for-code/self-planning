def Strongest_Extension(class_name, extensions):
    def extension_strength(extension):
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        return cap - sm

    strongest_extension = extensions[0]
    strongest_strength = extension_strength(strongest_extension)

    for extension in extensions[1:]:
        current_strength = extension_strength(extension)
        if current_strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = current_strength

    return f"{class_name}.{strongest_extension}"