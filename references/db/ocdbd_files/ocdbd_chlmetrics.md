# 渠道指标-ocdbd_chlmetrics

## 渠道指标-多语言表 t_ocdbd_chlmetrics_l

- **表名称：** 渠道指标-多语言表
- **表名：** t_ocdbd_chlmetrics_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_chlmetrics_l |  | fpkid |
| 2 | idx_ocdbd_chlmetrics_l |  | fid,flocaleid |

---

## 单据设置-子表 t_ocdbd_chlmetrics_entry

- **表名称：** 单据设置-子表
- **表名：** t_ocdbd_chlmetrics_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcountcol | 统计字段标识 | varchar | 100 |  | √ | ' ' | 统计字段标识 |
| 3 | fbillformid | 单据编码 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | ffilterscheme | 自定义过滤字段 | varchar | 2000 |  | √ | ' ' | 自定义过滤字段 |
| 5 | ffullcountcol | 统计字段全标识 | varchar | 100 |  | √ | ' ' | 统计字段全标识 |
| 6 | ffullchannelcol | 统计渠道字段全标识 | varchar | 100 |  | √ | ' ' | 统计渠道字段全标识 |
| 7 | fformula | 统计方式 | bpchar | 1 |  | √ | 'A' | 统计方式,枚举: 0 :累加 1 :扣减 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fchannelcol | 统计渠道字段标识 | varchar | 100 |  | √ | ' ' | 统计渠道字段标识 |
| 10 | fcountcol_name | 统计字段名称 | varchar | 100 |  | √ | ' ' | 统计字段名称 |
| 11 | fchannelcol_name | 统计渠道字段名称 | varchar | 100 |  | √ | ' ' | 统计渠道字段名称 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_chlmetrics_entry |  | fid |
| 2 | pk_ocdbd_chlmetrics_entry |  | fentryid |

---

## 渠道指标-主表 t_ocdbd_chlmetrics

- **表名称：** 渠道指标-主表
- **表名：** t_ocdbd_chlmetrics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 150 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fproperty | 指标属性 | bpchar | 1 |  | √ | 'A' | 指标属性,枚举: A :渠道 |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | fdimension | 指标维度 | bpchar | 1 |  | √ | '1' | 指标维度,枚举: 1 :单据字段 2 :单据数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_chlmetrics |  | fid |
| 2 | idx_ocdbd_chlmetrics |  | fdimension |
