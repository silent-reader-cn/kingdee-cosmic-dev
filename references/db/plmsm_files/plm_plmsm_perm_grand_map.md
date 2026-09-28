# 列表权限域映射表-plm_plmsm_perm_grand_map

## 列表权限域映射表-主表 t_plmsm_perm_grand_map

- **表名称：** 列表权限域映射表-主表
- **表名：** t_plmsm_perm_grand_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetdomainid | 参考目标域标识 | int8 | 64 |  | √ | 0 | 参考目标域标识 |
| 3 | fsourcedomainid | 源域标识 | int8 | 64 |  | √ | 0 | 源域标识 |
| 4 | fcontainerid | 域所属容器 | int8 | 64 |  | √ | 0 | 域所属容器 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_perm_grand_map |  | fid |
