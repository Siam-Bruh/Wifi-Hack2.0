import WifiHack

print("Available functions/objects in WifiHack")
print(dir(WifiHack))

if hasattr(WifiHack, "main"):
    WifiHack.main()
elif hasattr(WifiHack, "start"):
    WifiHack.start()
else:
    print("No main/start function found.")
