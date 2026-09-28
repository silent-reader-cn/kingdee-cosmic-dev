# 发票云配置-er_bd_kdinvoicecloudcfg

## 发票云配置-主表 t_er_kdinvoicecfg

- **表名称：** 发票云配置-主表
- **表名：** t_er_kdinvoicecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclients | 客户端标识 | varchar | 50 |  | √ | ' ' | 客户端标识 |
| 3 | fclient_secret | 授权密钥 | varchar | 50 |  | √ | ' ' | 授权密钥 |
| 4 | fnamenotmatch_ci | 发票抬头与企业名称不一致 | bpchar | 1 |  | √ | '0' | 发票抬头与企业名称不一致 |
| 5 | fsumexpnull | 费用项目为空的增值税发票汇总报销 | bpchar | 1 |  | √ | '1' | 费用项目为空的增值税发票汇总报销 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftaxnumnotmatch_ci | 发票上购方税号与企业税号不一致 | bpchar | 1 |  | √ | '0' | 发票上购方税号与企业税号不一致 |
| 8 | ffirmname | 企业工商登记名 | varchar | 100 |  | √ | ' ' | 企业工商登记名 |
| 9 | fclientkey | 接入标识 | varchar | 50 |  | √ | ' ' | 接入标识 |
| 10 | fnonoffsetcomputoutaount | 抵扣为否，是否计算转出金额 | bpchar | 1 |  | √ | '0' | 抵扣为否，是否计算转出金额,枚举: 1 :是 0 :否 |
| 11 | fclient_id | 发票云授权标识 | varchar | 50 |  | √ | ' ' | 发票云授权标识 |
| 12 | fencrypt_key | 加密密钥 | varchar | 50 |  | √ | ' ' | 加密密钥 |
| 13 | freimed_ci | 已报销 | bpchar | 1 |  | √ | '0' | 已报销 |
| 14 | fenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 15 | fchecknotpass_ci | 发票查验不通过 | bpchar | 1 |  | √ | '0' | 发票查验不通过 |
| 16 | ftaxregnum | 企业税号 | varchar | 50 |  | √ | ' ' | 企业税号 |
| 17 | foffsetonlyfrominvoice | 仅按发票判断是否抵扣 | bpchar | 1 |  | √ | '0' | 仅按发票判断是否抵扣,枚举: 1 :是 0 :否 |
| 18 | fbuyernamele5_ci | 个人发票 | bpchar | 1 |  | √ | '1' | 个人发票 |
| 19 | fdeductibleoftaxpayer | 按纳税人类型判断是否抵扣 | bpchar | 1 |  | √ | '1' | 按纳税人类型判断是否抵扣,枚举: 1 :是 0 :否 |
| 20 | fnonoffsetimporttaxamout | 导入不可抵扣发票的税额 | bpchar | 1 |  | √ | '0' | 导入不可抵扣发票的税额,枚举: 1 :是 0 :否 |

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
