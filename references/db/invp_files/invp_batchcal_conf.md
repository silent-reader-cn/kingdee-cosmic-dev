# 因子分批计算参数-invp_batchcal_conf

## 因子分批计算参数-主表 t_invp_batchcalconf

- **表名称：** 因子分批计算参数-主表
- **表名：** t_invp_batchcalconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fcalentityid | 计算方案实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fenablelog | 是否记录分批日志 | bpchar | 1 |  | √ | '0' | 是否记录分批日志 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fbatchsize | 每批数据量 | int8 | 64 |  | √ | 0 | 每批数据量 |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_batchcalconf |  | fid |
| 2 | idx_t_invp_batchcalconf_num |  | fnumber |
