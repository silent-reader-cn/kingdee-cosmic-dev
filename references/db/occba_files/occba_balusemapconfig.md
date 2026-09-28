# 余额使用映射配置-occba_balusemapconfig

## 余额使用映射配置-多语言表 t_occba_balusemapconfig_l

- **表名称：** 余额使用映射配置-多语言表
- **表名：** t_occba_balusemapconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 250 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_bumcl_flid |  | fid,flocaleid |
| 2 | pk_occba_balusemapconfig_l |  | fpkid |

---

## 字段映射-子表 t_occba_balusemapconfig_e

- **表名称：** 字段映射-子表
- **表名：** t_occba_balusemapconfig_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetobjcol | 目标业务实体标识 | varchar | 100 |  | √ | ' ' | 目标业务实体标识 |
| 3 | fformuladesc | 计算公式 | varchar | 500 |  | √ | ' ' | 计算公式 |
| 4 | fsourcebillcol | 来源单据标识 | varchar | 100 |  | √ | ' ' | 来源单据标识 |
| 5 | fselectvalue | 来源单据取值 | bpchar | 1 |  | √ | '0' | 来源单据取值,枚举: 0 :源单字段 1 :计算公式 2 :按条件取值 |
| 6 | fformula | 计算公式json | varchar | 255 |  | √ | ' ' | 计算公式json |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsourcebillcolno | 来源单据名称 | varchar | 100 |  | √ | ' ' | 来源单据名称 |
| 9 | fformula_tag | 计算公式json_详情 | text | 0 |  |  | null | 计算公式json_详情 |
| 10 | ftargetobjcolno | 目标业务实体字段 | varchar | 100 |  | √ | ' ' | 目标业务实体字段 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_balusemapconfig_e |  | fentryid |
| 2 | idx_occba_bumce_fid |  | fid |

---

## 余额使用映射配置-主表 t_occba_balusemapconfig

- **表名称：** 余额使用映射配置-主表
- **表名：** t_occba_balusemapconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 250 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdescription | 用途描述 | varchar | 500 |  | √ | ' ' | 用途描述 |
| 6 | fispreset | 系统预设 | varchar | 1 |  | √ | '0' | 系统预设 |
| 7 | fbizappid | 所属应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbalmodelid | 余额模型表 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fsourcebillid | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | ftargetobjid | 目标业务实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_bumc_number |  | fnumber |
| 2 | pk_occba_balusemapconfig |  | fid |
