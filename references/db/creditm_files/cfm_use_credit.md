# 手工用信登记-cfm_use_credit

## 手工用信登记-主表 t_cfm_use_credit

- **表名称：** 手工用信登记-主表
- **表名：** t_cfm_use_credit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 组id | varchar | 50 |  | √ | ' ' | 组id |
| 3 | fcreditcurrencyid | 授信币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | forgid | 用信组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcurcyamountreleased | 已释放当前业务币别金额 | numeric | 19 | 6 | √ | 0.000000 | 已释放当前业务币别金额 |
| 6 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 7 | ffinorgid | 授信机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 8 | fchangetype | 变动类型 | varchar | 50 |  | √ | ' ' | 变动类型,枚举: A :占用 B :释放 |
| 9 | fcreditprop | fcreditprop | varchar | 50 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbindid | 绑定占用单 | varchar | 50 |  | √ | ' ' | 绑定占用单 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fcredittype | 授信类别 | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 14 | fbusinessamount | 业务金额 | numeric | 19 | 6 | √ | 0.000000 | 业务金额 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 17 | fcreditbusinesstype | 授信业务品种 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 18 | funiquecode | 单据唯一编码 | varchar | 50 |  | √ | ' ' | 单据唯一编码 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | freleaseamount | 释放授信金额 | numeric | 19 | 6 | √ | 0.000000 | 释放授信金额 |
| 21 | fbanktype | 授信机构类别 | varchar | 30 |  | √ | 'bd_finorginfo' | 授信机构类别,枚举: bd_finorginfo :机构授信 bos_org :内部授信 |
| 22 | fremark | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fregistrant | 登记人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fcreditamount | 占用授信金额 | numeric | 19 | 6 | √ | 0.000000 | 占用授信金额 |
| 29 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 30 | fcontractno | 授信合同 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 31 | fbusinesscode | 业务编号 | varchar | 255 |  | √ | ' ' | 业务编号 |
| 32 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 33 | fcreditrate | 折授信币别汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 折授信币别汇率 |
| 34 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 35 | fdiscreditamount | 折授信币别金额 | numeric | 19 | 6 | √ | 0.000000 | 折授信币别金额 |
| 36 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 37 | frootid | 关联占用单主键 | varchar | 50 |  | √ | ' ' | 关联占用单主键 |
| 38 | flockamount | 实际占用额度 | numeric | 19 | 6 | √ | 0.000000 | 实际占用额度 |
| 39 | famountreleased | 已释放额度 | numeric | 19 | 6 | √ | 0.000000 | 已释放额度 |
| 40 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 43 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_use_credit |  | fid |
| 2 | idx_cfm_use_credit_no |  | fbillno |
