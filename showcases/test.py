import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.
from models.openai import Generator
import streamlit as st

## コメンテーターエージェント
from agents.agent_commentators import Commentators
## リフレクターエージェント
from agents.agent_reflector import Reflector


def test():
    state = st.session_state
    
    ## サイドバーに「はじめに戻る」ボタンを追加
    with st.sidebar:
        
        if st.button("⬅　1つ前に戻る", use_container_width=True, type="primary"):
            state.page = "noticecomplete"
            st.rerun()
        
        if st.button("🏠　はじめに戻る", use_container_width=True, type="secondary"):
            # セッション状態を初期化
            keys_to_keep = ['generator']  # generatorだけは保持
            keys_to_delete = [key for key in state.keys() if key not in keys_to_keep]
            for key in keys_to_delete:
                del state[key]
            
            state.current_phase = 1
            state.page = "generate"
            st.rerun()
    
    # 画面を2分割
    col_left, col_middle, col_right = st.columns([7, 0.5, 7])
    
    # 左カラム：生成されたプロンプト
    with col_left:
        st.subheader("生成されたプロンプト")
        prompt_origin = st.text_area(
            "langgpt_prompt", 
            state.prompt, 
            height=400, 
            label_visibility="collapsed"
        )
        
        ## メッセージを生成済みの場合のみボタンを表示
        if st.button("プロンプトを分析＆改善", use_container_width=True):
            with st.spinner("プロンプトを分析＆改善中..."):
                ## 現在のプロンプトを履歴として保存
                if "prompt_history" not in state:
                    state.prompt_history = []
                state.prompt_history.append(state.prompt)
                
                ## ここでコメンテーターエージェントに接続する！
                print("【メインシステム】プロンプトを受け付けました。コメンテーターエージェントに接続中．．．") # デバッグ
                commentators = Commentators( ## 初期値定義できる
                    requirement = state.input,
                    prompt = state.prompt,
                    answer = state.response
                )
                ## 5つのコメンテーターエージェントからコメントを取得
                comment_criticize_1 = commentators.com_agent_criticize_1()
                comment_criticize_2 = commentators.com_agent_criticize_2()
                comment_favor_1 = commentators.com_agent_favor_1()
                comment_favor_2 = commentators.com_agent_favor_2()
                comment_natural = commentators.com_agent_natural()
                ## 5つのコメントをまとめる
                comment_overall = f"""
------------------------------------------------------------------
コメント1（批判的）
{comment_criticize_1}
------------------------------------------------------------------
コメント2（批判的）
{comment_criticize_2}
------------------------------------------------------------------
コメント3（好意的）
{comment_favor_1}
------------------------------------------------------------------
コメント4（好意的）
{comment_favor_2}
------------------------------------------------------------------
コメント5（中立的）
{comment_natural}
------------------------------------------------------------------
            """
                print("【コメンテーターエージェント】：コメントを作成しました。リフレクターエージェントに接続中...") ## デバッグ

                ## まとめたコメントをリフレクターエージェントに接続する
                reflector = Reflector(
                    prompt = state.prompt,
                    comment = comment_overall
                )

                ## プロンプトを書き換えて表示
                state.prompt = reflector.ref_agent()
                print(f""" 
----------------------------------------------------------------------
{state.prompt}
----------------------------------------------------------------------
【リフレクターエージェント】：コメントを反映し、プロンプトを改善しました。
            """) ##デバッグ用
                
                print("【メインシステム】新しいプロンプトでの回答が生成されました。") ##デバッグ用

            st.rerun() ## stateをと表示内容を同期

        ## 1つ前のバージョンを表示
        if "prompt_history" in state and len(state.prompt_history) > 0:
            st.divider()
            st.subheader("以前のバージョンのプロンプト")
            st.text_area(
                "previous_prompt",
                state.prompt_history[-1],
                height=400,
                label_visibility="collapsed",
            )

    # 右カラム：テストチャット
    with col_right:
        st.subheader("テストチャット")
        
        with st.container(border=True, height=400):
            ## 初回アクセス時はメッセージリストを初期化するのみ（自動実行しない）
            if "test_messages" not in state:
                state.test_messages = [{"role": "system", "content": state.prompt}]
            
            ## チャットの内容を順次表示
            for message in state.test_messages:
                if message["role"] == "system":
                    continue
                st.chat_message(message["role"]).write(message["content"])
        
        col_1, col_2 = st.columns([4 ,1])

        with col_1:
            ## 入力した会話から返事を生成
            if prompt := st.chat_input("会話を入力"):
                state.test_messages.append({"role": "user", "content": prompt})
                st.rerun()  
        
        ## ユーザーメッセージが追加されたが、AIの応答がまだない場合、ローディングマークを表示
        if len(state.test_messages) > 0 and state.test_messages[-1]["role"] == "user":
            with st.spinner("応答を生成中..."):
                response = state.generator.generate_response(state.test_messages)
                state.response = response ## 分析&改善用にstateにresponseを追加して保存
                state.test_messages.append({"role": "assistant", "content": response})
                st.rerun()
        
        with col_2:
            ## チャット履歴クリア
            if st.button("履歴をクリア", use_container_width=True, type="secondary"):
                del state.test_messages
                st.rerun()