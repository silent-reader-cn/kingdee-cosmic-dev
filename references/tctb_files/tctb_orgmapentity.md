# 税务组织映射方案-tctb_orgmapentity

## 税务组织映射方案-多语言表 t_tctb_orgmapentity_l

- **表名称：** 税务组织映射方案-多语言表
- **表名：** t_tctb_orgmapentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_orgmapentity_l |  | fpkid |
| 2 | idx_tctb_orgmapentity_l_0 |  | fid,flocaleid |

---

## 税务组织映射方案-主表 t_tctb_orgmapentity

- **表名称：** 税务组织映射方案-主表
- **表名：** t_tctb_orgmapentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmapobject | 映射对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_orgmapentity |  | fid |
| 2 | idx_orgmap_number |  | fnumber |

---

## 业务对象-子表 t_tctb_orgmap_busobject

- **表名称：** 业务对象-子表
- **表名：** t_tctb_orgmap_busobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxcategory | 适用税种 | varchar | 400 |  | √ | ' ' | 适用税种 |
| 2 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 3 | fbusinessid | 业务对象id | varchar | 80 |  | √ | ' ' | 业务对象id |
| 4 | fbusinessnumber | 业务对象编码 | varchar | 80 |  | √ | ' ' | 业务对象编码 |
| 5 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 6 | fbusinessname | 业务对象名称 | varchar | 150 |  | √ | ' ' | 业务对象名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fentrychangetype | fentrychangetype | varchar | 50 |  | √ | ' ' |  |
| 11 | fisdefault | fisdefault | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_orgmap_busobject |  | fdetailid |
| 2 | idx_tctb_orgmap_busobject_fk |  | fentryid |

---

## 税务组织-子表 t_tctb_orgmap_taxorg

- **表名称：** 税务组织-子表
- **表名：** t_tctb_orgmap_taxorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | ftaxorg | 税务组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fchangestatus | fchangestatus | varchar | 50 |  | √ | ' ' |  |
| 9 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 13 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 14 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 15 | fnumber | fnumber | varchar | 100 |  | √ | ' ' |  |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fversion | fversion | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_orgmap_taxorg |  | fentryid |
| 2 | idx_tctb_orgmap_taxorg_fk |  | fid |
