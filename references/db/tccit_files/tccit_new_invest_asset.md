# 新增投资资产台账-tccit_new_invest_asset

## 新增投资资产台账-主表 t_tccit_new_invest_asset

- **表名称：** 新增投资资产台账-主表
- **表名：** t_tccit_new_invest_asset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 投资标的名称 | varchar | 50 |  | √ | ' ' | 投资标的名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fljjysf | 累计交易税费 | numeric | 23 | 10 | √ | 0.0000000000 | 累计交易税费 |
| 8 | fljjsjc | 累计计税基础 | numeric | 23 | 10 | √ | 0.0000000000 | 累计计税基础 |
| 9 | finvesttype | 投资性质 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | ftaxpayerid | 被投资企业纳税人识别号 | varchar | 50 |  | √ | ' ' | 被投资企业纳税人识别号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fassettype | 资产类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 15 | fljtzcbrzje | 投资成本入账总额 | numeric | 23 | 10 | √ | 0.0000000000 | 投资成本入账总额 |
| 16 | fdesc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 17 | fbillno | 资产编号 | varchar | 30 |  | √ | ' ' | 资产编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fassetstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: 0 :持有 1 :处置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_new_invest_asset |  | fid |
| 2 | idx_tccit_new_invest_asset |  | fbillno |

---

## 新增明细-子表 t_tccit_new_invest_detail

- **表名称：** 新增明细-子表
- **表名：** t_tccit_new_invest_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 3 | ftzcbrzje | 投资成本入账金额 | numeric | 23 | 10 | √ | 0.0000000000 | 投资成本入账金额 |
| 4 | ftzbl | 投资比例 | numeric | 23 | 10 | √ | 0.0000000000 | 投资比例 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 7 | fsptaxtreetment | 适用特殊性税务处理情况 | varchar | 50 |  | √ | ' ' | 适用特殊性税务处理情况,枚举: 0 :不适用 1 :非货币性资产出资递延纳税 2 :股权收购 3 :资产收购 4 :企业合并 5 :企业分立 6 :债务重组递延纳税 7 :债转股 8 :损益调整 |
| 8 | ftradetaxfee | 交易税费 | numeric | 23 | 10 | √ | 0.0000000000 | 交易税费 |
| 9 | ftaxbase | 计税基础 | numeric | 23 | 10 | √ | 0.0000000000 | 计税基础 |
| 10 | fpriceform | 对价形式 | varchar | 50 |  | √ | ' ' | 对价形式,枚举: 0 :现金对价 1 :非现金对价 2 :现金+非现金对价 |
| 11 | fdate | 取得时间 | timestamp | 0 |  |  | null | 取得时间 |
| 12 | faccountingdoc | 相关会计凭证 | varchar | 50 |  | √ | ' ' | 相关会计凭证 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fquantity | 取得数量(已弃用) | varchar | 50 |  | √ | ' ' | 取得数量(已弃用) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_new_invest_detail_fk |  | fid |
| 2 | pk_tccit_new_invest_detail |  | fentryid |
