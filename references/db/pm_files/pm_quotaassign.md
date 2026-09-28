# 配额分配-pm_quotaassign

## 配额分配-主表 t_pm_quotaassign

- **表名称：** 配额分配-主表
- **表名：** t_pm_quotaassign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fquotaid | 配额方案 | int8 | 64 |  | √ | 0 | [配额方案 pm_quota](../pm_files/pm_quota.md) |
| 5 | fsrctype | 来源类型 | varchar | 5 |  | √ | ' ' | 来源类型,枚举: A :手工新增 B :配额方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_quotaassign_pkey |  | fid |
| 2 | idx_pm_quotaassign_org |  | forgid,fmaterialid |
