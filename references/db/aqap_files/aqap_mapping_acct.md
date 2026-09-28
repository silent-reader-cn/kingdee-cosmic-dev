# 银行账户映射表-aqap_mapping_acct

## 银行账户映射表-主表 t_aqap_mapping_acct

- **表名称：** 银行账户映射表-主表
- **表名：** t_aqap_mapping_acct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fswiftcode | SwiftCode | varchar | 50 |  |  | ' ' | SwiftCode |
| 3 | fchildacct | 子账户 | varchar | 255 |  |  | ' ' | 子账户 |
| 4 | fcurrency | 币别 | varchar | 50 |  |  | ' ' | 币别 |
| 5 | fparentacct | 父账户 | varchar | 255 |  |  | ' ' | 父账户 |
| 6 | freserve | 备用 | varchar | 512 |  |  | ' ' | 备用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_ma_fparent |  | fparentacct,fcurrency |
| 2 | pk_t_aqap_mapping_acct |  | fid |
