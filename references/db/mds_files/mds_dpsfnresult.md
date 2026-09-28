# 供应组织分配关联冲减结果-mds_dpsfnresult

## 供应组织分配关联冲减结果-多语言表 t_mds_dpsfnresult_l

- **表名称：** 供应组织分配关联冲减结果-多语言表
- **表名：** t_mds_dpsfnresult_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_dpsfnresult_l |  | fpkid |
| 2 | idx_y_mds_dpsfnresult_l |  | fid,flocaleid |

---

## 供应组织分配关联冲减结果-主表 t_mds_dpsfnresult

- **表名称：** 供应组织分配关联冲减结果-主表
- **表名：** t_mds_dpsfnresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmatchqty | 日生产计划匹配数量 | numeric | 23 | 10 | √ | 0.0000000000 | 日生产计划匹配数量 |
| 3 | fbillformid | 单据标识ID | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fdemandsourcetype | 来源需求类型 | varchar | 36 |  | √ | ' ' | 来源需求类型,枚举: ORDER :ORDER SOP :SOP ID :ID |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fisqtysetoff | 是否进行过冲减 | bpchar | 1 |  | √ | '0' | 是否进行过冲减 |
| 11 | ffnqty | 冲减数量 | numeric | 23 | 10 | √ | 0.0000000000 | 冲减数量 |
| 12 | ffndefineid | 预测冲减定义 | int8 | 64 |  | √ | 0 | [预测冲减定义 mds_setoffsetting](../mds_files/mds_setoffsetting.md) |
| 13 | fbaseunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | forderseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdpsschemeid | 供应组织分配方案 | int8 | 64 |  | √ | 0 | [供应组织分配方案定义 mds_siteschemedef](../mds_files/mds_siteschemedef.md) |
| 18 | forgsiteid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fbillentryid | 单据分录ID | varchar | 36 |  | √ | ' ' | 单据分录ID |
| 20 | ffntime | 冲减日期 | timestamp | 0 |  |  | null | 冲减日期 |
| 21 | fissalremainqty | 是否订单剩余数量 | bpchar | 1 |  | √ | '0' | 是否订单剩余数量 |
| 22 | fbillid | 单据ID | varchar | 36 |  | √ | ' ' | 单据ID |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 25 | fmateqty | 日生产计划数量 | numeric | 23 | 10 | √ | 0.0000000000 | 日生产计划数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_y_mds_dpsfnresult |  | forgsiteid |
| 2 | pk_t_mds_dpsfnresult |  | fid |
