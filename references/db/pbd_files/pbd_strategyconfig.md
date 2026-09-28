# 多系统对接策略配置-pbd_strategyconfig

## 多系统对接策略配置-多语言表 t_pbd_strategyconfig_l

- **表名称：** 多系统对接策略配置-多语言表
- **表名：** t_pbd_strategyconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 40 |  | √ | ' ' |  |
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
| 1 | idx_pbd_strategyconfig_l |  | fid,flocaleid |
| 2 | pk_pbd_strategyconfig_l |  | fpkid |

---

## 多系统对接策略配置-主表 t_pbd_strategyconfig

- **表名称：** 多系统对接策略配置-主表
- **表名：** t_pbd_strategyconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | fgroupid | 执行渠道 | varchar | 36 |  | √ | ' ' | [集成渠道 pbd_scdatachannel](../pbd_files/pbd_scdatachannel.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | ffilterjson | 通用过滤json | varchar | 512 |  | √ | ' ' | 通用过滤json |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | ffilterformula_tag | 通用过滤表达式_详情 | text | 0 |  |  | null | 通用过滤表达式_详情 |
| 12 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | fentityid | 数据处理对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | ffilterjson_tag | 通用过滤json_详情 | text | 0 |  |  | null | 通用过滤json_详情 |
| 15 | ffilterformula | 通用过滤表达式 | varchar | 512 |  | √ | ' ' | 通用过滤表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_strategyconfig |  | fid |
| 2 | idx_pbd_strategyconfig_fnumber |  | fnumber |
