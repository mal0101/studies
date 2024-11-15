def format_usernames(liste : list[str]) -> list[str]:
    names = []
    for username in liste:
            name = username.lower().replace(" ", "_")
            if not name.startswith("user_"):
                name = "user_" + name
            names.append(name)
    return names
