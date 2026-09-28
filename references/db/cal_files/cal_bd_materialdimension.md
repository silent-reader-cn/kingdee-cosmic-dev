# 物料核算维度设置-cal_bd_materialdimension

## 物料核算维度设置-主表 t_cal_materialdimension

- **表名称：** 物料核算维度设置-主表
- **表名：** t_cal_materialdimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcalsystemid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 8 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fapprovetime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 11 | fismigrate | 是否（企业版）迁移 | bpchar | 1 |  | √ | '0' | 是否（企业版）迁移 |
| 12 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_materialdimension_pkey |  | fid |
| 2 | idx_cal_matdimension_num |  | fnumber |

---

## 物料核算维度设置-多语言表 t_cal_materialdimension_l

- **表名称：** 物料核算维度设置-多语言表
- **表名：** t_cal_materialdimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_materialdimension_l_pkey |  | fpkid |
| 2 | idx_cal_matdis_l_id |  | fid,flocaleid |

---

## 分录-子表 t_cal_matdimensionentry

- **表名称：** 分录-子表
- **表名：** t_cal_matdimensionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 cal_bd_caldimension](../cal_files/cal_bd_caldimension.md) |
| 4 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_matdisentry_id |  | fid |
| 2 | t_cal_matdimensionentry_pkey |  | fentryid |
