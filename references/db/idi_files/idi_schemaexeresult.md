# 方案执行结果-idi_schemaexeresult

## 方案执行结果-主表 t_idi_schemaexeresult

- **表名称：** 方案执行结果-主表
- **表名：** t_idi_schemaexeresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: running :执行中 succeed :执行成功 failed :执行失败 |
| 3 | fpageid | 页面 | varchar | 255 |  | √ | ' ' | 页面 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftraceid | 请求id | varchar | 50 |  | √ | ' ' | 请求id |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbillid | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 9 | fschemaid | 智能洞察方案 | int8 | 64 |  | √ | 0 | [决策方案 idi_schema](../idi_files/idi_schema.md) |
| 10 | fbilltypeid | 单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_idi_schemaexeresult_tid |  | ftraceid |
| 2 | pk_t_idi_schemaexeresult |  | fid |
| 3 | idx_t_idi_schemaexeresult_sgid |  | fschemaid |
| 4 | idx_idi_schemaexeresult |  | fpageid |
