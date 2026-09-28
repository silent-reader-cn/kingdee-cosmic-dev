# 系统内部应用参数(存储数据)-xkrpt_internalparams

## 系统内部应用参数(存储数据)-主表 t_xkrpt_internalparams

- **表名称：** 系统内部应用参数(存储数据)-主表
- **表名：** t_xkrpt_internalparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisolatekey | 隔离字段 | varchar | 50 |  | √ | ' ' | 隔离字段 |
| 4 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fparamvalue | value | varchar | 255 |  | √ | ' ' | value |
| 6 | fparamvalue_tag | value_详情 | text | 0 |  |  | null | value_详情 |
| 7 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fparamkey | key | varchar | 50 |  | √ | ' ' | key |
| 10 | fappid | appid | varchar | 50 |  | √ | ' ' | appid,枚举: xkfsa :财务报表分析 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_internalparams |  | fid |
| 2 | idx_xkrpt_internalparams_key |  | fparamkey |
