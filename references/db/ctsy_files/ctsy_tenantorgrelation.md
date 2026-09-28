# 组织与租户隶属关系-ctsy_tenantorgrelation

## 组织与租户隶属关系-主表 t_ctsy_tenantorgrelation

- **表名称：** 组织与租户隶属关系-主表
- **表名：** t_ctsy_tenantorgrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | varchar | 30 |  | √ | '0' | 类型,枚举: 0 :行政组织 1 :业务单元 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | forgid | 行政组织/业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftenantid | 租户 | int8 | 64 |  | √ | 0 | [租户配置 ctsy_tenant](../ctsy_files/ctsy_tenant.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctsy_tenantorgrelation |  | fid |
| 2 | idx_ctsy_tenorgrel_typetenorg |  | ftype,ftenantid,forgid |
