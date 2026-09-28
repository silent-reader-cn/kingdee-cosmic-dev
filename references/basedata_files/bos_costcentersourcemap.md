# 成本中心映射配置-bos_costcentersourcemap

## 单据体-子表 t_bas_costcentermapentry

- **表名称：** 单据体-子表
- **表名：** t_bas_costcentermapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcetype | 来源类型 | varchar | 255 |  | √ | ' ' | 来源类型,枚举: bos_adminorg :行政组织 bos_org :业务单元 mpdm_workcentre :工作中心 |
| 3 | fsourcedataid | 来源数据编码 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_costcentermapentry_sid |  | fsourcedataid |
| 2 | pk_bas_costcentermapentry |  | fentryid |
| 3 | idx_bas_costcentermapentry_fk |  | fid |

---

## 成本中心映射配置-主表 t_bas_costcentersourcemap

- **表名称：** 成本中心映射配置-主表
- **表名：** t_bas_costcentersourcemap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 成本中心映射配置 bos_costcentersourcemap |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 9 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_cctsourcemap_cid |  | fcostcenterid |
| 2 | pk_bas_costcentersourcemap |  | fid |

---

## 成本中心映射配置-多语言表 t_bas_costcentersourcemap_l

- **表名称：** 成本中心映射配置-多语言表
- **表名：** t_bas_costcentersourcemap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_costcentersourcemap_l |  | fpkid |
| 2 | idx_bas_costcentersourcemap_l |  | fid,flocaleid |
