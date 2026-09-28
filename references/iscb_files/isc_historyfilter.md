# 历史数据过滤条件-isc_historyfilter

## 历史数据过滤条件-主表 t_isc_historyfilter

- **表名称：** 历史数据过滤条件-主表
- **表名：** t_isc_historyfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flargetext | 自定义过滤 | text | 0 |  |  | null | 自定义过滤 |
| 3 | flogid | 日志ID | varchar | 100 |  | √ | ' ' | 日志ID |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | ffiltertext | 字段过滤文本 | varchar | 4000 |  | √ | ' ' | 字段过滤文本 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :未执行 B :执行中 C :执行完成 D :执行失败 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | ffinishtime | 时间范围.结束 | timestamp | 0 |  |  | null | 时间范围.结束 |
| 10 | flargetext_tag | 自定义过滤_详情 | text | 0 |  |  | null | 自定义过滤_详情 |
| 11 | fnextentity | 金蝶云实体 | varchar | 100 |  | √ | ' ' | 金蝶云实体 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | ffiltertext_tag | 字段过滤文本_详情 | text | 0 |  |  | null | 字段过滤文本_详情 |
| 15 | forgnumber | 组织编码 | varchar | 100 |  | √ | ' ' | 组织编码 |
| 16 | fintegrateentity | 集成实体 | int8 | 64 |  | √ | 0 | 集成业务对象（废弃） isc_entity |
| 17 | fstarttime | 时间范围.开始 | timestamp | 0 |  |  | null | 时间范围.开始 |
| 18 | fsolution | 接口服务编码 | varchar | 100 |  | √ | ' ' | 接口服务编码 |
| 19 | fisenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 20 | fusedguide | 使用的方案 | int8 | 64 |  | √ | 0 | 集成方案（废弃） isc_guide |
| 21 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fregisterservice | 服务注册 | int8 | 64 |  | √ | 0 | 服务注册（废弃） isc_system |
| 23 | fcheckexcute | 是否执行 | bpchar | 1 |  | √ | '0' | 是否执行 |
| 24 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 25 | fmaxnumber | 单批处理最大条数 | int8 | 64 |  | √ | 20 | 单批处理最大条数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_historyf_fuseguide |  | fusedguide |
| 2 | t_isc_historyfilter_pkey |  | fid |

---

## 历史数据过滤条件-多语言表 t_isc_historyfilter_l

- **表名称：** 历史数据过滤条件-多语言表
- **表名：** t_isc_historyfilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_historyf_fid |  | fid,flocaleid |
| 2 | t_isc_historyfilter_l_pkey |  | fpkid |
