# 自定义数据来源-sbs_custdatasource

## 自定义数据来源-主表 t_sbs_idxdatasource

- **表名称：** 自定义数据来源-主表
- **表名：** t_sbs_idxdatasource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ffixperiod | 物化频率 | varchar | 50 |  | √ | ' ' | 物化频率,枚举: D :按天 H :按小时 M :按分钟（10分钟） |
| 5 | fcustplugin | 自定义插件 | varchar | 255 |  | √ | ' ' | 自定义插件 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | flastpersisttime | 最新物化时间 | timestamp | 0 |  |  | null | 最新物化时间 |
| 8 | fresultentitykey | 结果对象 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | fsupportfixed | 支持物化 | bpchar | 1 |  | √ | ' ' | 支持物化 |
| 10 | fdatefield | 业务日期维度字段 | varchar | 50 |  | √ | ' ' | 业务日期维度字段 |
| 11 | fgetdatarule | 取数规则 | varchar | 50 |  | √ | ' ' | 取数规则,枚举: fixdata :取物化数据 realdata :取实时数据 fixanddiff :取物化+差额数据 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fappid | fappid | varchar | 50 |  | √ | ' ' |  |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fservicename | fservicename | varchar | 50 |  | √ | ' ' |  |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | flastenddate | 最新物化的截止日期 | timestamp | 0 |  |  | null | 最新物化的截止日期 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | fcloud | fcloud | varchar | 50 |  | √ | ' ' |  |
| 22 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 23 | fdatatype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: plugin :自定义插件 sql :SQL |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sbs_idxdatasource |  | fid |
| 2 | idx_sbs_idxdatasource |  | fnumber |

---

## 自定义数据来源-多语言表 t_sbs_idxdatasource_l

- **表名称：** 自定义数据来源-多语言表
- **表名：** t_sbs_idxdatasource_l

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
| 1 | pk_sbs_idxdatasource_l |  | fpkid |
| 2 | idx_sbs_idxdatasource_l |  | fid |
