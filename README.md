# 翻牌记忆游戏
给娃玩的一个翻牌游戏

Pygame开发

## 功能

- 翻转卡片来查看其隐藏的图像
- 两张翻开的卡片匹配，它们会保持翻开状态
- 如果不匹配，卡片会在一段时间后翻回去
- 当所有卡片成功匹配时游戏结束，可以Retry

## 安装依赖
```bash
pip install requirements.txt
```

## 运行游戏
- 在项目目录下，确保有 image1.png 到 image5.png 的图片文件 (已预置)
- 运行游戏：
   ```bash
   python flip_card_game.py
  ```
- 游戏开始后，点击卡片进行翻转
- 匹配所有卡片后，点击“Retry”按钮重新开始游戏或点击“Success”按钮关闭游戏。

## 文件
- flip_card_game.py：主游戏文件。
- README.md：项目说明文件。
- image1.png 到 image5.png：游戏中使用的卡片图像，支持更换

