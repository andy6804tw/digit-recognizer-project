# MNIST python Flask API

## Structure
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

## Getting Started
### Clone Project
you can create a new project based on digit-recognizer-project by doing the following:

```bash
git clone https://github.com/andy6804tw/digit-recognizer-project.git
cd digit-recognizer-project
```

### Installation
When that's done, install the project dependencies.
```bash
python install -r requirements.txt
```

### Running the Project
After completing the installation step, you're ready to start the project.

| script | Description |
| ------| ------ |
| start | Serves your app at localhost:5001 |


`python run.py` running locally! Your app should now be running on [localhost:5001](http://localhost:5001/).

## Contribute
### Report Issues and Improvement Suggestions
File report at this project's [issue](https://github.com/andy6804tw/digit-recognizer-project/issues) tracker if you noticed some problem or have improvement suggestions.