# 汇总分支申报政策确认-tcvat_fz_policy_confirm

## 汇总分支申报政策确认-主表 t_tcvat_fz_policy_confirm

- **表名称：** 汇总分支申报政策确认-主表
- **表名：** t_tcvat_fz_policy_confirm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fhzfs | 汇总方式： | varchar | 30 |  | √ | ' ' | 汇总方式：,枚举: 1 :预征方式 2 :分配方式 |
| 8 | fhzqylx | 汇总企业类型： | varchar | 30 |  | √ | ' ' | 汇总企业类型：,枚举: 1 :航空运输企业 2 :铁路运输企业 3 :邮政企业 4 :电信企业 5 :一般企业 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 11 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fapplicablediffer | 差额扣除 | bpchar | 1 |  | √ | ' ' | 差额扣除 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fz_policy_confirm |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_fz_policy_confirm |  | fid |

---

## 单据体-子表 t_tcvat_fz_policy_entry

- **表名称：** 单据体-子表
- **表名：** t_tcvat_fz_policy_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frate | 税率/征收率 | int8 | 64 |  | √ | 0 | 税率模板 tpo_tcvat_taxrates |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fruleid | 规则id | varchar | 50 |  | √ | ' ' | 规则id |
| 6 | ftaxation | 征收方式 | int8 | 64 |  | √ | 0 | 征收方式模板 tpo_tcvat_taxperiod |
| 7 | frowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 8 | fdecaretype | 申报方式 | varchar | 30 |  | √ | ' ' | 申报方式,枚举: 1 :汇总申报 2 :自主申报 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fservicedesc | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 11 | fjzjt | 即征即退 | varchar | 30 |  | √ | ' ' | 即征即退,枚举: 0 :否 1 :是 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fz_policy_entry_fk |  | fid |
| 2 | pk_tcvat_fz_policy_entry |  | fentryid |
