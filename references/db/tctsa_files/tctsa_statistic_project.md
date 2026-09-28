# 统计项目-tctsa_statistic_project

## 统计项目-多语言表 t_tctsa_statistic_project_l

- **表名称：** 统计项目-多语言表
- **表名：** t_tctsa_statistic_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 400 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 1000 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_stat_project_l_0 |  | fid,flocaleid |
| 2 | pk_tctsa_statistic_project_l |  | fpkid |

---

## 统计项目-主表 t_tctsa_statistic_project

- **表名称：** 统计项目-主表
- **表名：** t_tctsa_statistic_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factivedate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 3 | fname | 名称 | varchar | 400 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 6 | fparentid | 上级统计项目 | int8 | 64 |  | √ | 0 | [统计项目 tctsa_statistic_project](../tctsa_files/tctsa_statistic_project.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | flongnumber | 长编号 | varchar | 600 |  | √ | ' ' | 长编号 |
| 9 | fexpdate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftaxationsysid | 适用税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | ftaxcategoryid | 适用税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 17 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fprojtype | 优惠项目类型 | varchar | 50 |  | √ | ' ' | 优惠项目类型,枚举: 1 :全额免税 2 :收入减计10% 3 :收入减计50% 4 :减半征收 5 :三免三减半 6 :超五百万部分减半 7 :两免三减半 8 :五免五减半 9 :其他 10 :500万以内免税，超500万减半 11 :加计100% 12 :2000万以内免税，超2000万减半 13 :十年内免税 14 :研发费用加计扣除 15 :按10%抵免税额 |
| 20 | fclassification | 项目分类 | varchar | 50 |  | √ | ' ' | 项目分类,枚举: 01 :优惠项目 |
| 21 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_statistic_project |  | fid |
| 2 | idx_tctsa_statisticp_tax |  | ftaxationsysid,ftaxcategoryid |
