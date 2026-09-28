# 收款单操作日志-cas_recoplogbill

## 收款单操作日志-主表 t_cas_recoplogbill

- **表名称：** 收款单操作日志-主表
- **表名：** t_cas_recoplogbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontract | 补充合同号 | varchar | 50 |  | √ | ' ' | 补充合同号 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcorebillseq | 核心单据行号 | varchar | 50 |  | √ | ' ' | 核心单据行号 |
| 5 | foptype | 收款处理 | varchar | 50 |  | √ | ' ' | 收款处理,枚举: |
| 6 | fbizamt | 业务处理金额 | numeric | 23 | 10 | √ | 0.0000000000 | 业务处理金额 |
| 7 | fdiscountamt | 现金折扣 | numeric | 23 | 10 | √ | 0.0000000000 | 现金折扣 |
| 8 | ffee | 手续费 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcorebillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsettledamt | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 13 | fentrydetailinfo | 分录详细 | text | 0 |  |  | null | 分录详细 |
| 14 | fcorebilltype | 核心单据类型 | varchar | 50 |  | √ | ' ' | 核心单据类型,枚举: |
| 15 | frecbillid | 收款单id | int8 | 64 |  | √ | 0 | 收款单id |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | funsettledamt | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 23 | fsettleorg | fsettleorg | int8 | 64 |  | √ | 0 |  |
| 24 | fupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 25 | fentrydetailinfo_tag | 分录详细_详情 | text | 0 |  |  | null | 分录详细_详情 |
| 26 | factrecamt | 实收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实收金额 |
| 27 | fentryid | 分录行id | int8 | 64 |  | √ | 0 | 分录行id |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_recoplogbill_entryid |  | fentryid |
| 2 | idx_cas_recoplogbill_orgid |  | forgid |
| 3 | idx_cas_recoplogbill_recid |  | frecbillid |
| 4 | pk_t_cas_recoplogbill |  | fid |
