#!/bin/bash

# Update and install proot-distro
pkg update -y && pkg upgrade -y
pkg install proot-distro -y

# Install Debian distribution
proot-distro install debian

# Create a script to launch Debian shell
cat <<EOF >$PREFIX/bin/debian
#!/bin/bash
proot-distro login debian
EOF

# Make the script executable
chmod +x $PREFIX/bin/debian

# Add the script to .bashrc to start Debian shell on opening Termux
echo "debian" >> ~/.bashrc

echo "Termux will now default to Debian shell. Please restart Termux."
