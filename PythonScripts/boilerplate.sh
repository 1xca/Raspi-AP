#!/usr/bin/env bash

readonly SCRIPT="$(test -L "${BASH_SOURCE[0]}" && readlink "${BASH_SOURCE[0]}" || echo "${BASH_SOURCE[0]}")"
readonly SCRIPT_DIR="$(cd "$(dirname "${SCRIPT}")"; pwd)"

execute_script() {
    local pass=$(python3 "${SCRIPT_DIR}/generateKey.py")         
    local wpa=$(grep /etc/hostapd/hostapd.conf -e wpa | cut -f 2 -d '=' | head -n 1)
    local ssid=$(grep /etc/hostapd/hostapd.conf -e ssid | cut -f 2 -d '=' | head -n 1)
    echo "wpa:${wpa} ssid:${ssid} pass:${pass}" 

    #QRCODE
    python3 "${SCRIPT_DIR}/qrCodeGenerator.py" "${ssid}" "${wpa}" "${pass}"

    #CHANGE PASSWORD
    sed "s/wpa_passphrase=.*/wpa_passphrase=${pass}/g" "/etc/hostapd/hostapd.conf"
}

# main
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
    echo "Script is being sourced"
else
    set -x
    set -euo pipefail
    execute_script "$@"
fi
