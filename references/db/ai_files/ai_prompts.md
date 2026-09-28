# AI记账提示词-ai_prompts

## AI记账提示词-多语言表 t_ai_llmprompt_l

- **表名称：** AI记账提示词-多语言表
- **表名：** t_ai_llmprompt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscenedesc | 场景描述 | varchar | 255 |  | √ | ' ' | 场景描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_llmprompt_l |  | fpkid |
| 2 | idx_ai_llmprompt_l_0 |  | fid,flocaleid |

---

## AI记账提示词-主表 t_ai_llmprompt

- **表名称：** AI记账提示词-主表
- **表名：** t_ai_llmprompt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprompts_tag | 大模型提示词_详情 | text | 0 |  |  | null | 大模型提示词_详情 |
| 2 | fprompts | 大模型提示词 | varchar | 2000 |  | √ | ' ' | 大模型提示词 |
| 3 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 4 | fscenenumber | 场景编码 | varchar | 50 |  | √ | ' ' | 场景编码 |
| 5 | fscenedesc | 场景描述 | varchar | 255 |  | √ | ' ' | 场景描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_llmprompt_m0 |  | fscenenumber |
| 2 | pk_ai_llmprompt |  | fid |
