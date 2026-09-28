# 管理员组行政组织管辖范围-perm_admingrouporg

## 管理员组行政组织管辖范围-主表 t_perm_admingrouporg

- **表名称：** 管理员组行政组织管辖范围-主表
- **表名：** t_perm_admingrouporg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fusergroupid | 管理员分组 | int8 | 64 |  | √ | 0 | 管理员分组 perm_admingroup |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_admingrouporg |  | fusergroupid,forgid |
| 2 | pk_t_perm_admingrouporg |  | fid |
