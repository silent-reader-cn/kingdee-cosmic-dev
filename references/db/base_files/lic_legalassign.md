# 组织机构许可分配-lic_legalassign

## 组织机构许可分配-主表 t_lic_legalassign

- **表名称：** 组织机构许可分配-主表
- **表名：** t_lic_legalassign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 许可分组 | int8 | 64 |  | √ | 0 | 许可分组 lic_group |
| 3 | forgid | 组织机构 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fassignednum | 分配数量 | int4 | 32 |  | √ | 0 | 分配数量 |
| 5 | fusednum | 使用数量 | int4 | 32 |  | √ | 0 | 使用数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lic_legalassign_group |  | fgroupid |
| 2 | pk_t_lic_legalassign |  | fid |
