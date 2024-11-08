from usbswitcher import samsungGalaxyToModemMode
from at_utils import enableADB
from adb_utils import waitForDevice, uploadAndRunFRPBypass, manualFRPBypass

def main():
    #samsungGalaxyToModemMode()
    enableADB()
    waitForDevice()
    manualFRPBypass()

if __name__ == "__main__":
    main()

