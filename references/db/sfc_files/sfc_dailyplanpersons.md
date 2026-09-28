# 日计划人员(废弃)-sfc_dailyplanpersons

## 日计划人员(废弃)-主表 t_sfc_dailyplanpersons

- **表名称：** 日计划人员(废弃)-主表
- **表名：** t_sfc_dailyplanpersons

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisteamleader | 是否领班 | bpchar | 1 |  | √ | '0' | 是否领班 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [日计划人员分类(废弃) sfc_dailypersongroup](../sfc_files/sfc_dailypersongroup.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fperson | 人员 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_manuperson](../mpdm_files/mpdm_manuperson.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fpersontype | 人员类型 | varchar | 50 |  | √ | ' ' | 人员类型,枚举: engineer :工程师 team :班组 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_dailyplanpersons_fgid |  | fgroupid |
| 2 | pk_sfc_dailyplanpersons |  | fid |

---

## 日计划人员(废弃)-多语言表 t_sfc_dailyplanpersons_l

- **表名称：** 日计划人员(废弃)-多语言表
- **表名：** t_sfc_dailyplanpersons_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_dailyplanpersons_l |  | fpkid |
| 2 | idx_sfc_dailyplanpersons_l_0 |  | fid,flocaleid |
