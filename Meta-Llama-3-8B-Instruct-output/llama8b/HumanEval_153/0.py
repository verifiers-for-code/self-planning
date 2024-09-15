def Strongest_Extension(class_name, extensions):
    extension_strength = {}
    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm
        extension_strength[extension] = strength
    max_strength = max(extension_strength.values())
    strongest_extension = [extension for extension, strength in extension_strength.items() if strength == max_strength][0]
    return f"{class_name}.{strongest_extension}"