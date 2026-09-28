# 核算单据同步配置-cal_calbillrule

## 核算单据同步配置-多语言表 t_cal_calbillrule_l

- **表名称：** 核算单据同步配置-多语言表
- **表名：** t_cal_calbillrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrortip | 提示信息 | varchar | 255 |  | √ | ' ' | 提示信息 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_calbillrule_l |  | fid,flocaleid |
| 2 | pk_cal_calbillrule_l |  | fpkid |

---

## 单据体-子表 t_cal_calfieldmap

- **表名称：** 单据体-子表
- **表名：** t_cal_calfieldmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 源单字段标识 | varchar | 50 |  | √ | ' ' | 源单字段标识 |
| 3 | fisorgfield | fisorgfield | bpchar | 1 |  | √ | '0' |  |
| 4 | fsourcefieldname | 源单字段名称 | varchar | 50 |  | √ | ' ' | 源单字段名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fisextendfield | 是否扩展字段 | bpchar | 1 |  | √ | '0' | 是否扩展字段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcalfieldname | 核算单字段名称 | varchar | 50 |  | √ | ' ' | 核算单字段名称 |
| 9 | fcalfield | 核算单字段标识 | varchar | 50 |  | √ | ' ' | 核算单字段标识 |
| 10 | forgtype | forgtype | varchar | 5 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_calfieldmap_pkey |  | fentryid |
| 2 | idx_cal_calfieldmap |  | fid |

---

## 核算单据同步配置-主表 t_cal_calbillrule

- **表名称：** 核算单据同步配置-主表
- **表名：** t_cal_calbillrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ferrortip | 提示信息 | varchar | 255 |  | √ | ' ' | 提示信息 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcalbillid | 核算单 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fbizdirection | fbizdirection | varchar | 5 |  | √ | ' ' |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsourcebillid | 源单 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 13 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | ffilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_calbillrule_pkey |  | fid |
| 2 | idx_cal_calbillrule_calbill |  | fcalbillid |
| 3 | idx_cal_billrule_sourceid |  | fsourcebillid |
