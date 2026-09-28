# 批量抵扣方案-rim_batch_deduct

## 适用组织分录-子表 t_rim_batchdeduct_userorg

- **表名称：** 适用组织分录-子表
- **表名：** t_rim_batchdeduct_userorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxpayer_name | 企业名称 | varchar | 120 |  | √ | ' ' | 企业名称 |
| 3 | fis_all_ele | 是否全电企业 | varchar | 2 |  | √ | ' ' | 是否全电企业,枚举: 0 :否 1 :是 |
| 4 | ftaxpayer_tax_no | 企业税号 | varchar | 32 |  | √ | ' ' | 企业税号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftaxpayer_org | 组织名称 | int8 | 64 |  | √ | 0 | 企业管理 bdm_org |
| 7 | fconfirm_secret | 确认签名密码 | varchar | 32 |  | √ | ' ' | 确认签名密码 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_batchde_userorg_fk |  | fid |
| 2 | idx_rim_batchde_taxno |  | ftaxpayer_tax_no |
| 3 | pk_t_rim_batchdeduct_userorg |  | fentryid |

---

## 批量抵扣方案-主表 t_rim_batch_deduct

- **表名称：** 批量抵扣方案-主表
- **表名：** t_rim_batch_deduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_batch_deduct |  | fid |
| 2 | idx_rim_batchdeduct_org |  | forg |
