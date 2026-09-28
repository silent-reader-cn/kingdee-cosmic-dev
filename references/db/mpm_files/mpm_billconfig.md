# 表单配置-mpm_billconfig

## 单据体-子表 t_mpm_billconfigentry

- **表名称：** 单据体-子表
- **表名：** t_mpm_billconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 80 |  |  | ' ' | 字段名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ffieldid | 字段标识 | varchar | 50 |  |  | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_billconfigentry |  | fentryid |
| 2 | idx_mpm_billconfig_id |  | fid |

---

## 表单配置-主表 t_mpm_billconfig

- **表名称：** 表单配置-主表
- **表名：** t_mpm_billconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | freadattachment | 是否读取附件 | bpchar | 1 |  |  | '0' | 是否读取附件 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fschemeid | 方案预览id | int8 | 64 |  | √ | 0 | 方案预览id |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbilldesc | 单据介绍 | varchar | 2000 |  |  | ' ' | 单据介绍 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsourcebillid | 来源单据标识 | varchar | 60 |  |  | ' ' | 来源单据标识 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_billconfig_billno |  | fbillno |
| 2 | pk_t_mpm_billconfig |  | fid |
| 3 | idx_billconfig_sourcebillid |  | fsourcebillid |
| 4 | idx_billconfig_schemeid |  | fschemeid |
