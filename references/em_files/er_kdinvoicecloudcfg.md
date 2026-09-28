# 发票云配置-er_kdinvoicecloudcfg

## 发票云配置-主表 t_er_kdinvoicecfg

- **表名称：** 发票云配置-主表
- **表名：** t_er_kdinvoicecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclients | fclients | varchar | 50 |  | √ | ' ' |  |
| 3 | fclient_secret | client_secret | varchar | 50 |  | √ | ' ' | client_secret |
| 4 | fnamenotmatch_ci | 发票抬头与企业名称不一致 | bpchar | 1 |  | √ | '0' | 发票抬头与企业名称不一致 |
| 5 | fsumexpnull | 费用项目为空的增值税发票汇总报销 | bpchar | 1 |  | √ | '1' | 费用项目为空的增值税发票汇总报销 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftaxnumnotmatch_ci | 发票上购方税号与企业税号不一致 | bpchar | 1 |  | √ | '0' | 发票上购方税号与企业税号不一致 |
| 8 | ffirmname | 企业工商登记名 | varchar | 100 |  | √ | ' ' | 企业工商登记名 |
| 9 | fclientkey | fclientkey | varchar | 50 |  | √ | ' ' |  |
| 10 | fnonoffsetcomputoutaount | fnonoffsetcomputoutaount | bpchar | 1 |  | √ | '0' |  |
| 11 | fclient_id | client_id | varchar | 50 |  | √ | ' ' | client_id |
| 12 | fencrypt_key | encrypt_key | varchar | 50 |  | √ | ' ' | encrypt_key |
| 13 | freimed_ci | 已报销 | bpchar | 1 |  | √ | '0' | 已报销 |
| 14 | fenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 15 | fchecknotpass_ci | 发票查验不通过 | bpchar | 1 |  | √ | '0' | 发票查验不通过 |
| 16 | ftaxregnum | 企业税号 | varchar | 50 |  | √ | ' ' | 企业税号 |
| 17 | foffsetonlyfrominvoice | foffsetonlyfrominvoice | bpchar | 1 |  | √ | '0' |  |
| 18 | fbuyernamele5_ci | 个人发票 | bpchar | 1 |  | √ | '1' | 个人发票 |
| 19 | fdeductibleoftaxpayer | fdeductibleoftaxpayer | bpchar | 1 |  | √ | '1' |  |
| 20 | fnonoffsetimporttaxamout | fnonoffsetimporttaxamout | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_kdinvoicecfg_pkey |  | fid |
| 2 | idx_bd_er_invoicecfg_ftax |  | fenable,ftaxregnum |
| 3 | idx_bd_er_invoicecfg_forg |  | forgid |
