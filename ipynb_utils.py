NOTEBOOKS_DATA = "SPECIFY FOLDER DIRECTORY WITH SAVED DATA FOR EASY SAVING AND LOADING OF PICKLED DATA"

def save_var(var, var_name):
    """Save a variable to NOTEBOOKS_DATA with pickle."""
    os.makedirs(NOTEBOOKS_DATA, exist_ok=True)
    path = os.path.join(NOTEBOOKS_DATA, f"{var_name}.pkl")
    with open(path, "wb") as f:
        pickle.dump(var, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"✅ Saved {var_name} → {path}")

def load_var(var_name):
    """Load a variable from NOTEBOOKS_DATA."""
    path = os.path.join(NOTEBOOKS_DATA, f"{var_name}.pkl")
    if not os.path.exists(path):
        raise FileNotFoundError(f"No saved variable named {var_name} at {path}")
    with open(path, "rb") as f:
        var = pickle.load(f)
    print(f"📂 Loaded {var_name} from {path}")
    globals()[var_name] = var
