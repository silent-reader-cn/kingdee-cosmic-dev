# 初始化任务项-er_initialconfig

## 初始化任务项-主表 t_er_initialconfig

- **表名称：** 初始化任务项-主表
- **表名：** t_er_initialconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | fisleaf | bpchar | 1 |  | √ | ' ' |  |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 初始化任务项分类维护 er_initialgroup |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fentitymeta | 初始化配置项目 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 6 | fispreset | 是否预设 | bpchar | 1 |  | √ | ' ' | 是否预设 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 12 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 13 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 14 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmustset | 必须配置 | bpchar | 1 |  | √ | ' ' | 必须配置 |
| 17 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | flongnumber | flongnumber | varchar | 255 |  | √ | ' ' |  |
| 20 | fdescription | 初始化要求 | varchar | 500 |  | √ | ' ' | 初始化要求 |
| 21 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 22 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | furl | 帮助链接 | varchar | 500 |  | √ | ' ' | 帮助链接 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_initialconfig |  | fid |
| 2 | idx_initial_config_number |  | fnumber |

---

## 初始化任务项-多语言表 t_er_initialconfig_l

- **表名称：** 初始化任务项-多语言表
- **表名：** t_er_initialconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_initialconfig_l |  | fpkid |
| 2 | idx_initconfigl_flocaleid |  | fid,flocaleid |
