# 齐套分析方案-mpdm_kitting_analysis

## 生产组织-多选基础资料表 t_mpdm_kittingorgs

- **表名称：** 生产组织-多选基础资料表
- **表名：** t_mpdm_kittingorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_kittingorgs |  | fpkid |
| 2 | idx_mpdm_kittingorgs_id |  | fid |

---

## 齐套分析方案-多语言表 t_mpdm_kittinganalysis_l

- **表名称：** 齐套分析方案-多语言表
- **表名：** t_mpdm_kittinganalysis_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 87 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_kittinganalysis_l |  | fpkid |
| 2 | idx_mpdm_kittinganalysis_l |  | fid,flocaleid |

---

## 齐套分析方案-主表 t_mpdm_kittinganalysis

- **表名称：** 齐套分析方案-主表
- **表名：** t_mpdm_kittinganalysis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fisconsidercrossproject | 考虑跨项目物料供应 | varchar | 5 |  | √ | '0' | 考虑跨项目物料供应 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisconsiderwarehouse | 仅考虑用料清单指定发料仓库 | varchar | 5 |  | √ | '1' | 仅考虑用料清单指定发料仓库 |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fispreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 11 | fmaterialreplace | 物料替代 | varchar | 5 |  | √ | ' ' | 物料替代,枚举: A :考虑替代 B :忽略替代 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | freservemark | 考虑预留 | varchar | 5 |  | √ | 'A' | 考虑预留,枚举: A :考虑弱预留 B :忽略弱预留 |
| 15 | fanalysistype | 分析方式 | varchar | 5 |  | √ | ' ' | 分析方式,枚举: A :齐套分析 B :齐套分析+创建强预留 C :齐套分析+创建弱预留 |
| 16 | fisconsideroutwarehouse | 仅考虑用料清单指定调出仓库 | varchar | 5 |  | √ | '1' | 仅考虑用料清单指定调出仓库 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fmaterialrange | 物料范围 | varchar | 5 |  | √ | ' ' | 物料范围,枚举: A :全部物料 B :非倒冲物料 C :关键物料 |
| 20 | forderstatus | 工单单据状态 | varchar | 30 |  | √ | ' ' | 工单单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fpreferred | 优先顺序 | varchar | 5 |  | √ | ' ' | 优先顺序,枚举: A :计划开工时间 B :计划完工时间 |
| 23 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_kittinganalysis |  | fnumber |
| 2 | pk_mpdm_kittinganalysis |  | fid |

---

## 供应参数-子表 t_mpdm_kittingsupplyparam

- **表名称：** 供应参数-子表
- **表名：** t_mpdm_kittingsupplyparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyid | 供应资源 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 3 | fallowearldays | 允许提前期间（天） | int4 | 32 |  | √ | 0 | 允许提前期间（天） |
| 4 | fisexclude | 排除 | bpchar | 1 |  | √ | '0' | 排除 |
| 5 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 9 | fsupplyenddays | 供应截止天数 | int4 | 32 |  | √ | 0 | 供应截止天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kittingsupplyparam |  | fentryid |
| 2 | idx_kittingsupplyparam |  | fid |

---

## 库存参数-子表 t_mpdm_kittinginvparam

- **表名称：** 库存参数-子表
- **表名：** t_mpdm_kittinginvparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fwarehouseid | 仓库编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kittinginvparam |  | fid |
| 2 | pk_kittinginvparam |  | fentryid |
