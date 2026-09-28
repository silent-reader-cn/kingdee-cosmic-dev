# 财务数据中心-didc_tenant_datacenter

## 财务数据中心-主表 t_didc_tenant_datacenter

- **表名称：** 财务数据中心-主表
- **表名：** t_didc_tenant_datacenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frepo_group_code | 报表分组.编码 | varchar | 255 |  | √ | ' ' | 报表分组.编码 |
| 3 | frepo_group_name | 报表分组.名称 | varchar | 255 |  | √ | ' ' | 报表分组.名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_tenant_datacenter |  | frepo_group_code |
| 2 | pk_didc_tenant_datacenter |  | fid |
