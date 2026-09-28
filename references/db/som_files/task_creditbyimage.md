# 影像超期降级设置-task_creditbyimage

## 单据体-子表 t_tk_creditbyimageentry

- **表名称：** 单据体-子表
- **表名：** t_tk_creditbyimageentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fminlevellimit | 最低级数限制 | int8 | 64 |  | √ | 0 | [信用等级 task_creditlevel](../fircm_files/task_creditlevel.md) |
| 3 | freducelevnum | 降级数 | int8 | 64 |  | √ | 0 | 降级数 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | foutdatenum | 影像未上传天数 | int8 | 64 |  | √ | 0 | 影像未上传天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_crebyimgentry_fid |  | fid |
| 2 | t_tk_creditbyimageentry_pkey |  | fentryid |

---

## 影像超期降级设置-主表 t_tk_creditbyimage

- **表名称：** 影像超期降级设置-主表
- **表名：** t_tk_creditbyimage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 13 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fsubscore | fsubscore | numeric | 19 | 6 | √ | 0.000000 |  |
| 16 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 17 | foutdatenum | foutdatenum | int8 | 64 |  | √ | 0 |  |
| 18 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_creditbyimage_pkey |  | fid |
| 2 | index_ssc_creditbyimage_num |  | fnumber |
| 3 | idx_t_tk_creditbyimage_master |  | fmasterid |
| 4 | idx_t_tk_creditbyimage_createorg |  | fcreateorgid |

---

## 影像超期降级设置-多语言表 t_tk_creditbyimage_l

- **表名称：** 影像超期降级设置-多语言表
- **表名：** t_tk_creditbyimage_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_creditbyimage_l_pkey |  | fpkid |
| 2 | index_ssc_creditbyimage_l_fid |  | fid,flocaleid |
