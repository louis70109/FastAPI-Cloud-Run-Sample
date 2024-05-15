# FastAPI 佈署到 Cloud Run 範例

本範例展示了如何使用 Google Cloud Run 快速佈署 FastAPI 應用程式。這個範例將引導您完成以下步驟：

- 使用 Dockerfile 建立一個 Docker 映像檔。
- 使用 gcloud CLI 在 Cloud Run 上啟動映像檔與佈署。
- 測試在 Cloud Run 上執行的 FastAPI 應用程式。

## 前置要求

在開始之前，您需要具備以下要求：

- 一個 Google Cloud Platform 帳戶。
- 安裝了 gcloud CLI 工具。
- 已經安裝 Docker 在本地端環境中。

## 使用方式

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)


```
git clone https://github.com/louis70109/FastAPI-Cloud-Run-Sample.git

cd FastAPI-Cloud-Run-Sample/

gcloud run deploy my-fastapi-example --source .
```

## 授權

## test

MIT
