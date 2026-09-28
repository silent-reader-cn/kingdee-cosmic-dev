# 经营单元-xkoac_unit

## 来源对象单据体-子表 t_xkoac_unitentry

- **表名称：** 来源对象单据体-子表
- **表名：** t_xkoac_unitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fambobjectid | 业务对象id | varchar | 50 |  | √ | ' ' | 业务对象id |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fambobjectnumber | 业务对象编码 | varchar | 255 |  | √ | ' ' | 业务对象编码 |
| 5 | fambobjectname | 业务对象名称 | varchar | 255 |  | √ | ' ' | 业务对象名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_unitentry |  | fid |
| 2 | pk_xkoac_unitentry |  | fentryid |

---

## 来源对象单据体-多语言表 t_xkoac_unitentry_l

- **表名称：** 来源对象单据体-多语言表
- **表名：** t_xkoac_unitentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fambobjectname | 业务对象名称 | varchar | 255 |  | √ | ' ' | 业务对象名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_unitentry_l |  | fpkid |
| 2 | idx_xkoac_unitentry_l |  | fentryid,flocaleid |

---

## 所属组织-多选基础资料表 t_xkoac_unitorg

- **表名称：** 所属组织-多选基础资料表
- **表名：** t_xkoac_unitorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_unitorg |  | fpkid |
| 2 | idx_xkoac_unitorg |  | fbasedataid |

---

## 经营单元-主表 t_xkoac_unit

- **表名称：** 经营单元-主表
- **表名：** t_xkoac_unit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fprincipal | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fambobjecttype | 业务对象类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 12 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 13 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fapprovedate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fsrcobjtext | 业务对象名称 | varchar | 2000 |  | √ | ' ' | 业务对象名称 |
| 19 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 20 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 21 | fctrlstrategy | fctrlstrategy | varchar | 2 |  | √ | '5' |  |
| 22 | ftouchbiz | 关联业务对象 | bpchar | 1 |  | √ | '0' | 关联业务对象 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 25 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 26 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_unit |  | fid |
| 2 | idx_xkoac_unit_fnum |  | fnumber |

---

## 使用组织-多选基础资料表 t_xkoac_unitentryorg

- **表名称：** 使用组织-多选基础资料表
- **表名：** t_xkoac_unitentryorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_unitentryorg |  | fbasedataid |
| 2 | pk_xkoac_unitentryorg |  | fpkid |

---

## 经营单元-多语言表 t_xkoac_unit_l

- **表名称：** 经营单元-多语言表
- **表名：** t_xkoac_unit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fsrcobjtext | 业务对象名称 | varchar | 2000 |  | √ | ' ' | 业务对象名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_unit_l |  | fpkid |
| 2 | idx_xkoac_unit_l |  | fid,flocaleid |
