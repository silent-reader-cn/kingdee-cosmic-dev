# 客户分类标准页签-bd_customergroupdetail

## 客户分类标准页签-主表 t_bd_customergroupdetail

- **表名称：** 客户分类标准页签-主表
- **表名：** t_bd_customergroupdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 分类创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fstandardid | 分类标准 | int8 | 64 |  | √ | 0 | [客户分类标准 bd_customergroupstandard](../basedata_files/bd_customergroupstandard.md) |
| 4 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [客户分类 bd_customergroup](../basedata_files/bd_customergroup.md) |
| 5 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_customergroupdetail_pkey |  | fid |
| 2 | idx_customergroupdetail_std |  | fstandardid |
| 3 | idx_customergroupdetail_group |  | fgroupid,fcreateorgid |
| 4 | idx_customergroupdetail_cus |  | fcustomerid |
