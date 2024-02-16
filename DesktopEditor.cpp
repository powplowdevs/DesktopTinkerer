#include <windows.h>
#include <commctrl.h>
#include <iostream>

using namespace std;

//Icon info
struct IconInfo {
    string name;
    string imgPath;
    int x;
    int y;
};

//-------------------ICON EDITOR-------------------

bool editDeskstopIcons() {
    HWND hWindow;
    HANDLE hExplorer;
    DWORD pid;

    hWindow = FindWindowA("Progman", NULL);
    hWindow = FindWindowExA(hWindow, 0, "SHELLDLL_DefView", NULL);
    hWindow = FindWindowExA(hWindow, 0, "SysListView32", NULL);
    printf("hw %ls",hWindow);
    GetWindowThreadProcessId(GetDesktopWindow(), &pid);
    hExplorer = OpenProcess(PROCESS_VM_OPERATION | PROCESS_VM_WRITE | PROCESS_VM_READ, false, pid);

    POINT *pC = (POINT*) VirtualAllocEx(hExplorer, NULL, sizeof(POINT), MEM_COMMIT, PAGE_READWRITE);
    WriteProcessMemory(hExplorer, pC, &pC, sizeof(POINT), NULL);

    for(int i=0; i < 1000; i++){
        ListView_SetItemPosition(hWindow, 0, i,i);
        Sleep(10);
    }

    VirtualFreeEx(hExplorer, pC, 0, MEM_RELEASE);    

    return true;
}

//-------------------WALLPAPER EDITOR-------------------

bool setWallPaper(PVOID path){
    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE);
    return true;
}

bool downloadWallpaper(){
    system("python.exe .\\wallpaperEditor.py download");
    return true;
}

bool uploadWallPaper(){
    system("python.exe .\\wallpaperEditor.py upload");
    return true;
}

bool screenshotbWallPaper(){
    system("python.exe .\\wallpaperEditor.py ss");
    return true;
}

//-------------------MESSAGE-------------------
bool showMessage(){
    return true;
}

bool grabMessage(){
    return "Hello test msg!!";
}

//-------------------MAIN LOOP-------------------
void mainLoop(){
    return;
}

//-------------------MAIN-------------------
int main() {
    //ONLOAD
    //Screenshot wallpaper
    screenshotbWallPaper();
    //Set wallpaper
    downloadWallpaper(); 
    setWallPaper((PVOID)"G:\\My Drive\\Programing\\Personal scripts\\RemoteAccess\\wallpaper.png");
    //Upload wallpaper
    uploadWallPaper();

    //MAIN LOOP
    mainLoop();

    return 0;
}

