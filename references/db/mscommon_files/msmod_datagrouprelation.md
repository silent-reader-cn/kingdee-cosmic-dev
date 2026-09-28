# 数据分组关系-msmod_datagrouprelation

## 数据分组关系-多语言表 t_msmod_datagrouprelation_l

- **表名称：** 数据分组关系-多语言表
- **表名：** t_msmod_datagrouprelation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_datagrprelation_l_id |  | fid,flocaleid |
| 2 | pk_t_msmod_datagrouprelation_l |  | fpkid |

---

## 数据分组关系-主表 t_msmod_datagrouprelation

- **表名称：** 数据分组关系-主表
- **表名：** t_msmod_datagrouprelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | flongnumberkey | 长编码字段 | varchar | 50 |  | √ | ' ' | 长编码字段 |
| 4 | fname | 名称 | varchar | 250 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | frelationtype | 关联方式 | varchar | 5 |  | √ | ' ' | 关联方式,枚举: in :字段关联 out :外表关联 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fgroupobjid | 分组对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fstatus | 数据状态 | varchar | 60 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fdataobjid | 数据对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fdatakey | 数据字段 | varchar | 50 |  | √ | ' ' | 数据字段 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fgroupkey | 分组字段 | varchar | 50 |  | √ | ' ' | 分组字段 |
| 15 | fenable | 使用状态 | varchar | 60 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 17 | frelationobjid | 外表对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_datagrouprelation |  | fid |
| 2 | idx_datagrprelation_id |  | fdataobjid,fgroupobjid |
| 3 | idx_datagrprelation_fnumber |  | fnumber |
