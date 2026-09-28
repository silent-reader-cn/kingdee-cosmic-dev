# 业务关联方案-ids_biz_associate_scheme

## 业务关联方案-主表 t_ids_associate_scheme

- **表名称：** 业务关联方案-主表
- **表名：** t_ids_associate_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | freceivenotice | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 4 | fresulttype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: |
| 5 | fresulttypename | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型 |
| 6 | fdescription | 方案说明 | varchar | 255 |  | √ | ' ' | 方案说明 |
| 7 | fappid | 智能应用 | varchar | 50 |  | √ | ' ' | 智能应用,枚举: |
| 8 | fmodeltypename | 预测模型方案 | varchar | 50 |  | √ | ' ' | 预测模型方案 |
| 9 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :未启用 1 :已启用 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | feventnumber | 事件编码 | varchar | 50 |  | √ | ' ' | 事件编码 |
| 14 | fappname | 智能应用 | varchar | 50 |  | √ | ' ' | 智能应用 |
| 15 | fqueue | 队列（Queue） | varchar | 50 |  | √ | ' ' | 队列（Queue） |
| 16 | fregion | 区域（Region） | varchar | 50 |  | √ | ' ' | 区域（Region） |
| 17 | fmodeltypeid | 预测方案 | varchar | 50 |  | √ | ' ' | 预测方案,枚举: |
| 18 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 19 | fbizobj | 业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | ffiltercondition | 过滤条件 | varchar | 512 |  |  | null | 过滤条件 |
| 21 | fcustomparams | 自定义参数 | varchar | 255 |  | √ | ' ' | 自定义参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_scheme_name |  | fname |
| 2 | pk_t_ids_associate_scheme |  | fid |

---

## 单据体-子表 t_ids_field_mapping_entry

- **表名称：** 单据体-子表
- **表名：** t_ids_field_mapping_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frenamefield | 重命名业务对象字段 | varchar | 50 |  | √ | ' ' | 重命名业务对象字段 |
| 3 | fbizobjfield | 业务对象字段 | varchar | 255 |  |  | ' ' | 业务对象字段,枚举: |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fquotefield | 引用数据字段 | varchar | 100 |  | √ | ' ' | 引用数据字段,枚举: |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_fiele_mapping_fid |  | fid |
| 2 | pk_t_ids_field_mapping_entry |  | fentryid |

---

## 业务关联方案-多语言表 t_ids_associate_scheme_l

- **表名称：** 业务关联方案-多语言表
- **表名：** t_ids_associate_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_associate_scheme_l |  | fpkid |
| 2 | idx_ids_scheme_l_fid |  | fid |
