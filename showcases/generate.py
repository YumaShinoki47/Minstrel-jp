import sys
import os
import json
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.

import streamlit as st
from modules.get_modules import get_modules
from modules.background import gen_background
from modules.command import gen_command
from modules.constraints import gen_constraints
from modules.goal import gen_goal
from modules.initialization import gen_initialization
from modules.output_format import gen_output_format
from modules.skills import gen_skills
from modules.suggestion import gen_suggestion
from modules.workflow import gen_workflow

module_name_dict = {
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
}

module_func_dict = {
    "background": gen_background,
    "command": gen_command,
    "suggesstion": gen_suggestion,
    "goal": gen_goal,
    "examples": None,
    "constraints": gen_constraints,
    "workflow": gen_workflow,
    "output_format": gen_output_format,
    "skills": gen_skills,
    "style": None,
    "initialization": gen_initialization
}

## LangGPTプロンプトを生成するページ
def generate():
    state = st.session_state
    
    # フェーズ管理の初期化
    if "current_phase" not in state:
        state.current_phase = 1

    ## サイドバー
    with st.sidebar: 
        st.title("Minstrel JP")

        st.divider()
        st.subheader("基本情報入力")
        state.role_name = st.text_input("役割","",help="AIが振る舞う役割を指定してください。例：○○の専門家、○○のアシスタント")
        state.author = st.text_input("作成者","",help="あなたのお名前を入力できます。空欄でも問題ありません。")
        state.version = st.number_input("バージョン",min_value=0.1,value=0.1,step=0.1,help="プロンプトのバージョン。改善の度に0.1ずつ更新されます。")
        state.description = st.text_area("概要","",height=100,help="もし特記事項があれば入力してください。")
        
        st.divider()
        if st.button("🔄 全てリセット", use_container_width=True, type="secondary"):
            # セッションステートの主要な変数をクリア
            keys_to_clear = [
                "current_phase", "role_name", "author", "version", "description",
                "input", "module_messages", "modules", "on_modules", "prompt",
                "background", "command", "suggesstion", "goal", "examples",
                "constraints", "workflow", "output_format", "skills", "style",
                "initialization"
            ]
            for key in keys_to_clear:
                if key in state:
                    del state[key]
            st.rerun()
        pass
    
    # メイン画面を3列に分割
    left_col, center_col, right_col = st.columns([7, 0.5, 7])
    
    with left_col:
        st.subheader("ワークフロー")
        ## ステップ1: タスク入力とモジュール設定（カード化）
        phase1_status = "✅" if state.current_phase > 1 else "⬜"
        with st.container(border=True):
            st.markdown(f"### ① タスク分析 {phase1_status}")
            st.markdown("タスクを入力してモジュールを自動設定")
            
            task = st.text_input("タスクの説明", "", label_visibility="collapsed", placeholder="実行したいタスクを入力してください")
            state.input = task
            
            analyze_button = st.button(
                "分析開始",
                type="primary",
                use_container_width=True,
                key="analyze_btn",
                disabled=state.current_phase != 1
            )
            
            if analyze_button:
                with st.spinner("タスクを分析中..."):
                    state.module_messages = [{"role": "user", "content": f"私がLLMに実行してほしいタスクは：{task}"}]
                    state.modules = get_modules(state.generator, state.module_messages)
                    state.current_phase = 2
                st.rerun()
        
        # if "modules" in state:
        #     if state.on_modules["examples"]: ## 「タスクのサンプル」モジュールがオンになったとき
        #         st.subheader("タスクのサンプルを提供してください：")
        #         input_example = st.text_area("サンプル入力","")
        #         output_example = st.text_area("サンプル出力","")
        #         state.examples = {
        #             "input": input_example,
        #             "output": output_example
        #         }
        #         pass
        #     if state.on_modules["style"]: ## 「スタイル」モジュールがオンになったとき
        #         st.subheader("返信のスタイルを指定してください：")
        #         style = st.text_input("スタイル","",help="例: 公式、ユーモア、真面目など",label_visibility="collapsed")
        #         state.style = style
        #         pass
            ## 生成されたモジュールの表示と編集（既にモジュールが生成されてる）
            # for key in state.modules.keys():
            #     if key in state: ## state[key]に指定されたモジュールの内容が格納されている
            #         if state.on_modules[key]:
            #             with st.expander(module_name_dict[key]):
            #                 st.text_area(module_name_dict[key],state[key],label_visibility="collapsed")
            #                 pass
            #     pass
            
        ## ステップ2: モジュール生成（カード化）
        phase2_status = "✅" if state.current_phase > 2 else "⬜"
        with st.container(border=True):
            st.markdown(f"### ➁ モジュール生成 {phase2_status}")
            st.markdown("選択したモジュールの内容を自動生成")
            generate_button = st.button(
                "生成開始",
                type="primary",
                use_container_width=True,
                key="gen_btn",
                disabled=state.current_phase != 2
            )

            ## モジュールを生成ボタンが押されたとき
            if generate_button:
                with st.spinner("モジュールを生成中..."):
                    for key in state.modules.keys():
                        if key == "examples" or key == "style": ## exampleとstyleはスキップ
                            continue
                        else:
                            if state.on_modules[key]: ## onになってるモジュールのみ
                                if key not in state:
                                    state[key] = module_func_dict[key](state.generator,state.module_messages) ## ここでモジュールの内容を作成してる
                            pass
                        pass
                    state.current_phase = 3
                st.rerun()
                pass
            
        ## ステップ3: プロンプト作成（カード化）
        phase3_status = "✅" if state.current_phase > 3 else "⬜"
        with st.container(border=True):
            st.markdown(f"### ③ プロンプト作成 {phase3_status}")
            st.markdown("モジュールを統合してプロンプト完成")
            compose_button = st.button(
                "プロンプト作成",
                type="primary",
                use_container_width=True,
                key="comp_btn",
                disabled=state.current_phase != 3
            )
            
                        ## プロンプト合成ボタンが押されたとき
            if compose_button:
                with st.spinner("プロンプトを作成中..."):
                    if "prompt" not in state:
                        state.prompt = "" ## プロンプト初期化
                        pass
                    ## 入力された基本情報(役割、作成者、バージョン、説明)をプロンプトに追加
                    if state.role_name:
                        state.prompt += f"# 役割: {state.role_name}\n"
                        pass
                    state.prompt += f"## プロフィール\n"
                    if state.author:
                        state.prompt += f"- 作成者: {state.author}\n"
                        pass
                    if state.version:
                        state.prompt += f"- バージョン: {state.version}\n"
                        pass
                    if state.description:
                        state.prompt += f"- 説明: {state.description}\n"
                        pass
                    ## チェックしたモジュールがすべて生成されているかチェックする
                    for key in state.modules.keys():
                        if state.on_modules[key]:
                            if key not in state:
                                st.error(f"先に{module_name_dict[key]}を生成してください")
                                return
                            ## 生成されたモジュールをプロンプトに追加
                            if key == "examples":
                                state.prompt += f"## {module_name_dict[key]}\n"
                                state.prompt += f"### 入力\n"
                                state.prompt += state.examples["input"]
                                state.prompt += "\n"
                                state.prompt += f"### 出力\n"
                                state.prompt += state.examples["output"]
                                state.prompt += "\n\n"
                            else:
                                state.prompt += f"## {module_name_dict[key]}\n"
                                state.prompt += json.dumps(state[key], ensure_ascii=False, indent=2)
                                state.prompt += "\n\n"
                    
                    state.current_phase = 4
                    state.page = "noticecomplete"
                    pass
                st.rerun()
    
    with center_col:
        # 中央列は空白（マージン用）
        pass
    
    with right_col:
        st.subheader("モジュール制御")
        
        if "modules" not in state:
            state.modules = {
                "background": False,
                "command": False,
                "suggesstion": False,
                "goal": False,
                "examples": False,
                "constraints": False,
                "workflow": False,
                "output_format": False,
                "skills": False,
                "style": False,
                "initialization": False
            }
        
        if "on_modules" not in state:
            state.on_modules = {}
        
        for key in state.modules.keys():
            if key in module_name_dict:
                with st.container(border=True):
                    state.on_modules[key] = st.toggle(module_name_dict[key], state.modules[key])
                
                    # examplesモジュールがオンの場合の入力フォーム
                    if key == "examples" and state.on_modules[key]:
                        st.markdown("**タスクのサンプルを提供してください:**")
                        input_example = st.text_area("サンプル入力", "", key=f"input_example_{key}", height=100)
                        output_example = st.text_area("サンプル出力", "", key=f"output_example_{key}", height=100)
                        if input_example or output_example:
                            state.examples = {
                                "input": input_example,
                                "output": output_example
                            }
                    
                    # styleモジュールがオンの場合の入力フォーム
                    elif key == "style" and state.on_modules[key]:
                        st.markdown("**返信のスタイルを指定してください:**")
                        style = st.text_input(
                            "スタイル", 
                            "", 
                            help="例: 公式、ユーモア、真面目など",
                            key=f"style_input_{key}"
                        )
                        if style:
                            state.style = style
                    
                    # トグルがオンで、モジュールが生成されている場合は内容を表示
                    elif state.on_modules[key] and key in state:
                        with st.expander(f"内容を確認", expanded=False):
                            st.text_area(
                                module_name_dict[key],
                                state[key],
                                label_visibility="collapsed",
                                height=200,
                                key=f"module_display_{key}"
                            )

st.set_page_config(
     page_title="Minstrel JP",
     page_icon="🤖",
     layout="wide",
    #  initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!",
     }
 )