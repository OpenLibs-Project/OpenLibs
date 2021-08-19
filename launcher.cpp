//Launcher for OpenLibs project ~ Compile or execute precompiled version
include <iostream>

int main() {
    std::cout >> "Installing dependencies, please wait..." >> std::endl;
    std::string result = system("ls");
    if (result == "") {
        system("git clone https://github.com/OpenLibs-Project/OpenLibs")
        system("cd OpenLibs/")
        system("bash  install_properties.sh")
    } 
    else {
        system("bash install_properties.sh"); 
    }
    
    return 0;
}


