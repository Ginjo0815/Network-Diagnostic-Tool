import tkinter as tk
import tkinter.font as tkFont
from command_internet_pingv6 import display_gateway_v4
from get_myip import display_myip_v4

def update_gateway_display():
    results_gateway = display_gateway_v4()

    # Gateway表示の更新
    widget_gateway_text.delete('1.0', tk.END)
    bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
    widget_gateway_text.insert(tk.END, results_gateway[0])
    widget_gateway_text.tag_add("title", "1.0", "1.end")
    widget_gateway_text.tag_config(f"title", foreground="yellow",font=bold_font)
    # 全体のステータスに対するタグ設定
    widget_gateway_text.tag_add("overall", "2.0", f"2.{len(results_gateway[1])}")
    widget_gateway_text.tag_config("overall", foreground="green" if results_gateway[1] == "OK" else "red", font=bold_font)
    # Short の結果に適用するタグを追加（文字色で表示）
    widget_gateway_text.tag_add("short", "2.4", "2.10")  # "Short"
    widget_gateway_text.tag_config("short", foreground="green" if results_gateway[2] == 0 else "red", font=bold_font)
    # Large の結果に適用するタグを追加（文字色で表示）
    widget_gateway_text.tag_add("large", "2.12", "2.17")  # "Large"
    widget_gateway_text.tag_config("large", foreground="green" if results_gateway[3] == 0 else "red", font=bold_font)

    # 3秒後に再度update_gateway_displayを呼び出す
    root.after(1000, update_gateway_display)

def view_all():
    global root, widget_myip_text, widget_gateway_text
    root = tk.Tk()
    root.title("Network Diagnostic Tool")
    root.configure(bg="black")
    results_myip = display_myip_v4()
    results_gateway = display_gateway_v4()

    widget_myip_text = tk.Text(root, height=7, width=60, bg="black", fg="white",borderwidth=0, highlightthickness=0)
    widget_myip_text.grid(row=0, column=0, padx=10, pady=10)

    widget_gateway_text = tk.Text(root, height=3, width=60, bg="black", fg="white",borderwidth=0, highlightthickness=0)
    widget_gateway_text.grid(row=1, column=0, padx=10, pady=10)

    bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
    widget_myip_text.insert(tk.END, results_myip)
    widget_myip_text.tag_add(f"1", f"1.0",f"1.end")
    widget_myip_text.tag_config(f"1", foreground="yellow",font=bold_font)

    bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
    widget_gateway_text.insert(tk.END,results_gateway[0])
    widget_gateway_text.tag_add(f"title", f"1.0",f"1.end")
    widget_gateway_text.tag_config(f"title", foreground="yellow",font=bold_font)    
    # 全体のステータスに対するタグ設定
    widget_gateway_text.tag_add("overall", "2.0", f"2.{len(results_gateway[1])}")
    widget_gateway_text.tag_config("overall", foreground="green" if results_gateway[1] == "OK" else "red", font=bold_font)
    # Short の結果に適用するタグを追加（文字色で表示）
    widget_gateway_text.tag_add("short", "2.4", "2.10")  # "Short"
    widget_gateway_text.tag_config("short", foreground="green" if results_gateway[2] == 0 else "red", font=bold_font)
    # Large の結果に適用するタグを追加（文字色で表示）
    widget_gateway_text.tag_add("large", "2.12", "2.17")  # "Large"
    widget_gateway_text.tag_config("large", foreground="green" if results_gateway[3] == 0 else "red", font=bold_font)

    update_gateway_display()  # 初回のゲートウェイ情報更新
    root.mainloop()


    def display_myip_v4():
    results = {}
    title = "-------Network Setting-------\n"
    results_text = f"{title}"
    results = get_myip_v4v6()

    if results[0]:
        results_text += f"Interface: {results[0]}\n"

    if results[1] and results[2]:
        results_text += f"IPv4 Address: {results[1]}\n"
        results_text += f"Netmask: {results[2]}\n"

    if results[3]:
        results_text += f"Default Gateway: {results[3]}\n"

    if results[4]:
        results_text += f"IPv6 Address: {results[4]}\n"

    return results_text
