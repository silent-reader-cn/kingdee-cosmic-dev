# 政府补助递延收益台账-tccit_gov_subsidy_defer

## 结转损益登记台账-子表 t_tccit_carry_fwd_loss

- **表名称：** 结转损益登记台账-子表
- **表名：** t_tccit_carry_fwd_loss

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbookeddate | 入账日期 | timestamp | 0 |  |  | null | 入账日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | faccountingdoc | 相关会计凭证 | varchar | 50 |  | √ | ' ' | 相关会计凭证 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_carry_fwd_loss |  | fentryid |
| 2 | idx_tccit_carry_fwd_loss_fk |  | fid |

---

## 政府补助递延收益台账-主表 t_tccit_gov_subsidy_defer

- **表名称：** 政府补助递延收益台账-主表
- **表名：** t_tccit_gov_subsidy_defer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 补助项目名称 | varchar | 50 |  | √ | ' ' | 补助项目名称 |
| 4 | fljjzsyamount | 累计结转损益金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计结转损益金额 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 0 :禁用 1 :可用 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | faccountingmethod | 核算方法 | varchar | 50 |  | √ | ' ' | 核算方法,枚举: 1 :总额法 2 :净额法 |
| 8 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcontractstart | 合同期间.开始 | timestamp | 0 |  |  | null | 合同期间.开始 |
| 10 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fsywjzamount | 剩余未结转金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余未结转金额 |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fgovdepartment | 发放补助政府主管部门 | varchar | 50 |  | √ | ' ' | 发放补助政府主管部门 |
| 15 | frelateassetcode | 关联资产编码 | varchar | 50 |  | √ | ' ' | 关联资产编码 |
| 16 | ftotalamt | 合同总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合同总金额 |
| 17 | fljsdbzamount | 累计收到补助金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计收到补助金额 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcontractend | 合同期间.结束 | timestamp | 0 |  |  | null | 合同期间.结束 |
| 20 | fbillno | 项目编号 | varchar | 30 |  | √ | ' ' | 项目编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fsubsidytype | 补助类型 | varchar | 50 |  | √ | ' ' | 补助类型,枚举: 1 :资产相关 2 :收益相关 3 :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_gov_subsidy_defer |  | fbillno,forgid |
| 2 | pk_tccit_gov_subsidy_defer |  | fid |

---

## 收到补助登记台账-子表 t_tccit_rec_subsidy

- **表名称：** 收到补助登记台账-子表
- **表名：** t_tccit_rec_subsidy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbookeddate | 入账日期 | timestamp | 0 |  |  | null | 入账日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | facountingdoc | 相关会计凭证 | varchar | 50 |  | √ | ' ' | 相关会计凭证 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_rec_subsidy_fk |  | fid |
| 2 | pk_tccit_rec_subsidy |  | fentryid |
