import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path)

import streamlit as st
import streamlit.components.v1 as components

## プロンプト生成完了通知ページ
def noticecomplete():
    state = st.session_state
    
    col1, col2, col3 = st.columns([1, 7, 1])
    
    with col2:
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        
        # 完成アイコンと見出し
        st.markdown("# 🎉 プロンプト生成完了です！")
        
        st.markdown("---")
        
        # 完成したプロンプトの情報
        st.markdown("### ✅ 完成したプロンプト")
        
        with st.expander("内容を確認", expanded=True):
            if "prompt" in state:
                # テキストエリア
                st.text_area(
                    "",
                    state.prompt,
                    height=300,
                    label_visibility="visible"
                )
                
                # JavaScriptを使ったコピーボタン
                copy_button_html = f"""
                <script>
                function copyToClipboard() {{
                    const text = `{state.prompt.replace('`', '//`').replace('$', '//$')}`;
                    navigator.clipboard.writeText(text).then(function() {{
                        const btn = document.getElementById('copy-btn');
                        btn.innerHTML = '✅ コピーしました！';
                        btn.style.backgroundColor = '#28a745';
                        setTimeout(function() {{
                            btn.innerHTML = '📋 プロンプトをコピー';
                            btn.style.backgroundColor = '#0068c9';
                        }}, 2000);
                    }}, function(err) {{
                        alert('コピーに失敗しました');
                    }});
                }}
                </script>
                <button id="copy-btn" onclick="copyToClipboard()" style="
                    width: 100%;
                    padding: 0.5rem 1rem;
                    background-color: #0068c9;
                    color: white;
                    border: none;
                    border-radius: 0.5rem;
                    cursor: pointer;
                    font-size: 1rem;
                    margin-top: 0.5rem;
                ">📋 プロンプトをコピー</button>
                """
                components.html(copy_button_html, height=60)
            else:
                st.warning("プロンプトが生成されていません")
        
        st.markdown("")
        
        # ボタンの配置
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button(
                "← 編集画面に戻る",
                use_container_width=True,
                type="secondary"
            ):
                state.current_phase = 3
                state.page = "generate"
                st.rerun()
        
        with col_btn2:
            if st.button(
                "実際に試す →",
                use_container_width=True,
                type="primary"
            ):
                # テストページに必要な初期化
                if "test_messages" not in state:
                    state.test_messages = [{"role": "system", "content": state.prompt}]
                state.page = "test"
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # サイドバー情報
        with st.sidebar:
            st.title("Minstrel JP")
            st.divider()
            
            st.subheader("📋 プロンプト情報")
            
            if "role_name" in state and state.role_name:
                st.markdown(f"**役割:** {state.role_name}")
            
            if "author" in state and state.author:
                st.markdown(f"**作成者:** {state.author}")
            
            if "version" in state and state.version:
                st.markdown(f"**バージョン:** {state.version}")
            
            if "description" in state and state.description:
                st.markdown(f"**概要:** {state.description}")
            
            st.subheader("🎯 アクティブなモジュール")
            if "on_modules" in state:
                active_modules = [
                    name for key, name in {
                        "background": "背景",
                        "command": "命令",
                        "suggesstion": "提案",
                        "goal": "目標",
                        "examples": "タスクのサンプル",
                        "constraints": "制約",
                        "workflow": "ワークフロー",
                        "output_format": "出力形式",
                        "skills": "スキル",
                        "style": "スタイル",
                        "initialization": "初期化"
                    }.items()
                    if key in state.on_modules and state.on_modules[key]
                ]
                
                if active_modules:
                    for module in active_modules:
                        st.markdown(f"✅ {module}")
                else:
                    st.markdown("_モジュールが選択されていません_")


