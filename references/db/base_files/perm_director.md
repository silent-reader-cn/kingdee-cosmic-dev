# 指定主管-实体-perm_director

## 指定主管-实体-主表 t_perm_director

- **表名称：** 指定主管-实体-主表
- **表名：** t_perm_director

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | foperationruleobjid | 特殊操作权限分配对象 | varchar | 18 |  | √ | ' ' | 特殊操作权限分配对象 perm_operationruleobj |
| 4 | fdirectorid | 主管 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_director_pkey |  | fid |
| 2 | ix_perm_opruleobj_director |  | foperationruleobjid,fdirectorid |
