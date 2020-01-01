# Structure

```
API
┌── config.py // 環境變數設置
│   
├── app
│   ├── controllers  // 處理控制流程和回應
│   ├── modules // 後端資料庫進行運作or載入機器學習模型
│   └── __init__.py  // 各路徑的設定點
│
└── run.py  // 程式進入點
```