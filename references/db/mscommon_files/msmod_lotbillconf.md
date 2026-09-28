# 批号单据配置-msmod_lotbillconf

## 批号主档返回单据字段映射-子表 t_msmod_lotcfgretentry

- **表名称：** 批号主档返回单据字段映射-子表
- **表名：** t_msmod_lotcfgretentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flotmfreturnsrcbillcolno | flotmfreturnsrcbillcolno | varchar | 100 |  | √ | ' ' |  |
| 3 | freturnbill | 返回单据 | bpchar | 1 |  | √ | '0' | 返回单据 |
| 4 | flotmfreturncolno | flotmfreturncolno | varchar | 100 |  | √ | ' ' |  |
| 5 | fselectcondition | 查询条件 | bpchar | 1 |  | √ | '0' | 查询条件 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | flotmfreturnsrcbillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 8 | flotmfreturnispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | flotmfreturncol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_lotcfgretentry |  | fentryid |
| 2 | idx_msmod_lotcfgre_id |  | fid |

---

## 批号单据配置-主表 t_msmod_lotbillconf

- **表名称：** 批号单据配置-主表
- **表名：** t_msmod_lotbillconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | flotnumberfield | 单据批号字段 | varchar | 100 |  | √ | ' ' | 单据批号字段 |
| 5 | flotidfield | 单据批号主档字段 | varchar | 100 |  | √ | ' ' | 单据批号主档字段 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fgenlot | 允许生成批号主档 | bpchar | 1 |  | √ | '1' | 允许生成批号主档 |
| 8 | fdescription | fdescription | varchar | 50 |  | √ | ' ' |  |
| 9 | fsrcbillobj | 单据 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 10 | fmasterfiletypeid | 类型 | int8 | 64 |  | √ | '1401417099242528768' | [批号/序列号类型 bd_masterfile_type](../sbd_files/bd_masterfile_type.md) |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fsrcbillentry | 单据体标识 | varchar | 50 |  | √ | ' ' | 单据体标识 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | flotid | 批号主档标识 | varchar | 100 |  | √ | ' ' | 批号主档标识 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fbillfilter | 单据过滤条件 | varchar | 2000 |  | √ | ' ' | 单据过滤条件 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fmovedirection | 移动方向 | bpchar | 1 |  | √ | 'A' | 移动方向,枚举: A :来源 B :去向 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fsrcbillentryname | fsrcbillentryname | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_lotcfg_srcbill |  | fsrcbillobj,fsrcbillentry |
| 2 | idx_msmod_lotcfg_number |  | fnumber |
| 3 | pk_t_msmod_lotbillconf |  | fid |

---

## 主档字段映射-子表 t_msmod_lotbillcfgmfentry

- **表名称：** 主档字段映射-子表
- **表名：** t_msmod_lotbillcfgmfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmainfcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 3 | fmainfispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fmainfsrcbillcolno | fmainfsrcbillcolno | varchar | 100 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmainfsrcbillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 7 | fmainfcolno | fmainfcolno | varchar | 100 |  | √ | ' ' |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_lotcfgmfe_id |  | fid |
| 2 | pk_t_msmod_lotbillcfgmfentry |  | fentryid |

---

## 轨迹字段映射-子表 t_msmod_lotcfgtrkentry

- **表名称：** 轨迹字段映射-子表
- **表名：** t_msmod_lotcfgtrkentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftrackispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 3 | ftrackcolno | ftrackcolno | varchar | 100 |  | √ | ' ' |  |
| 4 | ftrackcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 5 | ftracksrcbillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftracksrcbillcolno | ftracksrcbillcolno | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_lotcfgtrke_id |  | fid |
| 2 | pk_t_msmod_lotcfgtrkentry |  | fentryid |

---

## 批号单据配置-多语言表 t_msmod_lotbillconf_l

- **表名称：** 批号单据配置-多语言表
- **表名：** t_msmod_lotbillconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_lotbillconf_l |  | fpkid |
| 2 | idx_msmod_lotcfg_l_flid |  | fid,flocaleid |
