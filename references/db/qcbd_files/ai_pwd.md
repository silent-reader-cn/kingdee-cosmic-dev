# 密钥-ai_pwd

## 密钥-主表 t_ai_pwd

- **表名称：** 密钥-主表
- **表名：** t_ai_pwd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpublickey | 公钥 | varchar | 2048 |  | √ | '' | 公钥 |
| 3 | fqwenapikey | 通义API密钥 | varchar | 2048 |  | √ | '' | 通义API密钥 |
| 4 | ftextinappid | 合合应用ID | varchar | 2048 |  | √ | '' | 合合应用ID |
| 5 | ftextinapikey | 合合API密钥 | varchar | 2048 |  | √ | '' | 合合API密钥 |
| 6 | fnumber | 单据编号 | varchar | 50 |  | √ | '' | 单据编号 |
| 7 | fprivatekey | 密钥 | varchar | 2048 |  | √ | '' | 密钥 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_pwd_fnumber |  | fnumber |
| 2 | pk_t_ai_pwd |  | fid |
