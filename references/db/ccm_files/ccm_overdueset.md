# 信用逾期设置-ccm_overdueset

## 信用逾期设置-主表 t_ccm_overdueset

- **表名称：** 信用逾期设置-主表
- **表名：** t_ccm_overdueset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcalcamount | 逾期计算金额 | varchar | 50 |  | √ | ' ' | 逾期计算金额,枚举: |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbkgcheckfilter | 逾期来源条件(后台) | varchar | 255 |  | √ | ' ' | 逾期来源条件(后台) |
| 7 | fcalcdate | 逾期计算日期 | varchar | 50 |  | √ | ' ' | 逾期计算日期,枚举: |
| 8 | fbkgcheckfilter_tag | 逾期来源条件(后台)_详情 | text | 0 |  |  | ' ' | 逾期来源条件(后台)_详情 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fissys | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fentityid | 逾期来源单据 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 17 | fcheckdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccm_overdueset |  | fid |
| 2 | idx_ccm_overdueset_num |  | fnumber |

---

## 信用逾期设置-多语言表 t_ccm_overdueset_l

- **表名称：** 信用逾期设置-多语言表
- **表名：** t_ccm_overdueset_l

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
| 1 | idx_ccm_overdueset_fid_flocale |  | fid,flocaleid |
| 2 | pk_t_ccm_overdueset_l |  | fpkid |
