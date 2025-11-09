# Minstrel-JP: 自動プロンプトエンジニアリングツール

こちらからランディングページにアクセスできます: [Minstrel-JP ランディングページ](https://minstrel-jp-lp.netlify.app/)

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

5.  ブラウザで開かれたアプリケーションで以下の手順を実行します。

    - サイドバーで基本情報（役割、作成者、バージョン、概要）を入力
    - ステップ1でタスクを入力し、「分析開始」をクリック
    - ステップ2で右側のモジュール制御パネルで必要なモジュールを選択し、「生成開始」をクリック
    - ステップ3で「プロンプト作成」をクリックして最終的なプロンプトを生成

## システムアーキテクチャ

Minstrel-JPは、以下のAIエージェントが連携して動作します。

*   **Analyzer**: ユーザーのタスク要求を分析し、必要なプロンプトモジュールを特定
*   **Designer**: 特定されたモジュールに基づいて、プロンプトの具体的な内容を生成
*   **Simulator**: 生成されたプロンプトをテストし、期待される出力を生成
*   **Questioner**: シミュレーション結果に基づいて、プロンプトの改善点を特定するための質問を生成
*   **Commentator**: シミュレーション結果と質問に対する回答を評価し、プロンプトの改善点を提案
*   **Reflector**: Commentatorの提案に基づいて、プロンプトを改善

## 使用技術

*   **プログラミング言語**: Python 3.10+
*   **生成AI**: GPT-4o (OpenAI)
*   **UIフレームワーク**: Streamlit
*   **プロンプトフレームワーク**: LangGPT

## プロジェクト構成

```
Minstrel-jp/
├── app.py                    # メインアプリケーション
├── showcases/
│   └── generate.py          # プロンプト生成UI
├── modules/                 # モジュール生成関数
│   ├── get_modules.py      # モジュール分析
│   ├── background.py       # 背景モジュール
│   ├── command.py          # 命令モジュール
│   ├── constraints.py      # 制約モジュール
│   ├── goal.py             # 目標モジュール
│   ├── initialization.py   # 初期化モジュール
│   ├── output_format.py    # 出力形式モジュール
│   ├── skills.py           # スキルモジュール
│   ├── suggestion.py       # 提案モジュール
│   └── workflow.py         # ワークフローモジュール
└── requirements.txt         # 依存パッケージ
```

## 参考文献

- [LangGPT: Rethinking Structured Reusable Prompt Design Framework](https://arxiv.org/abs/2409.13449)
