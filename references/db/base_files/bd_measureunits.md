# 计量单位-bd_measureunits

## 计量单位-多语言表 t_bd_measureunit_l

- **表名称：** 计量单位-多语言表
- **表名：** t_bd_measureunit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_measureunit_l_fid |  | fid,flocaleid |
| 2 | t_bd_measureunit_l_pkey |  | fpkid |

---

## 计量单位-主表 t_bd_measureunit

- **表名称：** 计量单位-主表
- **表名：** t_bd_measureunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fgroupid | 单位分组 | int8 | 64 |  | √ | 0 | [计量单位分组 bd_measureunitsgroup](../base_files/bd_measureunitsgroup.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fprecision | 单位精度 | int8 | 64 |  | √ | 0 | 单位精度 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fk_kdxk_fcheckunit | 基准单位 | bpchar | 1 |  | √ | '0' | 基准单位 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 13 | fispreset | 系统预设 | bpchar | 1 |  | √ | '1' | 系统预设 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fprecisiontype | 精度处理 | varchar | 50 |  | √ | ' ' | 精度处理,枚举: 1 :四舍五入 2 :舍位 3 :进位 |
| 16 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fdisablestatus | fdisablestatus | bpchar | 1 |  | √ | '1' |  |
| 21 | fcoefficient | fcoefficient | numeric | 23 | 10 |  | null |  |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fconverttype | 换算类型 | varchar | 50 |  | √ | ' ' | 换算类型,枚举: 1 :固定 2 :浮动 |
| 24 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_measureunit_pkey |  | fid |
| 2 | idx_t_bd_measureunit_number |  | fnumber |
