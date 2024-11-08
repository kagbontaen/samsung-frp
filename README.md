## Samsung FRP Bypass

- grab python from <a href="https://www.python.org/downloads/">here</a><br>
- grab ADB from <a href="https://developer.android.com/tools/releases/platform-tools">here</a><br>
- ensure you have the samsung usb drivers have been installed (Search Google fo how)
- Make sure you have all the dependencies listed in `requirements.txt` installed
- Install them using `pip install -r requirements.txt`
- You can simply plug the samsung over USB and run `python main.py`


![Screenshot 2024-11-08 011527](https://github.com/user-attachments/assets/acd1dc7b-a0dc-4c30-99fd-ce18f8d74c09)
![Screenshot 2024-11-08 011452](https://github.com/user-attachments/assets/260c97a9-79e8-4d3c-b71f-83e6052d6326)
  
## unlock.sh

```
git clone https://github.com/sudo-self/samsung-frp.git
cd samsung-frp
chmod +x unlock.sh
./unlock.sh
```



### runs ADB commands


```
execute_adb_command "settings put global setup_wizard_has_run 1"
execute_adb_command "settings put secure user_setup_complete 1"
execute_adb_command "content insert --uri content://settings/secure --bind name:s:DEVICE_PROVISIONED --bind value:i:1"
execute_adb_command "content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:i:1"
execute_adb_command "content insert --uri content://settings/secure --bind name:s:INSTALL_NON_MARKET_APPS --bind value:i:1"
execute_adb_command "am start -c android.intent.category.HOME -a android.intent.action.MAIN"
```
### wait for 5 seconds

```
execute_adb_command "am start -n com.android.settings/com.android.settings.Settings"
```
then reboot..
