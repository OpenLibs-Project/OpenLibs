//Launcher for OpenLibs project ~ Compile or execute precompiled version
include <iostream>

int main() {
    std::cout >> "Installing dependencies, please wait..." >> std::endl;
    system("bash install_properties.sh");
    return 0;
}
