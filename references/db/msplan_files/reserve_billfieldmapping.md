# 预留映射配置-reserve_billfieldmapping

## 字段映射-子表 t_reserve_billfieldmap_e

- **表名称：** 字段映射-子表
- **表名：** t_reserve_billfieldmap_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetobjcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 3 | fformuladesc | 计算公式 | varchar | 512 |  | √ | ' ' | 计算公式 |
| 4 | fsourcebillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 5 | fselectvalue | 取值 | bpchar | 1 |  | √ | '0' | 取值,枚举: 0 :源单字段 1 :计算公式 2 :按条件取值 |
| 6 | fformula | 计算公式json | varchar | 255 |  | √ | ' ' | 计算公式json |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fsourcebillcolno | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 9 | fformula_tag | 计算公式json_详情 | text | 0 |  |  | null | 计算公式json_详情 |
| 10 | ftargetobjcolno | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_billfieldmap_eid |  | fid |
| 2 | pk_t_reserve_billfieldmap_e |  | fentryid |

---

## 预留映射配置-多语言表 t_reserve_billfieldmap_l

- **表名称：** 预留映射配置-多语言表
- **表名：** t_reserve_billfieldmap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_billfieldmap_l |  | fpkid |
| 2 | idx_reserve_bfieldmap_lid |  | fid,flocaleid |

---

## 预留映射配置-主表 t_reserve_billfieldmap

- **表名称：** 预留映射配置-主表
- **表名：** t_reserve_billfieldmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fissysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 5 | ftargetobj | 目标业务实体 | varchar | 72 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsourcebill | 来源单据 | varchar | 72 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fbizappid | 所属应用 | varchar | 72 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fisenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fmapuse | 映射用途 | varchar | 5 |  | √ | ' ' | 映射用途,枚举: 0 :通用 1 :预留查询 2 :返还件 |
| 13 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_billfieldmap |  | fid |
| 2 | idx_reserve_billfieldmap_n |  | fnumber |
