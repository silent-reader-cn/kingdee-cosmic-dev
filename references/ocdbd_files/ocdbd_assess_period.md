# 营销周期-ocdbd_assess_period

## 考核周期单据体-子表 t_ocdbd_assess_entity

- **表名称：** 考核周期单据体-子表
- **表名：** t_ocdbd_assess_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmonthname | 月度名称 | varchar | 80 |  | √ | ' ' | 月度名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentrymonth | 月份 | int4 | 32 |  | √ | 0 | 月份 |
| 5 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fseason | 季度 | int4 | 32 |  | √ | 0 | 季度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_assessentity_fid |  | fid |
| 2 | pk_ocdbd_assess_entity |  | fentryid |

---

## 营销周期-主表 t_ocdbd_assess_period

- **表名称：** 营销周期-主表
- **表名：** t_ocdbd_assess_period

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 时间周期分组 ocdbd_timeperiod_group |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fuestype | 周期用途 | varchar | 30 |  | √ | ' ' | 周期用途,枚举: A :目标管理周期 B :营销费用预算周期 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbegindate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fgenerateway | 生成方式 | bpchar | 1 |  | √ | 'A' | 生成方式,枚举: A :自然年 B :自定义 |
| 14 | fperiod | 周期 | int4 | 32 |  | √ | 0 | 周期 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fheadseason | 季度 | int4 | 32 |  | √ | 1 | 季度 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fperiodyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 19 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '1' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_assessperiod_no |  | fnumber |
| 2 | pk_ocdbd_assess_period |  | fid |

---

## 营销周期-多语言表 t_ocdbd_assess_period_l

- **表名称：** 营销周期-多语言表
- **表名：** t_ocdbd_assess_period_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_assess_period_l |  | fpkid |
| 2 | idx_ocdbd_assessperiodl_flid |  | fid,flocaleid |
