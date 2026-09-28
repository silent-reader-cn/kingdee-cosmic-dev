# 委托条件-bos_org_relationcond

## 委托条件-主表 t_org_relationcond

- **表名称：** 委托条件-主表
- **表名：** t_org_relationcond

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fcondition | 委托条件 | varchar | 4000 |  | √ | ' ' | 委托条件 |
| 4 | forgrelationid | 组织协作 | int8 | 64 |  | √ | 0 | [组织协作 bos_org_orgrelation](../base_files/bos_org_orgrelation.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_org_relationcond_pkey |  | fid |
| 2 | idx_t_org_relcondpro_rel |  | forgrelationid |
