# 进项转出手工登记-til_in_transfer_out_bill

## 单据体-子表 t_til_in_transfer_out_ent

- **表名称：** 单据体-子表
- **表名：** t_til_in_transfer_out_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 进项转出类型 | varchar | 50 |  | √ | ' ' | 进项转出类型,枚举: 2 :免税项目用 3 :集体福利、个人消费 4 :非正常损失 5 :简易计税方法征税项目用 6 :免抵退税办法不得抵扣的进项税额 8 :开具红字专用发票信息表 13 :纳税检查调减进项税额 9 :上期留抵税额抵减欠税 10 :上期留抵税额退税 12 :异常凭证转出进项税额 11 :其他 |
| 3 | fsumincome | 收入总额 | numeric | 23 | 10 | √ | 0.0000000000 | 收入总额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | famount | 进项转出税额 | numeric | 23 | 10 | √ | 0.0000000000 | 进项转出税额 |
| 6 | fprojectamount | 项目收入 | numeric | 23 | 10 | √ | 0.0000000000 | 项目收入 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_til_in_transfer_out_ent |  | fentryid |
| 2 | idx_til_in_transfer_out_ent_fk |  | fid |

---

## 进项转出手工登记-主表 t_til_in_transfer_out

- **表名称：** 进项转出手工登记-主表
- **表名：** t_til_in_transfer_out

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fallocatestate | 分摊状态 | varchar | 50 |  | √ | ' ' | 分摊状态,枚举: 1 :—— 2 :待分摊 3 :已分摊 |
| 4 | ftransferdate | 转出所属税期 | timestamp | 0 |  |  | null | 转出所属税期 |
| 5 | fcheckorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsignamount | 本次登记税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次登记税额 |
| 9 | flook | 明细链接 | varchar | 50 |  | √ | ' ' | 明细链接 |
| 10 | finvoicesigntype | 发票登记来源 | varchar | 50 |  | √ | ' ' | 发票登记来源,枚举: invoicesign :专票、电子通行费登记 einvoicesign :电子普通发票登记 airsign :飞机票登记 trainsign :火车票登记 |
| 11 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 12 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmark | 登记备注 | varchar | 500 |  | √ | ' ' | 登记备注 |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 20 | finvoiceid | 发票id | int8 | 64 |  | √ | 0 | 发票id |
| 21 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :按发票登记 2 :手工登记 3 :数据导入 |
| 22 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | ' ' | 生成凭证 |
| 23 | fsigntype | 登记方式 | varchar | 50 |  | √ | ' ' | 登记方式,枚举: 1 :直接登记转出 2 :无法划分 |
| 24 | fprojecttype | 项目混用情况 | varchar | 50 |  | √ | ' ' | 项目混用情况,枚举: 1 :—— 2 :一般计税和免税项目混用 3 :一般计税和简易计税项目混用 4 :一般计税、免税和简易计税项目混用 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_til_in_transfer_out |  | fid |
| 2 | idx_til_in_transfer_out |  | finvoicecode,finvoiceno |
