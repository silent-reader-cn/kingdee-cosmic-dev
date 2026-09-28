# 产线日产能F7-mrp_prodline_f7

## 产线日产能F7-多语言表 t_mrp_prodline_l

- **表名称：** 产线日产能F7-多语言表
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

## 产线日产能F7-主表 t_mrp_prodline

- **表名称：** 产线日产能F7-主表
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
| 10 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 11 | fbillname | 产线名称 | varchar | 50 |  | √ | ' ' | 产线名称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fminhours | 最小排产时间(h) | numeric | 23 | 10 | √ | 0 | 最小排产时间(h) |
| 15 | fbillno | 产线编码 | varchar | 30 |  | √ | ' ' | 产线编码 |
| 16 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_prodline |  | fid |
| 2 | idx_mrp_prodline_bn |  | fbillno |
