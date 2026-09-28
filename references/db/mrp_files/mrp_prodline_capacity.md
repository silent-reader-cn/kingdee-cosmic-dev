# 产线日产能-mrp_prodline_capacity

## 单据体-子表 t_mrp_prodline_chglog

- **表名称：** 单据体-子表
- **表名：** t_mrp_prodline_chglog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangeqty | 调整人/机数量 | numeric | 23 | 10 | √ | 0 | 调整人/机数量 |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fchangerate | 调整比率 | numeric | 23 | 10 | √ | 0 | 调整比率 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fchangehours | 调整工时(h) | numeric | 23 | 10 | √ | 0 | 调整工时(h) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_prodline_chglog |  | fid,fseq |
| 2 | pk_t_mrp_prodline_chglog |  | fentryid |

---

## 单据体-子表 t_mrp_prodline_capacity

- **表名称：** 单据体-子表
- **表名：** t_mrp_prodline_capacity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstaworhours | 单位标准工时 | numeric | 23 | 10 | √ | 0 | 单位标准工时 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fperhours | 单件工时(h) | numeric | 23 | 10 | √ | 0 | 单件工时(h) |
| 6 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexpiredate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | ftimeunit | 时间单位 | varchar | 30 |  | √ | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 10 | fswitchinterval | 换产间隔(h) | numeric | 23 | 10 | √ | 0 | 换产间隔(h) |
| 11 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料计划信息 mpdm_materialplan](../sbd_files/mpdm_materialplan.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | funit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fdailycapacity | 日产量 | numeric | 23 | 10 | √ | 0 | 日产量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_prodline_capacity |  | fentryid |
| 2 | idx_mrp_prodline_capacity |  | fid,fseq |

---

## 产线日产能-多语言表 t_mrp_prodline_l

- **表名称：** 产线日产能-多语言表
- **表名：** t_mrp_prodline_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fbillname | 产线名称 | varchar | 100 |  | √ | ' ' | 产线名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mrp_prodline_l |  | fid,flocaleid |
| 2 | pk_t_mrp_prodline_l |  | fpkid |

---

## 产线日产能-主表 t_mrp_prodline

- **表名称：** 产线日产能-主表
- **表名：** t_mrp_prodline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 人/机数量 | numeric | 23 | 10 | √ | 0 | 人/机数量 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fworkhours | 计划工时(h) | numeric | 23 | 10 | √ | 0 | 计划工时(h) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fbillname | 产线名称 | varchar | 50 |  | √ | ' ' | 产线名称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fminhours | 最小排产时间(h) | numeric | 23 | 10 | √ | 0 | 最小排产时间(h) |
| 15 | fbillno | 产线编码 | varchar | 30 |  | √ | ' ' | 产线编码 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_prodline |  | fid |
| 2 | idx_mrp_prodline_bn |  | fbillno |
