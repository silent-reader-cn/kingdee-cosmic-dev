# 返利计算方案-msrcs_rebateschema

## 判断标准分录-子表 t_msrcs_rebateschema_js

- **表名称：** 判断标准分录-子表
- **表名：** t_msrcs_rebateschema_js

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjudgestandardid | 编码 | int8 | 64 |  | √ | 0 | 返利计算公式库 msrcs_rebateformula |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebateschemajs_fid |  | fid |
| 2 | pk_msrcs_rebateschema_js |  | fentryid |

---

## 返利计算方案-多语言表 t_msrcs_rebateschema_l

- **表名称：** 返利计算方案-多语言表
- **表名：** t_msrcs_rebateschema_l

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
| 1 | pk_msrcs_rebateschema_l |  | fpkid |
| 2 | idx_msrcs_rebateschemal_flid |  | fid,flocaleid |

---

## 数据源分录-子表 t_msrcs_rebateschema_se

- **表名称：** 数据源分录-子表
- **表名：** t_msrcs_rebateschema_se

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqfitlerstr_tag | 取数条件(字符串)_详情 | text | 0 |  |  | null | 取数条件(字符串)_详情 |
| 3 | fqfitlerstr | 取数条件(字符串) | varchar | 2000 |  | √ | ' ' | 取数条件(字符串) |
| 4 | fsrcbillid | 来源单据 | varchar | 40 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | frebatesourceid | 数据源编码 | varchar | 80 |  | √ | ' ' | 返利计算数据源 msrcs_rebatesource |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebateschemase_fid |  | fid |
| 2 | pk_msrcs_rebateschema_se |  | fentryid |

---

## 计算公式分录-子表 t_msrcs_rebateschema_cf

- **表名称：** 计算公式分录-子表
- **表名：** t_msrcs_rebateschema_cf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcalformulaid | 编码 | int8 | 64 |  | √ | 0 | 返利计算公式库 msrcs_rebateformula |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebateschemacf_fid |  | fid |
| 2 | pk_msrcs_rebateschema_cf |  | fentryid |

---

## 返利计算方案-主表 t_msrcs_rebateschema

- **表名称：** 返利计算方案-主表
- **表名：** t_msrcs_rebateschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | frebatemodelid | 返利计算模型 | varchar | 40 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebateschema |  | fid |
| 2 | idx_msrcs_rebateschema_num |  | fnumber |
