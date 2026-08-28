#include <iostream>
#include <string>

using namespace std;

int main() {
    string text;
    char ch;
    
    cout << "Enter string: ";
    getline(cin, text);
    
    cout << "Enter character to delete: ";
    cin >> ch;
    
    string result = "";
    
    for (int i = 0; i < text.length(); i++) {
        if (text[i] != ch) {
            result += text[i];
        }
    }
    
    cout << "\nResult after deleting '" << ch << "':" << endl;
    cout << result << endl;
    
    return 0;
}