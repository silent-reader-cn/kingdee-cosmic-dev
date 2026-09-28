# 项目保证金-pac_projectsuretybill

## 项目保证金-主表 t_pac_prosuretybill

- **表名称：** 项目保证金-主表
- **表名：** t_pac_prosuretybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fprojectld | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | famount | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 5 | freceivedamt | 已收款金额 | numeric | 23 | 10 | √ | 0 | 已收款金额 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fenddate | 保证结束日期 | timestamp | 0 |  |  | null | 保证结束日期 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: |
| 13 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcontactunittype | 往来单位类型 | varchar | 50 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | fsourcebillnumber | 源单编码 | varchar | 50 |  | √ | ' ' | 源单编码 |
| 18 | fstartdate | 保证开始日期 | timestamp | 0 |  |  | null | 保证开始日期 |
| 19 | fdeductedamt | 已扣款金额 | numeric | 23 | 10 | √ | 0 | 已扣款金额 |
| 20 | fbalance | 保证金余额 | numeric | 23 | 10 | √ | 0 | 保证金余额 |
| 21 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 22 | fcontactunit | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 23 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 24 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: 0 :质保金 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pac_prosuretybill |  | fbillno |
| 2 | pk_pac_prosuretybill |  | fid |

---

## 项目保证金-反写记录表 t_pac_prosuretybill_wb

- **表名称：** 项目保证金-反写记录表
- **表名：** t_pac_prosuretybill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pac_prosuretybill_wb_fid |  | fid |
| 2 | pk_pac_prosuretybill_wb |  | fentryid |

---

## 关联子实体-子表 t_pac_prosuretybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pac_prosuretybill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pac_prosuretybill_lk_fid |  | fid |
| 2 | pk_pac_prosuretybill_lk |  | fpkid |

---

## 项目保证金-关联追踪表 t_pac_prosuretybill_tc

- **表名称：** 项目保证金-关联追踪表
- **表名：** t_pac_prosuretybill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pac_prosuretybill_tc_ftb |  | ftbillid |
| 2 | idx_pac_prosuretybill_tc_tid |  | ftid |
| 3 | idx_pac_prosuretybill_tc_tbill |  | ftbillid |
| 4 | pk_pac_prosuretybill_tc |  | fid |

---

## 扣款信息-子表 t_pac_suretybill_entry

- **表名称：** 扣款信息-子表
- **表名：** t_pac_suretybill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeductdate | 扣款日期 | timestamp | 0 |  |  | null | 扣款日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdeductreason | 扣款事由 | varchar | 500 |  | √ | ' ' | 扣款事由 |
| 5 | fdeductamt | 扣款金额 | numeric | 23 | 10 | √ | 0 | 扣款金额 |
| 6 | fdeductbillid | 扣款单编号 | int8 | 64 |  | √ | 0 | 项目保证金扣款单 pac_projectdeductbill |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pac_suretybill_entry |  | fentryid |
| 2 | idx_pac_suretybill_entry |  | fid |
