# Minstrel-JP: 自動プロンプトエンジニアリングツール

 [こちら](https://minstrel-jp-lp.netlify.app/)からランディングページにアクセスできます。

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3ef19346-50e6-448a-927b-f4b64d65c6f7" />


Minstrel-JPは、生成AIへのプロンプト作成を自動化するプロンプトエンジニアリングツールです。ユーザーのタスク要求を分析し、LangGPTフレームワークに基づいた構造化プロンプトを自動生成します。

## 主な機能

### 3ステップワークフロー

1. **タスク分析**: タスクの説明を入力すると、必要なプロンプトモジュールを自動で特定
2. **モジュール生成**: 選択したモジュールの内容を自動生成
3. **プロンプト作成**: 生成したモジュールを統合して完成したプロンプトを作成

### 11種類のモジュールサポート

- **背景 (Background)**: タスクの背景情報
- **命令 (Command)**: 具体的な実行命令
- **提案 (Suggestion)**: 推奨事項やヒント
- **目標 (Goal)**: タスクの目的
- **タスクのサンプル (Examples)**: 入出力のサンプル
- **制約 (Constraints)**: 制限事項や注意点
- **ワークフロー (Workflow)**: 実行手順
- **出力形式 (Output Format)**: 期待される出力の形式
- **スキル (Skills)**: 必要な能力
- **スタイル (Style)**: 応答のトーン
- **初期化 (Initialization)**: 初期設定

## 使用方法

### 前提条件

*   Python 3.10以上
*   OpenAI APIキー

### インストール手順

1.  リポジトリをクローンします。

    ```bash
    git clone https://github.com/ShinokiYuma/Minstrel-jp.git
    cd Minstrel-jp
    ```

2.  必要なパッケージをインストールします。

    ```bash
    pip install -r requirements.txt
    ```

3.  OpenAI APIキーを設定します。

    Minstrel-JP は OpenAI の GPT-4o モデルを使用します。OpenAI の API キーを取得し、環境変数に設定してください。

    ```bash
    export OPENAI_API_KEY="your_api_key_here"
    ```

    または、コード内で直接APIキーを設定することも可能です。（非推奨）

    ```python
    generator = Generator(
        api_key="your_api_key_here",  # ここに直接記述
        base_url="https://api.openai.com/v1"
    )
    ```

4.  Streamlit アプリケーションを実行します。

    ```bash
    streamlit run app.py
    ```

## 使用技術

*   **プログラミング言語**: Python 3.10+
*   **生成AI**: GPT-4o (OpenAI)
*   **UIフレームワーク**: Streamlit
*   **プロンプトフレームワーク**: LangGPT

## プロジェクト構成

```
Minstrel-jp/
├── app.py                      # メインアプリケーション
├── README.md                   # プロジェクト説明
├── requirements.txt            # 依存パッケージ
├── agents/                     # エージェント関連
│   ├── agent_commentators.py  # コメンテーターエージェント
│   ├── agent_reflector.py     # リフレクターエージェント
│   └── models/                # エージェント用モデル
│       ├── openai.py          # OpenAI モデル
│       └── transformers.py    # Transformers モデル
├── lp/                        # ランディングページ
│   ├── index.html            # HTMLファイル
│   ├── script.js             # JavaScriptファイル
│   └── style.css             # CSSファイル
├── models/                    # モデル関連
│   ├── openai.py             # OpenAI モデル
│   └── transformers.py       # Transformers モデル
├── modules/                   # モジュール生成関数
│   ├── get_modules.py        # モジュール分析
│   ├── background.py         # 背景モジュール
│   ├── command.py            # 命令モジュール
│   ├── constraints.py        # 制約モジュール
│   ├── goal.py               # 目標モジュール
│   ├── initialization.py     # 初期化モジュール
│   ├── output_format.py      # 出力形式モジュール
│   ├── skills.py             # スキルモジュール
│   ├── suggestion.py         # 提案モジュール
│   └── workflow.py           # ワークフローモジュール
└── showcases/                 # サンプル・デモ
    ├── generate.py           # プロンプト生成UI
    ├── noticecomplete.py     # 完了通知
    └── test.py               # テストファイル
```

## 参考文献

- [LangGPT: Rethinking Structured Reusable Prompt Design Framework](https://arxiv.org/abs/2409.13449)
