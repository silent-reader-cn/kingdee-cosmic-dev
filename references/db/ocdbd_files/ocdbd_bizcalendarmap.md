# 业务日历映射表-ocdbd_bizcalendarmap

## 状态映射分录-子表 t_ocdbd_bizcalstmapentry

- **表名称：** 状态映射分录-子表
- **表名：** t_ocdbd_bizcalstmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcalendarstatusnumber | 日历状态编码 | varchar | 20 |  | √ | ' ' | 日历状态编码 |
| 3 | fshallowcolor | 日历展示颜色(浅) | varchar | 20 |  | √ | ' ' | 日历展示颜色(浅) |
| 4 | fbdcolorid | 日历展示颜色(深) | int8 | 64 |  | √ | 0 | [业务日历颜色 ocdbd_bizcalendarcolor](../ocdbd_files/ocdbd_bizcalendarcolor.md) |
| 5 | fbillstatus | 单据状态 | varchar | 20 |  | √ | ' ' | 单据状态 |
| 6 | fcalendarstatus | 日历状态 | varchar | 20 |  | √ | ' ' | 日历状态 |
| 7 | fbillstatusnumber | 单据状态编码 | varchar | 20 |  | √ | ' ' | 单据状态编码 |
| 8 | fcolor | 日历展示颜色(深) | varchar | 20 |  | √ | ' ' | 日历展示颜色(深) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fbdshallowcolorid | 日历展示颜色(浅) | int8 | 64 |  | √ | 0 | [业务日历颜色 ocdbd_bizcalendarcolor](../ocdbd_files/ocdbd_bizcalendarcolor.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_bizcalstmape_fid |  | fid |
| 2 | pk_ocdbd_bizcalstmapentry |  | fentryid |

---

## 业务日历-多选基础资料表 t_ocdbd_bizcalendarform

- **表名称：** 业务日历-多选基础资料表
- **表名：** t_ocdbd_bizcalendarform

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_bizcalform_fid |  | fid |
| 2 | pk_ocdbd_bizcalendarform |  | fpkid |

---

## 字段映射分录-子表 t_ocdbd_bizcalfldmapentry

- **表名称：** 字段映射分录-子表
- **表名：** t_ocdbd_bizcalfldmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 3 | ffieldqueue | 字段queue | varchar | 1500 |  | √ | ' ' | 字段queue |
| 4 | fdimfieldname | 维度字段 | varchar | 100 |  | √ | ' ' | 维度字段 |
| 5 | fbillfieldnumber | 单据字段标识 | varchar | 100 |  | √ | ' ' | 单据字段标识 |
| 6 | fnecessary | 必要维度字段 | bpchar | 1 |  | √ | '0' | 必要维度字段 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdim | 维度 | varchar | 100 |  | √ | ' ' | 维度,枚举: A :基础信息 B :关键资源 C :预计费用 D :进度状态 E :衡量指标 |
| 9 | fexpressionqueue | 表达式queue | varchar | 1500 |  | √ | ' ' | 表达式queue |
| 10 | fdateformat | 日期格式 | varchar | 100 |  | √ | ' ' | 日期格式,枚举: yyyy-MM-dd :2025-06-15 yyyy年MM月dd日 :2025年06月15日 yyyy-MM-dd HH:mm:ss :2025-06-06 13:14:23 |
| 11 | fdimfieldnumber | 维度字段标识 | varchar | 100 |  | √ | ' ' | 维度字段标识 |
| 12 | fbillfieldname | 单据字段 | varchar | 100 |  | √ | ' ' | 单据字段 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_bizcalfldmape_fid |  | fid |
| 2 | pk_ocdbd_bizcalfldmapentry |  | fentryid |

---

## 业务日历映射表-主表 t_ocdbd_bizcalendarmap

- **表名称：** 业务日历映射表-主表
- **表名：** t_ocdbd_bizcalendarmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbizcalendardimid | 业务日历维度表 | int8 | 64 |  | √ | 0 | [业务日历维度表 ocdbd_bizcalendardim](../ocdbd_files/ocdbd_bizcalendardim.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbillobj | 业务单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 8 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fmobilebillobj | 移动端单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_bizcalmap_number |  | fnumber |
| 2 | pk_ocdbd_bizcalendarmap |  | fid |

---

## 业务日历映射表-多语言表 t_ocdbd_bizcalendarmap_l

- **表名称：** 业务日历映射表-多语言表
- **表名：** t_ocdbd_bizcalendarmap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_bizcalendarmap_l |  | fpkid |
| 2 | idx_ocdbd_bizcalmap_l_flid |  | fid,flocaleid |
