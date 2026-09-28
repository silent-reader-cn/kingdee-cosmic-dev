# 供应商分类标准页签-bd_suppliergroupdetail

## 供应商分类标准页签-主表 t_bd_suppliergroupdetail

- **表名称：** 供应商分类标准页签-主表
- **表名：** t_bd_suppliergroupdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 分类创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fstandardid | 分类标准 | int8 | 64 |  | √ | 0 | 供应商分类标准 bd_suppliergroupstandard |
| 4 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | 供应商分类 bd_suppliergroup |
| 5 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_suppliergroupdetail_pkey |  | fid |
| 2 | idx_suppliergroupdetail_std |  | fstandardid |
| 3 | idx_suppliergroupdetail_group |  | fgroupid,fcreateorgid |
| 4 | idx_suppliergroupdetail_sup |  | fsupplierid |
