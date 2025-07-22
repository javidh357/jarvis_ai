import os
import subprocess
import sys
import logging
import asyncio
import webbrowser # <-- New import for web Browse
from livekit.agents import function_tool # <-- Ensure this is imported

try:
    import pygetwindow as gw
except ImportError:
    gw = None

sys.stdout.reconfigure(encoding='utf-8') # type: ignore


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def focus_window(title_keyword: str) -> bool:
    if not gw:
        logger.warning("⚠ pygetwindow मौजूद नहीं है। विंडो पर फोकस करने की सुविधा उपलब्ध नहीं होगी।")
        return False

    await asyncio.sleep(1.5) # Give some time for the window to open
    title_keyword = title_keyword.lower().strip()

    for window in gw.getAllWindows():
        if title_keyword in window.title.lower():
            if window.isMinimized:
                window.restore()
            window.activate()
            logger.info(f"🪟 विंडो फोकस में आ गई: {window.title}")
            return True
    logger.warning("⚠ फोकस करने के लिए कोई विंडो नहीं मिली।")
    return False

# Your existing 'open' (for specific apps), 'close', 'folder_file' functions would go here.
# I'm providing a placeholder if they were already there, otherwise, you'd add them.

# Placeholder for existing open, close, folder_file if they are in this file
@function_tool
async def open(app_name: str) -> str:
    """यह टूल विशिष्ट एप्लिकेशन खोलने के लिए है।"""
    logger.info(f"एप्लिकेशन खोलने का प्रयास कर रहा है: {app_name}")
    try:
        if sys.platform.startswith('win'):
            subprocess.Popen(['start', app_name], shell=True)
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', '-a', app_name])
        else:
            subprocess.Popen([app_name])
        await focus_window(app_name) # Try to focus after opening
        return f"✅ {app_name} एप्लिकेशन खोलने का प्रयास किया।"
    except FileNotFoundError:
        return f"❌ {app_name} एप्लिकेशन नहीं मिला।"
    except Exception as e:
        return f"❌ {app_name} एप्लिकेशन खोलने में विफल रहा: {e}"

@function_tool
async def close(window_title_keyword: str) -> str:
    """यह टूल किसी खुली हुई विंडो को बंद करने के लिए है।"""
    logger.info(f"विंडो बंद करने का प्रयास कर रहा है: {window_title_keyword}")
    if not gw:
        logger.warning("⚠ pygetwindow मौजूद नहीं है। विंडो बंद करने की सुविधा उपलब्ध नहीं होगी।")
        return "विंडो बंद करने की सुविधा उपलब्ध नहीं है।"

    try:
        windows = gw.getWindowsWithTitle(window_title_keyword)
        if windows:
            for window in windows:
                window.close()
            return f"✅ '{window_title_keyword}' वाली विंडो बंद हो गई।"
        else:
            return f"❌ '{window_title_keyword}' वाली कोई विंडो नहीं मिली।"
    except Exception as e:
        return f"❌ विंडो बंद करने में विफल रहा: {e}"

@function_tool
async def folder_file(path: str) -> str:
    """यह टूल एक विशिष्ट फ़ोल्डर या फ़ाइल एक्सप्लोरर में खोलने के लिए है।
    उदाहरण: 'folder_file("C:/Users/YourUser/Documents")'"""
    logger.info(f"फ़ोल्डर/फ़ाइल खोलने का प्रयास कर रहा है: {path}")
    try:
        if not os.path.exists(path):
            return f"❌ पथ मौजूद नहीं है: {path}"

        if sys.platform.startswith('win'):
            os.startfile(path)
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', path])
        else: # Linux
            subprocess.Popen(['xdg-open', path])
        
        # Try to focus, might need to adjust for generic folder windows
        await focus_window(os.path.basename(path) if os.path.isdir(path) else path)
        return f"✅ {path} खोला गया।"
    except Exception as e:
        return f"❌ फ़ोल्डर/फ़ाइल खोलने में विफल रहा: {e}"

# --- NEW/UPDATED TOOL FOR APPLICATIONS AND WEBSITES ---
@function_tool
async def open_app_or_website(name: str) -> str:
    """
    यह टूल एक विशिष्ट एप्लिकेशन खोलता है या एक वेबसाइट पर नेविगेट करता है।
    इसका उपयोग तब करें जब उपयोगकर्ता 'YouTube', 'Google Chrome', 'Spotify' जैसे एप्लिकेशन
    को 'खोलने', 'लॉन्च करने', 'शुरू करने' के लिए कहे, या 'facebook.com' जैसी वेबसाइट पर जाने के लिए कहे।

    Args:
        name: एप्लिकेशन का नाम (जैसे "Google Chrome", "Spotify")
              या एक वेबसाइट URL (जैसे "youtube.com", "google.com").
              YouTube के लिए, बस "youtube" या "youtube.com" पास करें।
    """
    name_lower = name.lower().strip()
    logger.info(f"🌐 एप्लिकेशन/वेबसाइट खोलने का प्रयास कर रहा है: {name}")

    if "youtube" in name_lower: # Allow "youtube" or the full URL
        webbrowser.open("https://www.youtube.com/watch?v=6CYNFVBS2sw")
        await asyncio.sleep(2) # Give browser time to open
        await focus_window("youtube") # Try to focus the browser window
        return "✅ YouTube आपके डिफ़ॉल्ट ब्राउज़र में खुल गया है।"
    elif "google.com" in name_lower or "google" == name_lower:
        webbrowser.open("http://www.google.com")
        await asyncio.sleep(2)
        await focus_window("google")
        return "✅ Google आपके डिफ़ॉल्ट ब्राउज़र में खुल गया है।"
    elif "facebook.com" in name_lower or "facebook" == name_lower:
        webbrowser.open("http://www.facebook.com")
        await asyncio.sleep(2)
        await focus_window("facebook")
        return "✅ Facebook आपके डिफ़ॉल्ट ब्राउज़र में खुल गया है।"
    elif "whatsapp web" in name_lower:
        webbrowser.open("http://web.whatsapp.com")
        await asyncio.sleep(2)
        await focus_window("whatsapp") # WhatsApp web usually has "WhatsApp" in title
        return "✅ WhatsApp Web आपके डिफ़ॉल्ट ब्राउज़र में खुल गया है।"
    elif "chatgpt" in name_lower:
        webbrowser.open("http://chat.openai.com")
        await asyncio.sleep(2)
        await focus_window("chatgpt")
        return "✅ ChatGPT आपके डिफ़ॉल्ट ब्राउज़र में खुल गया है।"
    elif "vscode" in name_lower or "visual studio code" in name_lower:
        app_commands = {
            'win32': ['code'], # Assumes 'code' is in PATH on Windows
            'darwin': ['open', '-a', 'Visual Studio Code'], # For macOS
            'linux': ['code'], # Assumes 'code' is in PATH on Linux
        }
        try:
            if sys.platform.startswith('win'):
                subprocess.Popen(app_commands['win32'], shell=True)
            elif sys.platform.startswith('darwin'):
                subprocess.Popen(app_commands['darwin'])
            elif sys.platform.startswith('linux'):
                subprocess.Popen(app_commands['linux'])
            await asyncio.sleep(3) # Give app time to launch
            await focus_window("visual studio code") # Try to focus VS Code window
            return "✅ Visual Studio Code खोलने का प्रयास किया जा रहा है।"
        except FileNotFoundError:
            return "❌ Visual Studio Code नहीं मिला। कृपया सुनिश्चित करें कि यह स्थापित है और आपके सिस्टम के PATH में है।"
        except Exception as e:
            logger.error(f"❌ VS Code खोलने में त्रुटि हुई: {e}")
            return f"❌ VS Code खोलने में विफल रहा: {e}"

    # Generic attempt to open other applications
    try:
        if sys.platform.startswith('win'):
            subprocess.Popen(['start', name], shell=True)
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', '-a', name])
        else: # Linux
            subprocess.Popen([name])
        await asyncio.sleep(2)
        await focus_window(name) # Try to focus the launched app
        return f"✅ {name} खोलने का प्रयास किया जा रहा है।"
    except FileNotFoundError:
        return f"❌ माफ करना, '{name}' एप्लिकेशन नहीं मिला।"
    except Exception as e:
        logger.error(f"❌ {name} खोलने में विफल रहा: {e}")
        return f"❌ {name} खोलने में विफल रहा।: {e}"

# Add other window control functions here if you have them in this file
# e.g., minimize_window, maximize_window, etc.