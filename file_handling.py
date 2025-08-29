# name cleaning code
# Reads names from one file, cleans them, and writes to another file

# Step 1: Create a file with unclean names
file = open("names_raw.txt", "w")
file.write("alice\nbob\nCHARLIE\ndavE\n")
file.close()

# Step 2: Read names from the file
file = open("names_raw.txt", "r")
names = file.readlines()
file.close()

# Step 3: Clean the names (capitalize properly)
cleaned_names = [name.strip().capitalize() + "\n" for name in names]

# Step 4: Write cleaned names to a new file
file = open("names_clean.txt", "w")
file.writelines(cleaned_names)
file.close()

print("✅ Names cleaned and saved to names_clean.txt")
# Step 5: Verify the cleaned names
file = open("names_clean.txt", "r")
cleaned_names = file.readlines()
file.close()

print("✅ Cleaned Names:")
for name in cleaned_names:
    print(name.strip())
