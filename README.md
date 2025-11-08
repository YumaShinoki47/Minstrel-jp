# Minstrel-JP: 自動プロンプトエンジニアリングツール


## 使用方法

#### 前提条件

*   Python 3.10
*   OpenAI APIキー

#### 手順

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
    export OPENAI_API_KEY="OPENAI_API_KEY"
    ```

    または、コード内で直接APIキーを設定することも可能です。（非推奨）

    ```python
    generator = Generator(
        api_key="OPENAI_API_KEY",  # ここに直接記述
        base_url="https://api.openai.com/v1"
    )
    ```

4.  Streamlit アプリケーションを実行します。

    ```bash
    streamlit run app.py
    ```


## 概要

Minstrel-JPは、生成AIへのプロンプト改善を自動化するプロンプトエンジニアリングツールです。ユーザーのタスク要求を分析し、プロンプトフレームワークで定義されたモジュールと要素に基づいて、適切なプロンプトを自動生成します。

[<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3625313/db17fa02-8aad-4e8e-ac52-ad533f3aa215.png" width="400">](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3625313/db17fa02-8aad-4e8e-ac52-ad533f3aa215.png)

Minstrel-JPは、以下のAIエージェントが連携して動作します。

*   **Analyzer**: ユーザーのタスク要求を分析し、必要なプロンプトモジュールを特定します。
*   **Designer**: 特定されたモジュールに基づいて、プロンプトの具体的な内容を生成します。
*   **Simulator**: 生成されたプロンプトをテストし、期待される出力を生成します。
*   **Questioner**: シミュレーション結果に基づいて、プロンプトの改善点を特定するための質問を生成します。
*   **Commentator**: シミュレーション結果と質問に対する回答を評価し、プロンプトの改善点を提案します。
*   **Reflector**: Commentator の提案に基づいて、プロンプトを改善します。

## 使用技術

*   **プログラミング言語**: Python
*   **生成AI**: GPT-4o (OpenAI)
*   **フレームワーク**: Streamlit

## 参考
https://arxiv.org/abs/2409.13449#
