def main(args):
      name = args.get("name", "stranger")
      user_from=args.get("from")
      user_to=args.get("to")
      
      return {"body": greeting,"name":user_from,"to":user_to}
  
