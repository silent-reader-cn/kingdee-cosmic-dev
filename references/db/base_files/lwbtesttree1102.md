# lwbtesttree1102-lwbtesttree1102

## lwbtesttree1102-多语言表 t_lwbtesttree1102_l

- **表名称：** lwbtesttree1102-多语言表
- **表名：** t_lwbtesttree1102_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lwbtesttree1102_l |  | fpkid |
| 2 | idx_lwbtesttree1102_l_0 |  | fid,flocaleid |

---

## lwbtesttree1102-主表 t_lwbtesttree1102

- **表名称：** lwbtesttree1102-主表
- **表名：** t_lwbtesttree1102

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | forgfield | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 4 | forgfield41 | 核算组织1-委托 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | forgfield21 | 组织控件-核算 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 10 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 12 | fparentid | 上级 | int8 | 64 |  |  | null | lwbtesttree1102 lwbtesttree1102 |
| 13 | forgfield4 | 核算组织2 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 16 | forgfield1 | 组织控件-行政 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 17 | forgfield2 | 组织控件-自定义核算 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 18 | forgfield3 | 销售组织2-委托 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 19 | forgfield31 | 销售组织1 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 20 | fbasedatafield2 | 人员基础资料 | int8 | 64 |  |  | null | 人员 bos_user |
| 21 | flevel | 级次 | int8 | 64 |  |  | null | 级次 |
| 22 | fbasedatafield1 | 业务单元 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 23 | fbasedatafield | 行政组织 | int8 | 64 |  |  | null | 行政组织（部门） bos_adminorg |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lwbtesttree1102 |  | fid |
