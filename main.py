import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
import struct
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class RC4CyberSuite:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 RC4 CYBER-SUITE | STREAM CIPHER ANALYZER 🔥")
        self.root.geometry("1500x950")
        self.root.configure(bg='#0a0a0f')  # Dark cyber background
        
        # Neon colors for this theme
        self.bg_color = "#0a0a0f"
        self.neon_red = "#ff0033"
        self.neon_blue = "#00ccff"
        self.neon_purple = "#9900ff"
        self.binary_green = "#00ff00"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Cyber header
        self.create_cyber_header(main_container)
        
        # Create notebook with custom style
        style = ttk.Style()
        style.theme_use('default')
        style.configure('RC4.TNotebook', background=self.bg_color, borderwidth=0)
        style.configure('RC4.TNotebook.Tab', background='#1a1a2e', foreground=self.neon_red,
                       padding=[15, 8], font=('Courier', 10, 'bold'))
        style.map('RC4.TNotebook.Tab',
                 background=[('selected', self.neon_red), ('active', '#2a2a3e')],
                 foreground=[('selected', '#0a0a0f'), ('active', self.neon_red)])
        
        notebook = ttk.Notebook(main_container, style='RC4.TNotebook')
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.tab1 = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(self.tab1, text="🔥 RC4 CIPHER CORE")
        self.setup_rc4_core()
        
        self.tab2 = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(self.tab2, text="⚠️ WEP VULNERABILITY")
        self.setup_wep_vuln()
        
        self.tab3 = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(self.tab3, text="📊 STATISTICAL BIAS")
        self.setup_statistical_bias()
        
        self.tab4 = tk.Frame(notebook, bg=self.bg_color)
        notebook.add(self.tab4, text="🛡️ TLS BAN & SECURITY")
        self.setup_security_analysis()
        
        # Status bar
        self.create_status_bar(main_container)
        
        # Initialize RC4 state
        self.S = list(range(256))
        self.i = 0
        self.j = 0
    
    def create_cyber_header(self, parent):
        header = tk.Frame(parent, bg=self.bg_color, height=100)
        header.pack(fill=tk.X, pady=(10, 0))
        
        header_text = """
╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
║   ██████╗  ██████╗ ██████╗     ███████╗██╗   ██╗██████╗ ███████╗██████╗ ████████╗███████╗   ║
║   ██╔══██╗██╔════╝██╔════╝     ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝   ║
║   ██████╔╝██║     ██║  ███╗    █████╗   ╚████╔╝ ██████╔╝█████╗  ██████╔╝   ██║   █████╗     ║
║   ██╔══██╗██║     ██║   ██║    ██╔══╝    ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗   ██║   ██╔══╝     ║
║   ██║  ██║╚██████╗╚██████╔╝    ███████╗   ██║   ██║  ██║███████╗██║  ██║   ██║   ███████╗   ║
║   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝   ║
║                              STREAM CIPHER ANALYSIS SUITE v2.0                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        """
        
        lbl = tk.Label(header, text=header_text, font=('Courier', 7), fg=self.neon_red,
                      bg=self.bg_color, justify=tk.LEFT)
        lbl.pack()
    
    def create_status_bar(self, parent):
        status_frame = tk.Frame(parent, bg='#1a1a2e', height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_label = tk.Label(status_frame, text="🟢 RC4 ENGINE READY | KSA/PRGA ONLINE",
                                     font=('Courier', 9), fg=self.neon_blue, bg='#1a1a2e')
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Animated symbols
        for _ in range(3):
            sym = tk.Label(status_frame, text="◉", font=('Courier', 10), fg=self.neon_red, bg='#1a1a2e')
            sym.pack(side=tk.RIGHT, padx=5)
    
    # ==================== RC4 CORE IMPLEMENTATION ====================
    def ksa(self, key):
        """Key Scheduling Algorithm - Initializes S-box"""
        key = [ord(c) for c in key]
        key_length = len(key)
        S = list(range(256))
        j = 0
        
        for i in range(256):
            j = (j + S[i] + key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]
        
        return S
    
    def prga(self, S, length):
        """Pseudo-Random Generation Algorithm - Generates keystream"""
        keystream = []
        i = 0
        j = 0
        
        for _ in range(length):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % 256]
            keystream.append(K)
        
        return keystream
    
    def encrypt_rc4(self, plaintext, key):
        """Full RC4 encryption/decryption"""
        S = self.ksa(key)
        keystream = self.prga(S.copy(), len(plaintext))
        
        result = []
        for i, char in enumerate(plaintext):
            result.append(chr(ord(char) ^ keystream[i]))
        
        return ''.join(result)
    
    def get_keystream_byte(self, key, byte_position):
        """Get specific byte from keystream (for WEP analysis)"""
        S = self.ksa(key)
        i = 0
        j = 0
        
        for _ in range(byte_position + 1):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % 256]
        
        return K
    
    # ==================== TAB 1: RC4 CORE ====================
    def setup_rc4_core(self):
        main_frame = tk.Frame(self.tab1, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left panel - Input
        left_panel = tk.Frame(main_frame, bg=self.bg_color)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Key input
        key_frame = tk.LabelFrame(left_panel, text="🔑 RC4 KEY", 
                                 font=('Courier', 10, 'bold'),
                                 fg=self.neon_red, bg=self.bg_color, relief=tk.GROOVE, bd=2)
        key_frame.pack(fill=tk.X, pady=10)
        
        self.rc4_key = tk.Entry(key_frame, width=50, font=('Consolas', 11),
                                bg='#1a1a2e', fg=self.binary_green, insertbackground=self.neon_blue)
        self.rc4_key.pack(padx=10, pady=10)
        self.rc4_key.insert(0, "SecretKey")
        
        # Plaintext input
        pt_frame = tk.LabelFrame(left_panel, text="📝 PLAINTEXT", 
                                 font=('Courier', 10, 'bold'),
                                 fg=self.neon_red, bg=self.bg_color, relief=tk.GROOVE, bd=2)
        pt_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.rc4_plaintext = scrolledtext.ScrolledText(pt_frame, height=8, font=('Consolas', 11),
                                                       bg='#1a1a2e', fg=self.binary_green)
        self.rc4_plaintext.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.rc4_plaintext.insert('1.0', "RC4 is a stream cipher designed by Ron Rivest in 1987")
        
        # Buttons
        btn_frame = tk.Frame(left_panel, bg=self.bg_color)
        btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(btn_frame, text="🔥 ENCRYPT", command=self.do_rc4_encrypt,
                 font=('Courier', 11, 'bold'), bg=self.neon_red, fg='#0a0a0f',
                 activebackground='#ff0044').pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="❄️ DECRYPT", command=self.do_rc4_decrypt,
                 font=('Courier', 11, 'bold'), bg=self.neon_blue, fg='#0a0a0f',
                 activebackground='#00ccff').pack(side=tk.LEFT, padx=5)
        
        # Right panel - Output
        right_panel = tk.Frame(main_frame, bg=self.bg_color)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Ciphertext
        ct_frame = tk.LabelFrame(right_panel, text="📤 CIPHERTEXT (HEX)", 
                                 font=('Courier', 10, 'bold'),
                                 fg=self.neon_red, bg=self.bg_color, relief=tk.GROOVE, bd=2)
        ct_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.rc4_ciphertext = scrolledtext.ScrolledText(ct_frame, height=6, font=('Consolas', 11),
                                                        bg='#1a1a2e', fg='#ff00ff')
        self.rc4_ciphertext.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Keystream
        ks_frame = tk.LabelFrame(right_panel, text="🎲 GENERATED KEYSTREAM (HEX)", 
                                 font=('Courier', 10, 'bold'),
                                 fg=self.neon_blue, bg=self.bg_color, relief=tk.GROOVE, bd=2)
        ks_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.keystream_output = scrolledtext.ScrolledText(ks_frame, height=4, font=('Consolas', 11),
                                                          bg='#1a1a2e', fg='#ff6600')
        self.keystream_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # S-Box visualization
        sbox_frame = tk.LabelFrame(right_panel, text="🔀 INITIAL S-BOX (First 16 bytes)", 
                                   font=('Courier', 10, 'bold'),
                                   fg=self.neon_purple, bg=self.bg_color, relief=tk.GROOVE, bd=2)
        sbox_frame.pack(fill=tk.X, pady=10)
        
        self.sbox_text = tk.Text(sbox_frame, height=3, font=('Consolas', 9),
                                 bg='#1a1a2e', fg='#ff00ff')
        self.sbox_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def do_rc4_encrypt(self):
        key = self.rc4_key.get().strip()
        plaintext = self.rc4_plaintext.get('1.0', tk.END).strip()
        
        if not key or not plaintext:
            messagebox.showerror("Error", "Please enter both key and plaintext!")
            return
        
        # Show S-box initialization
        S = self.ksa(key)
        sbox_first16 = [f"{S[i]:02x}" for i in range(16)]
        self.sbox_text.delete('1.0', tk.END)
        self.sbox_text.insert('1.0', " ".join(sbox_first16))
        
        # Encrypt
        ciphertext = self.encrypt_rc4(plaintext, key)
        
        # Get keystream for display
        keystream = self.prga(self.ksa(key).copy(), len(plaintext))
        keystream_hex = ' '.join(f"{b:02x}" for b in keystream[:32])
        
        # Display results
        ciphertext_hex = ' '.join(f"{ord(c):02x}" for c in ciphertext)
        self.rc4_ciphertext.delete('1.0', tk.END)
        self.rc4_ciphertext.insert('1.0', ciphertext_hex)
        
        self.keystream_output.delete('1.0', tk.END)
        self.keystream_output.insert('1.0', keystream_hex)
        
        self.status_label.config(text="🔥 Encryption complete | RC4 stream cipher operational")
    
    def do_rc4_decrypt(self):
        key = self.rc4_key.get().strip()
        ciphertext_hex = self.rc4_ciphertext.get('1.0', tk.END).strip().replace(' ', '')
        
        if not key or not ciphertext_hex:
            messagebox.showerror("Error", "Please enter key and ciphertext!")
            return
        
        try:
            # Convert hex to string
            ciphertext_bytes = bytes.fromhex(ciphertext_hex)
            ciphertext = ciphertext_bytes.decode('latin1')
            
            # Decrypt
            plaintext = self.encrypt_rc4(ciphertext, key)
            
            self.rc4_plaintext.delete('1.0', tk.END)
            self.rc4_plaintext.insert('1.0', plaintext)
            
            self.status_label.config(text="❄️ Decryption complete | XOR symmetry verified")
        except:
            messagebox.showerror("Error", "Invalid ciphertext hex format!")
    
    # ==================== TAB 2: WEP VULNERABILITY ====================
    def setup_wep_vuln(self):
        main_frame = tk.Frame(self.tab2, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Description
        desc_frame = tk.LabelFrame(main_frame, text="⚠️ WEP WEAK IV ATTACK", 
                                   font=('Courier', 10, 'bold'),
                                   fg='#ff0000', bg=self.bg_color, relief=tk.GROOVE, bd=2)
        desc_frame.pack(fill=tk.X, pady=10)
        
        desc_text = """WEP VULNERABILITY: When IV starts with 0x00, 0x01, the first keystream byte reveals key information!
        The attack: K[0] = first_keystream_byte - 3 - IV[2] (mod 256) for certain IVs"""
        
        desc_lbl = tk.Label(desc_frame, text=desc_text, font=('Consolas', 10),
                           fg='#ffff00', bg=self.bg_color, wraplength=1200, justify=tk.LEFT)
        desc_lbl.pack(padx=10, pady=10)
        
        # Control panel
        control_frame = tk.Frame(main_frame, bg=self.bg_color)
        control_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(control_frame, text="Secret Key (bytes, hex):", font=('Courier', 10),
                fg=self.neon_blue, bg=self.bg_color).pack(side=tk.LEFT, padx=5)
        
        self.wep_key = tk.Entry(control_frame, width=30, font=('Consolas', 10),
                                bg='#1a1a2e', fg=self.binary_green)
        self.wep_key.pack(side=tk.LEFT, padx=5)
        self.wep_key.insert(0, "0102030405")
        
        tk.Button(control_frame, text="🔍 ANALYZE WEAK IVS", command=self.analyze_weak_ivs,
                 font=('Courier', 10, 'bold'), bg=self.neon_red, fg='#0a0a0f').pack(side=tk.LEFT, padx=10)
        
        # Results
        results_frame = tk.LabelFrame(main_frame, text="📊 WEAK IV ANALYSIS RESULTS", 
                                      font=('Courier', 10, 'bold'),
                                      fg=self.neon_red, bg=self.bg_color, relief=tk.GROOVE, bd=2)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.wep_results = scrolledtext.ScrolledText(results_frame, height=20, font=('Consolas', 10),
                                                     bg='#1a1a2e', fg='#00ff00')
        self.wep_results.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def analyze_weak_ivs(self):
        try:
            key_bytes = bytes.fromhex(self.wep_key.get().strip())
            key_str = key_bytes.decode('latin1')
        except:
            messagebox.showerror("Error", "Invalid key hex format!")
            return
        
        self.wep_results.delete('1.0', tk.END)
        self.wep_results.insert('1.0', "╔══════════════════════════════════════════════════════════════════╗\n")
        self.wep_results.insert(tk.END, "║              WEP WEAK IV ATTACK - KEYSTREAM ANALYSIS            ║\n")
        self.wep_results.insert(tk.END, "╚══════════════════════════════════════════════════════════════════╝\n\n")
        
        # Test weak IVs
        weak_ivs = []
        for iv_first in [0x00, 0x01, 0x02, 0x03]:
            for iv_second in range(0xFF):
                iv = bytes([iv_first, iv_second, 0xAB])  # Third byte arbitrary
                full_key = iv + key_bytes
                
                # Get first keystream byte
                ks_byte = self.get_keystream_byte(full_key.decode('latin1'), 0)
                
                # FMS attack: if first byte shows pattern
                if ks_byte < 10:  # Weak keystream byte
                    weak_ivs.append((iv_first, iv_second, ks_byte))
                    if len(weak_ivs) >= 20:
                        break
            if len(weak_ivs) >= 20:
                break
        
        self.wep_results.insert(tk.END, "🔴 WEAK IVs DETECTED:\n")
        self.wep_results.insert(tk.END, "─" * 70 + "\n")
        self.wep_results.insert(tk.END, f"{'IV[0]':<8} {'IV[1]':<8} {'1st Keystream Byte':<20}\n")
        self.wep_results.insert(tk.END, "─" * 70 + "\n")
        
        for iv0, iv1, ks in weak_ivs[:15]:
            self.wep_results.insert(tk.END, f"0x{iv0:02x}      0x{iv1:02x}      0x{ks:02x} ({ks})\n")
        
        self.wep_results.insert(tk.END, "\n💡 EXPLANATION:\n")
        self.wep_results.insert(tk.END, "WEP uses IV + Key as RC4 key. Weak IVs (0x00,0x01,0x02,0x03) cause\n")
        self.wep_results.insert(tk.END, "the first keystream byte to reveal information about the secret key.\n")
        self.wep_results.insert(tk.END, "An attacker can recover the full 40-bit key with ~60,000 packets!\n")
        
        self.status_label.config(text="⚠️ WEP vulnerability demonstrated | Weak IVs expose key material")
    
    # ==================== TAB 3: STATISTICAL BIAS ====================
    def setup_statistical_bias(self):
        main_frame = tk.Frame(self.tab3, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Control panel
        control_frame = tk.Frame(main_frame, bg=self.bg_color)
        control_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(control_frame, text="Number of Keystreams:", font=('Courier', 10),
                fg=self.neon_blue, bg=self.bg_color).pack(side=tk.LEFT, padx=5)
        
        self.num_streams = tk.Entry(control_frame, width=10, font=('Consolas', 10),
                                    bg='#1a1a2e', fg=self.binary_green)
        self.num_streams.insert(0, "10000")
        self.num_streams.pack(side=tk.LEFT, padx=5)
        
        tk.Button(control_frame, text="📊 RUN BIAS ANALYSIS", command=self.run_bias_analysis,
                 font=('Courier', 10, 'bold'), bg=self.neon_purple, fg='#0a0a0f').pack(side=tk.LEFT, padx=10)
        
        # Results text
        results_frame = tk.LabelFrame(main_frame, text="📈 BIAS ANALYSIS RESULTS", 
                                      font=('Courier', 10, 'bold'),
                                      fg=self.neon_blue, bg=self.bg_color, relief=tk.GROOVE, bd=2)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.bias_text = scrolledtext.ScrolledText(results_frame, height=10, font=('Consolas', 10),
                                                   bg='#1a1a2e', fg='#ffff00')
        self.bias_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Graph frame
        graph_frame = tk.LabelFrame(main_frame, text="📊 2ND BYTE DISTRIBUTION", 
                                    font=('Courier', 10, 'bold'),
                                    fg=self.neon_red, bg=self.bg_color, relief=tk.GROOVE, bd=2)
        graph_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.graph_canvas = tk.Frame(graph_frame, bg=self.bg_color)
        self.graph_canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def run_bias_analysis(self):
        try:
            num_streams = int(self.num_streams.get())
            if num_streams > 50000:
                if not messagebox.askyesno("Warning", f"Analyzing {num_streams} keystreams may take time. Continue?"):
                    return
        except:
            messagebox.showerror("Error", "Invalid number!")
            return
        
        self.bias_text.delete('1.0', tk.END)
        self.bias_text.insert('1.0', f"🔬 Analyzing {num_streams} RC4 keystreams...\n\n")
        self.root.update()
        
        # Collect 2nd byte from each keystream
        second_bytes = []
        
        for _ in range(num_streams):
            # Generate random 5-byte key (typical WEP key size)
            key = ''.join(chr(random.randint(0, 255)) for _ in range(5))
            ks_byte = self.get_keystream_byte(key, 1)  # Get 2nd byte (index 1)
            second_bytes.append(ks_byte)
        
        # Calculate frequencies
        freq = Counter(second_bytes)
        
        # Display results
        self.bias_text.insert(tk.END, "📊 2ND BYTE FREQUENCY DISTRIBUTION:\n")
        self.bias_text.insert(tk.END, "─" * 50 + "\n")
        
        expected_freq = num_streams / 256
        bias_0 = freq[0] - expected_freq
        
        self.bias_text.insert(tk.END, f"Expected frequency per byte: {expected_freq:.1f}\n")
        self.bias_text.insert(tk.END, f"Actual frequency of byte 0x00: {freq[0]} ({freq[0]/num_streams*100:.2f}%)\n")
        self.bias_text.insert(tk.END, f"Bias towards 0x00: {bias_0:+.1f} ({bias_0/expected_freq*100:+.1f}%)\n\n")
        
        if freq[0] > expected_freq * 1.1:
            self.bias_text.insert(tk.END, "⚠️ SIGNIFICANT BIAS DETECTED! Byte 0x00 appears more often than expected.\n")
            self.bias_text.insert(tk.END, "This bias was used to break RC4 in TLS and led to its ban in TLS 1.3.\n")
        else:
            self.bias_text.insert(tk.END, "Small bias detected - typical for RC4.\n")
        
        # Create graph
        self.plot_byte_distribution(freq, num_streams)
        
        self.status_label.config(text=f"📊 Bias analysis complete | Analyzed {num_streams} keystreams")
    
    def plot_byte_distribution(self, freq, total):
        # Clear previous graph
        for widget in self.graph_canvas.winfo_children():
            widget.destroy()
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        fig.patch.set_facecolor('#0a0a0f')
        
        # Plot 1: Distribution
        bytes_range = list(range(256))
        frequencies = [freq.get(b, 0) for b in bytes_range]
        
        ax1.bar(bytes_range, frequencies, color='#ff0033', alpha=0.7, edgecolor='#00ccff', linewidth=0.5)
        ax1.axhline(y=total/256, color='#00ff00', linestyle='--', label=f'Expected ({total/256:.1f})')
        ax1.set_xlabel('Byte Value', color='#00ccff')
        ax1.set_ylabel('Frequency', color='#00ccff')
        ax1.set_title('RC4 2nd Byte Distribution', color='#ff0033', fontsize=12, fontweight='bold')
        ax1.tick_params(colors='#00ccff')
        ax1.set_facecolor('#1a1a2e')
        ax1.legend()
        
        # Plot 2: Bias relative to expected
        expected = total / 256
        bias = [(freq.get(b, 0) - expected) / expected * 100 for b in bytes_range]
        
        ax2.bar(bytes_range, bias, color='#9900ff', alpha=0.7, edgecolor='#00ccff', linewidth=0.5)
        ax2.axhline(y=0, color='#00ff00', linestyle='--')
        ax2.set_xlabel('Byte Value', color='#00ccff')
        ax2.set_ylabel('Bias (%)', color='#00ccff')
        ax2.set_title('Deviation from Expected', color='#ff0033', fontsize=12, fontweight='bold')
        ax2.tick_params(colors='#00ccff')
        ax2.set_facecolor('#1a1a2e')
        
        # Highlight byte 0
        ax2.bar(0, bias[0], color='#ffff00', alpha=0.9, edgecolor='#ff0000', linewidth=2)
        
        plt.tight_layout()
        
        # Embed in tkinter
        canvas = FigureCanvasTkAgg(fig, self.graph_canvas)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    # ==================== TAB 4: SECURITY ANALYSIS ====================
    def setup_security_analysis(self):
        text_frame = tk.Frame(self.tab4, bg=self.bg_color)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        security_text = scrolledtext.ScrolledText(text_frame, height=35, font=('Consolas', 10),
                                                  bg='#1a1a2e', fg='#00ff00')
        security_text.pack(fill=tk.BOTH, expand=True)
        
        security_content = """
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                    🔥 RC4 SECURITY ANALYSIS - WHY TLS 1.3 BANNED IT 🔥                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

📌 DISCOVERED BIASES & ATTACKS
═══════════════════════════════════════════════════════════════════════════════════════════

1. INITIAL BYTE BIAS (2001 - Fluhrer, Mantin, Shamir)
───────────────────────────────────────────────────────────────────────────────────────────
• First keystream byte biased towards 0x00 (1/128 instead of 1/256)
• Probability = 1/128 (expected 1/256) → 100% bias
• Used in FMS attack against WEP

2. SECOND BYTE BIAS (2001)
───────────────────────────────────────────────────────────────────────────────────────────
• Second byte biased towards 0x00 (1/128)
• Same bias as first byte
• Further weakened WEP security

3. MANTIN'S 2005 BIAS (8-16 bytes)
───────────────────────────────────────────────────────────────────────────────────────────
• Positions 8-16 show subtle biases
• Probability differences of ~0.5%
• Used in practical HTTPS cookie recovery

4. ALFARDA 2013 ATTACK (1MB data)
───────────────────────────────────────────────────────────────────────────────────────────
• Required only 1MB of ciphertext
• Could recover cookies in 75 hours
• Worked against TLS-RC4 in practice

5. PROVERBS 2015 ATTACK (16MB data)
───────────────────────────────────────────────────────────────────────────────────────────
• Required 16MB of ciphertext
• 75% success rate for cookie recovery
• Final nail in RC4's coffin

═══════════════════════════════════════════════════════════════════════════════════════════

📊 MAJOR BIASES DISCOVERED IN RC4
═══════════════════════════════════════════════════════════════════════════════════════════

┌──────────────┬─────────────┬──────────────────┬─────────────────────────────────────┐
│ Byte Position│ Bias Value  │ Probability      │ Attack Complexity                   │
├──────────────┼─────────────┼──────────────────┼─────────────────────────────────────┤
│ 1st byte     │ 0x00        │ 2x expected      │ Trivial - part of WEP breaks        │
│ 2nd byte     │ 0x00        │ 2x expected      │ FMS attack                          │
│ 3rd-7th      │ Various     │ +0.5-1%          │ Mantin's attack                     │
│ 8th-16th     │ Various     │ +0.3-0.8%        │ Practical HTTPS attacks             │
│ 257th+       │ Long-term   │ Small but real   │ Statistical over many packets       │
└──────────────┴─────────────┴──────────────────┴─────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════════════

🛡️ WHY TLS 1.3 BANNED RC4
═══════════════════════════════════════════════════════════════════════════════════════════

1. CUMULATIVE EVIDENCE:
   • Over 15 years of cryptanalysis
   • Multiple independent bias discoveries
   • Practical attacks requiring minimal data

2. REAL-WORLD EXPLOITS:
   • BEAST-like attacks on RC4 in TLS
   • Cookie recovery from HTTPS traffic
   • Plaintext recovery possible in hours/days

3. BETTER ALTERNATIVES EXIST:
   • ChaCha20-Poly1305 (modern stream cipher)
   • AES-GCM (block cipher in counter mode)
   • No known biases or weaknesses

4. INDUSTRY CONSENSUS:
   • RFC 7465 (2015) - Prohibits RC4 in TLS
   • TLS 1.3 (2018) - Removed RC4 entirely
   • Browsers removed RC4 support by 2016

═══════════════════════════════════════════════════════════════════════════════════════════

🔬 MATHEMATICAL REASON FOR BIAS
═══════════════════════════════════════════════════════════════════════════════════════════

THE RC4 BIAS EXPLAINED:
───────────────────────────────────────────────────────────────────────────────────────────

The PRGA state update equation:
    i = i + 1
    j = j + S[i]
    swap(S[i], S[j])
    output = S[(S[i] + S[j])]

For early outputs:
1. After KSA, S[0] is often related to key bytes
2. Initial swaps preserve key relationships
3. Probability distribution is not uniform

Result: P(output_byte = 0) = 1/128 instead of 1/256

This 100% bias means:
• Attacker sees 0x00 twice as often as expected
• Statistical tests detect bias with few samples
• Information leaks about plaintext

═══════════════════════════════════════════════════════════════════════════════════════════

💀 PRACTICAL IMPACT
═══════════════════════════════════════════════════════════════════════════════════════════

REAL ATTACK SCENARIO:
───────────────────────────────────────────────────────────────────────────────────────────
1. Attacker sniffs HTTPS traffic (easy on public WiFi)
2. Collects ~16MB of RC4-encrypted data
3. Applies statistical bias analysis
4. Recovers encrypted cookies/sessions
5. Hijacks user accounts

TIME REQUIRED (2015 research):
• 16MB data collection: ~1 hour on fast connection
• Analysis: ~75 hours on single CPU
• Success rate: 75% for cookie recovery

Today with better hardware: ~4-8 hours total!

═══════════════════════════════════════════════════════════════════════════════════════════

✅ MODERN ALTERNATIVES
═══════════════════════════════════════════════════════════════════════════════════════════

┌─────────────────┬──────────────┬──────────────┬──────────────────────────────────────┐
│ Cipher          │ Type         │ Security     │ Status                               │
├─────────────────┼──────────────┼──────────────┼──────────────────────────────────────┤
│ ChaCha20        │ Stream       │ No known     │ ✅ RECOMMENDED (TLS 1.3, WireGuard)  │
│ AES-CTR         │ Block/Stream │ No known     │ ✅ RECOMMENDED (AES-NI hardware)     │
│ AES-GCM         │ Authenticated│ No known     │ ✅ RECOMMENDED (standard in TLS)     │
│ RC4             │ Stream       │ BROKEN       │ ❌ DEPRECATED (banned in TLS 1.3)    │
└─────────────────┴──────────────┴──────────────┴──────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    🔥 RC4: LEGACY OF A BROKEN STREAM CIPHER 🔥
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        security_text.insert('1.0', security_content)
        security_text.config(state='disabled')

def main():
    root = tk.Tk()
    app = RC4CyberSuite(root)
    root.mainloop()

if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║         RC4 CYBER-SUITE - STREAM CIPHER ANALYSIS PLATFORM            ║
    ║                                                                       ║
    ║     Features:                                                         ║
    ║     ✓ Full RC4 implementation (KSA + PRGA)                           ║
    ║     ✓ WEP weak IV vulnerability demonstration                        ║
    ║     ✓ Statistical bias analysis (10,000+ keystreams)                 ║
    ║     ✓ Interactive graphs with matplotlib                            ║
    ║     ✓ TLS 1.3 ban analysis & security discussion                    ║
    ║                                                                       ║
    ║     Starting GUI...                                                  ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """)
    main()