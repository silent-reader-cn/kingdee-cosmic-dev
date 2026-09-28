# 移动质检显示配置-qcmp_mobconfignew

## 单据详情单据体-子表 t_qcmp_cfgbillentry

- **表名称：** 单据详情单据体-子表
- **表名：** t_qcmp_cfgbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkeybillcol | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 3 | fnamebillcol | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fisbillsys | 是否系统预置字段 | bpchar | 1 |  | √ | '0' | 是否系统预置字段 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fiscollapsiblebillcol | 是否可折叠 | bpchar | 1 |  | √ | '0' | 是否可折叠 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fisotherbillcol | 是否其它单据字段(其它单据字段最后拼接) | bpchar | 1 |  | √ | '0' | 是否其它单据字段(其它单据字段最后拼接) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcmp_cfgbillentry_kb |  | fkeybillcol |
| 2 | pk_t_qcmp_cfgbillentry |  | fentryid |

---

## 移动质检显示配置-主表 t_qcmp_mobcfg

- **表名称：** 移动质检显示配置-主表
- **表名：** t_qcmp_mobcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillobj | 单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 5 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 10 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 11 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 12 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 13 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fbillentry | 单据体标识（这里暂时隐藏，目前限定死为检验单的分录，后续配置界面需要调整） | varchar | 50 |  | √ | ' ' | 单据体标识（这里暂时隐藏，目前限定死为检验单的分录，后续配置界面需要调整） |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | fctrlstrategy | fctrlstrategy | varchar | 5 |  | √ | '5' |  |
| 19 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | fisshowentry | 按分录显示（这里暂时隐藏，目前全是按分录显示） | bpchar | 1 |  | √ | '1' | 按分录显示（这里暂时隐藏，目前全是按分录显示） |
| 21 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 24 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 25 | fisdefault | 默认配置 | bpchar | 1 |  | √ | '0' | 默认配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_qcmp_mobcfg_master |  | fmasterid |
| 2 | idx_t_qcmp_mobcfg_createorg |  | fcreateorgid |
| 3 | idx_qcmp_mobcfg_fnumber |  | fnumber |
| 4 | pk_t_qcmp_mobcfg |  | fid |

---

## 列表配置单据体-子表 t_qcmp_cfglistentry

- **表名称：** 列表配置单据体-子表
- **表名：** t_qcmp_cfglistentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjointfields | 拼接字段 | varchar | 50 |  | √ | ' ' | 拼接字段 |
| 3 | fkeylistcol | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 4 | fisislistsys | 是否系统预置字段 | bpchar | 1 |  | √ | '0' | 是否系统预置字段 |
| 5 | fnamelistcol | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fisissys | fisissys | bpchar | 1 |  | √ | '0' |  |
| 7 | fiscollapsiblelistcol | 是否可折叠 | bpchar | 1 |  | √ | '0' | 是否可折叠 |
| 8 | fisjoint | 是否被拼接字段（被拼接的字段，不需要动态创建控件字段） | bpchar | 1 |  | √ | '0' | 是否被拼接字段（被拼接的字段，不需要动态创建控件字段） |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcmp_listentry_fid |  | fid |
| 2 | pk_t_qcmp_cfglistentry |  | fentryid |

---

## 移动质检显示配置-多语言表 t_qcmp_mobcfg_l

- **表名称：** 移动质检显示配置-多语言表
- **表名：** t_qcmp_mobcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcmp_mobcfg_l |  | fpkid |
| 2 | idx_qcmp_mobcfg_fid |  | fid |
