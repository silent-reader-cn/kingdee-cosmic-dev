# 指标模型-cbi_agent_datamodel

## 指标模型-主表 t_cbi_datamodel

- **表名称：** 指标模型-主表
- **表名：** t_cbi_datamodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: announced :已发布 offline :已下线 unannounced :待发布 temp :草稿 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodeltype | 数据模型类型 | varchar | 20 |  | √ | ' ' | 数据模型类型,枚举: indicator :指标模型 trd_indicator :指标模型-第三方指标 entity :实体模型 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 8 | fpicturefield | 头像 | varchar | 255 |  | √ | ' ' | 头像 |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_datamodel |  | fid |
