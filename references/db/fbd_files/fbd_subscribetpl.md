# 订阅模板-fbd_subscribetpl

## 订阅模板-主表 t_fbd_subscribetpl

- **表名称：** 订阅模板-主表
- **表名：** t_fbd_subscribetpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 模板名称 | varchar | 80 |  | √ | ' ' | 模板名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 制单组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 7 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdatasourceid | 业务对象 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 10 | ffilter_tag | 可变条件_详情 | text | 0 |  |  | null | 可变条件_详情 |
| 11 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | fmaxsubscribe | 最大订阅次数 | int4 | 32 |  | √ | 0 | 最大订阅次数 |
| 14 | ffixfilter | 固定条件 | varchar | 255 |  | √ | ' ' | 固定条件 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | ffixfilter_tag | 固定条件_详情 | text | 0 |  |  | null | 固定条件_详情 |
| 19 | ftplscenid | 消息模板 | int8 | 64 |  | √ | 0 | 消息场景 msg_tplscene |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | ffilter | 可变条件 | varchar | 255 |  | √ | ' ' | 可变条件 |
| 23 | fnumber | 模板编码 | varchar | 50 |  | √ | ' ' | 模板编码 |
| 24 | feffectday | 有效天数 | int4 | 32 |  | √ | 0 | 有效天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fbd_subscribetpl_number |  | fnumber |
| 2 | pk_t_fbd_subscribetpl |  | fid |
| 3 | idx_t_fbd_subscribetpl_status |  | fstatus,fenable |

---

## 订阅模板-多语言表 t_fbd_subscribetpl_l

- **表名称：** 订阅模板-多语言表
- **表名：** t_fbd_subscribetpl_l

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
| 1 | pk_t_fbd_subscribetpl_l |  | fpkid |
| 2 | idx_t_fbd_subscribetpl_l_fid |  | fid,flocaleid |

---

## 数据范围-子表 t_fbd_subscribetpl_dorgs

- **表名称：** 数据范围-子表
- **表名：** t_fbd_subscribetpl_dorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_subscribetpl_dorgs |  | fentryid |
| 2 | idx_t_fbd_subtpl_orgfid |  | fid |

---

## 行政组织-子表 t_fbd_subscribetpl_orgs

- **表名称：** 行政组织-子表
- **表名：** t_fbd_subscribetpl_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
