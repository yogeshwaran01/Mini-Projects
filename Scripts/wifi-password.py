"""
This Scripts Saved wifi password in your Windows PC
"""

import subprocess


def get_all_profiles():
    data = subprocess.check_output(
        ["netsh", "wlan", "show", "profiles", "key=clear"]
    ).decode("utf-8", errors="backslashreplace")

    return data


def get_profiles_info(profile):
    try:
        data = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles", profile, "key=clear"]
        ).decode("utf-8", errors="backslashreplace")

        return data
    except subprocess.CalledProcessError:

        return "Profile Not Found"


if __name__ == "__main__":
    print(get_all_profiles())
    profile = input("Enter the profile Name: ")
    print(get_profiles_info(profile))