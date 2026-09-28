# 打回原因-ent_reject

## 打回原因-主表 t_mal_prorejectreason

- **表名称：** 打回原因-主表
- **表名：** t_mal_prorejectreason

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigin | 打回方 | bpchar | 1 |  | √ | '0' | 打回方,枚举: 1 :供应商 2 :采购方 |
| 3 | fpriceproid | 协议ID | varchar | 80 |  | √ | ' ' | 协议ID |
| 4 | frejectdate | 打回日期 | timestamp | 0 |  |  | null | 打回日期 |
| 5 | frejectphone | 打回人联系方式 | varchar | 50 |  | √ | ' ' | 打回人联系方式 |
| 6 | frejector | 打回人 | varchar | 80 |  | √ | ' ' | 打回人 |
| 7 | frejectorid | frejectorid | int8 | 64 |  | √ | 0 |  |
| 8 | frejectreason | 打回原因 | varchar | 512 |  | √ | ' ' | 打回原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_prorejectreason |  | fid |
| 2 | idx_mal_prorejectreason_fproid |  | fpriceproid |
