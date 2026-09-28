# 飞书-cts_fly_book

## 飞书-主表 t_bas_fly_book

- **表名称：** 飞书-主表
- **表名：** t_bas_fly_book

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhost | fhost | varchar | 128 |  | √ | ' ' |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fwebformid | fwebformid | varchar | 36 |  | √ | ' ' |  |
| 5 | fappsecret | 应用秘钥 | varchar | 50 |  | √ | ' ' | 应用秘钥 |
| 6 | fmobileformid | fmobileformid | varchar | 36 |  | √ | ' ' |  |
| 7 | fcreatetime | fcreatetime | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 8 | fweburl | fweburl | varchar | 600 |  | √ | ' ' |  |
| 9 | fconnstatus | fconnstatus | bpchar | 1 |  | √ | '0' |  |
| 10 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fappname | 应用名称 | varchar | 50 |  | √ | ' ' | 应用名称 |
| 14 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 15 | fmobileurl | fmobileurl | varchar | 600 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_fly_book |  | fid |
| 2 | index_t_bas_fly_book |  | fappid |
