import os

# Remplacez ces hashes par vos commits "mauvais" et "bons"
badhash = "c1a4be04b972b6c17db242fc37752ad517c29402"
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

# Démarre le bisect
os.system(f"git bisect start {badhash} {goodhash}")

# Lance le bisect automatique avec votre script de test
os.system("git bisect run python test_bug.py")

# Réinitialise le dépôt après le bisect
os.system("git bisect reset")
