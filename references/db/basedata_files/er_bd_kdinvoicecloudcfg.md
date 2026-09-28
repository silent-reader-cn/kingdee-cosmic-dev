# 发票云配置-er_bd_kdinvoicecloudcfg

## 发票云配置-主表 t_er_kdinvoicecfg

- **表名称：** 发票云配置-主表
- **表名：** t_er_kdinvoicecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnamenotmatch_ci | 发票抬头与企业名称一致： | bpchar | 1 |  | √ | '0' | 发票抬头与企业名称一致：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ffirmname | 企业工商登记名 | varchar | 100 |  | √ | ' ' | 企业工商登记名 |
| 5 | fclientkey | 接入标识 | varchar | 50 |  | √ | ' ' | 接入标识 |
| 6 | finvoicecurrency | 发票币种设置 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fencrypt_key | 加密密钥 | varchar | 50 |  | √ | ' ' | 加密密钥 |
| 8 | freimed_ci | 重复报销： | bpchar | 1 |  | √ | '0' | 重复报销：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 9 | fchecknotpass_ci | 发票真伪： | bpchar | 1 |  | √ | '0' | 发票真伪：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 10 | fidenticalpartyinvcom | 往来单位与开票公司一致 | bpchar | 1 |  | √ | '2' | 往来单位与开票公司一致,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 11 | fclients | 客户端标识 | varchar | 50 |  | √ | ' ' | 客户端标识 |
| 12 | fclient_secret | 授权密钥 | varchar | 50 |  | √ | ' ' | 授权密钥 |
| 13 | fsumexpnull | 费用项目为空的增值税发票汇总报销 | bpchar | 1 |  | √ | '1' | 费用项目为空的增值税发票汇总报销 |
| 14 | ftaxnumnotmatch_ci | 发票税号与企业税号一致： | bpchar | 1 |  | √ | '0' | 发票税号与企业税号一致：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 15 | fnonoffsetcomputoutaount | 抵扣为否，是否计算转出金额 | bpchar | 1 |  | √ | '0' | 抵扣为否，是否计算转出金额,枚举: 1 :是 0 :否 |
| 16 | fignorechar | 忽略特殊符号差异 | varchar | 80 |  | √ | ' ' | 忽略特殊符号差异,枚举: 1 :空格（企业名称首尾空格） 5 :空格（所有空格） 2 :中英文括号 3 :中英文破折号 |
| 17 | fclient_id | 发票云授权标识 | varchar | 50 |  | √ | ' ' | 发票云授权标识 |
| 18 | ftaxlenvalidrang | 校验税号长度 | varchar | 100 |  | √ | ' ' | 校验税号长度 |
| 19 | fenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 20 | ftaxregnum | 企业税号 | varchar | 50 |  | √ | ' ' | 企业税号 |
| 21 | foffsetonlyfrominvoice | 仅按发票判断可抵扣 | bpchar | 1 |  | √ | '0' | 仅按发票判断可抵扣,枚举: 1 :是 0 :否 |
| 22 | fbuyernamele5_ci | 个人发票抬头与企业名称一致： | bpchar | 1 |  | √ | '1' | 个人发票抬头与企业名称一致：,枚举: 0 :严格控制 1 :仅提示 2 :不控制 |
| 23 | fdeductibleoftaxpayer | 按纳税人类型判断可抵扣 | bpchar | 1 |  | √ | '1' | 按纳税人类型判断可抵扣,枚举: 1 :是 0 :否 |
| 24 | fnonoffsetimporttaxamout | 导入不可抵扣发票的税额 | bpchar | 1 |  | √ | '0' | 导入不可抵扣发票的税额,枚举: 1 :是 0 :否 |
| 25 | fcountry | 国家/区域 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

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
