# 折旧方法-fa_depremethod

## 折旧方法-多语言表 t_fa_depremethod_l

- **表名称：** 折旧方法-多语言表
- **表名：** t_fa_depremethod_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | fformula | 静态折旧公式 | text | 0 |  |  | null | 静态折旧公式 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 6 | fformuladyn | 动态折旧公式 | text | 0 |  |  | null | 动态折旧公式 |
| 7 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depremethod_l_pkey |  | fpkid |
| 2 | idx_fa_dm_l_fid_flocaleid |  | fid,flocaleid |

---

## 折旧方法-主表 t_fa_depremethod

- **表名称：** 折旧方法-主表
- **表名：** t_fa_depremethod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftimes | 折旧率（%） | int8 | 64 |  | √ | 1 | 折旧率（%） |
| 3 | fcustomformula | 公式配置 | varchar | 1000 |  |  | null | 公式配置 |
| 4 | fyeardeprerate | 折旧率信息 | text | 0 |  |  | null | 折旧率信息 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 11 | fformula | 静态折旧公式 | text | 0 |  |  | ' ' | 静态折旧公式 |
| 12 | fformuladyn | 动态折旧公式 | text | 0 |  |  | ' ' | 动态折旧公式 |
| 13 | fperioddeprerate | fperioddeprerate | text | 0 |  |  | null |  |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 17 | fperioddepreamount | 折旧期限 | int8 | 64 |  | √ | 0 | 折旧期限 |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 20 | ftype | 类型 | varchar | 50 |  | √ | 'FORMULA' | 类型,枚举: 1 :表 2 :公式 3 :余额递减 4 :双倍余额递减 5 :工作量 6 :年数总和 7 :平均年限法 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 23 | fbase | 基数 | varchar | 30 |  | √ | ' ' | 基数,枚举: 1 :原值 2 :净额 |
| 24 | fyeardepreamount | 折旧年限 | int8 | 64 |  | √ | 0 | 折旧年限 |
| 25 | fdeductresidualval | 扣除残值 | bpchar | 1 |  | √ | '0' | 扣除残值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depremethod_pkey |  | fid |
| 2 | idx_fa_depmth_fnumber |  | fnumber |

---

## 年折旧率-子表 t_fa_depremethodentry

- **表名称：** 年折旧率-子表
- **表名：** t_fa_depremethodentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyeardeprerate | 折旧率(%) | numeric | 19 | 6 | √ | 0.000000 | 折旧率(%) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fyearnumber | 年度 | int8 | 64 |  | √ | 0 | 年度 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depremethodentry_pkey |  | fentryid |
| 2 | idx_fa_depmthent_fseq |  | fseq |

---

## 每期折旧率-子表 t_fa_depremethodentry_d

- **表名称：** 每期折旧率-子表
- **表名：** t_fa_depremethodentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fperiodnumber | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fperioddeprerate | 折旧率(%) | numeric | 19 | 6 | √ | 0.000000 | 折旧率(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depremethodentry_d_pkey |  | fdetailid |
| 2 | idx_fa_depmthent_d_fseq |  | fseq |
