# Powershell Preparation for PEN300
-------------------------


// Quick Variables:



    $YOU="YourUserName"           # Replace YourUserName with your username on (e.g) Windows #    
    PS > $PWDV="C:\Users\",$YOU,"\Desktop\" # Another Version (With \newlines) #
    PS > $PWDV="C:\Users\"+$YOU+"\Desktop\" # outputs C:\Users\YourUserName\Desktop\ #
    PS >






## Registry
-------------------------

#### to set a variable, do `$varname="Value/Can/Be/A/Path/or/Whatever"`

      PS C:\Windows\system32> echo $R0,$R1,$R2,$RX

      # --------------- Outputs --------------- #
      HKLM\SYSTEM\CurrentControlset\Enum\
      HKLM\SYSTEM\CurrentControlset\Enum\USB
      HKLM\SYSTEM\CurrentControlset\Enum\USBSTOR
      HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs

-------------------------


### Do that, but Hidden from user - and output it to a file!

    # --------------- Outputs a file on Desktop, which contains $R0. --------------- #
    
    PS C:\Windows\system32> powershell -W hidden reg query $R0 | Out-File C:\Users\YOU\Desktop\OUTPUT.reg

### How about you obfuscate that cake?
    # --------------- Does the same as above, except now it's in format:HEX --------------- #
    
    PS C:\Windows\system32> powershell -W hidden reg query $R0 | Out-File C:\Users\YOU\Desktop\OUTPUT.reg

Outputs This (Or, something (on those) lines):


           00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F

        00000000   48 4B 45 59 5F 4C 4F 43 41 4C 5F 4D 41 43 48 49  HKEY_LOCAL_MACHI
        00000010   4E 45 5C 53 59 53 54 45 4D 5C 43 75 72 72 65 6E  NE\SYSTEM\Curren
        00000020   74 43 6F 6E 74 72 6F 6C 73 65 74 5C 45 6E 75 6D  tControlset\Enum

 
-------------------------



## FileSystem (FileSys, or (mosto ften) just 'FS')

-------------------------

