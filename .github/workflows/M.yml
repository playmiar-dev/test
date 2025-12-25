name: Build APK

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - name: Checkout repo
      uses: actions/checkout@v4

    - name: Install system dependencies
      run: |
        sudo apt update
        sudo apt install -y \
          python3 python3-pip \
          git zip unzip \
          openjdk-17-jdk \
          libncurses5 libstdc++6

    - name: Install Buildozer & Kivy
      run: |
        pip3 install --user buildozer cython kivy
        echo "$HOME/.local/bin" >> $GITHUB_PATH

    - name: Build APK
      run: |
        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: apk
        path: bin/*.apk
