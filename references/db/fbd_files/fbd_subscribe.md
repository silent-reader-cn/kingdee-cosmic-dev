# 订阅方案-fbd_subscribe

## 数据范围-子表 t_fbd_subscribe_orgs

- **表名称：** 数据范围-子表
- **表名：** t_fbd_subscribe_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_subscribe_orgs |  | fentryid |
| 2 | idx_t_fbd_sub_id |  | fid |

---

## 订阅方案-主表 t_fbd_subscribe

- **表名称：** 订阅方案-主表
- **表名：** t_fbd_subscribe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsubfilter | 订阅条件 | varchar | 255 |  | √ | ' ' | 订阅条件 |
| 4 | fsubfilter_tag | 订阅条件_详情 | text | 0 |  |  | null | 订阅条件_详情 |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fdatasourceid | 业务对象 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 7 | fsubscribedate | 订阅生效日期 | timestamp | 0 |  |  | null | 订阅生效日期 |
| 8 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 9 | fmaxsubscribe | 最大订阅次数 | int4 | 32 |  | √ | 0 | 最大订阅次数 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 订阅人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ffixfilter_tag | 固定条件_详情 | text | 0 |  |  | null | 固定条件_详情 |
| 14 | ftplscenid | 消息模板 | int8 | 64 |  | √ | 0 | [消息场景 msg_tplscene](../wftask_files/msg_tplscene.md) |
| 15 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 17 | ffilter | 可变条件 | varchar | 255 |  | √ | ' ' | 可变条件 |
| 18 | fsubscribetplid | 模板编码 | int8 | 64 |  | √ | 0 | [订阅模板 fbd_subscribetpl](../fbd_files/fbd_subscribetpl.md) |
| 19 | fsubscribenum | 已订阅次数 | int4 | 32 |  | √ | 0 | 已订阅次数 |
| 20 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 24 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | ffilter_tag | 可变条件_详情 | text | 0 |  |  | null | 可变条件_详情 |
| 26 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 27 | ffixfilter | 固定条件 | varchar | 255 |  | √ | ' ' | 固定条件 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 订阅方案编码 | varchar | 50 |  | √ | ' ' | 订阅方案编码 |
| 30 | feffectday | 有效天数 | int4 | 32 |  | √ | 0 | 有效天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fbd_subscribe_biz |  | fdatasourceid,fvaliddate |
| 2 | idx_t_fbd_subscribe_number |  | fnumber |
| 3 | pk_t_fbd_subscribe |  | fid |

---

## 行政组织-子表 t_fbd_subscribetpl_orgs

- **表名称：** 行政组织-子表
- **表名：** t_fbd_subscribetpl_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fbd_sub_orgs_org |  | forgid |
| 2 | pk_t_fbd_subscribetpl_orgs |  | fentryid |
| 3 | idx_t_fbd_sub_orgs_fid |  | fid |

---

## 消息接收人-多选基础资料表 t_fbd_subscribe_recusers

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_fbd_subscribe_recusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_subscribe_recusers |  | fpkid |
| 2 | idx_t_fbd_sub_rec_fid |  | fid |
| 3 | idx_t_fbd_sub_rec_dataid |  | fbasedataid |

---

## 订阅方案-多语言表 t_fbd_subscribe_l

- **表名称：** 订阅方案-多语言表
- **表名：** t_fbd_subscribe_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 80 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fbd_subscribe_l_fid |  | fid,flocaleid |
| 2 | pk_t_fbd_subscribe_l |  | fpkid |
