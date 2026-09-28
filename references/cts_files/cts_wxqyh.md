# 企业微信号-cts_wxqyh

## 企业微信号-主表 t_bas_wxqyh

- **表名称：** 企业微信号-主表
- **表名：** t_bas_wxqyh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 3 | fagentname | 应用名称 | varchar | 50 |  | √ | ' ' | 应用名称 |
| 4 | fcorpid | 企业ID | varchar | 50 |  | √ | ' ' | 企业ID |
| 5 | fcorpname | 企业名称 | varchar | 50 |  | √ | ' ' | 企业名称 |
| 6 | fcorpsecret | 应用秘钥 | varchar | 100 |  | √ | ' ' | 应用秘钥 |
| 7 | fcustomdata | 自定义数据 | varchar | 1024 |  | √ | ' ' | 自定义数据 |
| 8 | fisscan | 用于扫码登录 | varchar | 1 |  | √ | '0' | 用于扫码登录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_wxqyh_corpid |  | fcorpid |
| 2 | t_bas_wxqyh_pkey |  | fid |
