def create_user(username, password, roles):
    user = User(username=username,
                password=password,
                roles=roles)
    db.session.add(user) 
    return user
