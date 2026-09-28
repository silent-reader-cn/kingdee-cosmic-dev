# 汇总申报政策确认-tcvat_hz_policy_confirm

## 汇总申报政策确认-主表 t_tcvat_hz_policy_confirm

- **表名称：** 汇总申报政策确认-主表
- **表名：** t_tcvat_hz_policy_confirm

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
| 9 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 13 | fapplicablediffer | 差额扣除 | bpchar | 1 |  | √ | ' ' | 差额扣除 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fisapplicableplus | 加计抵减进项税 | bpchar | 1 |  | √ | ' ' | 加计抵减进项税 |
| 16 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 17 | fdeductionrate | 加计抵减比例： | varchar | 30 |  | √ | ' ' | 加计抵减比例：,枚举: |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_hz_policy_confirm |  | forgid,fstartdate,fenddate,fstatus |
| 2 | pk_tcvat_hz_policy_confirm |  | fid |

---

## 单据体-子表 t_tcvat_hz_policy_entry

- **表名称：** 单据体-子表
- **表名：** t_tcvat_hz_policy_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frate | 税率/征收率 | int8 | 64 |  | √ | 0 | 税率模板 tpo_tcvat_taxrates |
| 3 | fsuborgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdeclaretype | 申报方式 | varchar | 30 |  | √ | ' ' | 申报方式,枚举: 1 :被汇总 2 :汇总 |
| 7 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 8 | ftaxation | 征税方式 | int8 | 64 |  | √ | 0 | 征收方式模板 tpo_tcvat_taxperiod |
| 9 | frowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fservicedesc | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 12 | fjzjt | 即征即退 | varchar | 30 |  | √ | ' ' | 即征即退,枚举: 0 :否 1 :是 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_policy_entry |  | fentryid |
| 2 | idx_tcvat_hz_policy_entry_fk |  | fid |
