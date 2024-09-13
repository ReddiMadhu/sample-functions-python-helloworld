def main(args):
    name = args.get("name", "stranger")
    user_from = args.get("from")
    user_to = args.get("to")
    
    # Constructing the greeting string using the inputs
    if user_from and user_to:
        greeting = f"Hello {name}, from {user_from} to {user_to}!"
    else:
        greeting = f"Hello {name}!"
    
    return {"body": greeting}

