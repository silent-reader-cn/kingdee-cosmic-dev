# 对账通用设置_继承-ai_rec_common_filter

## 字段映射-子表 t_ai_acctfieldmapentry

- **表名称：** 字段映射-子表
- **表名：** t_ai_acctfieldmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentityid | 实体类型 | varchar | 100 |  | √ | ' ' | 实体类型 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdatatype | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 7 | ffieldkey | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_acctfieldmapentry_pkey |  | fentryid |
| 2 | idx_ai_acctfieldmapentry |  | fid |

---

## 单据体-子表 t_ai_rec_common_entry

- **表名称：** 单据体-子表
- **表名：** t_ai_rec_common_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizassist3 | 对账维度4 | varchar | 200 |  |  | ' ' | 对账维度4,枚举: |
| 3 | fbizassist2 | 对账维度3 | varchar | 200 |  |  | ' ' | 对账维度3,枚举: |
| 4 | fbizassist5 | 对账维度6 | varchar | 200 |  |  | ' ' | 对账维度6,枚举: |
| 5 | fbizassist4 | 对账维度5 | varchar | 200 |  |  | ' ' | 对账维度5,枚举: |
| 6 | fbizassist1 | 对账维度2 | varchar | 200 |  |  | ' ' | 对账维度2,枚举: |
| 7 | fbizassist0 | 对账维度1 | varchar | 200 |  |  | ' ' | 对账维度1,枚举: |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fbizassist7 | 对账维度8 | varchar | 200 |  |  | ' ' | 对账维度8,枚举: |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fbizassist6 | 对账维度7 | varchar | 200 |  |  | ' ' | 对账维度7,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ai_rec_common_entry |  | fid |
| 2 | t_ai_rec_common_entry_pkey |  | fentryid |

---

## 对账维度-多选基础资料表 t_ai_rec_common_assist

- **表名称：** 对账维度-多选基础资料表
- **表名：** t_ai_rec_common_assist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | '0' | 主实体对象 bos_entityobject |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_rec_common_assist |  | fid |
| 2 | t_ai_rec_common_assist_pkey |  | fpkid |

---

## 对账通用设置_继承-主表 t_ai_rec_common_filter

- **表名称：** 对账通用设置_继承-主表
- **表名：** t_ai_rec_common_filter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizorg | 业务组织 | varchar | 36 |  | √ | ' ' | 业务组织,枚举: |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fitemclasstype | 多基础资料类别 | varchar | 500 |  | √ | ' ' | 多基础资料类别 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fentity | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 11 | fbizdate | 业务日期 | varchar | 36 |  | √ | ' ' | 业务日期,枚举: |
| 12 | fperiod | 会计期间 | varchar | 36 |  | √ | ' ' | 会计期间,枚举: |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | fdetailrule | 明细对账设置 | bpchar | 1 |  | √ | '1' | 明细对账设置,枚举: 1 :DAP关系 2 :凭证号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_rec_common_filter |  | fentity |
| 2 | t_ai_rec_common_filter_pkey |  | fid |

---

## 对账通用设置_继承-多语言表 t_ai_rec_common_filter_l

- **表名称：** 对账通用设置_继承-多语言表
- **表名：** t_ai_rec_common_filter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_rec_common_filter_l |  | fid,flocaleid |
| 2 | t_ai_rec_common_filter_l_pkey |  | fpkid |
