# 反写库存单据成本配置-cal_revinvbillcf

## 反写库存单据成本配置-多语言表 t_cal_revinvbillcf_l

- **表名称：** 反写库存单据成本配置-多语言表
- **表名：** t_cal_revinvbillcf_l

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
| 1 | idx_cal_revinvbillcf_l_u |  | fid,flocaleid |
| 2 | pk_cal_revinvbillcf_l |  | fpkid |

---

## 反写字段配置-子表 t_cal_revinvbillcfentry

- **表名称：** 反写字段配置-子表
- **表名：** t_cal_revinvbillcfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostrecordfieldkey | 标识 | varchar | 255 |  | √ | ' ' | 标识 |
| 3 | fimbillfieldkey | 标识 | varchar | 255 |  | √ | ' ' | 标识 |
| 4 | fcostrecordfield | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fimbillfield | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_revinvbillcfentry |  | fentryid |
| 2 | idx_cal_revinvbillcfentry_id |  | fid |

---

## 反写库存单据成本配置-主表 t_cal_revinvbillcf

- **表名称：** 反写库存单据成本配置-主表
- **表名：** t_cal_revinvbillcf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbillentry | 单据体 | varchar | 255 |  | √ | ' ' | 单据体 |
| 6 | fimbill | 库存单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fcalbilltype | 出入库类型 | varchar | 30 |  | √ | ' ' | 出入库类型,枚举: IN :入库 OUT :出库 |
| 8 | fismaincostaccount | 默认成本主体 | bpchar | 1 |  | √ | ' ' | 默认成本主体 |
| 9 | fbillentrykey | 单据体标识 | varchar | 255 |  | √ | ' ' | 单据体标识 |
| 10 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_revinvbillcf |  | fid |
