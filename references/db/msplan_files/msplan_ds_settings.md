# 同步设置-msplan_ds_settings

## 同步设置-主表 t_msplan_syncsettings

- **表名称：** 同步设置-主表
- **表名：** t_msplan_syncsettings

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffilterval_tag | 过滤器_详情 | text | 0 |  |  | null | 过滤器_详情 |
| 3 | fentitymapping | 实体字段映射 | int8 | 64 |  | √ | 0 | [实体字段映射 mrp_billfieldtransfer](../msplan_files/mrp_billfieldtransfer.md) |
| 4 | fbillstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :提交 C :已审核 D :审核 |
| 5 | fdatasrc | 数据源配置 | int8 | 64 |  | √ | 0 | [数据源配置 mrp_resource_dataconfig](../msplan_files/mrp_resource_dataconfig.md) |
| 6 | fentitytype | 实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsrctype | 字段来源类型设置 | varchar | 50 |  | √ | ' ' | 字段来源类型设置,枚举: A :数据源设置 B :实体字段映射 C :实体 |
| 10 | fmaterialfield | 物料字段 | varchar | 50 |  | √ | ' ' | 物料字段 |
| 11 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fbillstatusfield | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | ffilterval | 过滤器 | varchar | 255 |  | √ | ' ' | 过滤器 |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 16 | fdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fdesc_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_syncsettings |  | fid |
| 2 | idx_msplan_syncsettings |  | fnumber |

---

## 同步设置-多语言表 t_msplan_syncsettings_l

- **表名称：** 同步设置-多语言表
- **表名：** t_msplan_syncsettings_l

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
| 1 | pk_t_msplan_syncsettings_l |  | fpkid |
| 2 | idx_msplan_syncsettings_l |  | fid,flocaleid |

---

## 显示定义-子表 t_msplan_ssentry

- **表名称：** 显示定义-子表
- **表名：** t_msplan_ssentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | ffield | 标识 | varchar | 200 |  | √ | ' ' | 标识 |
| 4 | fisref | 引用 | bpchar | 1 |  | √ | ' ' | 引用 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_ssentry |  | fentryid |
| 2 | idx_msplan_ssentry |  | fid,fseq |
