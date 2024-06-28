import os
import tkinter as tk
from tkinter import ttk
from ignore_patterns import read_gitignore, is_ignored

def run_gui_file_selector(project_dir):
    root = tk.Tk()
    root.title("Select Files to Exclude from Summary")

    # ウィンドウを画面中央に配置
    window_width = 400
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    # 説明ラベルの追加
    label = ttk.Label(root, text="除外したいファイルやフォルダを選択してください。\n選択したアイテムはサマリーに含まれません。", wraplength=380)
    label.pack(pady=10)

    # Treeviewの設定
    style = ttk.Style()
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 12))
    style.configure("Treeview.Item", indicatorsize=0)
    style.map("Treeview", background=[('selected', 'white')], foreground=[('selected', 'black')])

    tree = ttk.Treeview(root, columns=('Checkbox',), show='tree')
    tree.heading('Checkbox', text='Select')
    tree.column('Checkbox', width=50, anchor='center')
    tree.pack(expand=True, fill='both')

    # チェックボックスの状態を保存する辞書
    checkbox_states = {}

    # .gitignore パターンを取得
    gitignore_patterns = read_gitignore(project_dir)
    additional_ignore_patterns = []  # 追加の除外パターンがあればここに追加

    def populate_tree(parent, path):
        items = sorted(os.listdir(path), key=lambda x: (not os.path.isdir(os.path.join(path, x)), x))
        for item in items:
            if item == '.gitignore':
                continue
            item_path = os.path.join(path, item)
            full_path = os.path.normpath(os.path.join(path, item))

            # .gitignore パターンに一致するかどうかをチェック
            if is_ignored(full_path, project_dir, gitignore_patterns, additional_ignore_patterns, []):
                continue

            checkbox_states[full_path] = tk.BooleanVar(value=False)
            tree_item = tree.insert(parent, 'end', text=item, open=False, values=('□',))
            if os.path.isdir(item_path):
                populate_tree(tree_item, item_path)

    populate_tree('', project_dir)

    def toggle_checkbox(event):
        item = tree.identify_row(event.y)
        if item:
            full_path = get_full_path(item)
            checkbox_states[full_path].set(not checkbox_states[full_path].get())
            update_checkbox_display(item)
            update_children(item)
            update_parent(tree.parent(item))
        return "break"

    def update_checkbox_display(item):
        full_path = get_full_path(item)
        tree.set(item, 'Checkbox', '■' if checkbox_states[full_path].get() else '□')

    def update_children(parent):
        for child in tree.get_children(parent):
            full_path = get_full_path(child)
            checkbox_states[full_path].set(checkbox_states[get_full_path(parent)].get())
            update_checkbox_display(child)
            if tree.get_children(child):
                update_children(child)

    def update_parent(parent):
        if parent:
            full_path = get_full_path(parent)
            children_checked = all(checkbox_states[get_full_path(child)].get() for child in tree.get_children(parent))
            checkbox_states[full_path].set(children_checked)
            update_checkbox_display(parent)
            update_parent(tree.parent(parent))

    def get_full_path(item):
        path_parts = []
        while item:
            path_parts.insert(0, tree.item(item, 'text'))
            item = tree.parent(item)
        return os.path.normpath(os.path.join(project_dir, *path_parts))

    tree.bind('<ButtonRelease-1>', toggle_checkbox)

    def get_excluded_items():
        excluded = []
        for path, var in checkbox_states.items():
            if var.get():
                excluded.append(os.path.relpath(path, project_dir))
        return excluded

    def on_ok():
        nonlocal excluded_items
        excluded_items = get_excluded_items()
        root.quit()
        root.destroy()

    ok_button = ttk.Button(root, text="OK", command=on_ok)
    ok_button.pack(pady=10)

    excluded_items = None
    root.protocol("WM_DELETE_WINDOW", root.quit)  # ×ボタンでウィンドウを閉じたときの処理
    root.mainloop()
    
    if excluded_items is None:
        print("ユーザーがキャンセルしました。プログラムを終了します。")
        import sys
        sys.exit(0)
    
    return excluded_items