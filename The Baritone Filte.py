## The Baritone Filte

def baritone_only(func):
    def wrapper(*args,**kwargs):
        if args[0].capitalize() != "Baritone":
            print("ERROR: Voice type not supported!")
            return None
        return func(*args,**kwargs)
    return wrapper

@baritone_only
def sing_funk(voice, song):
    return f"Singing {song} as a {voice}"

print(sing_funk("Baritone", "Kagandahan na Marahuyo")) # Should work
print(sing_funk("Soprano", "Random Song"))            # Should fail