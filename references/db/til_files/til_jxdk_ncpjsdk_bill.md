# 农产品计算抵扣单据-til_jxdk_ncpjsdk_bill

## 农产品计算抵扣单据-主表 t_til_jxdk_ncpjsdk

- **表名称：** 农产品计算抵扣单据-主表
- **表名：** t_til_jxdk_ncpjsdk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | ftaxrate | 扣除率 | varchar | 50 |  | √ | ' ' | 扣除率,枚举: 0.09 :9% 0.10 :10% 0.01 :1% |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdatasources | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 3 :增值税普通发票 4 :小规模纳税人增值税专用发票 xz :手工新增 26 :增值税全电普票 27 :小规模纳税人增值税全电专票 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fissdxz | 是否手工新增 | bpchar | 1 |  | √ | ' ' | 是否手工新增 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fncpmj | 农产品买价 | numeric | 23 | 10 | √ | 0.0000000000 | 农产品买价 |
| 14 | fnumber | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fdktax | 计算抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 计算抵扣税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_til_jxdk_ncpjsdk |  | fbillno |
| 2 | pk_til_jxdk_ncpjsdk |  | fid |

---

## 单据体-子表 t_til_jxdk_ncpjsdk_entry

- **表名称：** 单据体-子表
- **表名：** t_til_jxdk_ncpjsdk_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdataid | 来源数据id | varchar | 50 |  | √ | ' ' | 来源数据id |
| 3 | ffpje | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffpdkse | 发票抵扣税额 | numeric | 23 | 10 | √ | 0 | 发票抵扣税额 |
| 6 | feffectivetaxamount | 合计有效税额 | numeric | 23 | 10 | √ | 0 | 合计有效税额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_til_jxdk_ncpjsdk_entry |  | fentryid |
| 2 | idx_til_jxdk_ncpjsdk_entry_fk |  | fid |
