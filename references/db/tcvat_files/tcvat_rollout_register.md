# 进项转出登记单据体-tcvat_rollout_register

## 进项转出登记单据体-主表 t_tcvat_rollout_register

- **表名称：** 进项转出登记单据体-主表
- **表名：** t_tcvat_rollout_register

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrentregistertaxamount | 本次登记税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次登记税额 |
| 3 | fregistercoshareid | 登记关联分摊id | varchar | 100 |  | √ | ' ' | 登记关联分摊id |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fregisteredtaxamount | 已登记税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已登记税额 |
| 6 | frolloutrate | 转出比例 | numeric | 23 | 10 | √ | 0.0000000000 | 转出比例 |
| 7 | feffectivetaxamount | 有效税额 | numeric | 23 | 10 | √ | 0.0000000000 | 有效税额 |
| 8 | fincomesummary | 收入总额 | numeric | 23 | 10 | √ | 0.0000000000 | 收入总额 |
| 9 | frolloutperiod | 转出属期 | timestamp | 0 |  |  | null | 转出属期 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | frollouttaxperiod | 转出所属税期 | varchar | 100 |  | √ | ' ' | 转出所属税期 |
| 13 | fapportionstatus | 分摊状态 | varchar | 30 |  | √ | ' ' | 分摊状态,枚举: 1 :已分摊 2 :未分摊 |
| 14 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 15 | fapportionmodifytime | 分摊修改日期 | timestamp | 0 |  |  | null | 分摊修改日期 |
| 16 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 17 | fsummaryflag | 标志位 | varchar | 30 |  | √ | ' ' | 标志位,枚举: 0 :标志位0 1 :标志位1 |
| 18 | fapportionremark | 分摊备注 | varchar | 250 |  | √ | ' ' | 分摊备注 |
| 19 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 22 | fremark | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fregistercoid | 登记关联id | varchar | 100 |  | √ | ' ' | 登记关联id |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 27 | fregisterstatus | 登记状态 | varchar | 30 |  | √ | ' ' | 登记状态,枚举: 1 :未取消登记 2 :已取消登记 |
| 28 | frollouttype | 进项转出类型 | varchar | 30 |  | √ | ' ' | 进项转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税项目用 5 :开具红字专用发票信息表 6 :其他 7 :免税项目用、简易计税项目用 |
| 29 | fapportionrate | 划分比例 | numeric | 23 | 10 | √ | 0.0000000000 | 划分比例 |
| 30 | fapportiontype | 分摊类型 | varchar | 30 |  | √ | ' ' | 分摊类型,枚举: 1 :分摊计算 2 :取消分摊 |
| 31 | fapportioncreatetime | 分摊创建日期 | timestamp | 0 |  |  | null | 分摊创建日期 |
| 32 | finvoicepkid | 发票主键id | varchar | 100 |  | √ | ' ' | 发票主键id |
| 33 | fapportiontaxamount | 分摊税额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊税额 |
| 34 | fconsumertype | 进项转出用途标识 | varchar | 30 |  | √ | ' ' | 进项转出用途标识,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税项目用 5 :开具红字专用发票信息表 6 :其他 7 :无法划分 : |
| 35 | fprojectincome | 项目收入 | numeric | 23 | 10 | √ | 0.0000000000 | 项目收入 |
| 36 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 4 :增值税专用发票 15 :通行费发票 2 :增值税专用电子发票 |
| 37 | frollouttaxamount | 转出税额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出税额 |
| 38 | finvoiceregistertype | 发票登记类型 | varchar | 30 |  | √ | ' ' | 发票登记类型,枚举: 1 :全部登记 2 :部分登记 3 :未登记 |
| 39 | fregistertype | 登记类型 | varchar | 30 |  | √ | ' ' | 登记类型,枚举: 1 :转出登记 2 :取消登记 |
| 40 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | ' ' | 生成凭证 |
| 41 | fregisterrule | 登记规则 | varchar | 30 |  | √ | ' ' | 登记规则,枚举: 1 :全部登记 2 :按比例登记 3 :录入税额登记 |
| 42 | favaliabletaxamount | 可登记税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可登记税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_rollout_register_pkey |  | fid |
| 2 | idx_tcvat_rollout_register |  | forgid,ftaxperiod |
