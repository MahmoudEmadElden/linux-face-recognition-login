# Face Recognition Login & Unlock Implementation Plan

This plan outlines the steps to enable face recognition for system login, screen unlocking, and `sudo` authentication on Kali Linux using **Howdy**.

## Proposed Changes

### [Component Name] Howdy Installation & Configuration

Summary: We will install the necessary dependencies, download and install Howdy, configure it to use your laptop's camera (`/dev/video0`), and enroll your face.

#### [NEW] [howdy_install.sh](file:///home/noone/cameraa/howdy_install.sh)
A script to automate the installation of dependencies and Howdy from the official PPA or source.

#### [MODIFY] PAM Configuration
We will modify `/etc/pam.d/common-auth` (or similar) to include Howdy as an authentication option.

## Open Questions

> [!IMPORTANT]
> Howdy modifies your system's authentication modules (PAM). If misconfigured, you might be temporarily locked out of your system. It is highly recommended to have a separate root shell open or another way to access your system (like a password) during this process. 

1. **Wayland vs X11**: Are you using GNOME on Wayland or X11? Howdy may have issues with Wayland screen locks.
2. **Camera IR**: Does your camera have IR (Infrared) support? If not, standard RGB recognition will be used, which is less secure but functional.

## Verification Plan

### Manual Verification
- **Sudo Test**: Run `sudo -i` in a terminal. The camera should turn on and recognize your face.
- **Login Test**: Lock your screen and try to unlock it using your face.
- **Configuration Check**: Verify `/dev/video0` is correctly mapped in `/etc/howdy/config.ini`.

### Automated Tests
- Scripted checks to ensure Howdy is active in the PAM stack.
