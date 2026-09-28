# 信息确认-tcvvt_policy_confirm

## 信息确认-主表 t_tcvvt_policy_confirm

- **表名称：** 信息确认-主表
- **表名：** t_tcvvt_policy_confirm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhbsyzqybdb | 合并所有者权益变动表 | bpchar | 1 |  | √ | ' ' | 合并所有者权益变动表 |
| 3 | fhbzcfzb | 合并资产负债表 | bpchar | 1 |  | √ | ' ' | 合并资产负债表 |
| 4 | flrb | 利润表 | bpchar | 1 |  | √ | ' ' | 利润表 |
| 5 | forgid | 纳税人名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fhblrb | 合并利润表 | bpchar | 1 |  | √ | ' ' | 合并利润表 |
| 7 | fzcfzb | 资产负债表 | bpchar | 1 |  | √ | ' ' | 资产负债表 |
| 8 | fxjllb | 现金流量表 | bpchar | 1 |  | √ | ' ' | 现金流量表 |
| 9 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :未开始 1 :第一步 2 :第二步 3 :第三步 4 :第四步 5 :第五步 |
| 10 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 11 | fshowmcinfo | 是否显示集团名册 | bpchar | 1 |  | √ | ' ' | 是否显示集团名册 |
| 12 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 13 | fsyzqybdb | 所有者权益变动表 | bpchar | 1 |  | √ | ' ' | 所有者权益变动表 |
| 14 | fhbxjllb | 合并现金流量表 | bpchar | 1 |  | √ | ' ' | 合并现金流量表 |
| 15 | fhbfz | 合并附注 | bpchar | 1 |  | √ | ' ' | 合并附注 |
| 16 | ffz | 附注 | bpchar | 1 |  | √ | ' ' | 附注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_policy_confirm |  | forgid,fenddate,fstartdate |
| 2 | pk_tcvvt_policy_confirm |  | fid |

---

## 树形单据体-子表 t_tcvvt_policy_orgs

- **表名称：** 树形单据体-子表
- **表名：** t_tcvvt_policy_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_policy_orgs |  | fentryid |
| 2 | idx_tcvvt_policy_orgs_fk |  | fid |
