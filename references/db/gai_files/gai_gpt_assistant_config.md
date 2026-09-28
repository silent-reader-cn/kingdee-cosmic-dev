# cosmic助手-gai_gpt_assistant_config

## cosmic助手-主表 t_gai_assistant_config

- **表名称：** cosmic助手-主表
- **表名：** t_gai_assistant_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpicture | 图片字段 | varchar | 255 |  |  | '' | 图片字段 |
| 3 | fradiogroupfield | 单选按钮组 | varchar | 50 |  |  | ' ' | 单选按钮组,枚举: 0 :有创意的风格 1 :平衡的风格 2 :精准的风格 |
| 4 | fname | Cosmic | varchar | 20 |  |  | ' ' | Cosmic |
| 5 | fpersona | 助手人设 | varchar | 50 |  |  | ' ' | 助手人设 |
| 6 | fintroduce | 自我介绍 | varchar | 255 |  |  | ' ' | 自我介绍 |
| 7 | fllm | 模型下拉列表 | varchar | 100 |  |  | ' ' | 模型下拉列表,枚举: |
| 8 | fswitchvoice | 复选框 | varchar | 1 |  |  | '0' | 复选框 |
| 9 | fprompt | 提示词 | int8 | 64 |  | √ | 0 | GPT提示 gai_prompt |
| 10 | fopeningspeech | 开场白 | varchar | 50 |  |  | ' ' | 开场白 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_assistant_config |  | fid |
| 2 | idx_gai_assistant_config |  | fname |
