# Minstrel-JP: 自動プロンプトエンジニアリングツール

Minstrel-JPは、生成AIへのプロンプト作成を自動化するプロンプトエンジニアリングツールです。ユーザーのタスク要求を分析し、LangGPTフレームワークに基づいた構造化プロンプトを自動生成します。

 [こちら](https://minstrel-jp-lp.netlify.app/)からランディングページにアクセスできます。

<img width="1900" height="868" alt="image" src="https://github.com/user-attachments/assets/94919e8a-9d3c-4eaf-a248-27b027d01cf7" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3ef19346-50e6-448a-927b-f4b64d65c6f7" />


## Minstrel-JPとは！

「生成AIに大きなタスクを任せよう！...でも、どんなプロンプトがいいかな？うまくできる気がしないな...」
こんな時はありませんか？プロンプトを作るのって難しいですよね...。Minstrel-JPは、そんなあなたのためのツールです！
このツールを使えば、あなたは簡単な指示を入力するだけで、複雑なプロンプトにAIが自動で拡張してくれます。

### プロンプトフレームワーク「LangGPT」に基づくプロダクト改善

Minstrel-JPは、ただ単にプロンプトを拡張するだけではありません。論文として発表されている[LangGPTフレームワーク](https://arxiv.org/abs/2409.13449)に基づき、構造化された再利用可能なプロンプトモジュールを生成します。これにより、プロンプトの品質と一貫性が向上し、様々なタスクに対応可能です。

## 簡単3ステップで完了！

### ①タスク分析

あなたがAIに任せたいタスクを簡単に説明してください。その説明をもとに、AIがタスク遂行に必要なプロンプトモジュールを自動で特定します。

### ②モジュール生成

特定されたプロンプトモジュールの内容をAIが作成します。各モジュールは、タスクに最適な指示や制約を含むように設計されています。

### ③プロンプト作成

生成されたモジュールを統合し、AIが改善されたプロンプトを提供します。テストチャット機能を使って、生成されたプロンプトをすぐに試すことも可能です。

## 11種類のプロンプトモジュールをサポート！

| モジュール名 | 説明 |
|------------|------|
| 背景 (Background) | タスクの背景情報 |
| 命令 (Command) | 具体的な実行命令 |
| 提案 (Suggestion) | 推奨事項やヒント |
| 目標 (Goal) | タスクの目的 |
| タスクのサンプル (Examples) | 入出力のサンプル |
| 制約 (Constraints) | 制限事項や注意点 |
| ワークフロー (Workflow) | 実行手順 |
| 出力形式 (Output Format) | 期待される出力の形式 |
| スキル (Skills) | 必要な能力 |
| スタイル (Style) | 応答のトーン |
| 初期化 (Initialization) | 初期設定 |

## AIエージェントによる改善サイクル！

テストチャット画面では、改善されたプロンプトをさらに改善することが可能です。コメンテーターエージェントがプロンプトの問題点を指摘し、リフレクターエージェントが改善案を提案します。これにより、プロンプトの品質を継続的に向上させることができます。これらの操作をワンボタンで、数10秒で実現します。

## 使用方法（リポジトリをクローンしてローカルで実行する場合）

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

- [LangGPT: Rethinking Structured Reusable Prompt Design Framework for LLMs from the Programming Language](https://arxiv.org/pdf/2402.16929)
- [Minstrel: Structural Prompt Generation with Multi-Agents Coordination for Non-AI Experts](https://arxiv.org/pdf/2409.13449)