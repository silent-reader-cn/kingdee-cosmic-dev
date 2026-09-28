# 工作日计划-working_plan

## 公共假期-子表 t_int_workingplanholiday

- **表名称：** 公共假期-子表
- **表名：** t_int_workingplanholiday

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fholidayid | 名称 | int8 | 64 |  | √ | 0 | [公共假期 public_holiday](../base_files/public_holiday.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_workingplanholiday |  | fentryid |
| 2 | idx_int_wph_fid |  | fid |

---

## 工作日模式卡片-子表 t_int_workingtime_card

- **表名称：** 工作日模式卡片-子表
- **表名：** t_int_workingtime_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 有效期.结束 | timestamp | 0 |  |  | null | 有效期.结束 |
| 3 | fstartdate | 有效期.开始 | timestamp | 0 |  |  | null | 有效期.开始 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fworkingtimeid | 工作日模式 | int8 | 64 |  | √ | 0 | [工作日模式 working_time](../base_files/working_time.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_working_card |  | fid |
| 2 | pk_t_int_workingtime_card |  | fentryid |

---

## 例外日期-子表 t_int_workingplanhours

- **表名称：** 例外日期-子表
- **表名：** t_int_workingplanhours

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 日期类型 | bpchar | 1 |  | √ | ' ' | 日期类型,枚举: 1 :工作日 2 :半工作日 3 :休息日 |
| 3 | fenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 4 | fhoursid | 工作时段编码 | int8 | 64 |  | √ | 0 | [工作时段 working_hours](../base_files/working_hours.md) |
| 5 | fdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fspecialdesc | 日期说明 | varchar | 255 |  | √ | ' ' | 日期说明 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_workingplanhours |  | fentryid |
| 2 | idx_int_wplanhours_fid |  | fid |

---

## 适用组织-多选基础资料表 t_int_workingplan_org

- **表名称：** 适用组织-多选基础资料表
- **表名：** t_int_workingplan_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_workingplan_org |  | fid,fbasedataid |
| 2 | pk_t_int_workingplan_org |  | fpkid |

---

## 例外日期-多语言表 t_int_workingplanhours_l

- **表名称：** 例外日期-多语言表
- **表名：** t_int_workingplanhours_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fspecialdesc | 日期说明 | varchar | 255 |  | √ | ' ' | 日期说明 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_workingplanhours_l |  | fpkid |
| 2 | idx_t_int_workingplh_l |  | fentryid |

---

## 工作日计划-多语言表 t_int_workingplan_l

- **表名称：** 工作日计划-多语言表
- **表名：** t_int_workingplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_workingplan_l |  | fpkid |
| 2 | idx_t_int_workingplan_l |  | fid |

---

## 工作日计划-主表 t_int_workingplan

- **表名称：** 工作日计划-主表
- **表名：** t_int_workingplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fcountryid | 国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fworkingtimeid | fworkingtimeid | int8 | 64 |  | √ | 0 |  |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 12 | fenddate | 有效期.结束 | timestamp | 0 |  |  | null | 有效期.结束 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fstartdate | 有效期.开始 | timestamp | 0 |  |  | null | 有效期.开始 |
| 17 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 64 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_workingplan_number |  | fnumber |
| 2 | pk_t_int_workingplan |  | fid |
