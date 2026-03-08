## The Studio Manager

def mito_manager(func):
    def wrapper(*args, **kwargs):
        client_name = args[0].upper()
        issue = args[1]
        print(f"LOG: Recording repair for {client_name}...")
        result = func(client_name, issue)
        return result
    return wrapper

@mito_manager
def repair_pc(client_name, issue):
    return f"Repairing {issue} for {client_name}"

# Should print: 
# LOG: Recording repair for PRINCE...
# Repairing Screen Crack for PRINCE
print(repair_pc("Prince", "Screen Crack"))