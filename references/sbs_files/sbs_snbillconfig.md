# 序列号单据配置-sbs_snbillconfig

## 序列号单据配置-多语言表 t_sbs_snbillconfig_l

- **表名称：** 序列号单据配置-多语言表
- **表名：** t_sbs_snbillconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 77 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_sncfg_l_flid |  | fid,flocaleid |
| 2 | pk_t_sbs_snbillconfig_l |  | fpkid |

---

## 操作映射-子表 t_sbs_snbillcfgopeentry

- **表名称：** 操作映射-子表
- **表名：** t_sbs_snbillcfgopeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | 单据操作 | varchar | 50 |  | √ | ' ' | 单据操作,枚举: |
| 3 | fsnservices | 序列号服务 | varchar | 50 |  | √ | ' ' | 序列号服务,枚举: 1 :占用 2 :反占用 3 :处理 4 :反处理 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sbs_snbillcfgopeentry |  | fentryid |
| 2 | idx_sbs_sncfgope_id |  | fid |

---

## 序列号单据配置-主表 t_sbs_snbillconfig

- **表名称：** 序列号单据配置-主表
- **表名：** t_sbs_snbillconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialcol | 物料库存信息字段标识 | varchar | 100 |  | √ | ' ' | 物料库存信息字段标识 |
| 3 | fsnsamewithparent | 子分录序列号与分录一致 | bpchar | 1 |  | √ | '0' | 子分录序列号与分录一致 |
| 4 | fistran | 是否调拨 | bpchar | 1 |  | √ | '0' | 是否调拨 |
| 5 | fsnreqbill | 仅占用序列号 | bpchar | 1 |  | √ | '0' | 仅占用序列号 |
| 6 | fbalancetype | 余额表类型 | varchar | 36 |  | √ | ' ' | 余额表 bal_balanceinfo |
| 7 | fsrcbillobj | 来源单据 | varchar | 36 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 8 | fmasterfiletypeid | 类型 | int8 | 64 |  | √ | '1401417099242528768' | 批号/序列号类型 bd_masterfile_type |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fbillfilter | 单据过滤条件 | varchar | 2000 |  | √ | ' ' | 单据过滤条件 |
| 15 | fsnstatus | 允许序列号状态 | varchar | 50 |  | √ | ' ' | 允许序列号状态,枚举: A :待入库 B :在库 C :待出库 D :出库 E :调拨在途 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fsnbaseqtycol | 序列号数量字段标识 | varchar | 100 |  | √ | ' ' | 序列号数量字段标识 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | finvflu | 库存更新方向 | varchar | 50 |  | √ | ' ' | 库存更新方向,枚举: 1 :库存增加 2 :库存减少 3 :库存转移 |
| 20 | fallowsplit | 支持分批更新 | bpchar | 1 |  | √ | '0' | 支持分批更新 |
| 21 | fgensn | 允许生成序列号 | bpchar | 1 |  | √ | '1' | 允许生成序列号 |
| 22 | fsrcbillentry | 来源单据体标识 | varchar | 50 |  | √ | ' ' | 来源单据体标识 |
| 23 | freqrelease | 占用序列号释放 | bpchar | 1 |  | √ | '0' | 占用序列号释放 |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fsrcbillentryname | fsrcbillentryname | varchar | 100 |  | √ | ' ' |  |
| 27 | fallowempty | 序列号允许为空 | bpchar | 1 |  | √ | '0' | 序列号允许为空 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sbs_snbillconfig |  | fid |
| 2 | idx_sbs_sncfg_number |  | fnumber |
| 3 | idx_sbs_sncfg_srcbill |  | fsrcbillobj,fsrcbillentry |

---

## 序列号轨迹字段映射-子表 t_sbs_snbillcfgtrkentry

- **表名称：** 序列号轨迹字段映射-子表
- **表名：** t_sbs_snbillcfgtrkentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsntracksrcbillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 3 | fsntrackcolno | fsntrackcolno | varchar | 100 |  | √ | ' ' |  |
| 4 | fsntrackcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsntracksrcbillcolno | fsntracksrcbillcolno | varchar | 100 |  | √ | ' ' |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsntrackispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_sncfgtrke_id |  | fid |
| 2 | pk_t_sbs_snbillcfgtrkentry |  | fentryid |

---

## 序列号轨迹校验字段映射-子表 t_sbs_snbillcfgtrkventry

- **表名称：** 序列号轨迹校验字段映射-子表
- **表名：** t_sbs_snbillcfgtrkventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsntrkvalcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 3 | fsntrkvalispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fsntrkvalsrcbillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 5 | fsntrkvalcolno | fsntrkvalcolno | varchar | 100 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsntrkvalsrcbillcolno | fsntrkvalsrcbillcolno | varchar | 100 |  | √ | ' ' |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_sncfgtrkve_id |  | fid |
| 2 | pk_t_sbs_snbillcfgtrkventry |  | fentryid |

---

## 序列号主档字段映射-子表 t_sbs_snbillcfgsmfentry

- **表名称：** 序列号主档字段映射-子表
- **表名：** t_sbs_snbillcfgsmfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsnmainfsrcbillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 3 | fsnmainfispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fsnmainfcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsnmainfsrcbillcolno | fsnmainfsrcbillcolno | varchar | 100 |  | √ | ' ' |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsnmainfcolno | fsnmainfcolno | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_sncfgsmfe_id |  | fid |
| 2 | pk_t_sbs_snbillcfgsmfentry |  | fentryid |
