# 表单关联规则单据头F7-formlinkrule_headerf7

## 表单关联规则单据头F7-主表 t_mpm_formlinkrule

- **表名称：** 表单关联规则单据头F7-主表
- **表名：** t_mpm_formlinkrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :启用 1 :未启用 2 :禁用 |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 7 | frulename | 规则名称 | varchar | 80 |  | √ | ' ' | 规则名称 |
| 8 | fbillno | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |
| 9 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fruledesc | fruledesc | varchar | 2000 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_formlinkrule_billno |  | fbillno |
| 2 | pk_t_mpm_formlinkrule |  | fid |
