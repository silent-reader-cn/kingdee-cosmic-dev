# 常用指标信息-dfa_custom_metrics

## 指标信息-子表 t_dfa_metricsinfo

- **表名称：** 指标信息-子表
- **表名：** t_dfa_metricsinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmetricscode | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |
| 3 | fmetricsname | 指标名称 | varchar | 50 |  | √ | ' ' | 指标名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmetricsnumber | fmetricsnumber | varchar | 50 |  | √ | ' ' |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_metricsinfo_fk |  | fid |
| 2 | pk_dfa_metricsinfo |  | fentryid |

---

## 常用指标信息-主表 t_dfa_custom_metrics

- **表名称：** 常用指标信息-主表
- **表名：** t_dfa_custom_metrics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fbos_user | fbos_user | int8 | 64 |  | √ | 0 |  |
| 7 | fdatacenter | 租户数据中心 | int8 | 64 |  | √ | 0 | [租户数据中心 dfa_tenant_datacenter](../dfa_files/dfa_tenant_datacenter.md) |
| 8 | fstatus | fstatus | bpchar | 1 |  | √ | 'C' |  |
| 9 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 13 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_custom_metrics |  | fnumber |
| 2 | pk_dfa_custom_metrics |  | fid |
