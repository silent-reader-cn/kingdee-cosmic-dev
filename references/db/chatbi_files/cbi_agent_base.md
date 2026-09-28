# 智能体-cbi_agent_base

## 智能体-主表 t_cbi_agent_base

- **表名称：** 智能体-主表
- **表名：** t_cbi_agent_base

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: unannounced :待发布 announced :已发布 offline :已下线 temp :草稿 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fdatamodel | 数据模型 | int8 | 64 |  | √ | 0 | [指标模型 cbi_agent_datamodel](../chatbi_files/cbi_agent_datamodel.md) |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 8 | fpicturefield | 头像 | text | 0 |  |  | null | 头像 |
| 9 | finitstatus | 是否初始化 | varchar | 10 |  | √ | '0' | 是否初始化 |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_agent_base |  | fid |
